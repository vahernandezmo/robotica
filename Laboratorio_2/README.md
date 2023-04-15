# Laboratorio 2

## Codigo en RAPID

Para el codigo se reutilizo parte del codigo del laboratorio 1 como rutina de trabajo
De tal forma que se definieron unos puntos de aproximación a la rutina de trabajo 
para iniciar y finalizar. Además se crearon 2 entradas digitales y 2 salidas digitales
Que posteriomente se renombraron según el nombre indicado en el Flexpendant de el robot
industrial del laboratorio del LABSIR. Se crearon una serie de trayectorias independientes
con los puntos asociados del dibujo de letras, la posición de home y la posición de
cambio de la herramienta. Posteriomente se agrupo en un path definido como 'main' 
en el que se agrupan todas las trayectorias con una serie instrucciones de espera de la 
activación de las entradas digitales que permitan realizar el inicio de la rutina de trabajo
y el inicio del movimiento hacia la posición de cambio de herramienta. Tambien se realizo
la definición de set y off para una salida digital que esta encendida desde el inicio de la 
rutina de trabajo hasta que se inicia la rutina de cambio de herramienta, momento en el cual
su valor lógico pasa a cero. Para los movimientos a la posición de Home y herramienta se 
utilizaron comandos de MoveJ y para la rutina de trabajo MoveL a una velocidad v100.

Todo este procedimiento puede verse en el video de la simulación en el que se pueden 
visualizar las entradas y salidas y su intervención en el desarrollo de toda la aplicación
su activación y apagado segun lo indicado en el parrafo anterior.
