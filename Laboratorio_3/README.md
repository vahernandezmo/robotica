# Laboratorio 3

Para el desarrollo del laboratorio 3 se realizo un proceso siguiendo
el repositorio creado por el ing. Felipe Gonzales
https://github.com/fegonzalez7/rob_unal_clase2
Este permitió configurar e instalar el programa de manera correcta 
en los ordenadores de los integrantes del grupo.






## Matlab: 
Para la realización de operar Turtlesim mediante Matlab, para
el que fue necesario instalar el toolbox de Robotica de Mathworks.

Se probó el script de la guia de laboratorio.
-----------------------------------------------------------------
```matlab
%%
rosinit; %Conexión con nodo maestro
%%
velPub = rospublisher(’/turtle1/cmd_vel’,’geometry_msgs/Twist’); %Creación publicador
velMsg = rosmessage(velPub); %Creación de mensaje
%%
velMsg.Linear.X = 1; %Valor del mensaje
send(velPub,velMsg); %Envio
pause(1)
```
------------------------------------------------------------------
En este se inicia la conexión con el maestro, se cre un publisher
y se envian mensajes con la velocidad para modificar la posición
en la dirección x.

Esto puede visualizarce en el video matlab_example.webm
------------------------------------------------------------------
Ahora se crea un script para cubrir los otros puntos propuestos
por la guia No.1
------------------------------------------------------------------
```matlab
clear
clc
%%
rosinit; %Conexi ́on con nodo maestro
%%
velPub = rospublisher('/turtle1/cmd_vel','geometry_msgs/Twist'); %Creaci ́on publicador
velMsg = rosmessage(velPub); %Creaci ́on de mensaje
sub = rossubscriber('/turtle1/pose','turtlesim/Pose')
msg_twist = rosmessage('geometry_msgs/Twist');

%%
msg_twist.Linear.X = 5;   % Nueva posición X
msg_twist.Linear.Y = -2;   % Nueva posición Y
msg_twist.Linear.Z = 0.0;   % Nueva posición Z
msg_twist.Angular.X = 0.0;  % Nueva orientación X
msg_twist.Angular.Y = 0.0;  % Nueva orientación Y
msg_twist.Angular.Z = pi; % Nueva orientación Z (en radianes)
send(velPub,msg_twist); %Envio
pause(1)
H=sub.LatestMessage
%%
rosshutdown;
```
-------------------------------------------------------------------
con el siguiente comando se creo el suscriber
```matlab
sub = rossubscriber('/turtle1/pose','turtlesim/Pose') 
```
 y en H se almacena el ultimo mensaje obtenido.
 
 para modificar la pose de la tortuga se usa el mensaje creado en
 msg_twist, en este se puede modificar la posición y orientación
 para despues ser enviado.
 
 Finalmente la forma de finalizar el nodo maestro es con el comando
 rosshutdown
 
 El funcionamiento de esta comunicación y operación de la tortuga
 puede visualizarce en los videos de:
 - matlab1.webm
 - matlab2.webm
 - matlab3.webm
 --------------------------------------------------------------
 
