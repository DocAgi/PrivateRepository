#Op 
x= int(input ("Introduce un número "));
y= int(input ("Introduce otro número "));
operacion = 1
while (operacion != '0'):
    print ("Selecciona una operación: ");
    print ("1. Suma");
    print ("2. Resta");
    print ("3. Multiplicación");
    print ("4. División");
    print ("0. Salir")
operacion = input ("Ingresa el número de la operación");

if (operacion == '1' ):
    #Op Suma
    suma = x + y;
    print ("Total =", suma);
elif (operacion == '2' ):
    #Op Resta
    resta = x - y;
    print ("Total resta =", resta);
elif (operacion == '3' ):
    #Op multiplicación
    multi = x * y;
    print ("Total multiplicación =", multi);
elif (operacion == '4' ):
    #Op División
    div = x / y;
    print ("Total división =", div);
elif (operacion == 0):
    exit;
