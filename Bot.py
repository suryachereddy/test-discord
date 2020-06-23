import discord
from discord.ext import commands

TOKEN = 'NzI1MDY0MjIxNDIzMDQyNTky.XvJSzg.XFw10y5xiNVnI1havnQvr2hOFyk'

client= commands.Bot(command_prefix='g!')
client.remove_command('help')
#client = discord.Client()
@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.idle,activity=discord.Game("type g!.help"))
    print("bot is online")

@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency*1000)}ms')

client.run(TOKEN)