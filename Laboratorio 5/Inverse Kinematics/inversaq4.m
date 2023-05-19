clear clc

syms q4 l3

Tnoa=trotz(q4)*transl(l3,0,0)*trotz(-pi/2)*trotx(pi/2);

l = [0, 10.6, 10.6, 7.6];
qini = [0,0,0,0];
offset = [0, pi/2, 0, 0];
% Orden parametros funcion link [THETA D A ALPHA SIGMA(0R,1P) OFFSET]
DHparameters = [qini(1) 4.8 l(1) pi/2 0 offset(1);
                qini(2) 0   l(2) 0    0 offset(2);
                qini(3) 0   l(3) 0    0 offset(3);
                qini(4) 0   l(4) pi/2    0 offset(4)];
L(1) = Link(DHparameters(1,:));
L(2) = Link(DHparameters(2,:));
L(3) = Link(DHparameters(3,:));
L(4) = Link(DHparameters(4,:));
Robot_pincher = SerialLink(L,'name','Pincher');
ws = [-30 30 -30 30 -10 50];


