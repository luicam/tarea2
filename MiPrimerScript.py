#!/usr/bin/python
miarray = ['silvia','federico','miguel','julia','evaristo']
print miarray[2]
print " "

for elem in miarray :
  print elem, "es un valor contenido en el array miarray"
  print " "

for index in range(len(miarray)):
  print miarray[index], "es el valor contenido en el array sub", index
  print " "

index=0
for elem in miarray:
  print index, ":", elem
  index += 1
  print " "

miarray.append('carlos')
miarray.index('carlos')
print " "

miarray.index('carlitos')
print " "

'miguel' in miarray
print " "
'carlitos' in miarray
