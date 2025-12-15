#!/bin/bash

clear
ruta=$1
echo -e "\n La ruta que has pasado es: $ruta"
read -p "Indica un nombre categoria: " nombre
mkdir "$ruta/$nombre"
if [[ $? == "1" ]]; then
  clear
  exit 20
fi
clear
echo "Has creado la categoria $nombre"
exit 0

