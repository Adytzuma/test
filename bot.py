#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-
import discord
import random
from discord.ext import commands
import logging
import traceback
import asyncio
import os
from discord import opus
from asyncio import sleep



logging.basicConfig(level='INFO')
bot = commands.Bot(command_prefix='a?')
bot.load_extension("cogs.hi")

bot.load_extension("cogs.admin")
bot.load_extension("cogs.music")
bot.load_extension("cogs.fun")
bot.load_extension("cogs.utility")
bot.load_extension("cogs.moderation")

bot.remove_command('help')
colors = [discord.Colour.purple(), discord.Colour.blue(), discord.Colour.red(), discord.Colour.green(), discord.Colour.orange()]
owner = [404708655578218511]
"""
OPUS_LIBS = ['libopus-0.x86.dll', 'libopus-0.x64.dll', 'libopus-0.dll', 'libopus.so.0', 'libopus.0.dylib']

def load_opus_lib(opus_libs=OPUS_LIBS):
    if opus.is_loaded():
        return True
    for opus_lib in opus_libs:
        try:
            opus.load_opus(opus_lib)
            return
        except OSError:
            pass
    raise RuntimeError('Could not load an opus lib. Tried %s' % (', '.join(opus_libs)))
load_opus_lib()
"""
    




    
    

    
    

        
        

@bot.command()
async def help(ctx):
    em = discord.Embed(color=random.choice(colors))
    em.add_field(name='★Fun★', value='`8ball, lenny, respect, ping, poll, choose, calculate`', inline=True)                     
    em.add_field(name='★More★', value='`bug, feedback, dbl`', inline=True)
    em.add_field(name='★Moderation★', value='`kick, ban, purge`', inline=True)
    em.add_field(name='★Utility★', value='`servericon, serverroles, serverinfo, playerinfo, avatar, support, botinfo`', inline=True)
    em.add_field(name='★Music★', value='`play, stop, skip, queue, playing, pause, unpause, join`', inline=True)
    em.set_footer(text="Use 'a?' before each command", icon_url=ctx.me.avatar_url)
    em.set_thumbnail(url=ctx.me.avatar_url)
    await ctx.send(embed=em)
    


@bot.check
async def botcheck(ctx):
    return not ctx.message.author.bot


"""
  
@bot.command(aliases= ["kitten", "kitty"])
async def cat(ctx):
    fp = "cat/{}".format(random.choice(os.listdir("cat")))
    await ctx.send(file=discord.File(fp))    
"""
        
@bot.listen()
async def on_ready():
          print('Logging in as', bot.user.name)
       
            
         
            




@commands.cooldown(1, 5, commands.BucketType.user)
@bot.command(aliases= ["Say", "SAY"])
@commands.is_owner()
async def say( ctx, *, message):
    'Make the BOT say what you want'
    await ctx.send(f'{message}')




        
@commands.is_owner()
@bot.command(aliases= ["Shutdown", "SHUTDOWN"])
async def shutdown(ctx):
    await ctx.send('Shutting down...')
    await sleep(2)
    await ctx.bot.logout()

@commands.is_owner()
@bot.command(name='reload', hidden=True)
async def _reload(ctx, *, module):
         """Reloads a module."""
         try:
             bot.unload_extension(module)
             bot.load_extension(module)
         except Exception as e:
            return await ctx.send(f'```py\n{traceback.format_exc()}\n```')
         else:
            await ctx.send('\N{OK HAND SIGN}')
			

        

@bot.listen()
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        return await ctx.send(f':no_entry: | Hey, You are being ratelimited! Try again in** {int(error.retry_after)} **seconds!', delete_after=5)
    if isinstance(error, commands.NotOwner):
        return await ctx.send(':warning: You do not own this bot!')
    if isinstance(error, commands.MissingPermissions):
        return await ctx.send('You are missing permission to execute this command')
    if isinstance(error, commands.BotMissingPermissions):
        return await ctx.send('I am missing permission to perform this command!')

"""
@commands.cooldown(1, 5, commands.BucketType.user)
@bot.command()
async def search(ctx, *, query):
    search = query
    URL = 'https://www.google.com/search?q='
    words = search.split(" ")

    num = 0
    for w in words:
        if num is 0:
            URL = URL + w
            num = 1
        else:
            URL = URL + "+"+ w

    await ctx.send(URL)
    """




   
























    










async def presence():
    await bot.wait_until_ready()
    while not bot.is_closed():
        a = 0
        for i in bot.guilds:
            for u in i.members:
                if u.bot == False:
                    a = a + 1

        await bot.change_presence(activity=discord.Streaming(name=f"{len(bot.guilds)} servers | a?help", url='https://www.twitch.tv/adytzuma '))
        await sleep(30)
        await bot.change_presence(activity=discord.Streaming(name=f"{len(bot.users)} users | a?help", url='https://www.twitch.tv/adytzuma '))
        await sleep(30)




       

            








bot.loop.create_task(presence())
bot.run(os.getenv("TOKEN"))

