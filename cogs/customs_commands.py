import discord
import asyncio
import discord.utils 
import os
from discord.ext import commands

def isPrivateCommand():
    async def predicate(ctx):
        return ctx.guild.id == 726464239945908318
    return commands.check(predicate)  

class Customs(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    @isPrivateCommand()
    async def mute(self, ctx, user : discord.Member, *, reason=None):
        owner = self.bot.get_user(323111825975672862)
        await owner.send(f"``{ctx.author}`` à fait la commande ``mute`` dans le serveur ``{ctx.guild}``")
        role = discord.utils.get(ctx.guild.roles, name="Muted")
        membersrole = discord.utils.get(ctx.guild.roles, name="Membres")
        if ctx.channel.permissions_for(ctx.author).manage_roles :
            if role == None :
                await ctx.send("Le mute n'est pas mis en place sur ce serveur ! Faites ``w!setup mute`` pour le faire !")
            else :
                await user.add_roles(role)
                await user.remove_roles(membersrole)
                await ctx.channel.purge(limit=1)
                if reason == None :
                    await ctx.send(f"{user.mention} a été réduit au silence !")
                    await user.send(f'Vous avez été réduit au silence dans le serveur {ctx.guild} !')
                    embed=discord.Embed(
                        colour = discord.Colour.orange()
                    )
                    embed.set_author(name="Mute :", icon_url="https://winro-bot.000webhostapp.com/ressources/mute.png")
                    embed.add_field(name="Winro", value=f"{ctx.author.mention} a réduit au silence {user.mention} dans #{ctx.channel}", inline=True)
                    embed.set_footer(text="Créé par WhitePixels#9953")
                    if os.path.isfile(f"./cogs/logs/{ctx.guild.id}.txt") == True :
                        logfile = open(f"./cogs/logs/{ctx.guild.id}.txt", "r")
                        logchannel = logfile.read()
                        log = self.bot.get_channel(int(logchannel))
                        await log.send(embed=embed)
                else:
                    await ctx.send(f"{user.mention} a été réduit au silence pour la raison suivante : {reason}")
                    await user.send(f'Vous avez été réduit au silence dans le serveur {ctx.guild} pour la raison suivante : {reason}')
                    embed=discord.Embed(
                        colour = discord.Colour.orange()
                    )
                    embed.set_author(name="Mute :", icon_url="https://winro-bot.000webhostapp.com/ressources/mute.png")
                    embed.add_field(name="Winro", value=f"{ctx.author.mention} a réduit au silence {user.mention} dans #{ctx.channel} pour {reason}", inline=True)
                    embed.set_footer(text="Créé par WhitePixels#9953")
                    if os.path.isfile(f"./cogs/logs/{ctx.guild.id}.txt") == True :
                        logfile = open(f"./cogs/logs/{ctx.guild.id}.txt", "r")
                        logchannel = logfile.read()
                        log = self.bot.get_channel(int(logchannel))
                        await log.send(embed=embed)
        else : 
            await ctx.send("Vous n'avez pas la permission pour exécuter cette commande ! (Permission(s) requise(s) : gérer les rôles)")

    @mute.error
    async def mute_error(self, ctx, error):  
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Pour utiliser cette commande, il faut indiquer l'utilisateur à réduire au silence ainsi que la raison : ``w!mute @user spam``")
        elif isinstance(error, commands.BadArgument):
            await ctx.send("Pour utiliser cette commande, il faut indiquer l'utilisateur à réduire au silence ainsi que la raison : ``w!mute @user spam``")
        else:
            raise error

    @commands.command(pass_context=True)
    @isPrivateCommand()
    async def unmute(self, ctx, user : discord.Member):
        owner = self.bot.get_user(323111825975672862)
        await owner.send(f"``{ctx.author}`` à fait la commande ``unmute`` dans le serveur ``{ctx.guild}``")
        role = discord.utils.get(ctx.guild.roles, name="Muted")
        membersrole = discord.utils.get(ctx.guild.roles, name="Membres")
        if ctx.channel.permissions_for(ctx.author).manage_roles :
            await user.add_roles(membersrole)
            await user.remove_roles(role)
            await ctx.channel.purge(limit=1)
            await ctx.send(f"{user.mention} n'est plus réduit au silence !")
            await user.send(f"Vous n'êtes plus réduit au silence dans le serveur {ctx.guild} !")
            embed=discord.Embed(
                colour = discord.Colour.orange()
            )
            embed.set_author(name="UnMute :", icon_url="https://winro-bot.000webhostapp.com//ressources/mute.png")
            embed.add_field(name="Winro", value=f"{ctx.author.mention} a rétabli la voix à {user.mention}", inline=True)
            embed.set_footer(text="Créé par WhitePixels#9953")
            if os.path.isfile(f"./cogs/logs/{ctx.guild.id}.txt") == True :
                logfile = open(f"./cogs/logs/{ctx.guild.id}.txt", "r")
                logchannel = logfile.read()
                log = self.bot.get_channel(int(logchannel))
                await log.send(embed=embed)
        else : 
            await ctx.send("Vous n'avez pas la permission pour exécuter cette commande ! (Permission(s) requise(s) : gérer les rôles)")

    @unmute.error
    async def unmute_error(self, ctx, error):  
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Pour utiliser cette commande, il faut indiquer l'utilisateur auquel vous souhaitez rétablir la voix : ``w!unmute @user``")
        elif isinstance(error, commands.BadArgument):
            await ctx.send("Pour utiliser cette commande, il faut indiquer l'utilisateur auquel vous souhaitez rétablir la voix : ``w!unmute @user``")
        else:
            raise error

    
def setup(bot):
    bot.add_cog(Customs(bot))