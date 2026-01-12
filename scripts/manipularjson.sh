#!/bin/bash

clear
echo -e "\n🍻🍺🍻 MANIPULAR ARCHIVOS JSON\n"

# Obtener una propiedad del JSON
nombre=$(jq -r '.nombre' ../producto.json)
precio=$(jq -r '.precio' ../producto.json)
echo -e "\n\nEl nombre que buscas es: $nombre"
echo -e "El precio que buscas es: $precio€\n\n"

# Cambiar valor en un json
read -p "Dime el nuevo nombre: " nombre
jq --arg nombre "$nombre" '.nombre = $nombre' ../producto.json > ../tmp.json && mv ../tmp.json ../producto.json

#read -p "Dime un nuevo precio:" precio
#jq --arg precio "$precio" '.precio = $precio' ../producto.json > ../tmp.json && mv ../tmp.json ../producto.jso
