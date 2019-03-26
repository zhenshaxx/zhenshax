import discord
from discord.ext import commands
from discord.ext.commands import bot
import asyncio
import random
import os

client = commands.Bot(command_prefix='.')
player_dict = dict()

def has_permissions(ctx):
	return ctx.message.author.server_permissions.administrator

@client.event
async def on_ready():
	print('The bot is online and connected to discord!') 
	print(bot.user.name)
	print(bot.user.id)
	print('-------')

@client.command()
async def sub():
	await client.say('Go to this link and subscribe to PewDiePie. https://youtube.com/pewdiepie')
	
@client.command()
async def whoisdev():
	await client.say('```The developer is ZhensHax#2836.```')
	
@client.command()
async def devinfo():
	await client.say('```Developer discord: ZhensHax#2836. Developer Youtube Channel: ZhensHax GT.```')
    
@client.command()
async def prefix():
	await client.say('My command prefix is .')
	
@client.command(pass_context = True)
async def say(ctx, *, msg: str):
      await client.say(msg)
      
@client.command(pass_context = True)
async def clear(ctx, amount):
    channel = ctx.message.channel

    messages = []

    async for message in client.logs_from(channel, limit=int(amount) +1):

        messages.append(message)

    await client.delete_messages(messages)

    await client.say(str(amount) + ' Message were deleted.')
    
@client.command()
async def leet():
	await client.say('ZhensHax, LaYellow, and GDNXDD is 1337 ok, cuz we kill Reg4shi 24/7')

@client.command()
async def donate():
	await client.say('Support the developer by donating here: https://paypal.me/zhenshax, Thank you.')
    
@client.event
async def on_ready():	 await client.change_presence(game=discord.Game("with ZhensHax#2836","https://www.twitch.tv/ninja")
    
@client.command()
async def howgay( *args):
	
    g = random.randint(1,100)
    output = ''
    if str(args) == '()':
        args = 'You'
        areis = 'are'
    else:
        areis = 'is'
    for word in args:
        output += word
    await client.say(':gay_pride_flag: {} {} {}% gay '.format(output, areis ,g))
    
@client.command(pass_context = True)
@commands.check(has_permissions)
async def ban(ctx,user:discord.Member):
	await client.ban(user)
	await client.say("The ancient used ban to {}. https://youtube.com/pewdiepie".format(user.name))
	
@client.command(pass_context = True)
@commands.check(has_permissions)
async def kick(ctx,user:discord.Member):
	await client.kick(user)
	await client.say("The ancient used kick to {}. https://youtube.com/pewdiepie".format(user.name))

@client.command(pass_context=True)
async def ping(ctx):
    t = await client.say('Pong!')
    ms = (t.timestamp-ctx.message.timestamp).total_seconds() * 1000
    await client.edit_message(t, new_content='My heart is {}ms'.format(int(ms)))
	
	
    
client.run(str(os.environ.get('TOKEN')))
