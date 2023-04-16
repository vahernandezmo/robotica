# Laboratorio 2

## Descripción de la solución planteada

Para el codigo se reutilizo parte del codigo del laboratorio 1 como rutina de trabajo de tal forma que se definieron unos puntos de aproximación a la rutina de trabajo para iniciar y finalizar. Además se crearon 2 entradas digitales y 2 salidas digitales que posteriomente se renombraron según el nombre indicado en el Flexpendant, denominadas DI_01, DI_02 y DO_03, del robot industrial del laboratorio del LABSIR. Se crearon una serie de trayectorias independientes con los puntos asociados del dibujo de letras, la posición de home y la posición de cambio de la herramienta. Posteriomente se agrupo en un path definido como 'main' en el que se agrupan todas las trayectorias con una serie instrucciones de espera de la activación de las entradas digitales que permitan realizar el inicio de la rutina de trabajo y el inicio del movimiento hacia la posición de cambio de herramienta. Tambien se realizo la definición de set y off para una salida digital que esta encendida desde el inicio de la rutina de trabajo hasta que se inicia la rutina de cambio de herramienta, momento en el cual su valor lógico pasa a cero. Para los movimientos a la posición de Home y herramienta se utilizaron comandos de MoveJ y para la rutina de trabajo MoveL a una velocidad v100. 

```html
    PROC main()
		Home1;
		WaitDI EntDI_1,1;
		SetDO SalDO_1,1;
		Path_10;
		Path_20;
		Home1;
		WaitDI EntDI_2,1;
		ToolChange;
		SetDO SalDO_1,0;
    ENDPROC
```

Todo este procedimiento puede verse en el video de la simulación en el que se pueden visualizar las entradas y salidas y su intervención en el desarrollo de toda la aplicación su activación y apagado segun lo indicado en el parrafo anterior.

## Resultado

El desarrollo del laboratorio empezó con la identificación de los nombres con los que el controlador del manipulador identificaba cada una de las entradas y salidas digitales provenientes de una botonera previamente cableada. Después de obtener esta información se procedió a escribir dichos identificadores dentro del código de RAPID para que fueran reconocidas dentro del código y posteriormente, al ser cargadas al Flex Pendant, estás fueron compatibles.

Una serie de inconvenientes surgieron en cuanto a la transmisión del archivo de código de RobotSudio al Flex Pendant ya que la memoria USB no estaba siendo detectada por este último. Después del cambio a tres distintos dispositivos, finalmente se encontró la forma de transmitir el código para que fuera leído y cargado.

https://user-images.githubusercontent.com/14100413/232258565-9e41a4ac-2939-4639-b38b-d1a157677eae.mp4

<br>

En el video se puede observar, inmediatamente al empezar que se activa el primer botón para empezar con la secuencia de movimiento de arranque, esto a su vez ocasionó que la única salida digital configurada cambiara su estado a un “1“ lógico, evidenciado por la luz de color azul ubicada en la botonera del robot. Vale la pena mencionar que el desarrollo se realizó de manera secuencial paso a paso con ayuda de los botones del Flex Pendant por seguridad (en pruebas anteriores, una configuración del work Object errada ocasiono que la herramienta de trabajo sufriera daños en el marcador y en su soporte). En el segundo 56 se observa que el robot termina su primera secuencia de comandos y en el segundo 59 se presiona el botón 2 para iniciar con una segunda secuencia de movimiento; a la mitad del recorrido (minuto 1:22) se evidencia el cambio de estado en el led azul de la botonera, lo que indica que la única salida digital alterno al llegar al punto extremo asignado al robot por medio del código. Finalmente, el robot llega a la posición de Home como estaba previsto desde un principio. 

Debido a que el objetivo del laboratorio era el control de rutinas con entradas digitales, se utilizó un workobject que acercara el robot al tablero pero que además asegurara que la herramienta no sufriera daños, por lo que puede verse que inicialmente el robot escribe algunas partes de una letra y el resto de la rutina de escritura la realiza en el aire.  
