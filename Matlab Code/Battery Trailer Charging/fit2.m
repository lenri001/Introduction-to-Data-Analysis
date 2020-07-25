x=rand (1,100).*10;
noise=randn(1,100);
y=3*(x-4).^2+8+5*noise;
figure
plot(x,y,'b*')
% axis equal tight
grid on
constant=lsqcurvefit(@f2,[0;0;0],x,y);
a=constant(1)
b=constant(2)
c=constant(3)
xfit=0:0.1:10;
yfit=f2(constant,xfit);
figure
plot(x,y,'b*')
%axis equal tight
hold on
plot(xfit,yfit,'r', 'linewidth', 2)
grid on



