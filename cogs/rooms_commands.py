import discord
import discord.utils
import asyncio
import re
import os
from discord.ext.commands import has_permissions
from discord.ext import commands

class Rooms(commands.Cog):
    def __init__(self, bot):
        self.bot = bot 

    @commands.command(pass_context=True) #Cette commande permet aux membres d'un serveur de créer des salons privés
    @commands.cooldown(1, 7200, commands.BucketType.member)
    async def create(self, ctx, salon, time:float):
        owner = self.bot.get_user(323111825975672862)
        await owner.send(f"``{ctx.author}`` à fait la commande ``create`` dans le serveur ``{ctx.guild}``")
        name = salon.lower()
        room = discord.utils.get(ctx.guild.channels, name=name)
        category = discord.utils.get(ctx.guild.categories, name="Custom rooms")
        if time > 120 :
            await ctx.send("Vous ne pouvez que créer un salon privé pendant au maximum 120 minutes !")
            ctx.command.reset_cooldown(ctx)
        elif room != None:
            await ctx.send(f"Ce nom est déjà pris ! (Essayez avec {name}abc par exemple)")
            ctx.command.reset_cooldown(ctx)
        elif category is None:
            await ctx.send(f"Les salons privés ne sont pas activés sur ce serveur ! Faites ``w!setup rooms`` pour les activés !")
            ctx.command.reset_cooldown(ctx) 
        elif not re.match("^[a-z]*$", name):
            await ctx.send("Le nom de votre salon privé ne peut contenir que des lettres de a à z !")
            ctx.command.reset_cooldown(ctx) 
        elif len(name) > 20:
            await ctx.send("Les noms des salons privés sont limités à 20 carctères !")
            ctx.command.reset_cooldown(ctx)
        else :
            user = ctx.author
            await ctx.guild.create_text_channel(name=name, category=category)
            membres = discord.utils.get(ctx.guild.roles, name="@everyone")  
            roomrole = await ctx.guild.create_role(name=name)
            await user.add_roles(roomrole)
            roomroverwrite = discord.PermissionOverwrite(read_messages=True, send_messages=True)
            membresoverwrite = discord.PermissionOverwrite(read_messages=False, send_messages=False)
            room = discord.utils.get(ctx.guild.channels, name=name)
            await room.set_permissions(roomrole, overwrite=roomroverwrite)
            await room.set_permissions(membres, overwrite=membresoverwrite)
            await room.send(f"{user.mention}, Votre salon privé viens d'être créer ! Faites ``w!add {roomrole} @[utilisateur]`` pour ajouter quelqu'un dans ce dernier !")
            embed=discord.Embed(    
                colour = discord.Colour.orange()
            )
            embed.set_author(name="Create :", icon_url="https://winro-bot.000webhostapp.com/images/minia.png")
            embed.add_field(name="Winro", value=f"{ctx.author.mention} a créer le salon #{room} pour {round(time)} minutes", inline=True)
            embed.set_footer(text="Créer par WhitePixels#9953")
            if os.path.isfile(f"./cogs/logs/{ctx.guild.id}.txt") == True :
                logfile = open(f"./cogs/logs/{ctx.guild.id}.txt", "r")
                logchannel = logfile.read()
                log = self.bot.get_channel(int(logchannel))
                await log.send(embed=embed)
            await asyncio.sleep((round(time)*60))
            await room.delete(reason="Temps expiré")
            await roomrole.delete(reason="Temps expiré")
            await user.send(f"``{user}``, votre salon privé ``{name}`` dans le serveur ``{ctx.guild}`` vient d'expirer !")

    @create.error
    async def create_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            msg = 'Cette commande possède un cooldown, veuillez attendre {:.0f} secondes ! (Temps entre chaque commande : 2 heures)'.format(error.retry_after)
            await ctx.send(msg)
        elif isinstance(error, commands.MissingRequiredArgument): 
            await ctx.send("Pour utiliser cette commande, il faut spécifier un nom de salon, ainsi que la durée qu'il va mettre à expiré en minutes : ``w!create winro 120``")
            ctx.command.reset_cooldown(ctx)
        elif isinstance(error, commands.BadArgument): 
            await ctx.send("Pour utiliser cette commande, il faut spécifier un nom de salon, ainsi que la durée qu'il va mettre à expiré en minutes : ``w!create winro 120``")
            ctx.command.reset_cooldown(ctx)
        elif isinstance(error, commands.UnexpectedQuoteError): 
            await ctx.send("Indiquez un nom de salon privé sans caractères spéciaux !")
        elif isinstance(error, commands.CommandInvokeError):
            await ctx.send("Une erreur est survenue lors de la création de votre salon privé, veuillez réessayer (contactez un administrateur pour supprimer votre channel, sinon vous serez dans l'incapacité de récréer le même salon w!rdel winro)")
            ctx.command.reset_cooldown(ctx)
        else:
            raise error

    @commands.command(pass_context=True) #Cette commande permet au membres d'un salon privé d'ajouter d'autres personnes
    @commands.cooldown(1, 60, commands.BucketType.member)
    async def add(self, ctx, name, user:discord.Member):
        owner = self.bot.get_user(323111825975672862)
        await owner.send(f"``{ctx.author}`` à fait la commande ``add`` dans le serveur ``{ctx.guild}``")
        roomrole = discord.utils.get(ctx.guild.roles, name=name)
        room = discord.utils.get(ctx.guild.channels, name=name)
        if room != None:
            if roomrole in ctx.author.roles:
                await user.add_roles(roomrole)
                await room.send(f"{user} viens d'être ajouter dans ce salon privé !")
            else:
                await ctx.send("Vous ne faites pas parti de ce salon privé !")
        else :
            await ctx.send ("Veuillez saisir un nom de salon privé correct !")

    @add.error
    async def add_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            msg = "Cette commande possède un cooldown, veuillez attendre {:.0f} secondes ! (Temps entre chaque commande : 60 secondes)".format(error.retry_after)
            await ctx.send(msg)        
        elif isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Pour utiliser cette commande, il faut spécifier un nom de salon, ainsi que l'utilisateur que vous souhaiter ajouter dans votre salon privé : ``w!add winro @WhitePixels``")
            ctx.command.reset_cooldown(ctx)
        elif isinstance(error, commands.BadArgument):
            await ctx.send("Pour utiliser cette commande, il faut spécifier un nom de salon, ainsi que l'utilisateur que vous souhaiter ajouter dans votre salon privé : ``w!add winro @WhitePixels``")
            ctx.command.reset_cooldown(ctx)
        else:
            raise error

    @commands.command(pass_context=True) #Cette commande permet à un membre d'un salon privé de quitter ce dernier
    async def quit(self, ctx, caps):
        owner = self.bot.get_user(323111825975672862)
        await owner.send(f"``{ctx.author}`` à fait la commande ``quit`` dans le serveur ``{ctx.guild}``")
        name = caps.lower()
        roomrole = discord.utils.get(ctx.guild.roles, name=name)
        room = discord.utils.get(ctx.guild.channels, name=name)
        if room != None:
            if roomrole in ctx.author.roles:
                await ctx.author.remove_roles(roomrole)
                await room.send(f"{ctx.author} viens de quitter ce salon...")
            else:
                await ctx.send("Vous ne faites pas parti de ce salon privé !")
        else :
            await ctx.send ("Veuillez saisir un nom de salon privé correct !")  

    @quit.error
    async def quit_error(self, ctx, error):  
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Pour utiliser cette commande, il faut spécifier le nom de salon privé que vous voulez quitter : ``w!quit winro``")
        elif isinstance(error, commands.BadArgument):
            await ctx.send("Pour utiliser cette commande, il faut spécifier le nom de salon privé que vous voulez quitter : ``w!quit winro``")
        else:
            raise error

    @commands.command(pass_context=True) #Cette commande permet à un membre avec la permission manage_channel de forcer la suppression d'un salon privé (suite à une erreur par exemple)
    async def rdel(self, ctx, salon):
        owner = self.bot.get_user(323111825975672862)
        await owner.send(f"``{ctx.author}`` à fait la commande ``rdel`` dans le serveur ``{ctx.guild}``")
        if ctx.channel.permissions_for(ctx.author).manage_channels :
            name = salon.lower()
            roomrole = discord.utils.get(ctx.guild.roles, name=name)
            room = discord.utils.get(ctx.guild.channels, name=name)
            if room != None and roomrole != None:
                await room.delete(reason=f"Débug par {ctx.author}")
                await roomrole.delete(reason=f"Débug par {ctx.author}")
                await ctx.send(f"Salon {name} supprimé")
            elif room != None :
                await room.delete(reason=f"Débug par {ctx.author}")
                await ctx.send(f"Le rôle {name} n'a pas été trouver, le salon {name} est supprimé !")
            elif roomrole != None :
                await roomrole.delete(reason=f"Débug par {ctx.author}")
                await ctx.send(f"Le salon {name} n'a pas été trouver, le rôle {name} est supprimé !")
            else :
                await ctx.send("Veuillez saisir un salon privé qui existe !")
        else : 
            await ctx.send("Vous n'avez pas la permission pour exécuter cette commande ! (Permission(s) requise(s) : gérer les salons)")

    @rdel.error
    async def rdel_error(self, ctx, error):  
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Pour utiliser cette commande, il faut spécifier le nom de salon privé que vous voulez supprimer : ``w!rdel winro``")
        elif isinstance(error, commands.BadArgument):
            await ctx.send("Pour utiliser cette commande, il faut spécifier le nom de salon privé que vous voulez supprimer : ``w!rdel winro``")
        else:
            raise error

def setup(bot):
    bot.add_cog(Rooms(bot))

