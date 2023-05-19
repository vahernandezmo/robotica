% Laboratorio 4

%%
clc
clear
close all

ws = [-120 100 -100 100 -20 70]/5;

plot_options1 = {'workspace',ws,'scale',.5,'view',[-5 25]...
    ,'tilesize',2,  'ortho', 'lightpos',[2 2 10] };
L0=4
L1=10.5
L2=10.5
L3=10

L(1) = Link('revolute','d',L0,'a',0,'alpha',0,'offset',0,'standard');
L(2) = Link('revolute','d',0,'a',L1,'alpha',0,'offset',-pi/2,'standard');
L(3) = Link('revolute','d',0,'a',L2,'alpha',0,'offset',80*pi/180,'standard');
L(4) = Link('revolute','d',0,'a',L3,'alpha',0,'offset',0,'standard');

Robot0 = SerialLink(L,'name','Robot RRRR','plotopt',plot_options1)
Robot0.plot([0 0 0 0])
