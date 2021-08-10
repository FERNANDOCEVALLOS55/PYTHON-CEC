# -*- coding: utf-8 -*-
"""
Created on Fri Aug  6 01:45:54 2021

@author: Fernando
"""
from datetime import date

fecha=-(2002,12,1)

dia=date[0]
mes=date[1]
anio=date[2]

day = date.day
month = months[date.month - 1]
year = date.year
print(day,month,year)


date=(20,1,195)
def current_date_format(date):
    months = ("Enero", "Febrero", "Marzo", "Abri", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre")
    day = date.day
    month = months[date.month - 1]
    year = date.year
    messsage = "{} de {} del {}".format(day, month, year)

    return messsage

now = datetime.now()
print(current_date_format(now))


#Calcula el dia de la semana
#en cualquier fecha a partir de 1583
 
dia = int(input('Dia de nacimiento: '))
mes = int(input('Mes de nacimiento: '))
year = int(input('Anio de nacimiento: '))
 
if year < 1583:
  print('Solo acepta fechas mayores a 1582')
else:
  a = (14 - mes) // 12
  y = year - a
  m = mes + 12 * a - 2
 
  d = (dia + year + (year//4) - (year//100) + (year//400) + ((31 * m)//12)) % 7
 
  if d == 0:
    diaSemana = 'Domingo'
  elif d == 1:
    diaSemana = 'Lunes'
  elif d == 2:
    diaSemana = 'Martes'
  elif d == 3:
    diaSemana = 'Miercoles'
  elif d == 4:
    diaSemana = 'Jueves'
  elif d == 5:
    diaSemana = 'Viernes'
  else:
    diaSemana = 'Sabado'
 
  print('El dia %d del mes %d de %d es %s' %(dia,mes,year,diaSemana))




Su tarea es escribir y probar una función que toma tres argumentos (un año, un mes y un día del mes) y devuelve los días correspondiente del año, o devuelve None si alguno de los argumentos es inválido.
Use las funciones previamente escritas y probadas. Agregue algunos casos de prueba al código. 
Esta prueba es solo un comienzo.
def isYearLeap(year):
#
# your code from LAB 1
#
 
def daysInMonth(year, month):
#
# your code from LAB 2
#
 
def dayOfYear(year, month, day):
#
# put your new code here
#
 
print(dayOfYear(2000, 12, 31))
