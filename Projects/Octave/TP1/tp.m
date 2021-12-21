clear all
close all


% Modéle affine 

load('dataset1.mat');

N = length(x);
n = (0:N-1);

S = 0;

n = flip(rot90(n));
sn = n;
sxx = n;
sxy = n;

i = 0;

for i = sn+1
  sxx(i) = (x(i)).^2;
  sxy(i) = x(i).*y(i);
end

Sx = sum(x);
Sy = sum(y);
Sxy = sum(sxy);
Sxx = sum(sxx);


a = ((Sxy - (Sx * Sy * (1/N)))/((Sxx)-(1/N)*(Sx*Sx)));
b = (1/N)*(Sy - a*Sx);

for i = sn+1
  sn(i) = ( x(i)*a +b -y(i)).^2;

end

S = sum(sn);
f = x*a + b;

r = f - y;
mr = sum(r)/N
vr = var(r)
er = sqrt(vr)


figure(1)
plot(x,f);
xlabel("n");
ylabel("sn");
hold on 
scatter(x,y);











% Modéle polynomiale

load('dataset2.mat');

N = length(x)

for i=0:N-1;
  x0(i+1) = 1;
  xx(i+1) = x(i+1).^2;
end

x0 = flip(rot90(x0));
xx = flip(rot90(xx));

X = [(xx) , (x) , (x0)];
O = zeros(3,1);

O = (pinv(X'*X))*(X')*y

a = O(1)
b = O(2)
c = O(3)

##transposé  = A'



f = a*(xx) + b*x + c;

figure(2)
plot(x,f);
xlabel("x")
ylabel("y")
hold on 
scatter(x,y);














##Modéle général

load('dataset3.mat')

N = length(y)

for i=0:N-1;
  x0(i+1) = 1;
end

##x0 = flip(rot90(x0));

X = [(x0) , (x1) , (x2) , (x3)];

O = zeros(3,1);

O = (pinv(X'*X))*X'*y;

a = O(1);
b = O(2);
c = O(3);
d = O(4);

f = a + b*x1 + c*x2 + d*x3;

var(O)
e0 = sqrt(var(O))



figure(3)
plot(x1,f);
xlabel("x1")
ylabel("y")
hold on 
scatter(x1,y);

figure(4)
plot(x2,f);
xlabel("x2")
ylabel("y")
hold on
scatter(x2,y);


figure(5)
plot(x3,f);
xlabel("x3")
ylabel("y")
hold on
scatter(x3,y);

figure(6)
plot(t,f);
xlabel("t")
ylabel("y")
hold on
scatter(t,y);








% Modèle général avec convolution

load('dataset4.mat')

N = length(y_voxel)

for i=0:N-1;
  x0(i+1) = 1;
end

x0 = flip(rot90(x0));

X = [(p1) , (drift)];

O = zeros(2,1);

O = (pinv(X'*X))*(X')*y_voxel;

a = O(1)
b = O(2)



f = conv(a*p1,h,'same') + drift*b;
r = f - y_voxel

vr = var(r)
er = sqrt(var(r))

v0 = var(O)
e0 = sqrt(var(O))

publish('tp.m','pdf');

figure(7);
plot(t,f);
xlabel('temps');
ylabel('signal');
hold on
scatter(t,y_voxel);







%  Application multivariées
##
##load('dataset5.mat');
##
##y = reshape(im_2Dt,[400,2500]);
##
##
##X = [(p1) , (p2)];
##
##O = zeros(2,1);
##
##O = (pinv(X'*X))*(X');
##
##a = O(1)
##b = O(2)
##
##
##
##f = X*O;
##r = f - y
##
##vr = var(r)
##er = sqrt(var(r))
##
##v0 = var(O)
##e0 = sqrt(var(O))
##
##figure()
##plot(t,f)