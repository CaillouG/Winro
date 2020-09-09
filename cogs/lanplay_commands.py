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
        embed = discord.Embed(
            color = discord.Colour.orange()
        )
        embed.set_author(name='Winro', icon_url="http://winro.rf.gd/images/minia.png")
        embed.description="__Commandes LanPlay :__"
        embed.add_field(name='w!pack', value="-> Donne le lien pour le pack spécial LanPlay", inline=False)
        embed.add_field(name='w!serveur', value='-> Donne le lien du serveur discord LanPlay FR', inline=False)
        embed.add_field(name='w!site', value='-> Donne le lien du site LanPlay FR', inline=False)
        embed.set_footer(text="Créer par WhitePixels#9953")
        await ctx.send(embed=embed)

    @commands.command(pass_context=True)
    @isPrivateCommand()
    async def pack(self, ctx): 
        embed = discord.Embed(
            colour = discord.Colour.orange()
        )
        embed.set_author(name='Pack LanPlay', icon_url="http://winro.rf.gd/images/minia.png"")
        embed.add_field(name='Crée par WhitePixels', value="[Pack Complet LanPlay](https://1drv.ms/f/s!AjRUC3ntRrt1gX2CMItbpMMK9ghn)", inline=True)
        await ctx.send(embed=embed)

    @commands.command(pass_context=True)
    @isPrivateCommand()
    async def site(self, ctx):
        embed = discord.Embed(
            colour = discord.Colour.orange()
        )
        embed.set_author(name='Site LanPlay FR', icon_url="http://winro.rf.gd/images/minia.png")
        embed.add_field(name='Crée par WhitePixels ', value="[Site LanPlay FR](http://lanplay-fr.byethost4.com/)", inline=True)
        await ctx.send(embed=embed)

    @commands.command(pass_context=True)
    @isPrivateCommand()
    async def serveur(self, ctx):
        embed=discord.Embed(
            colour=discord.Colour.orange()
        )
        embed.set_author(name='Serveur Discord LanPlay FR :', icon_url="http://winro.rf.gd/images/minia.png")
        embed.add_field(name ='Lien pour le serveur discord LanPlay FR :', value="https://discord.gg/tfeeGXn", inline=True)
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(LanPlay(bot))
