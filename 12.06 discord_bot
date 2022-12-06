import discord, asyncio
from discord.ext.commands import Bot
from discord.ext import commands
import random
import numpy as np


TOKEN = 'my token' ### 내 디스코드 봇의 토큰 값 -> 디스코드 개발자 사이트를 통해서 알 수 

intents = discord.Intents.default()
### clent = discord.Clent() -> 어째선지 윗코드와 충돌나서 예외처리됨 -> 밑에 있는 코드가 실행 안됨

# !로 시작하면 명령어로 인식
bot = Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
  print(f'logged in as {bot.user}')  ### 내 봇이 디스코드에 로그인하면 터미널에 "logged in as {bot.user}" 메세지를 출력

# !hello 명령어 처리
# 디스코드 서버에 !hello를 입력하면 디스코드 봇이 'Hi, there!' 메세지를 출력
@bot.command()
async def hello(ctx):
  await ctx.channel.send('Hi, there!') ###ctx.channel send(?) 로 바꾸면 자기 채널로 메세지 나감

# !bye 명령어 처리
# 디스코드 서버에 !bye를 입력하면 디스코드 봇이 'Hi, there!' 메세지를 출력 
@bot.command()
async def bye(ctx):
  await ctx.channel.send('See you later!')

# !good 명령어 처리
# 디스코드 서버에 !good 입력하면 디스코드 봇이 'I'm good' 메세지를 출력
@bot.command()
async def good(ctx):
  await ctx.channel.send('I\'m good')  

# ! talk 명령어 처리
# 디스코드 서버에 !talk a b 입력하면 디스코드 봇이 '{a} talk to {b}' 메세지를 출력
@bot.command()
async def talk(ctx,b,c):
  
    await ctx.channel.send('{} talks to {}'.format(b,c))


### 오류 발생시 -> "명령어를 찾지 못했습니다" 메세지를 출력
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
    	await ctx.channel.send("명령어를 찾지 못했습니다")

### @bot.command() 한 후
### async def talk(ctx,b,c):
### await ctx.reply('{} talks to {}'.format(b,c)) 이러면 명령어 하나 생성하는 거임



### 주사위 게임 
### roll_dice를 입력하여 작동
@bot.command()
async def roll_dice(ctx):
  await ctx.send("주사위 굴리기")
  await ctx.send(rollADice())

def rollADice():

  a= random.randrange(1,7)
  b =random.randrange(1,7)

  if a>b:
    return "you  win! your number is" + str(a) +"my number is" + str(b)
  elif a==b:
    return "Draw! your number is" + str(a) +"my number is" + str(b)
  else:
    return "you lose! your number is" + str(b) +"my number is" + str(b)




### print(ctx.author.voice) -> 명령어를 사용한 유저가 현재 있는 음성채널의 정보를 가져옴
### print(ctx.author.voice.channel) -> 명령어를 사용한 유저가 현재 있는 음성채널의 이름을 가져옴

@bot.command()  ### 봇이 다른 채널에 접속시키게 함
async def play(ctx):
  channel = ctx.author.voice.channel
  await channel.connect()

@bot.command()
async def leave(ctx): ### 봇이 지금 채널에서 나가게 함
  await bot.voice_clients[0].disconnect()


@bot.command() ### 채팅 메세지를 amount 만큼 삭제
async def clear(ctx, amount: int):
  await ctx.channel.purge(limit = amount)

@bot.command() ### 봇이 음성채널에 접속시키게 함
async def come(ctx):
  try:
    global vc
    vc = await ctx.message.author.voice.channel.connect()
  except:
    try:
      await vc.move_to(ctx.message.author.voice.channel)
    except:
      await ctx.send("채널에 유저가 없음")

@bot.command() ### 봇이 음성채널에서 나가게 함
async def go_out(ctx):
  try:
    global vc
    vc = await vc.disconnect()
  except:
    await ctx.send("채널에 유저가 없음")


    
@bot.event
async def on_message(message): ### 봇의 정보를 알려줌
  if message.content ==  "봇정보":
    await message.channel.send("{} | {}, hello".format(message.author, message.author.mention))
    
  ### /사진 사진파일이름 을 입력
  if message.content.startswith("/사진"): ### discord_bot이 있는 파일에 사진이 있다면 파일안에 사진 파일을 입력하여 사진을 출력함
    pic = message.content.split(" ")[1]
    await message.channel.send(file = discord.File(pic))

  ### /채널메세지 ~~~ ~~~ 입력, 미완성
  if message.content.startswith("/채널메세지"): ### 다른 채널에 메세지를 보내는 함수
    channel = message.content.content[7:25]
    msg = message.content[26:]
    await client.get_channel(int(channel)).send(msg)


  ### /투표/투표이름/후보1/후보2 ~~~ 를 입력하여 작동, 미완성 
  if message.content.startswith("/투표"): ### 투표기능을 사용하는 함수
    vote = message.content[4:].split('/')
    await message.channel.send("투표 이름: " + vote[0])
    for i in range(1, len(vote)):
      choose = await message.channel.send("'''"+ vote[i] +"'''")
      await client.add_reaction(choose, '👍')



bot.run(TOKEN)
