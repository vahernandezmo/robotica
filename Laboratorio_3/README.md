# Laboratorio 3

Para el desarrollo del laboratorio 3 se realizo un proceso siguiendo
el repositorio creado por el ing. Felipe Gonzales
https://github.com/fegonzalez7/rob_unal_clase2
Este permitió configurar e instalar el programa de manera correcta 
en los ordenadores de los integrantes del grupo.

Como una primera aproximación se plantea desarrollar el ejercicio que emularía al “hola mundo” de los lenguajes de programación aplicado el entorno de desarrollo ROS, con el fin de familiarizarnos con sus características principales. Para ello, y después de haber instalado todos los programas pertinentes, clonamos en nuestro computador el repositorio https://github.com/felipeg17/hello_turtle.git dentro del directorio catkin_ws/src. En nuestro caso, decidimos instalar un entorno para la terminal de Linux llamado Kitty el cual nos permitió abrir cuatro terminales mostrados de forma simultanea. El directorio que se escoge para desarrollar el ejercicio no es aleatorio ya que la idea es ejecutar ROS mediante el compilador catkit.

En una primera terminal se corre el comando “roscore” lo cual nos permite inicializar ROS y se le dice al sistema que una instancia de ROS se va a estar ejecutando. En la segunda terminal se le indica a esa instancia de ROS que se va a correr el programa de “turtlesim”, específicamente, un nodo que muestra mediante una interfaz gráfica la ubicación de una tortuga y que permanentemente esta enviando su ubicación y orientación; de por si hasta este punto no es posible interactuar con la tortuga. En la tercera terminal se ejecuta un nodo el cual es capaz de justamente esto, “turtle_teleop_key” permite registrar entradas de teclado para enviarle instrucciones de movimiento a la tortuga que se pueden ver mediante la interfaz gráfica. 

Ya que la finalidad del laboratorio es realizar comunicaciones desde distintos programas (Python y Matlab) en este primer paso estas instrucciones son enviadas desde consola. Con todos los nodos, para este caso en particular activos, se envía una instrucción desde consola, enviando directamente un mensaje con instrucciones de movimiento para que la tortuga siga una trayectoria deseada. En la imagen siguiente se pueden visualizar las cuatro consolas de Linux abiertas y la interfaz gráfica con el movimiento de la tortuga indicado ya ejecutado junto con el código utilizado e instrucciones. 

```linux
rostopic pub -1 /turtle1/cmd_vel geometry_msgs/Twist "linear:
  x: 1.0
  y: 0.0
  z: 0.0
angular:
  x: 0.0
  y: 0.0
  z: 1.0" 
```
![ROSturtle](https://user-images.githubusercontent.com/14100413/235314796-850c5068-aab0-45d2-8cb5-9dbc6274096b.png)

## Matlab: 
Para la realización de operar Turtlesim mediante Matlab, para
el que fue necesario instalar el toolbox de Robotica de Mathworks.

<p>Se probó el script de la guia de laboratorio.</p>
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
 
