# -*- coding: utf-8 -*-
"""
Created on Thu Aug  5 10:58:54 2021

@author: Fernando
"""

#Numeros Primos
#Ingreso del numero
numero=int(input("Ingrese el numero a revisar si es Primo"))

if numero <=0:
    print("El numero debe ser mayor que cero")
else:
    
    print("Revision") 
  
def primo(numero):
    i=2
    numerodivisores=False
      
    while(i < numero and not numerodivisores ):
        resto = float(numero % i)
#Revision        print(resto,i)  
        
        if numero % i == 0:
            numerodivisores = True
#            print(i)
           
        i=i+1 
               
        
#        print("Salir IF")
#        print(i)
        
    
    if not numerodivisores and numero>1:
        print("El numero es primo  :","\t"*2,numero)
    
    else:
        print("El numero no es primo :","\t"*2,numero)
        
print("Salir")
primo(numero)

#Edgar Fernando Cevallos Cueva
