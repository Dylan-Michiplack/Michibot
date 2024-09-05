import discord 
from discord.ext import commands 
intents = discord.Intents.default()
intents.message_content = True

Michiplack = commands.Bot(command_prefix="Michi",intents=intents)
@Michiplack.event 
async def on_ready():
    print("el Michibot ha iniciado sesion")
@Michiplack.command ()
async def hola(ctx):
    await ctx.send("hola soy Michibot, en que lo ayudo ?")

Michiplack.run("")
