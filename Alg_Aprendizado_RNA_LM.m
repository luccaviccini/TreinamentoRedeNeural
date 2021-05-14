clear all; close all;
%% Configuração dos dados de entrada

%Comprimento do vetor de treinamento
N = 10000;

%Sinal de entrada
x = linspace(0,2*pi,N);

%Resposta desejada
t = sin(x) + 2*sin(2*x)+ 3*sin(3*x);

%Atrasos da Linha de memória
p = 11;

%Normalização das entradas e saídas no intervalos de 0 a 1
[x,PSx] = mapminmax(x,-1,1);
[t,PSt] = mapminmax(t,-1,1);

%Formação dos pares de treinamento
for j = 1:N-p
    X(:,j)  = x(j:p+j-1)';
end
    T = t(p-floor(p/2):N-floor(p/2)-1);

%% Aprendizado de Rede Neural Artificial pelo Algoritmo LM
%Quantidade de Neurônios
h = 8;
        

%Inicialização aleatória do vetor de pesos
W1  = 2*rand(h,size(X,1)+1)-1;	%Pesos da camada de entrada
W2  = 2*rand(size(T,1),h+1)-1;      %Pesos da camada de saída

%Pesos utilizados para comparar o código e toolbox do matlab
W1i = W1;
W2i = W2;

%Taxa de aprendizagem, máximo de epócas, termo momentum e regularização
epoc = 100;
lmbd = 0.0;

%Critérios de parada e aprendizagem
mui     = 0.001;
mi      = mui;
beta    = 10;
% mingrad = 1e-07;

net = feedforwardnet(h);
net = configure(net,X,T);
net = setwb(net,[W1i(:); W2i(:)]);
net.trainFcn                    = 'trainlm';
net.trainParam.mu               = mui;
net.trainParam.mu_dec           = 1/beta;
net.trainParam.mu_inc           = 1*beta;
net.trainParam.max_fail         = 500;
net.performParam.normalization  = 'none';
net.performParam.regularization = lmbd;
net.trainParam.epochs           = 1;
net.divideParam.trainRatio      = 1.0;
net.divideParam.valRatio        = 0.0;
net.divideParam.testRatio       = 0.0;
net.trainParam.showWindow       = false;

%Repetição do algoritmo segundo a quantidade de épocas
for i = 1:epoc

        %% FeedFoward
        %Camada Escondida
        Xb      = [ones(size(X,2),1)';  X];
        I1      = W1*Xb;
        Y1      = tanh(I1);

        %Camada de Saída
        Yb      = [ones(size(Y1,2),1)'; Y1];
        I2      = W2*Yb;
        Y2      = I2;
        
        B(:,i) = [W1(:); W2(:)];
        %% FeedBackward
        %Levemberg-Marquadt é realizado em todas as Camadas ao mesmo tempo :D
        %Concatenar pesos e jacobianas de todas as camadas
        E = T - Y2;
        Ean(i) = mse(E);

        for n = 1:h

            Atemp  = W1(n,:);
%             Atemp    = W1(n,2:end);
%             Btemp(n) = W1(n,1);
            J1temp = -1*(1-Y1(n,:).^2).*W2(n+1).*Xb;
            
            if n == 1
                A  = Atemp;
                J1 = J1temp';
            else
                A  = [A Atemp];
                J1 = [J1 J1temp'];
            end
            
        end
        
        A = [A W2];
%         A = [A Btemp];
        J = [J1 -Yb'];
%         A = [A W2(2:end) W2(1)];
        
        a = A;
        
        %Parâmetro de silenciamento (damper) igual
        H = J'*J/N;
        g = J'*E'/N;
        G(:,i) = g;
        M = mi*eye(size(J,2));
        A = a - g'*inv(H + M);
        for k = 1:h
            W1(k,:) = A((k-1)*size(Xb,1)+1:k*size(Xb,1));
        end

        W2 = A(h*size(Xb,1)+1:h*size(Xb,1)+h+1);
        
        % Recomputando o erro
        Xb      = [ones(size(X,2),1)';  X];
        I1      = W1*Xb;
        Y1      = tanh(I1);
        Yb      = [ones(size(Y1,2),1)'; Y1];
        I2      = W2*Yb;
        Y2      = I2;
        Eat(i)  = mse(T - Y2);
        
        if Eat(i) <= Ean(i)
            mi = max(mi/beta,1e-7);
            Yi = Y2;
            perf(i) = Eat(i);
        else
            while Eat(i) > Ean(i)
                mi = min(mi*beta,1e7);
                M = mi*eye(size(J,2));
        
                %Parâmetro de silenciamento (damper) aumentando
                A = a - g'*inv(H + M);
                
                for k = 1:h
                    W1(k,:) = A((k-1)*size(Xb,1)+1:k*size(Xb,1));
%                     W1(k,2:end) = A((k-1)*size(X,1)+1 : k*size(X,1));
%                     W1(k,1)     = A(h*size(X,1)+k);
                end

                W2 = A(h*size(Xb,1)+1:h*size(Xb,1)+h+1);
%                 W2(2:end) = A(h*size(Xb,1)+1:h*size(Xb,1)+h);
%                 W2(1) = A(h*size(Xb,1)+h+1);

                % Recomputando o erro
                Xb     = [ones(size(X,2),1)';  X];
                I1     = W1*Xb;
                Y1     = tanh(I1);
                Yb     = [ones(size(Y1,2),1)'; Y1];
                I2     = W2*Yb;
                Y2     = I2;
                Eat(i) = mse(T-Y2);
            end
            mi = max(mi/beta,1e-7);
            Yi = Y2;
            perf(i) = Eat(i);
        end
        
    [net, tr2] = train(net,X,T);
    W(:,i) = getwb(net);
    if i == 1
        perfnet(1) = tr2.perf(1);
        munet(1)   = tr2.mu(1);
        gradnet(1) = tr2.gradient(1);
    end
    perfnet(i+1) = tr2.perf(2);
    munet(i+1)   = tr2.mu(2);
    gradnet(i+1) = tr2.gradient(2);
        
        mu(i) = mi;
        Erro(:,i) = T-Yi;
       
end

%% Toobox de rede neural
net = feedforwardnet(h);
net = configure(net,X,T);
net = setwb(net,[W1i(:); W2i(:)]);
net.trainFcn                    = 'trainlm';
net.trainParam.mu               = mui;
net.trainParam.mu_dec           = 1/beta;
net.trainParam.mu_inc           = 1*beta;
net.trainParam.max_fail         = 500;
net.performParam.normalization  = 'none';
net.performParam.regularization = lmbd;
net.trainParam.epochs           = 1;
net.divideParam.trainRatio      = 1.0;
net.divideParam.valRatio        = 0.0;
net.divideParam.testRatio       = 0.0;
net.trainParam.showWindow       = false;

for i = 1:epoc
    [net, tr2] = train(net,X,T);
    W(:,i) = getwb(net);
    if i == 1
        perfnet(1) = tr2.perf(1);
        munet(1)   = tr2.mu(1);
        gradnet(1) = tr2.gradient(1);
    end
    perfnet(i+1) = tr2.perf(2);
    munet(i+1)   = tr2.mu(2);
    gradnet(i+1) = tr2.gradient(2);
end
            
Yffn = sim(net,X);
effn = T - Yffn;

rms(effn)

Effn = T - Yi;
rms(Effn)

figure(1)
plot(T); hold on; plot(Yi); plot(Yffn);
legend('Desejado','Código','Toolbox');

figure, plot(perfnet), hold on, plot([Ean(1) perf]), legend('Toolbox','Código');
figure, semilogy(munet), hold on, semilogy([mui mu]); legend('Toolbox','Código');
