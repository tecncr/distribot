# DistriBot (v0.5)
Un simple bot de sorteo de ejercicios de tareas grupales en español, escrito en Python 3 utilizando Discord.py (https://github.com/Rapptz/discord.py)

## Comandos disponibles (por ahora)
> **d!repartir** (primer ejercicio) (numero de ejercicios) @persona1 @persona2 @persona3...

*Sortea, entre los participantes mencionados, una cantidad de ejercicios de una tarea grupal, comenzando desde el número de ejercicio determinado, por ejemplo:*
+ d!repartir 1 6 @Juan @Pedro @María

*(Reparte **6 ejercicios** comenzando desde el **1** entre **Juan**, **Pedro** y **María**)*

> **d!arremedar** @MencionUsuario

*Repite el último mensaje del usuario mencionado en el canal donde se invocó el comando, sustituyendo todas las vocales por **i**.*

> **d!saludo**

*Retorna el siguiente mensaje:*
> Hola! Soy DistriBot :) Un bot en desarrollo que permitirá sortear tareas grupales.

*Con el fin de probar el funcionamiento del bot.*

## Implementación del bot

Colocar el token en la primera línea del archivo **token.txt** y ejecutar/desplegar el archivo **bot3.py**
