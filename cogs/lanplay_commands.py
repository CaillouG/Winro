import discord
import discord.utils
import asyncio
from discord.ext.commands import has_permissions
from discord.ext import commands

def isPrivateCommand():
    async def predicate(ctx):
        return ctx.guild.id == 691031678176722984
    return commands.check(predicate)  

class LanPlay(commands.Cog):
    def __init__(self, bot):
        self.bot = bot 

    @commands.command(pass_context=True)
    @isPrivateCommand()
    async def lanplay(self, ctx):
        owner = self.bot.get_user(323111825975672862)
        await owner.send(f"``{ctx.author}`` à fait la commande ``lanplay`` dans le serveur ``{ctx.guild}``")
        embed = discord.Embed(
            color = discord.Colour.orange()
        )
        embed.set_author(name='Winro', icon_url="https://winro-bot.000webhostapp.com/images/minia.png")
        embed.description="__Commandes LanPlay :__"
        embed.add_field(name='w!pack', value="-> Donne le lien pour le pack spécial LanPlay", inline=False)
        embed.add_field(name='w!serveur', value='-> Donne le lien du serveur discord LanPlay FR', inline=False)
        embed.add_field(name='w!site', value='-> Donne le lien du site LanPlay FR', inline=False)
        embed.set_footer(text="Créer par WhitePixels#9953")
        await ctx.send(embed=embed)

    @commands.command(pass_context=True)
    @isPrivateCommand()
    async def pack(self, ctx): 
        owner = self.bot.get_user(323111825975672862)
        await owner.send(f"``{ctx.author}`` à fait la commande ``pack`` dans le serveur ``{ctx.guild}``")
        embed = discord.Embed(
            colour = discord.Colour.orange()
        )
        embed.set_author(name='Pack LanPlay', icon_url="https://winro-bot.000webhostapp.com/images/minia.png")
        embed.add_field(name='Crée par WhitePixels', value="[Pack Complet LanPlay](https://1drv.ms/f/s!AjRUC3ntRrt1gX2CMItbpMMK9ghn)", inline=True)
        await ctx.send(embed=embed)

    @commands.command(pass_context=True)
    @isPrivateCommand()
    async def site(self, ctx):
        owner = self.bot.get_user(323111825975672862)
        await owner.send(f"``{ctx.author}`` à fait la commande ``site`` dans le serveur ``{ctx.guild}``")
        embed = discord.Embed(
            colour = discord.Colour.orange()
        )
        embed.set_author(name='Site LanPlay FR', icon_url="https://winro-bot.000webhostapp.com/images/minia.png")
        embed.add_field(name='Crée par WhitePixels ', value="[Site LanPlay FR](http://lanplay-fr.rf.gd/)", inline=True)
        await ctx.send(embed=embed)

    @commands.command(pass_context=True)
    @isPrivateCommand()
    async def serveur(self, ctx):
        owner = self.bot.get_user(323111825975672862)
        await owner.send(f"``{ctx.author}`` à fait la commande ``serveur`` dans le serveur ``{ctx.guild}``")
        embed=discord.Embed(
            colour=discord.Colour.orange()
        )
        embed.set_author(name='Serveur Discord LanPlay FR :', icon_url="https://winro-bot.000webhostapp.com/images/minia.png")
        embed.add_field(name ='Lien pour le serveur discord LanPlay FR :', value="https://discord.gg/tfeeGXn", inline=True)
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(LanPlay(bot))
