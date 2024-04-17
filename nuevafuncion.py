import discord
import os
import random
from discord.ext import commands
import requests

intents = discord.Intents.all()
intents.members = True
bot = commands.Bot(command_prefix="!", intents=intents)




@bot.event
async def on_ready():
    print(f"¡Bot conectado como {bot.user.name}!")


    for guild in bot.guilds:
        await guild.system_channel.send("Hola, soy el bot de este servidor, utiliza 'com' para ver mis comandos, recuerda utilizar '!' antes de cada uno")

@bot.command()
async def hola(ctx):
    await ctx.send("¡Hola! ¿En qué puedo ayudarte?")

@bot.command()
async def info_servidor(ctx):
    server = ctx.guild
    await ctx.send(f"Este servidor se llama {server.name} y tiene {server.member_count} miembros.")

@bot.command()
async def expulsar(ctx, miembro: discord.Member, *, razón="No especificada"):
    await miembro.kick(reason=razón)
    await ctx.send(f"{miembro.display_name} ha sido expulsado. Razón: {razón}")

@bot.command()
async def com(ctx):
    await ctx.send("Estos son mis comandos: 1 'hola', 2 'info_servidor', 3'expulsar',4'com'")

@bot.command()
async def mem(ctx):
    img_name=random.choice(os.listdir('images'))
    with open(f'images/{img_name}', 'rb') as f:
            picture = discord.File(f)
    await ctx.send(file=picture)

def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']


@bot.command('duck')
async def duck(ctx):
    '''Una vez que llamamos al comando duck, 
    el programa llama a la función get_duck_image_url'''
    image_url = get_duck_image_url()
    await ctx.send(image_url)

@bot.command()
async def dog(ctx):
    try:
        response = requests.get('https://random.dog/woof.json')
        data = response.json()
        image_url = data['url']
        await ctx.send(image_url)
    except Exception as e:
        print('Error al obtener la imagen del perro:', e)
        await ctx.send('¡Lo siento! No pude obtener una foto de perro en este momento.')
bot.run('MTIxOTc3MzkxNTkwMDAxODgxMA.GCVaQr.GVPOd_N-JpNxM92qIV2Kvx8s_TNIuUpKVqTAUA')