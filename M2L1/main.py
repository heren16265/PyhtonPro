import discord
from discord.ext import commands
from bot_token import token
from bot_mantik import gen_pass
# ayricaliklar (intents) değişkeni botun ayrıcalıklarını depolayacak
intents = discord.Intents.default()
# Mesajları okuma ayrıcalığını etkinleştirelim
intents.message_content = True
# client (istemci) değişkeniyle bir bot oluşturalım ve ayrıcalıkları ona aktaralım
bot = commands.Bot(command_prefix='', intents=intents)


@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')

@bot.command()
async def s56(ctx):
    await ctx.send(f'Merhaba {bot.user}! Ben bir botum!')

@bot.command()
async def s46(ctx, pass_length = 10):
    await ctx.send(gen_pass(int(pass_length)))

@bot.command()
async def s26(ctx):
    with open('M2L1\img\mem1.png', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)

bot.run(token)