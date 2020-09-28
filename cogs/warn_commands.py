import discord
import discord.utils
import os
from discord.ext import commands

class Warn_commands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def warn(self, ctx, user:discord.User, *, reason):
        owner = self.bot.get_user(323111825975672862)
        await owner.send(f"``{ctx.author}`` à fait la commande ``warn`` dans le serveur ``{ctx.guild}``")
        if ctx.channel.permissions_for(ctx.author).kick_members :
            if user == None or reason == None :
                await ctx.send("Veulliez indiquer une utilisateur valide ainsi qu'une raison valide !")
            else :
                if os.path.isdir(f"./cogs/warns/{ctx.guild.id}") == False :
                    os.mkdir(f"./cogs/warns/{ctx.guild.id}")
                    warns = open(f"./cogs/warns/{ctx.guild.id}/{user.id}.txt", "a")
                    warns.write(f"{ctx.author} : {reason}\n")
                    warns.close()
                    await ctx.send(f"{user.mention} a été avertis pour {reason}")
                    await user.send(f"Vous avez été averti sur le serveur : ``{ctx.guild}``, pour {reason}")
                else :
                    warns = open(f"./cogs/warns/{ctx.guild.id}/{user.id}.txt", "a")
                    warns.write(f"{ctx.author} : {reason}\n")
                    warns.close()
                    await ctx.send(f"{user.mention} a été avertis pour {reason}")
                    await user.send(f"Vous avez été averti sur le serveur : ``{ctx.guild}``, pour {reason}")
        else : 
            await ctx.send("Vous n'avez pas la permission pour exécuter cette commande ! (Permission(s) requise(s) : expluser des membres)")

    @warn.error
    async def warn_error(self, ctx, error):  
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Pour utiliser cette commande, il faut indiquer l'utilisateur à avertir ainsi que la raison de l'avertissement : ``w!warn @user spam``")
        elif isinstance(error, commands.BadArgument):
            await ctx.send("Pour utiliser cette commande, il faut indiquer l'utilisateur à avertir ainsi que la raison de l'avertissement : ``w!warn @user spam``")
        else:
            raise error

    @commands.command(pass_context=True)
    async def warns(self, ctx, user:discord.Member):
        owner = self.bot.get_user(323111825975672862)
        await owner.send(f"``{ctx.author}`` à fait la commande ``warns`` dans le serveur ``{ctx.guild}``")
        if ctx.channel.permissions_for(ctx.author).kick_members :
            warns = open(f"./cogs/warns/{ctx.guild.id}/{user.id}.txt", "r")
            reasons = warns.read()
            embed=discord.Embed(
            colour = discord.Colour.orange()
            )
            embed.set_author(name='Winro :', icon_url="https://winro-bot.000webhostapp.com/images/minia.png")
            embed.set_footer(text="Créer par WhitePixels#9953")
            embed.add_field(name=f"Warns de {user} :", value=f"``{reasons}``")
            await ctx.send(embed=embed)
        else : 
            await ctx.send("Vous n'avez pas la permission pour exécuter cette commande ! (Permission(s) requise(s) : expluser des membres)")

    @warns.error
    async def warns_error(self, ctx, error):  
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Pour utiliser cette commande, il faut indiquer l'utilisateur pour lequel vous voulez voir les avertissements : ``w!warns @user``")
        elif isinstance(error, commands.BadArgument):
            await ctx.send("Pour utiliser cette commande, il faut indiquer l'utilisateur pour lequel vous voulez voir les avertissements : ``w!warns @user``")
        elif isinstance(error, commands.CommandInvokeError):
            await ctx.send("Cet utilisateur n'a pas d'avertissements !")
        else:
            raise error

    @commands.command(pass_context=True)
    async def clearwarns (self, ctx, user:discord.Member):
        owner = self.bot.get_user(323111825975672862)
        await owner.send(f"``{ctx.author}`` à fait la commande ``clearwarns`` dans le serveur ``{ctx.guild}``")
        if ctx.channel.permissions_for(ctx.author).administrator :
            warn = f"./cogs/warns/{ctx.guild.id}/{user.id}.txt"
            os.remove(warn)
            await ctx.send(f"Tous les avertissements de {user} ont été clear !")
        else :
            await ctx.send("Vous n'avez pas la permission pour exécuter cette commande ! (Permission(s) requise(s) : administrateur)")

    @clearwarns.error
    async def clearwarns_error(self, ctx, error):  
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Pour utiliser cette commande, il faut indiquer l'utilisateur pour lequel vous voulez clear les avertissements : ``w!clearwarns @user``")
        elif isinstance(error, commands.BadArgument):
            await ctx.send("Pour utiliser cette commande, il faut indiquer l'utilisateur pour lequel vous voulez clear les avertissements : ``w!clearwarns @user``")
        else:
            raise error

def setup(bot):
    bot.add_cog(Warn_commands(bot))
