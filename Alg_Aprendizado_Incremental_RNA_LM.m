clear all; close all;
%% Configura��o dos dados de entrada

%Comprimento do vetor de treinamento
N = 1000;

%Sinal de entrada
%x = linspace(0,2*pi,N);
x = linspace(0,10,N);

%Resposta desejada
%t = sin(x) + 2*sin(2*x)+ 3*sin(3*x);
t = (x+3).*(x-2).*(x-3).*(x-7).*(x-10);

%Atrasos da Linha de mem�ria
p = 10;

%Normaliza��o das entradas e sa�das no intervalos de 0 a 1
[x,PSx] = mapminmax(x,-1,1);
[t,PSt] = mapminmax(t,-1,1);

%Forma��o dos pares de treinamento
% for j = 1:N-p
%     X(:,j)  = x(j:p+j-1)';
% end
%     T = t(p-floor(p/2):N-floor(p/2)-1);

%% Aprendizado de Rede Neural Artificial pelo Algoritmo LM
%Quantidade de Neur�nios
h = 8;

%Inicializa��o aleat�ria do vetor de pesos
        X = x(1:p)';
        T = t(1+floor(p-p/2));
        
W1  = 2*rand(h,size(X,1)+1)-1;	%Pesos da camada de entrada
W2  = 2*rand(size(T,1),h+1)-1;      %Pesos da camada de sa�da

%Pesos utilizados para comparar o c�digo e toolbox do matlab
W1i = W1;
W2i = W2;

%Taxa de aprendizagem, m�ximo de ep�cas, termo momentum e regulariza��o
epoc = 20;
lmbd = 0.0;

%Crit�rios de parada e aprendizagem
muini   = 0.001;
mi      = muini;
beta    = 10;

%Repeti��o do algoritmo segundo a quantidade de �pocas
for i = 1:epoc
    for j = 1:N-p
        X = x(j:p+j-1)';
        T = t(j+floor(p-p/2));
            %% FeedFoward
            %Etapa necess�ria para comparar o resultados dos pesos na �poca
            %com os valores desejados e computar o erro
            
            %Camada Escondida
            Xb      = [ones(size(X,2),1)';  X];
            I1      = W1*Xb;
            Y1      = tanh(I1);

            %Camada de Sa�da
            Yb      = [ones(size(Y1,2),1)'; Y1];
            I2      = W2*Yb;
            Y2      = I2;

            E = T - Y2;
            Ean(i) = mse(E);
            
            %% FeedBackward
            %Levemberg-Marquadt � realizado em todas as Camadas ao mesmo tempo :D
            %Concatenar pesos de todos os neur�nio e jacobianas
            %considerando todas as camadas
        
            for n = 1:h

                Wtemp  = W1(n,:);
                J1temp = -1*(1-Y1(n,:).^2).*W2(n+1).*Xb;

                if n == 1
                    W  = Wtemp;
                    J1 = J1temp';
                else
                    W  = [W Wtemp];
                    J1 = [J1 J1temp'];
                end

            end

            W = [W W2];
            J = [J1 -Yb'];

            w = W;

            %Par�metro de silenciamento (damper) igual
            %Atualiza��o dos Pesos por LM
            H = J'*J/N;
            g = J'*E'/N;
            G(:,i) = g;
            M = mi*eye(size(J,2));
            W = w - g'*inv(H + M);
            
            %Reposicionando os pesos
            for k = 1:h
                W1(k,:) = W((k-1)*size(Xb,1)+1:k*size(Xb,1));
            end

            W2 = W(h*size(Xb,1)+1:h*size(Xb,1)+h+1);

            %Recomputando o erro
            Xb      = [ones(size(X,2),1)';  X];
            I1      = W1*Xb;
            Y1      = tanh(I1);
            Yb      = [ones(size(Y1,2),1)'; Y1];
            I2      = W2*Yb;
            Y2      = I2;
            Eat(i)  = mse(T - Y2);

            %Caso o erro dos pesos atualizados seja melhor que o obtido
            %anteriormente o par�metro de sil�nciamento (damper) � 
            %diminu�do e o resultado final da rede � mantido para a pr�xima
            %�poca
            if Eat(i) <= Ean(i)
                mi = max(mi/beta,1e-7); %o damper n�o pode ser menor que 1e-7
                Yi(j) = Y2;
                perf(i) = Eat(i);
            else
                while Eat(i) > Ean(i)
                    %Par�metro de silenciamento (damper) aumentando
                    mi = min(mi*beta,1e7); %o damper n�o pode ser maior que 1e7
                    M = mi*eye(size(J,2));

                    %Recomputando os pesos com o novo damper
                    W = w - g'*inv(H + M);
                    
                    %Reposicionando os pesos com o novo damper
                    for k = 1:h
                        W1(k,:) = W((k-1)*size(Xb,1)+1:k*size(Xb,1));
                    end

                    W2 = W(h*size(Xb,1)+1:h*size(Xb,1)+h+1);

                    % Recomputando o erro com o novo damper
                    Xb     = [ones(size(X,2),1)';  X];
                    I1     = W1*Xb;
                    Y1     = tanh(I1);
                    Yb     = [ones(size(Y1,2),1)'; Y1];
                    I2     = W2*Yb;
                    Y2     = I2;
                    
                    % Atualizando o erro a ser comparado no la�o com o novo
                    % damper
                    Eat(i) = mse(T-Y2);
                end
                %o damper � diminu�do novamente quando o la�o � terminado
                mi = max(mi/beta,1e-7);
                
                %Resultado final obtido
                Yi(j) = Y2;
                
                %Perfomance da Rede
                perf(i) = Eat(i);
            end
            mu(i) = mi;
            Erro(:,i) = T-Yi(j);

    end
end
% %% Toobox de rede neural
% net = feedforwardnet(h);
% net = configure(net,X,T);
% net = setwb(net,[W1i(:); W2i(:)]);
% net.trainFcn                    = 'trainlm';
% net.trainParam.mu               = muini;
% net.trainParam.mu_dec           = 1/beta;
% net.trainParam.mu_inc           = 1*beta;
% net.trainParam.max_fail         = 500;
% net.performParam.normalization  = 'none';
% net.performParam.regularization = lmbd;
% net.trainParam.epochs           = 1;
% net.divideParam.trainRatio      = 1.0;
% net.divideParam.valRatio        = 0.0;
% net.divideParam.testRatio       = 0.0;
% net.trainParam.showWindow       = false;
% 
% for i = 1:epoc
%     for j = 1:N-p
%         X = x(j:p+j-1)';
%         T = t(j+floor(p-p/2));
%         [net, tr2] = train(net,X,T);
%         Wp(:,i) = getwb(net);
%         if i == 1
%             perfnet(1) = tr2.perf(1);
%             munet(1)   = tr2.mu(1);
%             gradnet(1) = tr2.gradient(1);
%         end
%         perfnet(i+1) = tr2.perf(2);
%         munet(i+1)   = tr2.mu(2);
%         gradnet(i+1) = tr2.gradient(2);
%     end
% end

% figure(1)
% plot(T); hold on; plot(Yi); plot(Yffn);
% legend('Desejado','C�digo','Toolbox');
% 
% figure, plot(perfnet), hold on, plot([Ean(1) perf]), legend('Toolbox','C�digo');
% figure, semilogy(munet), hold on, semilogy([muini mu]); legend('Toolbox','C�digo');