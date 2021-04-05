#Importamos la fecha
import datetime
from datetime import (date, time)

#Definimos la fecha de hoy
hoy = datetime.date.today()
print("Hoy es :", hoy)

#Leemos el contenido del archivo 1
archivo = open('fecha1.txt', 'r')
archivito = archivo.read()

#Imprimimos el archivo
print("La fecha 1 es :", archivito)

#Cerramos el archivo
archivo.close()

#Leemos el contenido del archivo 2
archivo1 = open('fecha2.txt', 'r')
archivitito = archivo1.read()

#Imprimimos el archivo
print("La fecha 2 es:", archivitito)

#Cerramos el archivo
archivo1.close()

#Guardamos los datos del archivo uno
abro = open('archivouno.txt', 'w+')
abro.write("La fecha 1 es:")
abro.write(archivito)

#Imprimimos la fecha actual
hoy = datetime.date.today()
print("La fecha actual del sistema es: ", hoy)

#Guardamos los datos del archivo dos
abri = open('archivodos.txt', 'w+')
abri.write("El contenido del archivo 2 es: ")
abri.write(archivitito)

#Convertimos la información del archivo uno
fechita1 = datetime.date(year=2000, month=9, day=14)
fechita2 = datetime.date(year=2007, month=4, day=15)

#Imprimimos la modificación
abro.write("Las fechas escritas correctamente son: ")
abro.write("Fecha 1: ")
abro.write(str(fechita1))
abro.write("Fecha 2: ")
abro.write(str(fechita2))

#Convertimos la información del archivo dos
fechaa1 = datetime.date(year=2020, month=9, day=14)
fechaa2 = datetime.date(year=2020, month=4, day=15)

#Imprimimos la modificación
abri.write("Las fechas escritas correctamente son: ")
abri.write("Fecha 1: ")
abri.write(str(fechaa1))
abri.write("Fecha 2: ")
abri.write(str(fechaa2))

#Modificamos las fechas del archivo 1
suma1 = fechita1 + datetime.timedelta(days=7305)
print(suma1)
suma2 = fechita2 + datetime.timedelta(days=4751)
print(suma2)

#Actualizamos el archivo uno
abro.write("La fecha 1 actualizada es: ")
abro.write(str(suma1))
abro.write("La fecha 2 actualizada es: ")
abro.write(str(suma2))

#Realizamos análisis con las fechas del archivo 2
tiempo1 = hoy - fechaa1
print(tiempo1)
tiempo2 = hoy - fechaa2
print(tiempo2)

#Actualizamos el archivo dos
abri.write("¿Cuánto tiempo ha transcurrido desde cada fecha?")
abri.write(str(tiempo1))
abri.write(str(tiempo2))

#Imprimimos el formato de fecha
fecha = datetime.date(2014, 7, 24)
print("La fecha es: ", fecha)
print("Identificamos fecha en escritura específica: {:%A, %d de %b de %Y}".
      format(fecha))
print("Identificamos fecha en escritura específica: {:%d/%m/%y}".format(fecha))
print("Día:", fecha.day)
print("Mes:", fecha.month)
print("Año:", fecha.year)
print("Día número:", fecha.weekday())

#Imprimimos el resultado
abro.write("La fecha es: ")
abro.write(str(fecha))
abro.write(
    "Identificamos fecha en escritura específica: {:%A, %d de %b de %Y}".
    format(fecha))
abro.write(
    "Identificamos fecha en escritura específica: {:%d/%m/%y}".format(fecha))
abro.write("Día: ")
abro.write(str(fecha.day))
abro.write("Mes: ")
abro.write(str(fecha.month))
abro.write("Año: ")
abro.write(str(fecha.year))
abro.write("Día número: ")
abro.write(str(fecha.weekday()))

#Cerramos los archivos
abro.close()
abri.close()
