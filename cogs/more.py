import discord
import random
from discord.ext import commands
import logging
import traceback
import asyncio
import os
from discord import opus
from asyncio import sleep


class More():
	def __init__(self, bot):
		self.bot = bot
		colors = [discord.Colour.purple(), discord.Colour.blue(), discord.Colour.red(), discord.Colour.green(), discord.Colour.orange()]





  	
        @commands.cooldown(1, 5, commands.BucketType.user)
        @commands.command(aliases= ["dbl", "dblist", "discordbl", "dbotl", "Discordbotlist", "DBL"])
        async def discordbotlist(self, ctx):
            em = discord.Embed(title="", color=random.choice(colors))
            em.add_field(name="Discord Bot List", value='[Atomical]( https://discordbots.org/bot/464683212174786561 )', inline=False)
            em.add_field(name="Discord Server List", value='[Atomical Tech Server]( https://discordbots.org/servers/465203534057570305 )', inline=False)
            await ctx.send(embed=em)




        @commands.cooldown(1, 60, commands.BucketType.user)
        @commands.command(aliases= ["Feedback", "FEEDBACK"])
        async def feedback(self, ctx, *, message=None):
            if message is None:
                await ctx.send('Hey, please do `a?feedback <feedback>`')
            if message is not None:
                await self.bot.get_channel(465222513887150080).send(f'{ctx.author.name} reported: {message}')
                await ctx.send('Your feedback was reported to the team')







        @commands.cooldown(1, 60, commands.BucketType.user)
        @commands.command(aliases= ["Bug", "BUG"])
        async def bug(self, ctx, *, message=None):
            if message is None:
                await ctx.send('Hey, please do `a?bug <bug>`')
            if message is not None:
                await self.bot.get_channel(465222806410362891).send(f'{ctx.author.name} reported: {message}')
                await ctx.message.channel.send('Your problem was reported to the team')







	




















def setup(bot):
        bot.add_cog(More(bot))

