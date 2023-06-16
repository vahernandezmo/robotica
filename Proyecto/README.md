# Proyecto Robótica

## Integrantes:
* Manuel Rojas
* Felipe Gutierrez
* Valentina Hernandez

## Descripción de la solución [Valentina]
## Piezas de Alistamiento [Valentina]
## Herramienta 
Para la realización de la herramienta se decidió reutilizar la herramienta fabricada para el Laboratorio 1 ya que se considero que con unas modificaciones sobre la pieza "Soporte", dentro de estas modificaciones esta la realización de un agujero en la zona posterior para poder ingresar el gancho y otro en la zona frontal inferior para sacar la terminal de la ventosa.
Cada una de las modificaciones se modelo previamente y se verifico en el laboratorio junto con el robot ABB IRB 140 de tal forma que una vez realizados los cambios, la herramienta funcionara de manera correcta.
El modelado tambien permitió alcanzar una mejor aproximación de la herramienta en RoboStudio y permitió reducir los tiempos de calibración de cada una de las tareas. El modelado se realizo en una carpeta conjunta del equipo de trabajo en el software Fusion 360 de Autodesk.

![image](https://github.com/vahernandezmo/robotica_lab/assets/58895880/24b66ba0-d76f-4489-9e4d-f645a37d35bf)

Este plano puede verse en detalle en la carpeta /Herramienta/Plano Ensamble Herramienta.pdf

## Modelado de Estanteria y banda trnasportadora

Los modelados de estas dos piezas se realizaron a partir de las medidas tomadas en el laboratorio con un flexometro como instrumento de medidad con una presición de 1 mm. Estos permitieron la implementación posterior en RobotStudio.

A continuación pueden verse imagenes referentes a estas piezas, la banda transportadora se modelo como un rectangulo a fin de simplificar la representación con la fisica necesaria.

![Estanteria](https://github.com/vahernandezmo/robotica_lab/assets/58895880/415717fa-8442-4eb6-a700-ccba60f542d2)
![banda Transportadora](https://github.com/vahernandezmo/robotica_lab/assets/58895880/fd63cd61-4199-4487-a889-b1eba3a1e636)

## Modelo en RobotStudio
Para la implementación en el entorno de RobotStudio se tienen diversos componentes que conforman la totalidad del desarrollo del proyecto; empezando por el manipulador IRB140 , el cual se importa desde la librería del programa y el controlador RobotWare 6.12 que permite el movimiento del manipulador para que se comporte como un brazo robótico. Las piezas CAD 3D que se importaron para simular la estación virtual se contabilizan en: un balde, un bloque banda transportadora, un estante, una herramienta (compuesta por la ventosa, el gancho y la estructura) y seis piezas para la estantería. Todas estas piezas se guardan dentro de la librería local del proyecto para que se pueden exportar de forma sencilla.
Como primer paso se ubicaron cada uno de los componentes en lugares definidos por el equipo que tuvieran la condición de que se ubicaran dentro del espacio diestro del robot, posteriormente se definieron tres “WorkObjects” para tener una facilidad de configuración de posicionamiento de cada uno de los puntos por sobre los cuales iban a estar definidas las trayectorias. Estos corresponden a tres puntos (visibles en la imagen); el primero esta ubicado en una esquina de la banda transportadora; el segundo se encuentra a nivel del piso y que está asociada con la ubicación del balde en el piso; y el tercero que se ubica en una esquina de la estantería. Cada uno de estos “WorkObjects” esta vinculado a los modelados por lo que, si se desplazan adrede, estos se desplazaran con su respectiva pieza.
La herramienta a ser usada se crea dentro del espacio de trabajo asociado a los mecanismos, en la imagen se observa que su nombre corresponde a “PF_Robotica”, esto se hace para que, de manera posterior, se le puedan asignar acciones dentro de las rutinas de los “SmartComponents”. Luego de esto es posible asociarla al brazo robótico para que, de manera automática, se ubique en el extremo del efector final.

![RobotStudio](https://github.com/vahernandezmo/robotica_lab/assets/14100413/89225e0c-5084-49fd-b5bf-2b1522c1f75d)

Ya que varias de las piezas que componen al espacio de trabajo, van a estar interactuando una con otras, se configuran las propiedades físicas de cada una de ellas dependiendo del nivel de interacción que van a tener. Por ejemplo, el “Balde” es una pieza con un tipo de comportamiento físico dinámico, mientras que la “Banda” es de tipo fijo. Además de la definición del comportamiento físico, también se configuraron algunas piezas del entorno para que fueran asociadas como “SmartComponents”, con esto fue posible asignarles acciones de interacción tales como; ubicación de la pieza en una posición establecida ante el accionamiento de una entrada virtual al controlador o asociar el cambio de posición del componente con el movimiento hecho por el robot. A la derecha de la imagen se pueden visualizar algunas de las entradas y salidas digitales que permiten activar estos comportamientos, otras se encuentran dentro del mismo código RAPID.
Finalmente se crean las trayectorias a partir de puntos definidos asociados a cada uno de los WorkObjects para el desarrollo de las rutinas que va a desempeñar el robot, para posteriormente ser sincronizados con el código en RAPID y ser simulados en el entorno virtual y programados en los robots del LABSiR.       
A continuación, se presentan cuatro videos correspondientes a las cuatro rutinas que tiene que cumplir el manipulador en donde se toman cuatro piezas del estante al azar para ser llevadas dentro del balde.

https://github.com/vahernandezmo/robotica_lab/assets/14100413/757da0cf-7143-4dbb-8f1d-cca71a1707f7
https://github.com/vahernandezmo/robotica_lab/assets/14100413/859d00cb-b065-4559-8b13-86100bc24aee
https://github.com/vahernandezmo/robotica_lab/assets/14100413/67a7f302-7c6a-4b91-9c3a-a1624d353f84
https://github.com/vahernandezmo/robotica_lab/assets/14100413/9cb221b8-c924-4923-aa2b-dfc30d30dc7a

## Codigo en RAPID[Manuel]
## Comparación entre Operación Manual y Operación Automatizada[Valentina]
## Video de Presentación [Felipe]


## 
