import discord
import googletrans
from googletrans import Translator
from discord.ext import commands

class Translate_commands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot 

    @commands.command(pass_context=True)
    async def translate(self, ctx, arg2, *, arg1,):
        owner = self.bot.get_user(323111825975672862)
        await owner.send(f"``{ctx.author}`` à fait la commande ``translate`` dans le serveur ``{ctx.guild}``")
        embed = discord.Embed(
            color = discord.Color.orange()
        )
        embed.set_author(name="Traduction :", icon_url="https://winro-bot.000webhostapp.com/images/minia.png")
        translator = Translator()
        result = translator.translate(arg1, dest=arg2)            
        embed.add_field(name="__Langue d'origine :__", value=result.src, inline=False)
       	embed.add_field(name="__Message d'origine :__", value=arg1, inline=False)
        embed.add_field(name="__Langue de la traduction :__", value=result.dest, inline=False)
        embed.add_field(name="__Message traduit :__", value=result.text, inline=False)			          
        embed.set_footer(text="Créé par WhitePixels#9953, source : Google Translate API")
        await ctx.send(embed=embed)
    
    @translate.error
    async def translate_error(self, ctx, error):  
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Pour utiliser cette commande, vous devez indiquer la langue dans laquelle vous voulez traduire votre message : ``w!translate [langue] [message]``. Si vous souhaitez avoir la liste des langues disponibles, faites ``w!translatelist``")
        else :
            raise error

    @commands.command(pass_context=True)
    async def translatelist(self, ctx):
        owner = self.bot.get_user(323111825975672862)
        await owner.send(f"``{ctx.author}`` à fait la commande ``translatelist`` dans le serveur ``{ctx.guild}``")
        embed = discord.Embed(
            color = discord.Color.orange()
        ) 
        embed.set_author(name="Liste des langues disponibles :", icon_url="https://winro-bot.000webhostapp.com/images/minia.png")
        embed.add_field(name="Français :", value="``fr``", inline=False)
        embed.add_field(name="Anglais :", value="``en``", inline=False)
        embed.add_field(name="Allemand :", value="``de``", inline=False)
        embed.add_field(name="Espagnol :", value="``es``", inline=False)
        embed.add_field(name="Russe :", value="``ru``", inline=False)
        await ctx.send(embed=embed)

    @commands.command(pass_context=True)
    async def language(self, ctx, *, arg):
        owner = self.bot.get_user(323111825975672862)
        await owner.send(f"``{ctx.author}`` à fait la commande ``language`` dans le serveur ``{ctx.guild}``")
        translator = Translator()
        result = translator.translate(arg)
        embed = discord.Embed(
            color = discord.Color.orange()
        ) 
        embed.set_author(name="Traduction :", icon_url="https://winro-bot.000webhostapp.com/images/minia.png")
        embed.add_field(name="__Langue d'origine de votre message :__", value=result.src)
        embed.set_footer(text="Créé par WhitePixels#9953, source : Google Translate API")
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Translate_commands(bot))
