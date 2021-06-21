n = 1:80
p = 0.999;
PM = (p.^(8*n)).*(9-8*(p.^n))
plot(n,PM)
nmax= sum (PM>0.5)

A = [1.2 1.7 1.5]
B = sum(A>1)