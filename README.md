# DistriBot (v0.6)
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

> **d!ayuda**

*Retorna un link a la página de ayuda https://distribot.xyz/comandos.html para ver los comandos disponibles*

## Cómo correr su propia instancia
**Con Docker:**
- `git clone https://github.com/tecncr/distribot`
- `cd distribot`
- `echo (token dado por discord) > token.txt`
- `docker build -t distribot .`
*(no olvidar el punto al final)*
- `docker run -it distribot`

**Con su intérprete de Python local:**
- `git clone https://github.com/tecncr/distribot`
- `cd distribot`
- `pip install -r requirements.txt`
- `echo (token dado por discord) > token.txt`
- `python3 bot3.py`
