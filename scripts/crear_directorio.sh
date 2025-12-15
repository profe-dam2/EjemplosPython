#!/bin/bash

ruta=$1
nombre=$2
archivo=$3

#echo -e "\n Hola, has pasado como argumentos:\n"
#echo -e "RUTA: $ruta"
#echo -e "NOMBRE: $nombre"
#echo -e "ARCHIVO: $archivo"
clear
# Capturar el nombre del directorio
read -p "Indica el nombre para $nombre" directorio

# Crear el directorio en la ruta
mkdir "$ruta/$directorio"

exit 3