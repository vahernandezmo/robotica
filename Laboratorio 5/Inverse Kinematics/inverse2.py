import numpy as np
import math
from roboticstoolbox import DHRobot, RevoluteDH
from spatialmath.base import tr2rpy

# Definir la configuración del robot
L1 = 1.0  # Longitud del primer eslabón
L2 = 1.0  # Longitud del segundo eslabón
L3 = 1.0  # Longitud del tercer eslabón

# Crear el modelo del robot
robot = DHRobot([
    RevoluteDH(d=0, a=L1, alpha=math.pi/2),
    RevoluteDH(d=0, a=L2, alpha=0),
    RevoluteDH(d=0, a=L3, alpha=0)
])

# Definir la posición y orientación deseada
T_desired = np.array([
     [-1 ,0 ,0 , 0],
       [0, 0, -1,  0],
       [0 ,-1 ,0 , 1],
       [0, 0 , 0 , 1]
])

# Calcular la configuración de las articulaciones para alcanzar la pose deseada
q_solutions = robot.ikine_LM(T_desired)

# Mostrar las soluciones de configuración de las articulaciones
for i, q_solution in enumerate(q_solutions):
    print(f"Solución {i+1}: {(q_solution)} (radianes)")
    
