import discord
import random
from discord.ext import commands
import logging
import traceback
import asyncio
import os
from discord import opus
from asyncio import sleep


class Utility():
	def __init__(self, bot):
		self.bot = bot
		colors = [discord.Colour.purple(), discord.Colour.blue(), discord.Colour.red(), discord.Colour.green(), discord.Colour.orange()]





        @commands.cooldown(1, 5, commands.BucketType.user)
	@commands.command(aliases= ['botinfo'])
        async def about(self, ctx):
            e = discord.Embed(color=random.choice(colors))
            e.add_field(name=':family_mwgb: Servers', value=f'{len(bot.guilds)}', inline=True)
            e.add_field(name=':bust_in_silhouette: Users', value=f'{len(bot.users)}', inline=True)
            e.add_field(name=':cloud: Latency', value=f'{ctx.bot.latency * 1000:.0f} MS')
            e.add_field(name=':crown: Owner', value=f'<@404708655578218511>')
            e.add_field(name=':clock1: Created at', value=ctx.me.created_at)
            e.add_field(name=':control_knobs: Library', value='Python (discord.py)')
            e.set_thumbnail(url=ctx.me.avatar_url)
            e.set_footer(text='Thank you for using Atomical <3')
            await ctx.send(embed=e)





        @commands.cooldown(1, 5, commands.BucketType.user)
        @commands.command(aliases= ["Avatar", "AVATAR"])
        async def avatar(self, ctx, member: discord.Member=None):
            """Get your info"""
            if member is None:
                member = ctx.author
            em = discord.Embed(title="", color=random.choice(colors))
            em.set_author(name=f"{member.mention}'s avatar")
            em.set_image(url=member.avatar_url)
            msg = await ctx.send(embed=em)





        @commands.cooldown(1, 5, commands.BucketType.user)
        @commands.command(aliases= ["Support", "SUPPORT"])
        async def support(self, ctx):
            em = discord.Embed(title="", description="", color=random.choice(colors))
            em.add_field(name='Support Server', value='[Here]( https://discord.gg/Aeq7jmK )')
            await ctx.send(embed=em)



        @commands.cooldown(1, 5, commands.BucketType.user)
        @commands.command(aliases= ["Invite", "INVITE"])
        async def invite(self, ctx):
            em = discord.Embed(title="", color=random.choice(colors))
            em.add_field(name=f'Invite **{ctx.me.name}**', value='[Here]( https://discordapp.com/oauth2/authorize?client_id=464683212174786561&permissions=104082502&scope=bot)')
            await ctx.send(embed=em)




        @commands.cooldown(1, 5, commands.BucketType.user)
        @commands.command(aliases= ["Serverinfo", "SERVERINFO", "Sinfo", "SINFO", "sinfo"])
        async def serverinfo(self, ctx):
            """Get the server info"""
            em = discord.Embed(color=random.choice(colors))
            em.add_field(name=':paintbrush: Name', value=f'{ctx.author.guild.name}', inline=False)
            em.add_field(name=':crown: Owner', value=f'{ctx.author.guild.owner.mention} [{ctx.author.guild.owner.id}]', inline=False)  
            em.add_field(name=':mountain_snow: Icon', value='Do a?servericon', inline=False)
            em.add_field(name=':family_mwgb: Roles', value='Do a?serverroles', inline=False)
            em.add_field(name=':bust_in_silhouette: Members', value=f'{ctx.guild.member_count}', inline=False)
            em.add_field(name=':clock1: Created at', value=ctx.guild.created_at, inline=False)
            em.set_thumbnail(url=ctx.guild.icon_url)
            await ctx.send(embed=em)



        @commands.cooldown(1, 5, commands.BucketType.user)
        @commands.command(aliases=['sroles', 'SROLES', 'Sroles', 'SERVERROLES', 'Serverroles'])
        async def serverroles(self, ctx):
            em = discord.Embed(color=random.choice(colors))
            em.add_field(name=f'Server Roles [{len(ctx.guild.roles)}]', value=', '.join(g.name for g in ctx.guild.roles))
            await ctx.send(embed=em)





        @commands.cooldown(1, 5, commands.BucketType.user)
        @commands.command(aliases =['Servericon', 'SERVERICON', 'sicon', 'Sicon', 'SICON'])
        async def servericon(self, ctx):
            em = discord.Embed(title="", color=random.choice(colors))
            em.set_author(name=f"{ctx.guild.name}'s icon")
            em.set_image(url=ctx.guild.icon_url)
            await ctx.send(embed=em)
        



        
        @commands.cooldown(1, 5, commands.BucketType.user)
        @commands.command(aliases= ["Playerinfo", "PLAYERINFO", "pinfo", "PINFO", "Pinfo"])
        async def playerinfo(self, ctx, member: discord.Member=None):
            """Get your info"""
            if member is None:
                member = ctx.author
            em = discord.Embed(title=f"{member}'s info", color=random.choice(colors))
            em.set_author(name="Player info")
            em.add_field(name="Name", value=member.name)
            em.add_field(name="ID", value=member.id)
            em.add_field(name="BOT:", value=member.bot)
            em.add_field(name="Tag", value=member.discriminator)
            em.add_field(name="Top Role", value=member.top_role)
            em.add_field(name="Nick", value=member.nick)
            em.add_field(name="Joined", value=member.joined_at)
            em.set_thumbnail(url=member.avatar_url)
            msg = await ctx.send(embed=em)


























def setup(bot):
        bot.add_cog(Utility(bot))
