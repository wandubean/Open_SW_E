# __E 팀 활동 기록지__

## 팀 구성  
* 팀장 : 인공지능학과 2022022160 이나영 
* 팀원 : 인공지능학과 2022034711 이경준  
* 팀원 : 인공지능학과 2021098904 권오준  
* 팀원 : 인공지능학과(다중전공) 2021075169 김도완  

## 프로젝트 개요
 본 프로젝트는 디스코드에 새로운 봇을 생성하여 자신의 디스코드 서버에 추가하는 것을 목적으로 한다. 자신이 디스코드를 사용하며 추가하고 싶었던 봇을 직접 생성하여 서버에 추가하는 데에 의의가 있으며, 개인이 느꼈을 때 추가하고 싶었던 기능의 봇을 생성하기 위해 해당 프로젝트를 진행하게 되었다.  

## __1주차__  

 ### __역할 분담__
  * 공통 : 회의 참여
  * 이나영, 이경준 : 보고서 작성
  * 김도완, 권오준 : 디스코드 봇 생성 및 서버 구현  

 ### __github 사진__
  ![깃헙 사진](https://cdn.discordapp.com/attachments/829035801849233451/1052227490355105843/image.png)

## __2주차__
 ### __활동 내용__
  명령어를 입력하면 그 명령어에 대한 대답을 출력하는 간단한 봇을 구현하였다. 디스코드 상에서 간단한 대화를 나눌 수 있는 프로그램으로, "!" 를 붙여 명령어로 인식시킬 수 있다.  

  현재 구현되어 있는 명령어는 4가지로 !hello, !bye, !good, !talk가 있다. 또한,등록되어 있지 않은 명령어가 입력된다면 "명령어를 찾지 못했습니다" 라는 메세지를 출력한다.

  ### _코드_
  ```python
  import discord, asyncio
  from discord.ext.commands import Bot
  from discord.ext import commands
  import random
  import numpy as np


  TOKEN = 'my token' ### 내 디스코드 봇의 토큰 값 -> 디스코드 개발자 사이트를 통해서 알 수 있음

  intents = discord.Intents.all()
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

  bot.run(TOKEN)
  ```
## __3주차__
 ### __활동내용__
 - Github 원격 저장소를 본격적으로 사용하였다.
 - 오류 발생 시 오류가 발생했다는 메시지를 출력하게 하였다.
 - Roll_dice명령어를 이용하여 주사위 게임을 작동시킬 수 있다.
 - 봇을 음성채널에 추가 및 제거하는 코드를 구현하였다.
 - 채팅 메시지를 특정 amount 만큼 삭제하는 것을 구현하였다.
 - 봇의 정보를 출력하는 기능을 구현하였다.
 - 봇이 있는 폴더에 있는 사진 파일을 전송시키는 기능을 구현하였다.
 - 도움말 기능을 추가하였다.
 - 이모티콘을 사용하기 위한 코드를 추가하였다.

 ### _코드_
 ```python
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
 ```
 ```python
 @bot.command()  ### 봇이 다른 채널에 접속시키게 함
async def play(ctx):
  channel = ctx.author.voice.channel
  await channel.connect()

@bot.command()
async def leave(ctx): ### 봇이 지금 채널에서 나가게 함
  await bot.voice_clients[0].disconnect()

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
 ```
 ```python
 @bot.command() ### 채팅 메세지를 amount 만큼 삭제
async def clear(ctx, amount: int):
  await ctx.channel.purge(limit = amount)
 ```
 ```python
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

 ```
 ```python
 @bot.command(name = "도움말")
async def HelpMessage(ctx):
  embed = discord.Embed(title = "명령어 목록")
  embed.add_field(name = "!안녕", value = "Hi there!", inline = False)
  embed.add_field(name = "!잘가", value = "C U later!", inline = False)
  embed.add_field(name = "!good", value = "I`m good", inline = False)
  embed.add_field(name = "!대화 (a) (b)", value = "(a) talk to (b)", inline = False)
  embed.add_field(name = "!이모티콘", value = "이모티콘 리스트", inline = False)
  await ctx.channel.send(embed = embed)
 ```
 ```python
 @bot.command(name = "이모티콘")
async def emoticon(ctx):
  embed = discord.Embed(title = "이모티콘 목록")
  embed.add_field(name = "!라이언", value = "라이언", inline = False)
  await ctx.channel.send(embed = embed)
 ```
 ```python
 @bot.command(name = "라이언")
async def RYAN(ctx):
    embed = discord.Embed(title = "")
    embed.set_image(url="https://cdn.discordapp.com/attachments/829035801849233451/1049585159210545152/2Q.png")
    await ctx.channel.send(embed = embed)
 ```
## __4주차__
 ### __활동내용__
- 명령어 식별자 (현재 프로젝트 기준 기호 "!") 없이 인식하는 명령어를 만들었다.
    - 기존에 있던 '안녕', '잘가', 'good' 등의 명령어를 구현하였다.
    - 다른 채널에 메시지를 보내주는 기능을 구현하였다.
    - FFmpeg를 이용해 음성 채널에서 음악을 재생시키는 기능을 구현하였다.
    - 1초후 삭제되는 메시지를 구현하였다.
- Google SpreadSheet와 연동하여 연결된 SpreadSheet의 데이터를 가져오는 기능을 구현하였다.
 ### _코드_
```python
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
 ```
 ```python
 import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds']
json_file_name = "./open-sw-e-10852ba80e41.json"
credentials = ServiceAccountCredentials.from_json_keyfile_name(json_file_name, scope)
gc = gspread.authorize(credentials)
spreadsheet_url = 'https://docs.google.com/spreadsheets/d/1tDD3vQBdLmL5-OG3OC5ovFRP2xbQfa0pIrI7MN6PgUs/edit?usp=sharing'
sheet = gc.open_by_url(spreadsheet_url).get_worksheet(0)

# 시트의 내용 출력
@bot.command(name = "내용")
async def sheet_out(ctx, a):
    data = sheet.get(a)
    await ctx.reply(data)
    return
 ```