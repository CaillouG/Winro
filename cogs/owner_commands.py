import discord 
import psutil
from discord.ext import commands 

class Owner(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def presence(self, ctx):
        if ctx.author.id == 323111825975672862 : 
            game = discord.Game(f"être sur {len(self.bot.guilds)} serveurs ! | prefix = w!")
            await self.bot.change_presence(status=discord.Status.online, activity=game)
            await ctx.send("Statut actualisé !")
        else :
            await ctx.send("Seul ``WhitePixels#9953`` peut actualiser le statut de Winro !")

    @commands.command(pass_context=True)
    async def slist(self, ctx):
        if ctx.author.id == 323111825975672862 : 
            embed=discord.Embed(
            colour = discord.Colour.orange()
            )
            embed.set_author(name='Winro :', icon_url="http://winro.rf.gd/images/minia.png")
            embed.set_footer(text="Créer par WhitePixels#9953")
            for guild in self.bot.guilds:
                embed.add_field(name = "Serveur :", value=f"``{guild}`` -> ``{guild.member_count} membres``", inline=False)
            await ctx.send(embed=embed)
        else :
            await ctx.send("Seul ``WhitePixels#9953`` peut voir la liste des serveurs sur lesquels est Winro !")

    @commands.command(pass_context=True)
    async def stats(self, ctx):
        if ctx.author.id == 323111825975672862 :
            embed=discord.Embed(
            colour = discord.Colour.orange()
            )
            embed.set_author(name='Winro :', icon_url="http://winro.rf.gd/images/minia.png")
            embed.description="__Statistiques du serveur de Winro :__"
            embed.add_field(name ="Utilisation CPU :", value=f"{psutil.cpu_percent(interval=None)}% d'utilisation CPU", inline=False)
            embed.add_field(name ="Utilisation Ram :", value=f"{psutil.virtual_memory()[2]}% de ram utilisé", inline=False)
            embed.add_field(name ="Ping :", value=f"{round(self.bot.latency * 1000)} ms", inline=False)
            embed.set_footer(text="Créé par WhitePixels#9953")
            await ctx.send(embed=embed)
        else :
            await ctx.send("Seul ``WhitePixels#9953`` peut voir les stats du serveur où est hébergé Winro !")

def setup(bot):
    bot.add_cog(Owner(bot))
