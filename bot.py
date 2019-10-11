import discord
from discord.ext import commands
from discord.ext.commands import bot
import asyncio
import random
import os
import time

client = commands.Bot(command_prefix='.')
player_dict = dict()

def has_permissions(ctx):
	return ctx.message.author.server_permissions.administrator

@client.event
async def on_ready():
	print('The bot is online and connected to discord!') 

@client.command()
async def sub():
	await client.say('sub Zhens X or b4n')
	
@client.command()
async def developer():
	await client.say('```The developer is ZhensHax#7992, some fixes by LaYellow#4241. © Bot by ZhensHax#7992 & LaYellow#4241```')
	
@client.command()
async def info():
     await client.say('```Developer: ZhensHax#7992. this most kanser bot in world```')
     await client.say('```my owner mad cuz me is kanser me orang bgst wait a sec me is not orang')
   

@client.command()
async def prefix():
	await client.say('My command prefix is . gk need ask')
	
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

    await client.say(str(amount) + ' message deleted expose ass')
    
@client.command()
async def leet():
	await client.say('ZhensHax, LaYellow, and GDNXDD is 1337 ok, cuz we kill Reg4shi 24/7')
	
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
	await client.say("Successfully banned {} like pro moms. https://youtube.com/pewdiepie".format(user.name))
	
@client.command(pass_context = True)
@commands.check(has_permissions)
async def kick(ctx,user:discord.Member):
	await client.kick(user)
	await client.say("Successfully kick {} to 荷兰. https://youtube.com/pewdiepie".format(user.name))

@client.command(pass_context=True)
async def ping(ctx):
    t = await client.say('Pong!')
    ms = (t.timestamp-ctx.message.timestamp).total_seconds() * 1000
    await client.edit_message(t, new_content='My heart is {}ms'.format(int(ms)))


@client.event
async def on_ready():
	await client.change_presence(game=discord.Game(name='with mom and my owner leet', type = 1))
	
	
@client.command()
async def howretard( *args):
	
    g = random.randint(1,100)
    output = ''
    if str(args) == '()':
        args = 'You'
        areis = 'are'
    else:
        areis = 'is'
    for word in args:
        output += word
    await client.say('**{} {} {}% retard.** '.format(output, areis ,g))

@client.command(pass_context = True)
async def fban(ctx,user:discord.Member):
	await client.say('**User has been successfully banned.**')


		
	

	
    
    
   
        
        


    
client.run(str(os.environ.get('TOKEN')))
