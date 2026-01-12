#!/bin/bash

clear

echo -e "Hola, gracias por entrar\n"

# Mostrar contenido de un archivo
cat ../archivo.txt

# Obtener el total de lineas
totalLineas=$(wc -l < ../archivo.txt)
echo -e "\nEl total de lineas es: $totalLineas"

# Leer un número de lineas concreto
read -p "Indica un número de línea: " linea
contenido=$(sed -n "$linea"'p' ../archivo.txt)
echo -e "\n El contenido de la linea $linea es: $contenido"

# Modificar una linea
read -p "Indica el nuevo contenido de la linea $linea: " nuevoContenido
sed -i "$linea"'s/'"$contenido"'/'"$nuevoContenido"'/' ../archivo.txt

read -p "Indica texto para añadir al final: " texto
echo "$texto" >> ../archivo.txt

# Eliminar una linea en concreto
read -p "Indica la linea a borrar: " linea
sed -i "$linea"'d' ../archivo.txt

cat ../archivo.txt

#Obtener coincidencias de busqueda
read -p "Indica la palabra a buscar: " palabra
grep -n "$palabra" ../archivo.txt

# Capturar el número de lineas donde aparece
lineas=$(grep -n "$palabra" ../archivo.txt | cut -d':' -f1)

for l in $lineas; do
  echo "La línea $l está presente"
done

