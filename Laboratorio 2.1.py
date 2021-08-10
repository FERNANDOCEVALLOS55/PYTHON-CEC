# -*- coding: utf-8 -*-
"""
Created on Thu Aug  5 19:22:48 2021

@author: Fernando
"""
#Ano bisiesto




def isYearLeap(year):
    
    if year % 4 != 0:
        print ("No es bisiesto")
        year1=year
        tfyear=False
        return year1,tfyear
    elif year % 4 == 0 and year % 100 !=0:
        #divisible 4 y no de 100 y 400
        print("Es bisiesto")
        year1=year
        tfyear=True
        return year1,tfyear
    
    elif year % 4 ==0 and year % 100 ==0 and year % 400 !=0:
        # no de 400
        print("No es bisiesto")
        year1=year
        tfyear=False
        return year1,tfyear 
    elif year % 4 ==0 and year % 100 ==0 and year % 400 ==0:
        
        print("Es bisiesto")
        year1=year
        tfyear=True
        return year1,tfyear
 
print("Salir")



resultado=isYearLeap(year)
year=resultado[0]
tf=resultado[1]
print(year,tf)

print(resultado)
#Datos entregados

testData = [1900, 2000, 2016, 1987]
testResults = [False, True, True, False]

for i in range(len(testData)):
            yr = testData[i]
            print(yr,"->",end="")
            result = isYearLeap(yr)
            prueba=result[1]
            
            if prueba == testResults[i]:
                        print("OK")
            else:
                        print("Failed")

print("FIN")


if año % 4 != 0: #no divisible entre 4
	print("No es bisiesto")
elif año % 4 == 0 and año % 100 != 0: #divisible entre 4 y no entre 100 o 400
	print("Es bisiesto")
elif año % 4 == 0 and año % 100 == 0 and año % 400 != 0: #divisible entre 4 y 10 y no entre 400
	print("No es bisiesto")
elif año % 4 == 0 and año % 100 == 0 and año % 400 == 0: #divisible entre 4, 100 y 400
	print("Es bisiesto")
    
    
    
    
    
    
    


testdata= [1900,2000,2016,1987]
testresultados=[False,True,true,False]

    
    
   
        


Su tarea es escribir y probar una función que toma un argumento (un año) y devuelve Verdadero si el año es bisiesto o Falso de lo contrario.
La semilla de la función está en el código adjunto.
Nota: también hemos preparado un breve código de prueba, que puede usar para probar su función.
El código usa dos listas: una con los datos de prueba y la otra con los resultados esperados. El código le dirá si alguno de sus resultados no es válido.
def isYearLeap(year):
#
# Su codigo AQUI
#
 
testData = [1900, 2000, 2016, 1987]
testResults = [False, True, True, False]
for i in range(len(testData)):
            yr = testData[i]
            print(yr,"->",end="")
            result = isYearLeap(yr)
            if result == testResults[i]:
                        print("OK")
            else:
                        print("Failed")
