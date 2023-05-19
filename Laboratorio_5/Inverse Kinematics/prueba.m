px=1.5
py=1.
pz=1.

t1=atan2(py,px)
c1=cos(t1)
s1=sin(t1)
rota=trotx(-pi/2) * trotz(-pi/2)
T_desired =[c1 ,-s1,0 ,1;s1,c1 , 0,  1;0 ,0 ,1 ,  1;0, 0 , 0 , 1]*rota

L0= 1;
L1 = 1; % Longitud del eslabón 1
L2 = 1; % Longitud del eslabón 2
L3 = 1; % Longitud del eslabón 3

% Paso 2: Crear una matriz de enlaces
L(1) = Link([0, L0, 0, -pi/2]); % Enlace 1 (Theta, d, a, alpha)
L(2) = Link([0, 0, L1, 0]); % Enlace 2
L(3) = Link([0,  L2, 0, 0]); % Enlace 3
L(4) = Link([0, L3, 0, 0]); % Enlace 4

% Paso 3: Crear el robot serial
robot = SerialLink(L, 'name', 'Robot de 4GDL');

% Paso 4: Definir la matriz de transformación homogénea deseada
p = [0.8 0 0];
T = T_desired; % Ejemplo de matriz de transformación deseada

% Paso 5: Realizar la cinemática inversa
q = robot.ikine(T,'mask',[1 1 1 0 0 0]); % Vector de posiciones articulares (en radianes)

% Paso 6: Mostrar los resultados
disp("Posiciones articulares:");
disp(q);
%% 
clear 
clc
%26.56505117707799 -51.82729237298775 103.6545847459755 -51.82729237298775
t1=deg2rad(26.565);
t2=deg2rad(-51.827292);
t3=deg2rad(103.654585);
t4=deg2rad(-51.827292);

r=cos(t2)+cos(t2+t3)+cos(t2+t3+t4)
z=1+sin(t2)+sin(t2+t3)+sin(t4+t2+t3)
x=r*cos(t1)
y=r*sin(t1)
