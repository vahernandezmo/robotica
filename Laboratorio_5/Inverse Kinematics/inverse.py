import numpy as np
import math
from roboticstoolbox import DHRobot, RevoluteDH
from spatialmath.base import *

# Definir la configuración del robot
L0 = 1.0
L1 = 1.0  # Longitud del primer eslabón
L2 = 1.0  # Longitud del segundo eslabón
L3 = 1.0  # Longitud del tercer eslabón

# Crear el modelo del robot
robot = DHRobot([
    RevoluteDH(d=L0, a=0, alpha=0),
    RevoluteDH(d=0, a=L1, alpha=0,offset=-math.pi/2),
    RevoluteDH(d=0, a=L2, alpha=0,offset=math.pi*8/18),
    RevoluteDH(d=0, a=L3, alpha=0)
])



# Definir la posición y orientación deseada
px=1.
py=1.
pz=1.

t1=math.atan2(py,px)
c1=math.cos(t1)
s1=math.sin(t1)
print(t1,c1,s1)

rota=trotx(-math.pi/2) @ trotz(-math.pi/2)
T_desired = np.array([
       [c1 ,-s1,0 ,1],
       [s1 ,c1 , 0,  1],
       [0 ,0 ,1 ,  1],
       [0, 0 , 0 , 1]
]) @ rota

print(T_desired)

# Calcular la configuración de las articulaciones para alcanzar la pose deseada
q_solutions = robot.ikine_LM(T_desired,1000)

# Mostrar las soluciones de configuración de las articulaciones
for i, q_solution in enumerate(q_solutions):
    print(f"Solución {i+1}: {(q_solution)} (radianes)")
    
