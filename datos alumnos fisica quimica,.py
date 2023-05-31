
#calculadora datos alumnos con notas de fisica y quimica para checkear si aprobaron o reprobaron el semestre :()

#BENJAMIN AGUILAR B.



print("RECORDATORIO: El programa solo funcionara con las asignaturas Fisica y Quimica")

print("Introduzca datos del alumno")

nombre = input ("introduzca nombre del alumno: ")
apellido = input ("introduzca apellido del alumno: ")
numero = "numero"

try: 
    numero =int(input("Introduzca su numero de Telefono: "))
    
except:
    print("Datos erroneos")
    exit()
    
    
    #ASIGNATURA DE FISICA


asignatura = input("¿que asignatura desea calificar?: ")
if asignatura== "fisica":
    fp1 = int(input("ingrese nota parcial n1: "))
    fef = int(input("ingrese nota del examen final: "))
    
    suma= fp1 + fef 
    promf= suma
    
    #aprobacion del ramo, reprobado o suspendido 


    if fef>11 and promf>=60:
            estado =("Aprobado")
    elif promf<60 and promf>30:
            estado= ("Suspendido")
    elif promf<30: 
         estado= ("Reprobado")    
    elif fef<12:
        estado= ("Suspendido") 



  #DATOS DEL ALUMNO/a




    if fp1>=0 and fp1<71 and fef>=0 and fef<31:
        print("El estudiante ", nombre, apellido)
        print("con numero de telefono ", numero)
        print("obtuvo en la asignatura de", asignatura)
        print("una nota final de", promf)
        print("que corresponde al estado de", estado)
        
        if promf>59 and fef<12:
            print("esto debido a que tuvo una calificacion de", fef)
            print("en el examen final de", asignatura) 
            
        
    else:
        print("datos incorrectos")
        exit()  
       
#ASIGNATURA DE QUIMICA 



if asignatura== "quimica":
    Qp1 = float(input("ingrese nota parcial n1: "))
    Qef = float(input("ingrese nota examen final: ")) 
        
    suma= Qp1 + Qef 
    promf= suma
    


      #aprobacion del ramo, reprobado o suspendido 



    if Qef>1.1 and promf>=6:
            estado =("Aprobado")
    elif promf<6 and promf>2.9:
            estado= ("Suspendido")
    elif promf<3: 
         estado= ("Reprobado")    
    elif Qef<1.2:
         estado= ("Suspendido")
    if Qp1>=0 and Qef<7.1 and Qef>=0 and Qef<3.1: 
            
           
           
            #DATOS DEL ALUMNO/a



         print("El estudiante ", nombre, apellido)
         print("con numero de telefono ", numero)
         print("obtuvo en la asignatura de", asignatura)
         print("una nota final de", promf)
         print("que corresponde al estado de", estado)
                
         if promf>5.9 and Qef<1.2:
             print("esto debido a que tuvo una calificacion de", Qef)
             print("en el examen final de", asignatura) 
         
        
    else:
        print("Datos erroneos")
        exit() 



     
