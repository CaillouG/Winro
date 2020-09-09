import discord
import os
import asyncio
import shutil
import random
from discord.ext import commands

class Games(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def island(self, ctx, arg1=None):
        if os.path.isfile(f"./Procfile") == True :
            await ctx.send("⚠ En raison de la configuration actuelle de Winro, votre progression sera effacée à chaque redémarrage")
        if arg1 == None :
            if os.path.isdir(f"./cogs/games/wnh/{ctx.author.id}") == False :
                embed = discord.Embed(
                    colour = discord.Colour.orange()
                )
                embed.set_author(name="Winro New Horizons :", icon_url="https://winro-bot.000webhostapp.com/images/minia.png")
                embed.add_field(name="Système d'îles de Winro :", value="Winro intègre un mini-jeu à la Animal Crossing New Horizons 🏝️ !\n Si vous souhaitez devenir délégué insulaire, veuillez suivre le guide du nouveau délégué insulaire 🏳️ !", inline=False)
                embed.add_field(name="Guide du nouveau délégué insulaire :", value=f"Bonjour {ctx.author.mention} ! Es tu prêt pour ta nouvelle vie insulaire ? Bien, si tu l'es, dit moi laquelle de ces 4 îles te plaît le plus :", inline=False)
                embed.add_field(name="Île n° 1 🏝️ :", value="Cette île est basée dans l'hémisphère nord, avec comme fruit de base des pommes 🍎\n Si vous souhaitez habiter sur cette île, tapez ``w!island 1``.", inline=False)
                embed.add_field(name="Île n° 2 🏝️ :", value="Cette île est basée dans l'hémisphère sud, avec comme fruit de base des pêches 🍑\n Si vous souhaitez habiter sur cette île, tapez ``w!island 2``.", inline=False)
                embed.add_field(name="Île n° 3 🏝️ :", value="Cette île est basée dans l'hémisphère nord, avec comme fruit de base des poires 🍐\n Si vous souhaitez habiter sur cette île, tapez ``w!island 3``.", inline=False)
                embed.add_field(name="Île n° 4 🏝️ :", value="Cette île est basée dans l'hémisphère sud, avec comme fruit de base des cerises 🍒\n Si vous souhaitez habiter sur cette île, tapez ``w!island 4``.", inline=False)
                await ctx.send(embed=embed)
            else : 
                island = open(f"./cogs/games/wnh/{ctx.author.id}/island.txt", "r")
                islandtype = island.read()
                money = open(f"./cogs/games/wnh/{ctx.author.id}/money.txt", "r")
                moneyamount = money.read()
                xp = open(f"./cogs/games/wnh/{ctx.author.id}/xp.txt", "r")
                xpamount = xp.read()
                embed=discord.Embed(
                    colour=discord.Colour.orange()
                )
                embed.set_author(name="Votre île :", icon_url="https://winro-bot.000webhostapp.com/images/minia.png")
                if "1" in islandtype:
                    embed.add_field(name="Type d'île :", value="Île basée dans l'hémisphère nord 🏝️", inline=False)
                    embed.add_field(name="Fruit principal :", value="Pommes 🍎", inline =False)
                elif "2" in islandtype:
                    embed.add_field(name="Type d'île :", value="Île basée dans l'hémisphère sud 🏝️", inline=False)
                    embed.add_field(name="Fruit principal :", value="Pêches 🍑", inline =False)
                elif "3" in islandtype:
                    embed.add_field(name="Type d'île :", value="Île basée dans l'hémisphère nord 🏝️", inline=False)
                    embed.add_field(name="Fruit principal :", value="Poires 🍐", inline =False)
                elif "4" in islandtype:
                    embed.add_field(name="Type d'île :", value="Île basée dans l'hémisphère sud 🏝️", inline=False)
                    embed.add_field(name="Fruit principal :", value="Cerises 🍒", inline =False)
                embed.add_field(name="Clochettes :", value=f"{moneyamount}", inline=False)
                embed.add_field(name="Points d'expérience:", value=f"{xpamount}", inline=False)
                embed.add_field(name="Vous cherchez une commande ?", value="Faites ``w!help`` pour avoir accès à la liste des commandes et ``w!help [commande]`` pour avoir des détails sur une commande !", inline=False)
                await ctx.send(embed=embed)
        else :
            if arg1 == "1":
                if os.path.isdir(f"./cogs/games/wnh/{ctx.author.id}") == True:
                    await ctx.send("Vous êtes déjà le délégué d'une île ! Faites ``w!island`` pour avoir des détails sur cette dernière ou ``w!delisland`` pour la supprimer")
                else :
                    embed=discord.Embed(
                        colour=discord.Colour.orange()
                    )
                    embed.set_author(name="Winro New Horizons :", icon_url="https://winro-bot.000webhostapp.com/images/minia.png")
                    embed.add_field(name="Île N° 1 🏝️ :", value="Bien, vous avez choisi l'île n°1 ! Vous allez bientôt atterir ! Bonne chance dans votre nouvelle vie de délégué insulaire 🏝️ !", inline=False)
                    await ctx.send(embed=embed)
                    os.mkdir(f"./cogs/games/wnh/{ctx.author.id}")
                    island = open(f"./cogs/games/wnh/{ctx.author.id}/island.txt", "a")
                    island.write(f"1")
                    island.close()
                    xp = open(f"./cogs/games/wnh/{ctx.author.id}/xp.txt", "a")
                    xp.write(f"0")
                    xp.close()
                    money = open(f"./cogs/games/wnh/{ctx.author.id}/money.txt", "a")
                    money.write(f"1000")
                    money.close()
                    os.mkdir(f"./cogs/games/wnh/{ctx.author.id}/inv")
                    await ctx.send("Vous venez d'atterir, amusez vous bien !")
            elif arg1 == "2":
                if os.path.isdir(f"./cogs/games/wnh/{ctx.author.id}") == True:
                    await ctx.send("Vous êtes déjà le délégué d'une île ! Faites ``w!island`` pour avoir des détails sur cette dernière ou ``w!delisland`` pour la supprimer")
                else :
                    embed=discord.Embed(
                        colour=discord.Colour.orange()
                    )
                    embed.set_author(name="Winro New Horizons :", icon_url="https://winro-bot.000webhostapp.com/images/minia.png")
                    embed.add_field(name="Île N° 2 🏝️ :", value="Bien, vous avez choisi l'île n°2 ! Vous allez bientôt atterir ! Bonne chance dans votre nouvelle vie de délégué insulaire 🏝️ !", inline=False)
                    await ctx.send(embed=embed)
                    os.mkdir(f"./cogs/games/wnh/{ctx.author.id}")
                    island = open(f"./cogs/games/wnh/{ctx.author.id}/island.txt", "a")
                    island.write(f"2")
                    island.close()
                    xp = open(f"./cogs/games/wnh/{ctx.author.id}/xp.txt", "a")
                    xp.write(f"0")
                    xp.close()
                    money = open(f"./cogs/games/wnh/{ctx.author.id}/money.txt", "a")
                    money.write(f"1000")
                    money.close()
                    os.mkdir(f"./cogs/games/wnh/{ctx.author.id}/inv")
                    await ctx.send("Vous venez d'atterir, amusez vous bien !")
            elif arg1 == "3":
                if os.path.isdir(f"./cogs/games/wnh/{ctx.author.id}") == True:
                    await ctx.send("Vous êtes déjà le délégué d'une île ! Faites ``w!island`` pour avoir des détails sur cette dernière ou ``w!delisland`` pour la supprimer")
                else :
                    embed=discord.Embed(
                        colour=discord.Colour.orange()
                    )
                    embed.set_author(name="Winro New Horizons :", icon_url="https://winro-bot.000webhostapp.com/images/minia.png")
                    embed.add_field(name="Île N° 3 🏝️ :", value="Bien, vous avez choisi l'île n°3 ! Vous allez bientôt atterir ! Bonne chance dans votre nouvelle vie de délégué insulaire 🏝️ !", inline=False)
                    await ctx.send(embed=embed)
                    os.mkdir(f"./cogs/games/wnh/{ctx.author.id}")
                    island = open(f"./cogs/games/wnh/{ctx.author.id}/island.txt", "a")
                    island.write(f"3")
                    island.close()
                    xp = open(f"./cogs/games/wnh/{ctx.author.id}/xp.txt", "a")
                    xp.write("0")
                    xp.close()
                    money = open(f"./cogs/games/wnh/{ctx.author.id}/money.txt", "a")
                    money.write("1000")
                    money.close()
                    os.mkdir(f"./cogs/games/wnh/{ctx.author.id}/inv")
                    await ctx.send("Vous venez d'atterir, amusez vous bien !")
            elif arg1 == "4":
                if os.path.isdir(f"./cogs/games/wnh/{ctx.author.id}") == True:
                    await ctx.send("Vous êtes déjà le délégué d'une île ! Faites ``w!island`` pour avoir des détails sur cette dernière ou ``w!delisland`` pour la supprimer")
                else :
                    embed=discord.Embed(
                        colour=discord.Colour.orange()
                    )
                    embed.set_author(name="Winro New Horizons :", icon_url="https://winro-bot.000webhostapp.com/images/minia.png")
                    embed.add_field(name="Île N° 4 🏝️ :", value="Bien, vous avez choisi l'île n°4 ! Vous allez bientôt atterir ! Bonne chance dans votre nouvelle vie de délégué insulaire 🏝️ !", inline=False)
                    await ctx.send(embed=embed)
                    os.mkdir(f"./cogs/games/wnh/{ctx.author.id}")
                    island = open(f"./cogs/games/wnh/{ctx.author.id}/island.txt", "a")
                    island.write(f"4")
                    island.close()
                    xp = open(f"./cogs/games/wnh/{ctx.author.id}/xp.txt", "a")
                    xp.write(f"0")
                    xp.close()
                    money = open(f"./cogs/games/wnh/{ctx.author.id}/money.txt", "a")
                    money.write(f"1000")
                    money.close()
                    os.mkdir(f"./cogs/games/wnh/{ctx.author.id}/inv")
                    await ctx.send("Vous venez d'atterir, amusez vous bien !")
        
    @commands.command(pass_context=True)
    async def delisland(self, ctx):
        if os.path.isdir(f"./cogs/games/wnh/{ctx.author.id}") == False :
            await ctx.send("Vous n'avez pas d'île à supprimer, si vous voulez enménager, faites ``w!island`` pour avoir plus d'informations !")
        else :
            def check(message):
                return message.content == "w!oui"
            await ctx.send("Êtes vous sûr de vouloir supprimer votre île ? (Cette action est irreverssible !) Si vous êtes sûr, répondez ``w!oui`` (Cette commande s'anule au bout de 10 secondes) 🏝️")
            await self.bot.wait_for("message", timeout=10.0, check=check)
            shutil.rmtree(f"./cogs/games/wnh/{ctx.author.id}")
            await ctx.send("Votre île à été supprimer, en espérant vous revoir bientôt 🏝️!")
    
    @delisland.error
    async def delisland_error(self, ctx, error):
        if isinstance(error, commands.CommandInvokeError):
            await ctx.send("La demande de suppression de votre île est annulée 🏝️ !")
        else:
            raise error
    
    @commands.command(pass_context=True)
    @commands.cooldown(1, 3600, commands.BucketType.user)
    async def picking(self, ctx):
        if os.path.isdir(f"./cogs/games/wnh/{ctx.author.id}") == False :
            await ctx.send("Vous n'avez pas d'île, si vous voulez enménager, faites ``w!island`` pour avoir plus d'informations !")
        else :
            embed = discord.Embed(
                colour = discord.Colour.orange()
            )
            embed.set_author(name="Winro New Horizons :", icon_url="https://winro-bot.000webhostapp.com/images/minia.png")
            luck = random.randint(1, 8)
            if round(luck) == 8:
                embed.add_field(name="Cueillette :", value="Aïe, des abeilles vous ont attaquées... Vous perdez 200 clochettes. Revenez dans une heure pour recommencer !")
                moneyfile = (f"./cogs/games/wnh/{ctx.author.id}/money.txt")
                money = open(moneyfile, "r")
                moneyamount = money.read()
                money.close()
                os.remove(moneyfile)
                newmoney = open(f"./cogs/games/wnh/{ctx.author.id}/money.txt", "a")
                newmoneyamount = (int(moneyamount))-200
                newmoney.write(str(newmoneyamount))               
            else :
                fruit = random.randint(1, 8)
                embed.add_field(name="Cueillette :", value=f"Vous avez cueillis {round(fruit)} fruits, ce qui vous rapporte {fruit*100} clochettes ! Revenez dans une heure pour recommencer !")
                moneyfile = (f"./cogs/games/wnh/{ctx.author.id}/money.txt")
                money = open(moneyfile, "r")
                moneyamount = money.read()
                money.close()
                os.remove(moneyfile)
                newmoney = open(f"./cogs/games/wnh/{ctx.author.id}/money.txt", "a")
                newmoneyamount = (int(moneyamount))+(fruit*100)
                newmoney.write(str(newmoneyamount))
            await ctx.send(embed=embed)

    @picking.error
    async def picking_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            msg = 'Cette commande possède un cooldown, veuillez attendre {:.0f} secondes ! (Temps entre chaque commande : 1 heure)'.format(error.retry_after)
            await ctx.send(msg)
        else :
            raise error

    @commands.command(pass_context=True)
    async def inv(self, ctx):
        if os.path.isdir(f"./cogs/games/wnh/{ctx.author.id}") == False :
            await ctx.send("Vous n'avez pas d'île, si vous voulez enménager, faites ``w!island`` pour avoir plus d'informations !")
        else : 
            embed = discord.Embed(
                colour=discord.Colour.orange()
            )
            embed.set_author(name="Winro New Horizons :", icon_url="https://winro-bot.000webhostapp.com/images/minia.png")
            embed.add_field(name="Inventaire :", value="Voici la liste des objets présents dans votre inventaire :", inline=False)
            inv = os.listdir(f"./cogs/games/wnh/{ctx.author.id}/inv")
            if len(inv) == 0:
                embed.add_field(name="Inventaire :", value="Votre inventaire est vide !", inline=False)
                await ctx.send(embed=embed)
            else :
                for x in inv:
                    item = open(f"./cogs/games/wnh/{ctx.author.id}/inv/{x}", "r")
                    itemamount = item.read()
                    embed.add_field(name=f"{x.replace('.txt', '')} :", value=f"Vous avez cet item ``{itemamount}`` fois 🏝️ !", inline=False)
                await ctx.send(embed=embed)
        
    @commands.command(pass_context=True)
    async def shop(self, ctx):
        if os.path.isdir(f"./cogs/games/wnh/{ctx.author.id}") == False :
            await ctx.send("Vous n'avez pas d'île, si vous voulez enménager, faites ``w!island`` pour avoir plus d'informations !")
        else :
            embed=discord.Embed(
                colour = discord.Colour.orange()
            )
            embed.set_author(name="Winro New Horizons :", icon_url="https://winro-bot.000webhostapp.com/images/minia.png")
            embed.add_field(name="Magasin Nook :", value="Voici la liste des objets disponible dans le magasin :", inline=False)
            embed.add_field(name="Pommes 🍎 :", value="Achetez une pommes pour 200 clochettes en faisant ``w!buy Pommes``\n Vendez la pour 10xp en faisant ``w!xpsell Pommes``", inline=False)
            embed.add_field(name="Poissons :", value="Achetez un poisson pour 400 clochettes en faisant ``w!buy Poissons``\n Vendez le pour 20xp en faisait ``w!xpsell Poissons``", inline=False)
            embed.add_field(name="Pneus :", value="Achetez un pneu pour 100 clochettes en faisant ``w!buy Pneus``\n Vendez le pour 1xp en faisant ``w!xpsell Pneus``", inline=False)
            await ctx.send(embed=embed)

    @commands.command(pass_context=True) #Ajouter le nombre d'item que l'on souhaite acheter et check si il y a assez de money
    async def buy(self, ctx, item) :
        if os.path.isdir(f"./cogs/games/wnh/{ctx.author.id}") == False :
            await ctx.send("Vous n'avez pas d'île, si vous voulez enménager, faites ``w!island`` pour avoir plus d'informations !")
        else : 
            sample = ["Pommes", "Poissons", "Pneus", "pommes", "poissons", "pneus", "pomme", "poisson", "pneu"]
            if item not in sample:
                await ctx.send("Cet objet n'existe pas, ou n'est pas en vente !")
            else :
                itemfilepath = f"./cogs/games/wnh/{ctx.author.id}/inv/{item}.txt"
                moneyfile = (f"./cogs/games/wnh/{ctx.author.id}/money.txt")
                money = open(moneyfile, "r")
                moneyamount = money.read()
                money.close()
                if item == "Pommes" or item == "pommes" or item == "pomme": #Prix item
                    price = 200
                if item == "Poissons" or item == "poissons" or item == "poisson":
                    price = 400
                if item == "Pneus" or item == "pneus" or item == "pneu": 
                    price = 100
                if int(moneyamount) < price:
                    await ctx.send("Vous n'avez pas assez de clochettes pour acheter cet objet !")
                else :
                    def check(message):
                        return message.content == "w!oui"
                    await ctx.send(f"Êtes vous sûr de vouloir acheter cet item pour {price} clochettes ? (Cette action est irreverssible !) Si vous êtes sûr, répondez ``w!oui`` (Cette commande s'anule au bout de 10 secondes) 🏝️")
                    await self.bot.wait_for("message", timeout=10.0, check=check)
                    os.remove(moneyfile)
                    newmoney = open(f"./cogs/games/wnh/{ctx.author.id}/money.txt", "a")
                    newmoneyamount = (int(moneyamount))-price #Prix item
                    newmoney.write(str(newmoneyamount))
                    if os.path.isfile(itemfilepath) == False:
                        itemfile = open(itemfilepath, "a")
                        itemfile.write("1")
                        itemfile.close()
                        await ctx.send(f"Vous venez d'acheter un(e) {item} 🏝️ !")
                    else :
                        itemfile = open(itemfilepath, "r")
                        itemfileamount = itemfile.read()
                        itemfile.close()
                        newitemfileamount = (int(itemfileamount))+1
                        os.remove(itemfilepath)
                        newitemfile = open(f"./cogs/games/wnh/{ctx.author.id}/inv/{item}.txt", "w")
                        newitemfile.write(str(newitemfileamount))
                        await ctx.send(f"Vous venez d'acheter un(e) {item} 🏝️ !")

    @buy.error
    async def buy_error(self, ctx, error):
        if isinstance(error, commands.CommandInvokeError):
            await ctx.send("La demande d'achat de votre objet est annulée 🏝️ !")
        else:
            raise error
    
    @commands.command(pass_context=True)#Ajouter le nombre d'item que l'on souhaite vendre
    async def xpsell(self, ctx, item):
        if os.path.isdir(f"./cogs/games/wnh/{ctx.author.id}") == False :
            await ctx.send("Vous n'avez pas d'île, si vous voulez enménager, faites ``w!island`` pour avoir plus d'informations !")
        else : 
            if os.path.isfile(f"./cogs/games/wnh/{ctx.author.id}/inv/{item}.txt") == True:
                itemfile= open(f"./cogs/games/wnh/{ctx.author.id}/inv/{item}.txt", "r")
                itemfilelist = itemfile.read()
                newitemfileamount = (int(itemfilelist))-1
                if newitemfileamount < 0:
                    await ctx.send("Vous ne pouvez pas vendre des objets que vous n'avez pas en quantité suffisante !")
                else :
                    def check(message):
                        return message.content == "w!oui"
                    await ctx.send("Êtes vous sûr de vouloir vendre cet item ? (Cette action est irreverssible !) Si vous êtes sûr, répondez ``w!oui`` (Cette commande s'anule au bout de 10 secondes) 🏝️")
                    await self.bot.wait_for("message", timeout=10.0, check=check)
                    os.remove(f"./cogs/games/wnh/{ctx.author.id}/inv/{item}.txt")
                    if newitemfileamount != 0:
                        newitemfile = open(f"./cogs/games/wnh/{ctx.author.id}/inv/{item}.txt", "w")
                        newitemfile.write(str(newitemfileamount))
                    if item == "Pommes": #Nombre d'xp rapporté par item
                        xp = 10
                    if item == "Poissons": #Nombre d'xp rapporté par item
                        xp = 20
                    if item == "Pneus": #Nombre d'xp rapporté par item
                        xp = 1
                    xpfile = open(f"./cogs/games/wnh/{ctx.author.id}/xp.txt", "r")
                    xpamount = xpfile.read()
                    os.remove(f"./cogs/games/wnh/{ctx.author.id}/xp.txt")
                    newxpfile = open(f"./cogs/games/wnh/{ctx.author.id}/xp.txt", "a")
                    newxpamout=(int(xpamount))+xp
                    newxpfile.write(str(newxpamout))
                    await ctx.send(f"Votre item a été vendu, ce qui vous rapporte {xp} points d'xp !")
            else:
                await ctx.send("Vous ne possèdez pas cet item !")

    @xpsell.error
    async def xpsell_error(self, ctx, error):
        if isinstance(error, commands.CommandInvokeError):
            await ctx.send("La demande de vente de votre objet est annulée 🏝️ !")
        else:
            raise error

    @commands.command(pass_context=True)
    @commands.cooldown(1, 3600, commands.BucketType.user)
    async def fishing(self, ctx):
        if os.path.isdir(f"./cogs/games/wnh/{ctx.author.id}") == False :
            await ctx.send("Vous n'avez pas d'île, si vous voulez enménager, faites ``w!island`` pour avoir plus d'informations !")
        else :
            embed = discord.Embed(
                colour = discord.Colour.orange()
            )
            embed.set_author(name="Winro New Horizons :", icon_url="https://winro-bot.000webhostapp.com/images/minia.png")
            luck = random.randint(1, 8)
            if round(luck) == 8:
                item = "Pneus"
                itemfilepath = f"./cogs/games/wnh/{ctx.author.id}/inv/{item}.txt"
                embed.add_field(name="Pêche :", value="Vous venez de pêcher un pneu, bien joué. Revenez dans une heure pour recommencer !")
                if os.path.isfile(itemfilepath) == False:
                    itemfile = open(itemfilepath, "a")
                    itemfile.write("1")
                    itemfile.close()       
                else :
                    itemfile = open(itemfilepath, "r")
                    itemfileamount = itemfile.read()
                    itemfile.close()
                    newitemfileamount = (int(itemfileamount))+1
                    os.remove(itemfilepath)
                    newitemfile = open(f"./cogs/games/wnh/{ctx.author.id}/inv/{item}.txt", "w")
                    newitemfile.write(str(newitemfileamount))
            else :
                item = "Poissons"
                itemfilepath = f"./cogs/games/wnh/{ctx.author.id}/inv/{item}.txt"
                fish = random.randint(1, 8)
                embed.add_field(name="Pêche :", value=f"Vous avez pêché {round(fish)} poissons ! Revenez dans une heure pour recommencer !")
                if os.path.isfile(itemfilepath) == False:
                    itemfile = open(itemfilepath, "a")
                    itemfile.write(str(fish))
                    itemfile.close()       
                else :
                    itemfile = open(itemfilepath, "r")
                    itemfileamount = itemfile.read()
                    itemfile.close()
                    newitemfileamount = (int(itemfileamount))+fish
                    os.remove(itemfilepath)
                    newitemfile = open(f"./cogs/games/wnh/{ctx.author.id}/inv/{item}.txt", "w")
                    newitemfile.write(str(newitemfileamount))
            await ctx.send(embed=embed)

    @fishing.error
    async def fishing_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            msg = 'Cette commande possède un cooldown, veuillez attendre {:.0f} secondes ! (Temps entre chaque commande : 1 heure)'.format(error.retry_after)
            await ctx.send(msg)
        else :
            raise error
         
def setup(bot):
    bot.add_cog(Games(bot))