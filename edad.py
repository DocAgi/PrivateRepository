print ("Selecciona una opción")
print ("1. Insertar edad, nombre y altura")
print ("2. Sumar dos números")
print ("3. Calcular el área de un círculo")
opción = input ("Inserte el número de su opción ");
#Aquí le damos la opción al usuario de elegir una de las 3 opciones
if (opción == '1' ):
    z= input ("Introduce tu nombre ");
    x= int(input ("Introduce tu edad "));
    y= float(input ("Introduce tu altura en metros (en vez de usar una coma, use un punto para separar decimales) "));
    print ("Te llamas", z)
    print ("Tienes",x ,"años")
    print ("Mides",y ,"metros")
#Aquí le pedimos tres variables y se la devolvemos
elif (opción == '2' ):
    num1= int(input ("Introduce un número "));
    num2= int(input ("Introduce otro número "));
    num3= num1 + num2
    print ("La suma de ",num1, "+",num2 ,"es =", num3)
#Aquí le pedimos dos números para sumarlos
elif (opción == '3' ):
    rad= int(input ("Introduce el radio "));
    π= 3.1416
    area= (rad * rad) * π
    print ("El aréa es ",area )
#Aquí le pedimos el radio para calcular el área