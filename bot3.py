import discord
import random
from discord.ext import commands


def leer_token():
    with open("token.txt", "r") as f:
        lines = f.readlines()
        return lines[0].strip()


bot = commands.Bot(command_prefix='d!', description="Bot de distribucion de tareas grupales (en desarrollo)")

@bot.command()
async def saludo(ctx):
    await ctx.send('Hola! Soy DistriBot :) Un bot en desarrollo que permitirá sortear tareas grupales.')

@bot.command()
async def repartir(ctx, *args):
    participantes = list(args)
    
    try:
        prim_e = int(participantes.pop(0))
    except ValueError:
        mensajeError = discord.Embed(title="Comando inválido :(", description="Parece que te equivocaste en el número del primer ejercicio.\n\nRecuerda:\n*d!repartir* **(primer ejercicio)** (numero de ejercicios) @persona1 @persona2 @persona3...\n\nEjemplo:\n**d!repartir 1 6 @Juan @Pedro @María**\n*(reparte 6 ejercicios comenzando desde el 1 entre Juan, Pedro y María)*")
        await ctx.send(embed=mensajeError)
    else:
        try:
            num_e = int(participantes.pop(0))
        except ValueError:
            mensajeError = discord.Embed(title="Comando inválido :(", description="Parece que te equivocaste en el número de ejercicios.\n\nRecuerda:\n*d!repartir* (primer ejercicio) **(numero de ejercicios)** @persona1 @persona2 @persona3...\n\nEjemplo:\n**d!repartir 1 6 @Juan @Pedro @María**\n*(reparte 6 ejercicios comenzando desde el 1 entre Juan, Pedro y María)*")
            await ctx.send(embed=mensajeError)
        else:
            try:
                if num_e > 100:
                    mensajeError = discord.Embed(title="No puedo estoi chikito", description="Para evitar sobrecargar mi servidor y la API de Discord, por el momento no puedo sortear más de 100 ejercicios a la vez :(\nSi tienes sorteos de cantidades más grandes intenta realizar varios sorteos de hasta 100 ejercicios.")
                    await ctx.send(embed=mensajeError)
                else:
                    num_p = len(participantes)
                    mensaje = discord.Embed(title=f"Sorteo de {num_e} ejercicios para {num_p} participantes.", description=f"Comenzando desde el ejercicio {prim_e}.")
                    ej_sorteados = 0
                    embfield_counter = 0
                    while ej_sorteados < num_e:
                        random.shuffle(participantes)
                        for i in range(0,num_p):
                            if ej_sorteados < num_e:
                                if embfield_counter >= 25:
                                    await ctx.send(embed=mensaje)
                                    mensaje.clear_fields()
                                    embfield_counter = 0   
                                mensaje.add_field(name=f"El Ejercicio {prim_e+ej_sorteados} le toca a:", value=f"{participantes[i]}")
                                ej_sorteados+=1
                                embfield_counter+=1
                    await ctx.send(embed=mensaje)

            except:
                mensajeError = discord.Embed(title="Oh no :(", description="Ocurrió un error inesperado que me impidió realizar el sorteo.\nInténtalo nuevamente.")
                await ctx.send(embed=mensajeError)

@bot.command()
async def arremedar(ctx, mencion):
    try:
        usuarioid = int(mencion[3:21])
        msj = await ctx.message.channel.history().find(lambda m: m.author.id == usuarioid)
        texto = msj.content
        reemplazo = {"a":"i","e":"i","o":"i","u":"i","A":"I","E":"I","O":"I","U":"I"}
        def reemplazar_por_i(text, dic):
            for i, j in reemplazo.items():
                text = text.replace(i, j)
            return text
        await ctx.send(reemplazar_por_i(texto,reemplazo))
    except:
        mensajeError = discord.Embed(title="Oh no :(", description="No pude arremedar el último mensaje de ese usuario.")
        await ctx.send(embed=mensajeError)

@bot.command()
async def ayuda(ctx):
    await ctx.send('Puedes ver todos los comandos que puedo ejecutar aquí ;)\nhttps://distribot.xyz/comandos.html')

@bot.event
async def on_ready():
    print("Bot iniciado y listo para usar :D")

bot.run(leer_token())
