import numpy as np
import math
import time
from spatialmath.base import * 
from moveRobot import Robot
import rospy
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
       print(P03,P04)
       cosT3=(P03[0]**2+P03[1]**2+(P03[2]-L0)**2-L1**2-L2**2)/(2*L1*L2)
       print(P04)
       print(cosT3)
       t3=math.atan2(-math.sqrt(1-cosT3**2),cosT3)

       s3=math.sin(t3)
       alpha=math.atan2(P03[2]-L0,math.sqrt(P03[0]**2+P03[1]**2))
       beta=math.atan2(L2*s3,L1+L2*cosT3)
       t2=alpha-beta
       """
       if t2 < -65*(math.pi)/180:
            #t3 = -t3
            s3=math.sin(t3)
            alpha=math.atan2(P03[2]-L0,math.sqrt(P03[0]**2+P03[1]**2))
            beta=math.atan2(L2*s3,L1+L2*cosT3)
            t2 = alpha-beta
        """

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
            y, x, z = linea.split(',')
            pareja = (float(x)*10, float(y)*10,float(z)*10)
            parejas.append(pareja)
    return parejas


if __name__ == '__main__':
    robot = Robot()

            
    #for qi in q_articulares:
        # print(qi)

    try:
        robot.poseRobot(0,0,0,0,0)
        time.sleep(0.1)
    

        while not rospy.is_shutdown():
            """
            robot.poseRobot(0,0,0,0,0)
            time.sleep(1)
            print(q_articulares[0])
            robot.poseRobot(q_articulares[0][0], q_articulares[0][1], q_articulares[0][2], q_articulares[0][3],-100)
            time.sleep(1)
            print(q_articulares[0])
            """
            alt = input("""Ingrese el dibujo que desee realizar:
            0. Tomar marcador
            1. Arco interno
            2. Arco externo
            3. Letras
            4. Cara
            5. Dejar marcador
            """)
            if alt == "0":
                robot.poseRobot(0,70-60,48-150,242-150,100)
                time.sleep(2)
                robot.poseRobot(230-150,75-60,33-150,250-150,100)
                robot.poseRobot(230-150,80-60,62-150,225-150,100)
                robot.poseRobot(230-150,80-60,62-150,225-150,-105)
                time.sleep(2)
                robot.poseRobot(230-150,90-60,80-150,230-150,-105)
                robot.poseRobot(0,0,0,0,-105)
                continue
            elif alt == "1":
                nombre_archivo = 'Arc_interno.csv'
                puntos = leer_parejas_csv(nombre_archivo)
                q_articulares=[]
                for punto in puntos:
                    q=InvKine(punto[0],punto[1],punto[2])
                    q_articulares.append(q)
            elif alt == "2":
                nombre_archivo = 'Arc_externo.csv'
                puntos = leer_parejas_csv(nombre_archivo)
                q_articulares=[]
                for punto in puntos:
                    q=InvKine(punto[0],punto[1],punto[2])
                    q_articulares.append(q)        
            elif alt == "3":
                nombre_archivo = 'Letras.csv'
                puntos = leer_parejas_csv(nombre_archivo)
                q_articulares=[]
                for punto in puntos:
                    q=InvKine(punto[0],punto[1],punto[2])
                    q_articulares.append(q)
            elif alt == "4":
                nombre_archivo = 'Cara2.csv'
                puntos = leer_parejas_csv(nombre_archivo)
                q_articulares=[]
                for punto in puntos:
                    q=InvKine(punto[0],punto[1],punto[2])
                    q_articulares.append(q)
            elif alt == "5":
                robot.poseRobot(232-150,90-60,80-150,230-150,-105)
                time.sleep(2)
                robot.poseRobot(232-150,90-60,50-150,225-150,-105)
                time.sleep(2)
                robot.poseRobot(232-150,90-60,50-150,225-150,100)
                robot.poseRobot(232-150,75-60,33-150,250-150,100)
                robot.poseRobot(0,0,0,0,0)
                continue
            else:
                print("Opción no valida")
                continue   
            for qi in q_articulares:
                robot.poseRobot(qi[0], qi[1], qi[2], qi[3],-105)
                print(qi)
            print("Done")
            robot.poseRobot(0,30,0,10,-105)
            time.sleep(1)
            robot.poseRobot(0,0,0,0,-105)
    except rospy.ROSInterruptException:
        pass

    
           
        
    
