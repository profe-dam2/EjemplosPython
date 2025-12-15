#!/bin/bash

rutaorigen=$1 #Ruta del directorio a cambiar el nombre
rutacategorias=$2 # Ruta a categorias
elementoorigen=$3 # Nombre del elemento que vas a modificar

echo -e "\n Vas a cambiar el nombre de $elementoorigen\n"
read -p "Indica el nombre de la nueva categoria: " nombre

# Ejecutar el comando

# Retornar codigos con exit