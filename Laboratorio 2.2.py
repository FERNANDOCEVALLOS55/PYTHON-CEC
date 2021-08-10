# -*- coding: utf-8 -*-
"""
Created on Thu Aug  5 23:58:42 2021

@author: Fernando
"""


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
 
#print("Salir")



resultado=isYearLeap(year)
year=resultado[0]
tf=resultado[1]
#print(year,tf)

#print(resultado)
#Datos entregados

#Dias en el mes


def daysInMonth(mes,year):
    
    # Abril, junio, septiembre y noviembre tienen 30
    if mes in [4, 6, 9, 11]:
        return 30
    # Febrero depende de si es o no bisiesto
    if mes == 2:
        resultado=isYearLeap(year)
        tf=resultado[1]
        if tf:
            return 29
        else:
            return 28
    else:
        # En caso contrario, tiene 31 días
        return 31
    
#print("Fin")

meses=("Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio",
       "Agosto","Septiembre","Octubre","Noviembre","Diciembre")




#mes=2
#year=2020
#print(meses[2])
#print(meses)
diasdelmes=daysInMonth(mes,year)

print(diasdelmes,"dias de",meses[mes-1], "del Anio",year )


 
testYears = [1900, 2000, 2016, 1987]
testMonths = [2, 2, 1, 11]
testResults = [28, 29, 31, 30]
for i in range(len(testYears)):
                yr = testYears[i]
                mo = testMonths[i]
                print(yr, mo, "->", end="",)
                
                result = daysInMonth(mo, yr)
                if result == testResults[i]:
                                print("OK")
                else:
                                print("Failed")
                                
print("Final")

