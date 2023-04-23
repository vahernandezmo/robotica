clear
clc
%%
rosinit; %Conexion con nodo maestro
%%
velPub = rospublisher('/turtle1/cmd_vel','geometry_msgs/Twist'); %Creaci ́on publicador
velMsg = rosmessage(velPub); %Creaci ́on de mensaje
sub = rossubscriber('/turtle1/pose','turtlesim/Pose')
%%
velMsg.Linear.X =1 ; %Valor del mensaje1
send(velPub,velMsg); %Envio
pause(1)
H=sub.LatestMessage
