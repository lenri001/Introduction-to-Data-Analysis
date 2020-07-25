clear all;
close all;
clc;

%  V = readtable('linregdata.xlsx');
% % V = readtable('linregdata.xlsx','Range','A2:A721');
% % P = readtable('linregdata.xlsx','Range','B2:B721');
% %V = readtable('linregdata.xlsx','Range','C2:C721');
%  v=V.voltage;
%  p=V.power;
%  q=V.VARs;
% % %plot(V,P)
% figure
%  plot(v,q)
%  hold on
%  figure
%  scatter(v, q)
%  hold on
%  figure
%  plot(v, q, 'x')
 
 %4th December 2018
 V = readtable('invdata4december.xlsx');
% V = readtable('invdata4december.xlsx','Range','A2:A721');
% P = readtable('invdata4december.xlsx','Range','B2:B721');
%V = readtable('invdata4december.xlsx','Range','C2:C721');
 v=V.voltage;
 p=V.power;
 q=V.VAR;
% %plot(V,P)
% figure
%  plot(q,v)
%  hold on
%  figure
%  scatter(q, v)
%  hold on
%  figure
%  plot(v, q, 'x')
%determine how many numbers




%% random practice from youtube for determining m and c using some data and using it for another set of data if it works (linear interpolation type)
N=length(v)
%fit to f(x)=b+m*x
 X=[ones(N,1)  p(:)] %% that colon is for making it a column matrix whatever it is
 a = (X.'*X)\(X.' *v(:)); % using least square to determine c and m
 b=a(1);
 m=a(2);
 %calculate line for graphics
 xa=min(p)
 xb=max(p)
 x = linspace (xa, xb, 180);
 f=b+m*x;
 plot (p, f, 'b.')
 hold on

 plot (p, f, '-r') 
 hold off
 
 
 
  






