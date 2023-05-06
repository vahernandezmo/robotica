# Laboratorio 4

## Integrantes

- Luis Felipe Gutierrez Garnica
- Valentina Hernandez
- Manuel Alejandro Rojas

## Objetivos

- Crear todos los Joint Controllers con ROS para manipular servomotores Dynamixel AX-12 del robot Phantom X Pincher.
- Manipular los tópicos de estado y comando para todos los Joint Controllers del robot Phantom X Pincher.
- Manipular los servicios para todos los Joint Controllers del robot Phantom X Pincher.
- Conectar el robot Phantom X Pincher con MATLAB o Python usan ROS.

## Mediciones
<div>
<p align = 'center'>
<img src="./images/medicion.jpeg" alt="Medición" width="400px">
</p>
</div>

Se utlizo un calibrador pie de rey para hacer la medición de cada una de las distancias de los eslabones del robot.

Una vez medidos los eslabones se procedio ubicar cada una de los sistemas coordenados para obtener los parametros de DH.

![pincher](https://user-images.githubusercontent.com/58895880/236598385-da5cd57b-954f-4532-a6f4-c3b4995d4cc8.png)

finalmente para obtener nuestra posición de Home seleccionada se utilizaron unas posiciones de offset.

![home](https://user-images.githubusercontent.com/58895880/236598044-2d5e0569-e7f1-4d22-b5d3-cf59a024e24d.png)


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

![home](https://user-images.githubusercontent.com/58895880/236598081-2b40471e-6a1a-4a12-a574-d03b2bc383e6.png)


2. -25, 15, -20, 20, 0.

![pose1](https://user-images.githubusercontent.com/58895880/236598085-8fcf66a6-bf32-4392-8cc5-c61afad3e86a.png)


3. 35,-35, 30, -30, 0.

![pose2](https://user-images.githubusercontent.com/58895880/236598091-b507c97b-331f-4db1-8bf0-d15be9c3f775.png)


4. -85, 20, -55, 17, 0.

![pose3](https://user-images.githubusercontent.com/58895880/236598107-a61e3464-0af2-4839-9ea7-20db86fc7c65.png)


5. -80, 35, -55, 45, 0.

![pose4](https://user-images.githubusercontent.com/58895880/236598112-f956ba10-1d81-45eb-97fa-f7b08cd668d3.png)

Finalmente se le solicita mediante el metodo trchain() la orientación y posición que tendría el NOA para una determinada configuración de las articulaciones q1,q2,q3,q4,q5,q6. Esto incluye una serie de rotaciones puras y traslaciones puras que permiten dermirminar dicha pose. 

NOA=Rz(q1)Tz(4)Rx(90)Rz(q2)Tx(10.5)Rz(q3)Tx(10.5)Rz(q4)Tx(6.5)



