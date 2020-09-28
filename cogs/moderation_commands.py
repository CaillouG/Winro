import discord
import asyncio
import discord.utils 
import os
from discord.ext import commands

class Moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def clear(self, ctx, limit:int):
        owner = self.bot.get_user(323111825975672862)
        await owner.send(f"``{ctx.author}`` à fait la commande ``clear`` dans le serveur ``{ctx.guild}``")
        if ctx.channel.permissions_for(ctx.author).manage_messages :
            await ctx.channel.purge(limit=limit+1)
            embed=discord.Embed(
                colour = discord.Colour.orange()
            )
            embed.set_author(name="Clear :", icon_url="https://winro-bot.000webhostapp.com/ressources/clear.png")
            embed.add_field(name="Winro", value=f"{ctx.author.mention} a supprimé {limit} messages dans #{ctx.channel}", inline=True)
            embed.set_footer(text="Créé par WhitePixels#9953")
            if os.path.isfile(f"./cogs/logs/{ctx.guild.id}.txt") == True :
                logfile = open(f"./cogs/logs/{ctx.guild.id}.txt", "r")
                logchannel = logfile.read()
                log = self.bot.get_channel(int(logchannel))
                await log.send(embed=embed)
        else: 
            await ctx.send("Vous n'avez pas la permission pour exécuter cette commande ! (Permission(s) requise(s) : gérer les messages)")

    @clear.error
    async def clear_error(self, ctx, error):  
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Pour utiliser cette commande, il vous suffit d'indiquer le nombre de messages que vous voulez supprimer : ``w!clear 15``")
        elif isinstance(error, commands.BadArgument):
            await ctx.send("Pour utiliser cette commande, il vous suffit d'indiquer le nombre de messages que vous voulez supprimer : ``w!clear 15``")
        else:
            raise error

    @commands.command(pass_context=True)
    async def tempmute(self, ctx, user : discord.Member, time:int, *, reason=None):
        owner = self.bot.get_user(323111825975672862)
        await owner.send(f"``{ctx.author}`` à fait la commande ``tempmute`` dans le serveur ``{ctx.guild}``")
        role = discord.utils.get(ctx.guild.roles, name="Muted")
        if ctx.channel.permissions_for(ctx.author).manage_roles :
            if role == None :
                await ctx.send("Le mute n'est pas mis en place sur ce serveur ! Faites ``w!setup mute`` pour le faire !")
            else :
                await user.add_roles(role)
                await ctx.channel.purge(limit=1)
                if reason == None :
                    await ctx.send(f"{user.mention} a été réduit au silence pour {time} minute(s)")
                    embed=discord.Embed(
                        colour = discord.Colour.orange()
                    )
                    embed.set_author(name="Mute :", icon_url="https://winro-bot.000webhostapp.com/ressources/mute.png")
                    embed.add_field(name="Winro", value=f"{ctx.author.mention} a réduit au silence {user.mention} dans #{ctx.channel} pour {time} minute(s)", inline=True)
                    embed.set_footer(text="Créé par WhitePixels#9953")
                    if os.path.isfile(f"./cogs/logs/{ctx.guild.id}.txt") == True :
                        logfile = open(f"./cogs/logs/{ctx.guild.id}.txt", "r")
                        logchannel = logfile.read()
                        log = self.bot.get_channel(int(logchannel))
                        await log.send(embed=embed)
                else:
                    await ctx.send(f"{user.mention} a été réduit au silence {time} minute(s) pour {reason}")
                    embed=discord.Embed(
                        colour = discord.Colour.orange()
                    )
                    embed.set_author(name="Mute :", icon_url="https://winro-bot.000webhostapp.com/ressources/mute.png")
                    embed.add_field(name="Winro", value=f"{ctx.author.mention} a réduit au silence {user.mention} dans #{ctx.channel} pour {time} minute(s), pour {reason}", inline=True)
                    embed.set_footer(text="Créé par WhitePixels#9953")
                    if os.path.isfile(f"./cogs/logs/{ctx.guild.id}.txt") == True :
                        logfile = open(f"./cogs/logs/{ctx.guild.id}.txt", "r")
                        logchannel = logfile.read()
                        log = self.bot.get_channel(int(logchannel))
                        await log.send(embed=embed)
                await asyncio.sleep(time*60)
                await user.remove_roles(role)
                await ctx.send(f"{user.mention} n'est plus réduit au silence !")
        else : 
            await ctx.send("Vous n'avez pas la permission pour exécuter cette commande ! (Permission(s) requise(s) : gérer les rôles)")

    @tempmute.error
    async def tempmute_error(self, ctx, error):  
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Pour utiliser cette commande, il faut indiquer l'utilisateur à réduire au silence ainsi que la durée en minutes  : ``w!tempmute @user 20``")
        elif isinstance(error, commands.BadArgument):
            await ctx.send("Pour utiliser cette commande, il faut indiquer l'utilisateur à réduire au silence ainsi que la durée en minutes  : ``w!tempmute @user 20``")
        else:
            raise error

    @commands.command(pass_context=True)
    async def mute(self, ctx, user : discord.Member, *, reason=None):
        owner = self.bot.get_user(323111825975672862)
        await owner.send(f"``{ctx.author}`` à fait la commande ``mute`` dans le serveur ``{ctx.guild}``")
        role = discord.utils.get(ctx.guild.roles, name="Muted")
        if ctx.channel.permissions_for(ctx.author).manage_roles :
            if role == None :
                await ctx.send("Le mute n'est pas mis en place sur ce serveur ! Faites ``w!setup mute`` pour le faire !")
            else :
                await user.add_roles(role)
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
    async def unmute(self, ctx, user : discord.Member):
        owner = self.bot.get_user(323111825975672862)
        await owner.send(f"``{ctx.author}`` à fait la commande ``unmute`` dans le serveur ``{ctx.guild}``")
        role = discord.utils.get(ctx.guild.roles, name="Muted")
        if ctx.channel.permissions_for(ctx.author).manage_roles :
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

    @commands.command(pass_context=True)
    async def kick(self, ctx, user : discord.Member, *, reason):
        owner = self.bot.get_user(323111825975672862)
        await owner.send(f"``{ctx.author}`` à fait la commande ``kick`` dans le serveur ``{ctx.guild}``")
        if ctx.channel.permissions_for(ctx.author).kick_members :
            await user.send(f'Vous avez été expulsé de {ctx.guild} pour la raison suivante : {reason}')
            await user.kick(reason=reason)
            await ctx.channel.purge(limit=1)
            embed=discord.Embed(
                colour = discord.Colour.orange()
            )
            embed.set_author(name="Kick :", icon_url="https://winro-bot.000webhostapp.com/ressources/ban.png")
            embed.add_field(name="Winro", value=f"{ctx.author.mention} a expulsé {user.mention} pour {reason}", inline=True)
            embed.set_footer(text="Créé par WhitePixels#9953")
            if os.path.isfile(f"./cogs/logs/{ctx.guild.id}.txt") == True :
                logfile = open(f"./cogs/logs/{ctx.guild.id}.txt", "r")
                logchannel = logfile.read()
                log = self.bot.get_channel(int(logchannel))
                await log.send(embed=embed)
        else : 
            await ctx.send("Vous n'avez pas la permission pour exécuter cette commande ! (Permission(s) requise(s) : expluser des membres)")

    @kick.error
    async def kick_error(self, ctx, error):  
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Pour utiliser cette commande, il faut indiquer l'utilisateur à expulser ainsi que la raison de l'expulsion : ``w!kick @user spam``")
        elif isinstance(error, commands.BadArgument):
            await ctx.send("Pour utiliser cette commande, il faut indiquer l'utilisateur à expulser ainsi que la raison de l'expulsion : ``w!kick @user spam``")
        else:
            raise error

    @commands.command(pass_context=True)
    async def ban(self, ctx, user : discord.Member, *, reason):
        owner = self.bot.get_user(323111825975672862)
        await owner.send(f"``{ctx.author}`` à fait la commande ``ban`` dans le serveur ``{ctx.guild}``")
        if ctx.channel.permissions_for(ctx.author).ban_members :
            await user.send(f'Vous avez été banni de {ctx.guild} pour la raison suivante : {reason}')
            await user.ban(reason=reason)
            await ctx.channel.purge(limit=1)
            embed=discord.Embed(
                colour = discord.Colour.orange()
            )
            embed.set_author(name="Ban :", icon_url="https://winro-bot.000webhostapp.com/ressources/ban.png")
            embed.add_field(name="Winro", value=f"{ctx.author.mention} a banni {user.mention} pour {reason}", inline=True)
            embed.set_footer(text="Créé par WhitePixels#9953")
            if os.path.isfile(f"./cogs/logs/{ctx.guild.id}.txt") == True :
                logfile = open(f"./cogs/logs/{ctx.guild.id}.txt", "r")
                logchannel = logfile.read()
                log = self.bot.get_channel(int(logchannel))
                await log.send(embed=embed)
        else : 
            await ctx.send("Vous n'avez pas la permission pour exécuter cette commande ! (Permission(s) requise(s) : bannir des membres)")

    @ban.error
    async def ban_error(self, ctx, error):  
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Pour utiliser cette commande, il faut indiquer l'utilisateur à bannir ainsi que la raison du bannissement : ``w!ban @user spam``")
        elif isinstance(error, commands.BadArgument):
            await ctx.send("Pour utiliser cette commande, il faut indiquer l'utilisateur à bannir ainsi que la raison du bannissement : ``w!ban @user spam``")
        else:
            raise error

    @commands.command(pass_context=True)
    async def tempban(self, ctx, user : discord.Member, days:int):
        owner = self.bot.get_user(323111825975672862)
        await owner.send(f"``{ctx.author}`` à fait la commande ``tempban`` dans le serveur ``{ctx.guild}``")
        if ctx.channel.permissions_for(ctx.author).ban_members :
            await user.send(f'Vous avez été banni de {ctx.guild} pour {days} jour(s) !')
            await user.ban(reason=f"{days} jour(s)")
            await ctx.channel.purge(limit=1)
            embed=discord.Embed(
                colour = discord.Colour.orange()
            )
            embed.set_author(name="Ban :", icon_url="https://winro-bot.000webhostapp.com/ressources/ban.png")
            embed.add_field(name="Winro", value=f"{ctx.author.mention} a banni {user.mention} pour {days} jour(s)", inline=True)
            embed.set_footer(text="Créé par WhitePixels#9953")
            if os.path.isfile(f"./cogs/logs/{ctx.guild.id}.txt") == True :
                logfile = open(f"./cogs/logs/{ctx.guild.id}.txt", "r")
                logchannel = logfile.read()
                log = self.bot.get_channel(int(logchannel))
                await log.send(embed=embed)
            await asyncio.sleep(days*84600)
            await ctx.guild.unban(user)
            await log.send(f"{user.mention} n'est plus banni !")
        else : 
            await ctx.send("Vous n'avez pas la permission pour exécuter cette commande ! (Permission(s) requise(s) : bannir des membres)")

    @tempban.error
    async def tempban_error(self, ctx, error):  
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Pour utiliser cette commande, il faut indiquer l'utilisateur à bannir ainsi que la durée du bannissement en jours : ``w!tempban @user 1``")
        elif isinstance(error, commands.BadArgument):
            await ctx.send("Pour utiliser cette commande, il faut indiquer l'utilisateur à bannir ainsi que la durée du bannissement en jours : ``w!tempban @user 1``")
        else:
            raise error

def setup(bot):
    bot.add_cog(Moderation(bot))
