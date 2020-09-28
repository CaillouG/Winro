import discord
import discord.utils 
import os
from discord.ext import commands

class Misc(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def ping(self, ctx):
        owner = self.bot.get_user(323111825975672862)
        await owner.send(f"``{ctx.author}`` à fait la commande ``ping`` dans le serveur ``{ctx.guild}``")
        await ctx.send(f"Pong {ctx.author.mention} ! Ma latence est de ``{round(self.bot.latency * 1000)} ms`` !")

    @commands.command(pass_context=True) 
    async def say(self, ctx, *, arg):
        owner = self.bot.get_user(323111825975672862)
        await owner.send(f"``{ctx.author}`` à fait la commande ``say`` dans le serveur ``{ctx.guild}``")
        role = discord.utils.get(ctx.guild.roles, name="Muted")
        await ctx.channel.purge(limit=1)
        if "discord.gg" in arg or "@everyone" in arg:
            await ctx.author.add_roles(role)
            await ctx.send(f"{ctx.author.mention} est réduit au silence pour : Tentative de pub | Mass ping")
            await ctx.author.send(f"Vous avez été réduit au silence pour la raison suivante : Tentative de pub | Mass ping")
        else :
            await ctx.send(arg)
        embed=discord.Embed(
            colour=discord.Colour.orange()
        )
        embed.set_author(name="Say :", icon_url="https://winro-bot.000webhostapp.com/ressources/say.png")
        embed.add_field(name="Winro", value=f"{ctx.author.mention} a dit avec w!say : {arg}", inline=True)
        embed.set_footer(text="Créé par WhitePixels#9953")
        if os.path.isfile(f"./cogs/logs/{ctx.guild.id}.txt") == True :
            logfile = open(f"./cogs/logs/{ctx.guild.id}.txt", "r")
            logchannel = logfile.read()
            log = self.bot.get_channel(int(logchannel))
            await log.send(embed=embed)

    @say.error
    async def say_error(self, ctx, error):  
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Pour utiliser cette commande, il faut indiquer les mots que Winro va répéter : ``w!say Salut !``")
        elif isinstance(error, commands.BadArgument):
            await ctx.send("Pour utiliser cette commande, il faut indiquer les mots que Winro va répéter : ``w!say Salut !``")
        else:
            raise error

    @commands.command(pass_context=True)
    async def winro(self, ctx):
        owner = self.bot.get_user(323111825975672862)
        await owner.send(f"``{ctx.author}`` à fait la commande ``winro`` dans le serveur ``{ctx.guild}``")
        embed=discord.Embed(
            colour = discord.Colour.orange()
        )
        embed.set_author(name='Winro :', icon_url="https://winro-bot.000webhostapp.com/images/minia.png")
        embed.add_field(name ='Description de Winro :', value="Je suis Winro, bot de modération et de commandes dédiées de base au serveur LanPlay FR ! Créer par WhitePixels#9953 le 4 avril 2020, je propose quelques commandes, des commandes de modération avancées ou encore des commandes pour créer des salons privés !", inline=False)
        embed.add_field(name ="Site :", value="http://winro.rf.gd", inline=True)
        embed.add_field(name ="Discord officiel :", value="https://discord.gg/cMJeGFh", inline=True)
        embed.set_footer(text="Créé par WhitePixels#9953")
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Misc(bot))