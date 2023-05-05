# Laboratorio 4

## Integrantes

- Luis Felipe Gutierrez Garnica
- Valentina Hernandez
- Manuel Alejandro Rojas

## Objetivos

- Crear todos los Joint Controllers con ROS para manipular servomotores Dynamixel AX-12 del robot Phantom X Pincher.
- Manipular los tópicos de estado y comando para todos los Joint Controllers del robot Phantom X Pincher.
- Manipular los servicios para todos los Joint Controllers del robot Phantom X Pincher.
- Conectar el robot Phantom X Pincher con MATLAB o Python usan ROS

## Mediciones

Se utlizo un calibrador pie de rey para hacer la medición de cada una de las distancias de los eslabones del robot.

Una vez medidos los eslabones se procedio ubicar cada una de los sistemas coordenados para obtener los parametros de DH.

finalmente para obtener nuestra posición de Home seleccionada se utilizaron unas posiciones de offset.

|i  | tetha (°)| d (mm)| a(mm)| alpha (°)| offset |
|---|----------|-------|------|----------|--------|
|1  |  q1      |   L_0 |  0   |   -90    | 0°     |
|2  |  q2      |   0   |  L1  |    0     | -90°   |
|3  |  q3      |   0   |  L2  |    0     |  80°   |
|4  |  q4      |   0   |  L3  |    0     |  0°    |
|noa|  -90     |   0   |  0   |    90    |  80°   |

Donde:

* L0=40 mm
* L1=105 mm
* L2=105 mm
* L3=65 mm

Posteriormente se realiza un un plot de esta posición de home desde el entorno de Matlab

De esta misma forma se realiza la intancia de un robot mediante serial link y se realiza la configuración de cada una de las posiciones esto se puede encontrar en el archivo de matlab toolbox.mlx. Se definió tambien la orientación del NOA respecto al ultimo eje de coordenadas.

1. 0, 0, 0, 0, 0.



2. -25, 15, -20, 20, 0.



3. 35,-35, 30, -30, 0.



4. -85, 20, -55, 17, 0.



5. -80, 35, -55, 45, 0.



Finalmente se le solicita mediante el metodo trchain() la orientación y posición que tendría el NOA para una determinada configuración de las articulaciones q1,q2,q3,q4,q5,q6. Esto incluye una serie de rotaciones puras y traslaciones puras que permiten dermirminar dicha pose. 

NOA=Rz(q1)Tz(4)Rx(90)Rz(q2)Tx(10.5)Rz(q3)Tx(10.5)Rz(q4)Tx(6.5)



