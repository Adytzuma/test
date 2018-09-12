
@bot.command()
async def cat(ctx):
    async with aiohttp.ClientSession() as cs:
	async with cs.get('http://aws.random.cat/meow') as r:
            res = await r.json()
	    embed = discord.Embed(color=0x000000)
	    embed.title = "Woof Woof, a cat!"
	    embed.set_image(url=res['file'])
	    embed.set_footer(text=f"hai la hora ca e o pisica")
	    embed.timestamp = datetime.datetime.utcnow()
	    await ctx.send(embed=embed)


