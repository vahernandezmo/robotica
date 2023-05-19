import numpy as np
import math
from spatialmath.base import * 

# Definir la configuración del robot

def InvKine(x,y,z):
       L0 = 40.0
       L1 = 105.0  
       L2 = 105.0  
       L3 = 65.0  

       px=x
       py=y
       pz=z

       t1=math.atan2(py,px)
       c1=math.cos(t1)
       s1=math.sin(t1)

       rota=trotx(-math.pi/2) @ trotz(-math.pi/2)
       T_desired = np.array([
              [c1 ,-s1,0 ,1],
              [s1,c1 , 0,  1],
              [0 ,0 ,1 ,  1],
              [0, 0 , 0 , 1]
       ])@rota

       P04=np.array([px,py,pz])

       P03=P04-np.array([L3*c1,L3*s1,0])
       #print(T_desired)
       #print(P03,P04)
       cosT3=(P03[0]**2+P03[1]**2+(P03[2]-L0)**2-L1**2-L2**2)/(2*L1*L2)
       t3=math.atan2(math.sqrt(1-cosT3**2),cosT3)
       s3=math.sin(t3)
       alpha=math.atan2(P03[2]-L0,math.sqrt(P03[0]**2+P03[1]**2))
       beta=math.atan2(L2*s3,L1+L2*cosT3)
       t2=alpha-beta

       T01=trotz(t1)@transl(0.0,0.0,L0)@trotx(-math.pi/2)
       T12=trotz(t2)@transl(L1,0.0,0.0)
       T23=trotz(t3)@transl(L2,0.0,0.0)
       T03=T01@T12@T23


       t4=-t3-t2
       return (math.degrees(t1), math.degrees(t2), math.degrees(t3),math.degrees(t4))


def leer_parejas_csv(nombre_archivo):
    parejas = []
    print(nombre_archivo)
    with open(nombre_archivo, 'r') as archivo_csv:
        contenido = archivo_csv.read().strip().split('\n')
        for linea in contenido:
            x, y, z = linea.split(',')
            pareja = (float(x), float(y),float(z))
            parejas.append(pareja)
    return parejas

# Ejemplo de uso
nombre_archivo = 'Puntos_Arco_interno.csv'
puntos = leer_parejas_csv(nombre_archivo)
q_articulares=[]
for punto in puntos:
     q=InvKine(punto[0],punto[1],punto[2])
     q_articulares.append(q)

    




for qi in q_articulares:
       print(qi)