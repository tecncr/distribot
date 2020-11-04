# DistriBot (v0.0.1)
Un simple bot de sorteo de ejercicios de tareas grupales en español, escrito en Python 3.8 con ayuda de Discord.py (https://github.com/Rapptz/discord.py)

## Comandos disponibles (por ahora)
+ **%sorteo** (número de participantes) (número de ejercicios) (ejercicio de inicio)

Sortea, entre la cantidad de participantes ingresados, una cantidad de ejercicios de una tarea grupal, comenzando desde un número de ejercicio determinado, por ejemplo:
> **%sorteo** 10 20 5

*(Sortea entre **10 participantes** la cantidad de **20 ejercicios** comenzando desde el **ejercicio 5**)*
**NOTA**: En caso de que el número de participantes exceda el número de miembros (excluyendo bots) del canal de texto en el que se invoca el comando, la ejecución del sorteo fallará.

+ **%arremedar** @MencionUsuario

Repite el último mensaje del usuario mencionado en el canal donde se invocó el comando, sustituyendo todas las vocales por **i**.

+ **%miembros**

Retorna la cantidad de **miembros elegibles** para un sorteo de ejercicios en el contexto del canal donde se invocó el comando.


+ **%prueba**

Retorna el siguiente mensaje:
> Hola! Soy DistriBot :) Un bot en desarrollo que permitirá sortear tareas grupales.

Con el fin de probar el funcionamiento del bot.

## Implementación del bot

Colocar el token en la primera línea del archivo **token.txt** y ejecutar/desplegar el archivo **bot3.py**
