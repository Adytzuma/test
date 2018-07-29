import discord
import random
from discord.ext import commands
import logging
import traceback
import asyncio
import os
from discord import opus
from asyncio import sleep



class Fun():
	def __init__(self, bot):
		self.bot = bot
	
	


        @commands.command(name='8ball')
        async def l8ball(self, ctx, question=None):
            if question is None:
                return await ctx.send('Hey, please do `a?8ball <question>`')
            if question is not None:
                await ctx.send(random.choice(['● It is certain.', '● It is decidedly so.', '● Without a doubt.', '● Yes - definitely.', '● You may rely on it', '● As I see it, yes.', '● Most likely.', '● Outlook good.', '● Yes.', '● Signs point to yes.', '● Reply hazy, try again', '● Ask again later.', '● Better not tell you now.', '● Cannot predict now.', '● Concentrate and ask again.', '● Don`t count on it.', '● My reply is no.', '● My sources say no', '● Outlook not so good.', '● Very doubtful.' ]))


        @commands.cooldown(1, 5, commands.BucketType.user)
        @commands.command(aliases= ['calc'])
        async def calculate(self, ctx, a: int, d, b: int):
            s = ['+', '-', '*', '/', '^']
            if d == '+':
                return await ctx.send(a + b)
            if d == '*':
                return await ctx.send(a * b)
            if d == '^':
                return await ctx.send(a ^ b)
            if d == '-':
                return await ctx.send(a - b)
            if d == '/':
                return await ctx.send(f'{a / b:.3f}')
            if d != s:
                await ctx.send('Invalid equation')


        @commands.cooldown(1, 5, commands.BucketType.user)
        @commands.command()
        async def choose(self, ctx, option1, option2):
            a = [option1, option2]
            if option1 == option2:
                return await ctx.send(":x: | I can't choose the same things")
            await ctx.send(f':thinking: | {ctx.author.mention}, i choose **' + random.choice(a) + '** !')


        @commands.cooldown(1, 5, commands.BucketType.user)
        @commands.command()
        async def poll(self, ctx, *, question):
            em = discord.Embed(color=random.choice(colors))
            em.add_field(name='Question:', value=question)
            em.set_footer(icon_url=ctx.author.avatar_url, text=f'Requested by {ctx.author}')
            msg = await ctx.send(embed=em)
            win = await msg.add_reaction('\N{THUMBS UP SIGN}')
            lose = await msg.add_reaction('\N{THUMBS DOWN SIGN}')




        @commands.cooldown(1, 5, commands.BucketType.user)
        @commands.command(aliases= ["Ping", "PING"])
        async def ping(self, ctx):
            """Get your MS"""
            em = discord.Embed(title="", description="", color=random.choice(colors))
            em.set_author(name="")
            em.add_field(name="Ping", value='Pong! :ping_pong:', inline=True)
            em.add_field(name="MS", value=f'Took : **{ctx.bot.latency * 1000:,.0f} MS**', inline=True)
            await ctx.send(embed=em)



        @commands.cooldown(1, 5, commands.BucketType.user)
        @commands.command(aliases= ["Lenny", "LENNY"])
        async def lenny(self, ctx):
            """Get the lenny face"""
            await ctx.send("( ͡° ͜ʖ ͡° )")





        @commands.cooldown(1, 5, commands.BucketType.user)
        @commands.command(aliases= ["Respect", "RESPECT"])
        async def respect(self, ctx):
            """Pay respect"""
            em = discord.Embed(title="", description="", color=random.choice(colors))
            em.set_author(name="")
            em.add_field(name=f"{ctx.author.name}", value='Press :regional_indicator_f: to pay respect', inline=True)
            msg = await ctx.send(embed=em)
            await msg.add_reaction('\N{regional indicator symbol letter f}')
    




        












def setup(bot):
        bot.add_cog(Fun(bot))
