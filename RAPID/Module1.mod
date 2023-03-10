MODULE Module1
	TASK PERS tooldata lab1_tool_t1:=[TRUE,[[0,0,0],[1,0,0,0]],[-1,[0,0,0],[1,0,0,0],0,0,0]];
    CONST robtarget AInicio:=[[-176.185998195,-371.405,-549.410082335],[0.866025404,0,-0.5,0],[0,0,0,0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]];
    CONST robtarget FTarget_10:=[[0,-225.593,0],[1,0,0,0],[0,0,0,0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]];
    CONST robtarget FTarget_20:=[[0,-209.44,0],[1,0,0,0],[0,0,0,0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]];
    CONST robtarget FTarget_30:=[[-80,-209.44,0],[1,0,0,0],[0,0,0,0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]];
    CONST robtarget FTarget_40:=[[-80,-264.284,0],[1,0,0,0],[0,0,0,0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]];
    CONST robtarget FTarget_50:=[[-66.466,-264.284,0],[1,0,0,0],[0,0,0,0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]];
    CONST robtarget FTarget_60:=[[-66.466,-225.593,0],[1,0,0,0],[0,0,0,0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]];
    CONST robtarget FTarget_70:=[[-47.849,-225.879,0],[1,0,0,0],[0,0,0,0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]];
    CONST robtarget FTarget_80:=[[-47.53,-258.99,0],[1,0,0,0],[0,0,0,0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]];
    CONST robtarget FTarget_90:=[[-33.997,-258.99,0],[1,0,0,0],[0,0,0,0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]];
    CONST robtarget FTarget_100:=[[-33.164,-226.306,0],[1,0,0,0],[0,0,0,0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]];
    CONST robtarget FTarget_110:=[[0,-225.593,0],[1,0,0,0],[0,0,0,0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]];
    CONST robtarget FTM1:=[[0,-225.593,-100],[1,0,0,0],[0,0,0,0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]];
    CONST robtarget FTM2:=[[0,-84.966,-100],[1,0,0,0],[0,0,0,0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]];
    CONST robtarget mTarget_10:=[[0,-84.966,0],[1,0,0,0],[0,0,0,0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]];
    CONST robtarget mTarget_20:=[[-80,-84.966,0],[1,0,0,0],[0,0,0,0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]];
    CONST robtarget mTarget_30:=[[-80,-109.14,0],[1,0,0,0],[0,0,0,0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]];
    CONST robtarget mTarget_40:=[[-25.429,-123.656,0],[1,0,0,0],[0,0,0,0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]];
    CONST robtarget mTarget_50:=[[-80,-138.008,0],[1,0,0,0],[0,0,0,0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]];
    CONST robtarget mTarget_60:=[[-76.954,-162.904,0],[1,0,0,0],[0,0,0,0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]];
    CONST robtarget mTarget_70:=[[0,-162.237,0],[1,0,0,0],[0,0,0,0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]];
    CONST robtarget mTarget_80:=[[0.53,-147.013,0],[1,0,0,0],[0,0,0,0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]];
    CONST robtarget mTarget_90:=[[-62.974,-147.23,0],[1,0,0,0],[0,0,0,0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]];
    CONST robtarget mTarget_100:=[[0,-131.35,0],[1,0,0,0],[0,0,0,0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]];
    CONST robtarget mTarget_110:=[[0,-115.798,0],[1,0,0,0],[0,0,0,0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]];
    CONST robtarget mTarget_120:=[[-62.974,-99.973,0],[1,0,0,0],[0,0,0,0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]];
    CONST robtarget mTarget_130:=[[-0.986,-101.003,0],[1,0,0,0],[0,0,0,0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]];
    CONST robtarget mTarget_140:=[[0,-84.966,0],[1,0,0,0],[0,0,0,0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]];
    CONST robtarget MTV1:=[[0,-84.966,-100],[1,0,0,0],[0,0,0,0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]];
    CONST robtarget MTV2:=[[0.326,-0.089,-100],[1,0,0,0],[0,0,0,0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]];
    CONST robtarget vTarget_10:=[[0.326,-0.089,0],[1,0,0,0],[0,0,0,0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]];
    CONST robtarget vTarget_20:=[[-80.066,28.469,0],[1,0,0,0],[0,0,0,0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]];
    CONST robtarget vTarget_30:=[[-80.616,11.146,0],[1,0,0,0],[0,0,0,0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]];
    CONST robtarget vTarget_40:=[[-20.791,-9.168,0],[1,0,0,0],[0,0,0,0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]];
    CONST robtarget vTarget_50:=[[-80,-28.758,0],[1,0,0,0],[0,0,0,0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]];
    CONST robtarget vTarget_60:=[[-80,-45.893,0],[1,0,0,0],[0,0,0,0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]];
    CONST robtarget vTarget_70:=[[0,-17.244,0],[1,0,0,0],[0,0,0,0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]];
    CONST robtarget vTarget_80:=[[0.326,-0.089,0],[1,0,0,0],[0,0,0,0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]];
    CONST robtarget vTarget_80_final:=[[0.326,-0.089,-100],[1,0,0,0],[0,0,0,0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]];
    CONST robtarget ZInicio:=[[0,-225.593,-100],[1,0,0,0],[0,0,0,0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]];
    CONST robtarget Target_10:=[[487.129610538,400,0],[0.120773877,-0.120773877,0.696716349,-0.696716349],[0,0,0,0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]];
    CONST robtarget Target_20:=[[407.129610538,371.405183254,0],[0.120773877,-0.120773877,0.696716349,-0.696716349],[0,0,0,0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]];
    CONST robtarget Target_30:=[[-176.185998195,-371.405,-549.410082335],[0.866025404,0,-0.5,0],[0,0,0,0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]];
    CONST robtarget Target_40:=[[487.129610538,325.511592804,0],[0.696679799,-0.696679799,0.120984533,-0.120984533],[0,0,0,0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]];
    CONST robtarget Target_50:=[[487.129610538,342.646655021,0],[0.5,-0.5,-0.5,0.5],[0,0,0,0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]];
    CONST robtarget Target_60:=[[427.920883655,362.237378536,0],[0.112493368,-0.112493368,-0.698101169,0.698101169],[0,0,0,0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]];
    CONST robtarget Target_70:=[[487.129610538,382.482947288,0],[0.697533719,-0.697533719,-0.115959956,0.115959956],[0,0,0,0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]];
    CONST robtarget Target_80:=[[487.129610538,286.4392938,0],[0,0,-0.707106781,0.707106781],[0,0,0,0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]];
    CONST robtarget Target_90:=[[407.129610538,286.4392938,0],[0,0,-0.707106781,0.707106781],[0,0,0,0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]];
    CONST robtarget Target_100:=[[407.129610538,271.432475029,0],[0.5,-0.5,0.5,-0.5],[0,0,0,0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]];
    CONST robtarget Target_110:=[[470.103691577,271.432475029,0],[0.707106781,-0.707106781,0,0],[0,0,0,0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]];
    CONST robtarget Target_120:=[[407.129610538,255.607098518,0],[0.086825756,-0.086825756,0.701755861,-0.701755861],[0,0,0,0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]];
    CONST robtarget Target_130:=[[407.129610538,240.054568229,0],[0.5,-0.5,0.5,-0.5],[0,0,0,0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]];
    CONST robtarget Target_140:=[[470.103691577,224.174632011,0],[0.701720432,-0.701720432,0.087111627,-0.087111627],[0,0,0,0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]];
    CONST robtarget Target_150:=[[407.129610538,224.174632011,0],[0,0,-0.707106781,0.707106781],[0,0,0,0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]];
    CONST robtarget Target_160:=[[407.129610538,209.167803703,0],[0.5,-0.5,0.5,-0.5],[0,0,0,0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]];
    CONST robtarget Target_170:=[[487.129610538,209.167803703,0],[0.707106781,-0.707106781,0,0],[0,0,0,0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]];
    CONST robtarget Target_180:=[[487.129610538,233.397005973,0],[0.5,-0.5,-0.5,0.5],[0,0,0,0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]];
    CONST robtarget Target_190:=[[432.55935049,247.748984275,0],[0.090675094,-0.090675094,-0.701268869,0.701268869],[0,0,0,0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]];
    CONST robtarget Target_200:=[[487.129610538,262.264670311,0],[0.701141063,-0.701141063,-0.09165811,0.09165811],[0,0,0,0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]];
    CONST robtarget Target_210:=[[487.129610538,286.4392938,0],[0.5,-0.5,-0.5,0.5],[0,0,0,0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]];
    CONST robtarget Target_220:=[[441.126879215,145.811728416,0],[0,0,0.707106781,0.707106781],[0,0,0,0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]];
    CONST robtarget Target_230:=[[407.129610538,145.811728416,0],[0,0,0.707106781,0.707106781],[0,0,0,0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]];
    CONST robtarget Target_240:=[[407.129610538,161.96452993,0],[0.5,0.5,0.5,0.5],[0,0,0,0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]];
    CONST robtarget Target_250:=[[487.129610538,161.96452993,0],[0.707106781,0.707106781,0,0],[0,0,0,0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]];
    CONST robtarget Target_260:=[[487.129610538,107.121409355,0],[0.5,0.5,-0.5,-0.5],[0,0,0,0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]];
    CONST robtarget Target_270:=[[473.596185207,107.121409355,0],[0,0,0.707106781,0.707106781],[0,0,0,0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]];
    CONST robtarget Target_280:=[[473.596185207,145.811728416,0],[0.5,0.5,0.5,0.5],[0,0,0,0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]];
    CONST robtarget Target_290:=[[454.660304546,145.811728416,0],[0,0,0.707106781,0.707106781],[0,0,0,0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]];
    CONST robtarget Target_300:=[[454.660304546,112.414740501,0],[0.5,0.5,-0.5,-0.5],[0,0,0,0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]];
    CONST robtarget Target_310:=[[441.126879215,112.414740501,0],[0,0,0.707106781,0.707106781],[0,0,0,0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]];
    CONST robtarget Target_320:=[[441.126879215,145.811728416,0],[0.5,0.5,0.5,0.5],[0,0,0,0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]];
    !***********************************************************
    !
    ! Módulo:  Module1
    !
    ! Descripción:
    !   <Introduzca la descripción aquí>
    !
    ! Autor: Valentina
    !
    ! Versión: 1.0
    !
    !***********************************************************
    
    
    !***********************************************************
    !
    ! Procedimiento Main
    !
    !   Este es el punto de entrada de su programa
    !
    !***********************************************************
    PROC main()
        Close;
        Letters;
        Close;
        !Añada aquí su código
    ENDPROC
    PROC Letters()
        MoveL FTarget_10,v100,z10,Tooldata_MARCADOR\WObj:=Workobject_INICIALES;
        MoveL FTarget_20,v100,z10,Tooldata_MARCADOR\WObj:=Workobject_INICIALES;
        MoveL FTarget_30,v100,z10,Tooldata_MARCADOR\WObj:=Workobject_INICIALES;
        MoveL FTarget_40,v100,z10,Tooldata_MARCADOR\WObj:=Workobject_INICIALES;
        MoveL FTarget_50,v100,z10,Tooldata_MARCADOR\WObj:=Workobject_INICIALES;
        MoveL FTarget_60,v100,z10,Tooldata_MARCADOR\WObj:=Workobject_INICIALES;
        MoveL FTarget_70,v100,z10,Tooldata_MARCADOR\WObj:=Workobject_INICIALES;
        MoveL FTarget_80,v100,z10,Tooldata_MARCADOR\WObj:=Workobject_INICIALES;
        MoveL FTarget_90,v100,z10,Tooldata_MARCADOR\WObj:=Workobject_INICIALES;
        MoveL FTarget_100,v100,z10,Tooldata_MARCADOR\WObj:=Workobject_INICIALES;
        MoveL FTarget_110,v100,z10,Tooldata_MARCADOR\WObj:=Workobject_INICIALES;
        MoveL FTM1,v100,z10,Tooldata_MARCADOR\WObj:=Workobject_INICIALES;
        MoveL FTM2,v100,z10,Tooldata_MARCADOR\WObj:=Workobject_INICIALES;
        MoveL mTarget_10,v100,z10,Tooldata_MARCADOR\WObj:=Workobject_INICIALES;
        MoveL mTarget_20,v100,z10,Tooldata_MARCADOR\WObj:=Workobject_INICIALES;
        MoveL mTarget_30,v100,z10,Tooldata_MARCADOR\WObj:=Workobject_INICIALES;
        MoveL mTarget_40,v100,z10,Tooldata_MARCADOR\WObj:=Workobject_INICIALES;
        MoveL mTarget_50,v100,z10,Tooldata_MARCADOR\WObj:=Workobject_INICIALES;
        MoveL mTarget_60,v100,z10,Tooldata_MARCADOR\WObj:=Workobject_INICIALES;
        MoveL mTarget_70,v100,z10,Tooldata_MARCADOR\WObj:=Workobject_INICIALES;
        MoveL mTarget_80,v100,z10,Tooldata_MARCADOR\WObj:=Workobject_INICIALES;
        MoveL mTarget_90,v100,z10,Tooldata_MARCADOR\WObj:=Workobject_INICIALES;
        MoveL mTarget_100,v100,z10,Tooldata_MARCADOR\WObj:=Workobject_INICIALES;
        MoveL mTarget_110,v100,z10,Tooldata_MARCADOR\WObj:=Workobject_INICIALES;
        MoveL mTarget_120,v100,z10,Tooldata_MARCADOR\WObj:=Workobject_INICIALES;
        MoveL mTarget_130,v100,z10,Tooldata_MARCADOR\WObj:=Workobject_INICIALES;
        MoveL mTarget_140,v100,z10,Tooldata_MARCADOR\WObj:=Workobject_INICIALES;
        MoveL MTV1,v100,z10,Tooldata_MARCADOR\WObj:=Workobject_INICIALES;
        MoveL MTV2,v100,z10,Tooldata_MARCADOR\WObj:=Workobject_INICIALES;
        MoveL vTarget_10,v100,z10,Tooldata_MARCADOR\WObj:=Workobject_INICIALES;
        MoveL vTarget_20,v100,z10,Tooldata_MARCADOR\WObj:=Workobject_INICIALES;
        MoveL vTarget_30,v100,z10,Tooldata_MARCADOR\WObj:=Workobject_INICIALES;
        MoveL vTarget_40,v100,z10,Tooldata_MARCADOR\WObj:=Workobject_INICIALES;
        MoveL vTarget_50,v100,z10,Tooldata_MARCADOR\WObj:=Workobject_INICIALES;
        MoveL vTarget_60,v100,z10,Tooldata_MARCADOR\WObj:=Workobject_INICIALES;
        MoveL vTarget_70,v100,z10,Tooldata_MARCADOR\WObj:=Workobject_INICIALES;
        MoveL vTarget_80,v100,z10,Tooldata_MARCADOR\WObj:=Workobject_INICIALES;
        MoveL vTarget_80_final,v100,z10,Tooldata_MARCADOR\WObj:=Workobject_INICIALES;
        MoveL ZInicio,v100,z10,Tooldata_MARCADOR\WObj:=Workobject_INICIALES;
    ENDPROC
    PROC Home()
        MoveJ Target_30,v1000,z100,Tooldata_MARCADOR\WObj:=Workobject_INICIALES;
    ENDPROC
    PROC Close()
        MoveJ AInicio,v100,z10,Tooldata_MARCADOR\WObj:=Workobject_INICIALES;
    ENDPROC
ENDMODULE