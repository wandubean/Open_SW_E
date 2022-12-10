import discord
from discord.ext import commands
import numpy as np
import gspread
from oauth2client.service_account import ServiceAccountCredentials

TOKEN = 'bot_token' ### 내 디스코드 봇의 토큰 값
intents = discord.Intents.all()

scope = ['https://spreadsheets.google.com/feeds']
json_file_name = "./open-sw-e-10852ba80e41.json"
credentials = ServiceAccountCredentials.from_json_keyfile_name(json_file_name, scope)
gc = gspread.authorize(credentials)
spreadsheet_url = 'https://docs.google.com/spreadsheets/d/1tDD3vQBdLmL5-OG3OC5ovFRP2xbQfa0pIrI7MN6PgUs/edit?usp=sharing'
sheet = gc.open_by_url(spreadsheet_url).get_worksheet(0)

# !로 시작하면 명령어로 인식
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'logged in as {bot.user}')  ### 내 봇이 디스코드에 로그인하면 터미널에 "logged in as {bot.user}" 메세지를 출력

# 도움말 메세지 출력
@bot.command(name = "도움말")
async def help_message(ctx):
    embed = discord.Embed(title = "명령어 목록")
    embed.add_field(name = "!안녕", value = "Hi there!", inline = False)
    embed.add_field(name = "!잘가", value = "C U later!", inline = False)
    embed.add_field(name = "!good", value = "I`m good", inline = False)
    embed.add_field(name = "!대화 (a) (b)", value = "(a) talk to (b)", inline = False)
    embed.add_field(name = "!이모티콘", value = "이모티콘 리스트", inline = False)
    embed.add_field(name = "!내용 (셀 번호)", value = "해당 셀의 내용을 출력합니다", inline = False)
    await ctx.channel.send(embed = embed)

# 디스코드 서버에 !이모티콘 입력하면 디스코드 봇이 이모티콘 리스트를 출력
@bot.command(name = "이모티콘")
async def emoticon(ctx):
    embed = discord.Embed(title = "이모티콘 목록")
    embed.add_field(name = "!라이언", value = "라이언", inline = False)
    await ctx.channel.send(embed = embed)

# !hello 명령어 처리
# 디스코드 서버에 !안녕 !hello를 입력하면 디스코드 봇이 'Hi, there!' 메세지를 출력
@bot.command(name = "안녕")
async def hello(ctx):
    await ctx.channel.send('Hi, there!') ###ctx.channel.send() 로 바꾸면 자기 채널로 메세지 나감

# !bye 명령어 처리
# 디스코드 서버에 !잘가 !bye를 입력하면 디스코드 봇이 'See you later!' 메세지를 출력 
@bot.command(name = "잘가")
async def bye(ctx):
    await ctx.reply('See you later!')

# !good 명령어 처리
# 디스코드 서버에 !good 입력하면 디스코드 봇이 'I'm good' 메세지를 출력
@bot.command()
async def good(ctx):
    await ctx.reply('I\'m good')  

# ! talk 명령어 처리
# 디스코드 서버에 !대화 !talk a b 입력하면 디스코드 봇이 '{a} talk to {b}' 메세지를 출력
@bot.command(name = "대화")
async def talk(ctx,b,c):
    await ctx.reply('{} talks to {}'.format(b,c))


### 오류 발생시 -> "명령어를 찾지 못했습니다" 메세지를 출력
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.channel.send("명령어를 찾지 못했습니다")

# 디스코드 서버에 !라이언 입력하면 디스코드 봇이 라이언 이모티콘 출력
@bot.command(name = "라이언")
async def RYAN(ctx):
    embed = discord.Embed(title = "")
    embed.set_image(url="https://cdn.discordapp.com/attachments/829035801849233451/1049585159210545152/2Q.png")
    await ctx.channel.send(embed = embed)
    return

# 시트의 내용 출력
@bot.command(name = "내용")
async def sheet_out(ctx, a):
    data = sheet.get(a)
    await ctx.reply(data)
    return

bot.run(TOKEN)