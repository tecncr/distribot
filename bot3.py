import discord
from random import choice
from discord.ext import commands


def leer_token():
    with open("token.txt", "r") as f:
        lines = f.readlines()
        return lines[0].strip()


bot = commands.Bot(command_prefix='%', description="Bot de distribucion de tareas grupales (en desarrollo)")

@bot.command()
async def prueba(ctx):
    await ctx.send('Hola! Soy DistriBot :) Un bot en desarrollo que permitirá sortear tareas grupales.')

@bot.command()
async def miembros(ctx):
  miembros = await ctx.guild.fetch_members(limit=200).flatten()
  await ctx.send(f"En este momento hay {len(miembros)} en el server.")

@bot.command()
@commands.guild_only()
async def sorteo(ctx, parti, ejer, empieza):
    
    miembros = await ctx.guild.fetch_members(limit=200).flatten()
    
    #TODO: implementar el manejo de excepciones cuando el comando no contenga enteros xD
    p = int(parti)
    e = int(ejer)
    s = int(empieza)
    
    lista = []
    for i in range(1, p+1):
            appended = False
            while not appended:
                a = choice(tuple(member.mention for member in miembros if not member.bot))
                if a not in lista:
                    lista.append(a)
                    appended = True
    
    def obtener_lista_miembros_random(participantes):
        for i in range(1, participantes+1):
            appended = False
            while not appended:
                a = choice(tuple(member.mention for member in miembros if not member.bot))
                if a in lista:
                    lista.append(a)
                    appended = True
    

    cant = len(tuple(member.mention for member in miembros if not member.bot))
    
    if p <= cant and p >= 1 and e <= 25:
        #Si la cantidad de ejercicios es multiplo del nro de participantes
        if e%p == 0:
            while len(lista) != e:
                #Rellenamos la lista random hasta tener el numero de participantes correcto
                obtener_lista_miembros_random(p)
        else:
            #Si no es multiplo, awebo, lo hacemos multiplo
            new_e = e - (e%p)
            while len(lista) != new_e:
                #Rellenamos la lista random hasta tener el numero de participantes multiplo
                obtener_lista_miembros_random(p)
            #Y luego rellenamos con unos randoms mas hasta tener el numero completo
            obtener_lista_miembros_random(e%p)
        #Hasta ahí deberiamos tener la lista de menciones completa y sino me voy alaverga y me cambio de carrera
        #Comencemos con el mensaje bonito
        mensaje = discord.Embed(title=f"Sorteo de {e} ejercicios para {p} participantes.", description=f"Comenzando desde el ejercicio {s}.")
        for i in range(0,len(lista)):
            mensaje.add_field(name=f"El Ejercicio {s+i} le toca a:", value=f"{lista[i]}")
        await ctx.send(embed=mensaje)
        print(f"\nSorteo realizado con exito. Ganadores: {lista}\n")
    
    else:
        await ctx.send('La cantidad de participantes no puede ser superior a la cantidad de miembros del server ni ser menor que uno :(')

@bot.command()
async def arremedar(ctx, mencion):
    usuarioid = int(mencion[3:21])
    msj = await ctx.message.channel.history().find(lambda m: m.author.id == usuarioid)
    texto = msj.content
    t1 = texto.replace("a", "i")
    t2 = t1.replace("e", "i")
    t3 = t2.replace("o", "i")
    t4 = t3.replace("u", "i")
    t5 = t4.replace("A", "I")
    t6 = t5.replace("E", "I")
    t7 = t6.replace("O", "I")
    t8 = t7.replace("U", "I")
    await ctx.send(t8)

@bot.event
async def on_ready():
    print("Bot iniciado y listo para usar :D")

bot.run(leer_token())
