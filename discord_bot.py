import discord
import asyncio
from discord.ext.commands import Bot
from discord.ext import commands
import random
import numpy as np
import youtube_dl



TOKEN = 'MTA1MTU1OTA2MTM3MzU4NzU4Nw.Gin5Ml.V8xQ4lXgJ06Bv3Yk3D0tLIs1Ta7iFUo1p-CY7A' ### 내 디스코드 봇의 토큰 값

intents = discord.Intents.default()

client = discord.Client(intents = intents) 

# !로 시작하면 명령어로 인식 -> bot.command일 경우에 작동
bot = Bot(command_prefix='!', intents=intents) ###-> !명령어로 작동

### 내 봇이 디스코드에 로그인하면 터미널에 "logged in as {bot.user}" 메세지를 출력
@bot.event
async def on_ready():
  print(f'logged in as {bot.user}')  
@bot.command()
async def hello(ctx):
  await ctx.send("Hello!")

# ! talk 명령어 처리
# 디스코드 서버에 !talk a b 입력하면 디스코드 봇이 '{a} talk to {b}' 메세지를 출력
@bot.command()
async def talk(ctx,b,c):
  
    await ctx.channel.send('{} talks to {}'.format(b,c))


### 코드에 없는 명령어 입력시 -> "명령어를 찾지 못했습니다" 메세지를 출력(예와 처리)
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
    	await ctx.channel.send("명령어를 찾지 못했습니다")
    

### 주사위 게임 
### !roll_dice를 입력하여 작동
@bot.command()
async def roll_dice(ctx):
  await ctx.send("주사위 굴리기")
  await ctx.send(rollADice())

def rollADice():

  a= random.randrange(1,7)
  b= random.randrange(1,7)

  if a>b:
    return "you  win! your number is " + str(a) +" my number is " + str(b)
  elif a==b:
    return "Draw! your number is " + str(a) +" my number is " + str(b)
  else:
    return "you lose! your number is " + str(b) +" my number is " + str(b)


### print(ctx.author.voice) -> 명령어를 사용한 유저가 현재 있는 음성채널의 정보를 가져옴
### print(ctx.author.voice.channel) -> 명령어를 사용한 유저가 현재 있는 음성채널의 이름을 가져옴


### @bot.command와 @bot.event가 동시에 있을 때 @bot.command가 실행이 안되었다.
### 이를 @bot.event의 on_message 함수 마지막 부분에 await bot.process_commands(message)를 입력하여 해결
### 이유 : on_message함수는 override를 하면 추가명령을(command)를 실행시키지 않기 때문에 코루틴 함수인 await bot.process_commands(message)를 입력해야함
### 코루틴이란? 일반적인 함수(메인 루틴)과 다르게 a함수가 동작하다 멈추고 또 다른 동작을 하다 다시 a함수로 돌아와 마저 작업을 하는 것을 말함

@bot.event
async def on_message(message): ### 명령어를 입력하면 다음 행동이 실행
  if message.content == "안녕":
    await message.channel.send("Hello")

  if message.content == "잘가":
    await message.channel.send("bye see you later")

  if message.content ==  "you good?":
    await message.channel.send("I'm good")
    
  ### 봇의 정보를 알려주는 함수
  ### message.author, message.author.mention -> 현재 채널에 있는 봇의 정보와 채널 주인의 정보 알려줌
  if message.content ==  "봇정보":
    await message.channel.send("{} | {}, hello".format(message.author, message.author.mention))

    
  ### 봇이 사진 파일을 업로드해주는 함수 
  ### 지금 이파일(discord_bot.py)과 같은 파일(bot_code)안에 사진이 있어야함
  ### 사진 사진파일이름 을 입력
  if message.content.startswith("사진"): 
    pic = message.content.split(" ")[1]
    await message.channel.send(file = discord.File(pic))

  
  ### 다른 채널에 메세지를 보내는 함수
  ### /채널메세지 ~~~ ~~~ 입력
  if message.content.startswith("/채널메세지"):
    channel = message.content.content[7:25]
    msg = message.content[26:]
    await client.get_channel(int(channel)).send(msg)

  ### 투표기능을 사용하는 함수
  ### /투표/투표이름/후보1/후보2 ~~~ 를 입력하여 작동, 미완성 
  if message.content.startswith("/투표"): 
    vote = message.content[4:].split('/')
    await message.channel.send("투표 이름: " + vote[0])
    for i in range(1, len(vote)):
      choose = await message.channel.send("'''"+ vote[i] +"'''")
      await client.add_reaction( '👍', choose)

    
  ### 삭제를 입력하면 1초 후 메세지 삭제
  if message.content ==  "삭제":
    msg = await message.channel.send("안녕하세요")
    await asyncio.sleep(1)
    await msg.delete()


  ### error가 남 AttributeError: 'User' object has no attribute 'voice'
  ### 음성채널에 입장,퇴장하고 유튜브 url을 통해 음악을 재생시키는 함수 -> 미완성-> 위의 오류 해결해야함 
  if message.content ==  "입장":
    await message.author.voice.channel.connect()
    await message.channel.send("음성채널에 입장")


  if message.content ==  "퇴장":
    for vc in client.voice_clients:
      if vc.guild == message.guild:
        voice = vc

    await voice.disconnect()
    await message.channel.send("음성 채널 퇴장")

  ### 봇이 가진 보이스를 길드에서 찾고 유튜브의 url을 mp3로 변환
  ### 그 후 mp3 파일을 다운로드 한 후 FFmpeg를 통해서 재생함
  if message.content ==  "재생": 
    for vc in client.voice_clients:
      if vc.guild == message.guild:
        voice = vc

    url = message.content.split(" ")[1]
    option = {
        'outtmpl' : "file/" + url.split('=')[1] + ".mp3"
    }

    with youtube_dl.YoutubeDL(option) as ydl:
      ydl.download(url)
      info = ydl.extract_info(url, download=False) #위 코드에서 다운로드했기 때문에 False
      title = info["title"] #곡의 제목 

    voice.play(discord.FFmpegPCMAudio("file/" + url.split('=')[1] + ".mp3"))
    await message.channel.send(title + "을 재생합니다")

    
  await bot.process_commands(message)


bot.run(TOKEN)




