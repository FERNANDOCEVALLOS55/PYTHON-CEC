# -*- coding: utf-8 -*-
"""
Created on Tue Aug  3 21:08:16 2021

@author: Fernando
"""

# En Europa litros por 100 km l/100Km
# En USA  millas por galon de combustible
# •	1 milla americana = 1609.344 metros;
# •	1 galón americano = 3.785411784 litros.
# l100kmtompg y mpgtol100km
# def l100kmtompg(liters):
#
# put your code here
#

#def mpgtol100km(miles):
#
# put your code here
#

milla=float(1609.344)
galon=float(3.785411784)
print("\n","Una milla es","\t"*4,":",milla,"\t"*2,"metros","\n","Un galon\
 americano es","\t"*2,":",galon,"\t"*2,"litros")

def l100kmtompg(liters):
    fliters=float(liters)
    resultado1=(100*1000/milla)/(liters/galon)
       
    print("\n"*1,"Numero de litros por 100 Km  : ","\t"*4,fliters)
    #type(fliters)
    print("\n"*0,"Numero de Millas por Galon  : ","\t"*4,resultado1)
    
    return resultado1

#nueva funcion

def mpgtol100km(millasporgalon):
    fmillasporgalon=float(millasporgalon)
    
    resultado2=(1000*galon*100)/(milla*fmillasporgalon) 
    
    print("\n"*1,"Numero de litros por 100 Km  : ","\t"*4,resultado2)
    #type(fliters)
    print("\n"*0,"Numero de Millas por Galon  : ","\t"*4,millasporgalon)
    
    return resultado2


res1=l100kmtompg(3.9)

res2=l100kmtompg(7.5)
res3=l100kmtompg(10)
res4=mpgtol100km(60.3)
res5=mpgtol100km(31.4)
res6=mpgtol100km(23.5)

print("\n",res1,res2,res3,res4,res5,res6)


#Edgar Fernando Cevallos Cueva

#FINAL
