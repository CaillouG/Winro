import discord
import os
import keep_alive
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix = 'w!', description='Dorime')
bot.remove_command('help')

@bot.event
async def on_ready():
    print(f'{bot.user} viens de se connecter à Discord !' )
    owner = bot.get_user(323111825975672862)
    await owner.send(f"Je viens de reboot, je suis actuellement connecté à ``{len(bot.guilds)}`` serveurs et j'ai une latence de ``{round(bot.latency * 1000)} ms``")
    game = discord.Game(f"prefix = w! | {len(set(bot.get_all_members()))} membres 🎉 !")
    await bot.change_presence(status=discord.Status.online, activity=game)

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')

commandslist = ["say", "ping", "help", "winro", "setup", "mute", "unmute", "tempmute", "clear", "kick", "ban", "tempban", "rdel", "create", "add", "quit", "toz", "arouf", "pertedetemps", "dorime", "island", "shop", "inv", "buy", "xpsell", "picking", "fishing", "delisland", "warn", "warns", "clearwarns", "autorole", "translate", "translatelist", "language"]

@bot.command(pass_context=True)
async def help(ctx, arg1=None):
    owner = bot.get_user(323111825975672862)
    await owner.send(f"``{ctx.author}`` à fait la commande ``help`` dans le serveur ``{ctx.guild}``")
    embed = discord.Embed(
        color = discord.Color.orange()
    )
    embed.set_author(name="Page d'aide de Winro:", icon_url="https://winro-bot.000webhostapp.com/images/minia.png")
    if arg1 in commandslist:
        if arg1 == "ping":
            embed.add_field(name="w!ping", value="Cette commande vous permet de savoir la latence moyenne de Winro sur les 10 dernières secondes", inline=False)
        elif arg1 == "say":
            embed.add_field(name="w!say [message]", value="Cette commande permet à Winro d'envoyer le contenu de votre message", inline=False)
        elif arg1 == "help":
            embed.add_field(name="w!help [commande]*", value="Cette commande vous permet d'obtenir la liste des commandes disponibles. Elle vous permet également de savoir de quelle façon doit être utilisée une commande", inline=False)
        elif arg1 == "winro":
            embed.add_field(name="w!winro", value="Cette commande vous donne une petite description de Winro", inline=False)
        elif arg1 == "setup":
            embed.add_field(name="w!setup [fonction]", value="Cette commande vous donne la liste des fonctions activées ou non sur votre serveur", inline=False)
        elif arg1 == "mute":
            embed.add_field(name="w!mute [@user] [raison]*", value="Cette commande vous permet de réduire au silence un utilisateur", inline=False)
        elif arg1 == "unmute":
            embed.add_field(name="w!unmute [@user]", value="Cette commande vous permet de rétablir la voix d'un utilisateur", inline=False)
        elif arg1 == "tempmute":
            embed.add_field(name="w!tempmute [@user] [durée] [raison]*", value="Cette commande vous permet de réduire au silence un membre pendant un lapse de temps défini", inline=False)
        elif arg1 == "clear":
            embed.add_field(name="w!clear [nombre]", value="Cette commande vous permet de supprimer le nombre de messages indiqué", inline=False)
        elif arg1 == "kick":
            embed.add_field(name="w!kick [@user] [raison]", value="Cette commande vous permet d'expulser un membre", inline=False)
        elif arg1 == "ban":
            embed.add_field(name="w!ban [@user] [raison]", value="Cette commande vous permet de bannir un membre", inline=False)
        elif arg1 == "tempban":
            embed.add_field(name="w!tempban [@user] [durée]", value="Cette commande vous permet de bannir un membre pour un certain nombre de jours", inline=False)
        elif arg1 == "rdel":
            embed.add_field(name="w!rdel [salon]", value="Cette commande vous permet de forcer la suppression d'un salon privé ", inline=False)
        elif arg1 == "create":
            embed.add_field(name="w!create [salon] [durée]", value="Cette commande vous permet de créer un salon textuel privé", inline=False)
        elif arg1 == "add":
            embed.add_field(name="w!add [salon] [@user]", value="Cette commande vous permet d'ajouter des membres à votre salon privé", inline=False)
        elif arg1 == "quit":
            embed.add_field(name="w!quit [salon]", value="Cette commande vous permet de quitter un salon privé", inline=False)
        elif arg1 == "toz":
            embed.add_field(name="w!toz", value="Essayes toi même", inline=False)
        elif arg1 == "arouf":
            embed.add_field(name="w!arouf", value="J'ai vraiment besoin de t'expliquer ?", inline=False)
        elif arg1 == "pertedetemps":
            embed.add_field(name="w!pertedetemps", value="Phillipe Etchebest MVP", inline=False)
        elif arg1 == "dorime":
            embed.add_field(name="w!dorime", value="Voilà d'où je puise toute mon inspiration", inline=False)
        elif arg1 == "island":
            embed.add_field(name="w!island [nombre]*", value="Cette commande vous permet de commencer votre aventure sur Winro new horizon", inline=False)
        elif arg1 == "shop":
            embed.add_field(name="w!shop", value="Cette commande vous permet de voir les objets présents dans la boutique Nook", inline=False)
        elif arg1 == "inv":
            embed.add_field(name="w!inv", value="Cette commande vous permet de voir le contenu de votre inventaire", inline=False)
        elif arg1 == "buy":
            embed.add_field(name="w!buy [item]", value="Cette commande vous permet d'acheter des objets qui sont présents dans la boutique", inline=False)
        elif arg1 == "xpsell":
            embed.add_field(name="w!xpsell [item]", value="Cette commande vous permet de vendre un objet de votre inventaire pour de l'xp", inline=False)
        elif arg1 == "picking":
            embed.add_field(name="w!picking", value="Cette commande vous de cueillir des fruits toute les heures", inline=False)
        elif arg1 == "fishing":
            embed.add_field(name="w!fishing", value="Cette commande vous de pêcher toute les heures", inline=False)
        elif arg1 == "delisland":
            embed.add_field(name="w!delisland", value="Cette commande vous permet de supprimer votre île (cette action est irréversible !)", inline=False)
        elif arg1 == "warn":
            embed.add_field(name="w!warn [user] [raison]", value="Cette commande vous permet d'avertir un utilisateur", inline=False)
        elif arg1 == "warns":
            embed.add_field(name="w!warns [user]", value="Cette commande vous permet de voir la liste des avertissements d'un utilisateur", inline=False)
        elif arg1 == "clearwarns":
            embed.add_field(name="w!clearwarns [user]", value="Cette commande vous permet de supprimer tous les avertissements d'un utilisateur", inline=False)
        elif arg1 == "autorole":
            embed.add_field(name="w!autorole [role]", value="Cette commande vous permet d'activer ou désactiver la fonctione d'auto-rôle de Winro", inline=False)
        elif arg1 == "translate":
            embed.add_field(name="w!translate [langue] [message]", value="Cette commande vous permet de traduire le contenu de votre message", inline=False)
        elif arg1 == "translatelist":
            embed.add_field(name="w!translatelist", value="Cette commande vous donne la liste des langues disponibles pour la commande ``w!translate``", inline=False)
        elif arg1 == "language":
            embed.add_field(name="w!language [message]", value="Cette commande vous permet de connaitre la langue de votre message", inline=False)
        else :
            embed.add_field(name="Erreur !", value="La page d'aide de cette commande est en cours de rédaction !", inline=False)
    else :
        embed.add_field(name="Liste des commandes", value="Voici la liste des commandes de Winro :", inline=False)
        embed.add_field(name="Commandes de modération :", value="``setup``, ``autorole``, ``mute``, ``unmute``, ``tempmute``, ``kick``, ``ban``, ``tempban``, ``clear``, ``warn``, ``warns``, ``clearwarns``", inline=False)
        embed.add_field(name="Commandes salons privés :", value="``rdel``, ``create``, ``add``, ``quit``", inline=False)
        embed.add_field(name="Commandes memes :", value="``toz``, ``arouf``, ``pertedetemps``, ``dorime``", inline=False)
        embed.add_field(name="Commandes Winro New Horizons [Bêta] :", value="``island``, ``shop``, ``inv``, ``buy``, ``xpsell``, ``picking``, ``fishing``, ``delisland``", inline=False)
        embed.add_field(name="Commandes diverses :", value="``say``, ``translate``, ``translatelist``, ``language``, ``ping``, ``help``, ``winro``", inline=False)
    embed.add_field(name="Une commande vous pose problème ?", value="Faites w!help [commande] pour avoir des détails sur la commande !", inline=False)
    embed.set_footer(text="Créé par WhitePixels#9953, * = facultatif")
    await ctx.send(embed=embed)        

keep_alive.keep_alive()
bot.run(TOKEN)

