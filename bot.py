import discord
from discord.ext import commands
import random
import numpy as np


TOKEN = 'MTA0NDYxODk2MTg4ODc1NTc2NA.GGIRu1.GCbX_VS4BUpnFJfxQn2udVnkk6NaQxbms-VfIw' ### 내 디스코드 봇의 토큰 값

intents = discord.Intents.all()

# !로 시작하면 명령어로 인식
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
  print(f'logged in as {bot.user}')  ### 내 봇이 디스코드에 로그인하면 터미널에 "logged in as {bot.user}" 메세지를 출력

@bot.command(name = "도움말")
async def HelpMessage(ctx):
  embed = discord.Embed(title = "명령어 목록")
  embed.add_field(name = "!안녕", value = "Hi there!", inline = False)
  embed.add_field(name = "!잘가", value = "C U later!", inline = False)
  embed.add_field(name = "!good", value = "I`m good", inline = False)
  embed.add_field(name = "!대화 (a) (b)", value = "(a) talk to (b)", inline = False)
  embed.add_field(name = "!이모티콘", value = "이모티콘 리스트", inline = False)
  await ctx.channel.send(embed = embed)

@bot.command(name = "이모티콘")
async def emoticon(ctx):
  embed = discord.Embed(title = "이모티콘 목록")
  embed.add_field(name = "!라이언", value = "라이언", inline = False)
  await ctx.channel.send(embed = embed)

# !hello 명령어 처리
# 디스코드 서버에 !hello를 입력하면 디스코드 봇이 'Hi, there!' 메세지를 출력
@bot.command(name = "안녕")
async def hello(ctx):
  await ctx.channel.send('Hi, there!') ###ctx.channel.send() 로 바꾸면 자기 채널로 메세지 나감

# !bye 명령어 처리
# 디스코드 서버에 !bye를 입력하면 디스코드 봇이 'See you later!' 메세지를 출력 
@bot.command(name = "잘가")
async def bye(ctx):
  await ctx.reply('See you later!')

# !good 명령어 처리
# 디스코드 서버에 !good 입력하면 디스코드 봇이 'I'm good' 메세지를 출력
@bot.command()
async def good(ctx):
  await ctx.reply('I\'m good')  

# ! talk 명령어 처리
# 디스코드 서버에 !talk a b 입력하면 디스코드 봇이 '{a} talk to {b}' 메세지를 출력
@bot.command(name = "대화")
async def talk(ctx,b,c):
  await ctx.reply('{} talks to {}'.format(b,c))


### 오류 발생시 -> "명령어를 찾지 못했습니다" 메세지를 출력
@bot.event
async def on_command_error(ctx, error):
  if isinstance(error, commands.CommandNotFound):
    await ctx.channel.send("명령어를 찾지 못했습니다")

@bot.command(name = "라이언")
async def RYAN(ctx):
    embed = discord.Embed(title = "")
    embed.set_image(url="https://cdn.discordapp.com/attachments/829035801849233451/1049585159210545152/2Q.png")
    await ctx.channel.send(embed = embed)
    return

bot.run(TOKEN)