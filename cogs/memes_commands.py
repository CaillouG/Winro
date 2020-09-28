import discord
import discord.utils 
from discord.ext import commands

class Memes(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def toz(self, ctx):
        owner = self.bot.get_user(323111825975672862)
        await owner.send(f"``{ctx.author}`` à fait la commande ``toz`` dans le serveur ``{ctx.guild}``")
        await ctx.send("Tu crois que c'est du respect ça mon garçon ?")

    @commands.command(pass_context=True)
    async def arouf(self, ctx):
        owner = self.bot.get_user(323111825975672862)
        await owner.send(f"``{ctx.author}`` à fait la commande ``arouf`` dans le serveur ``{ctx.guild}``")
        await ctx.send("Arouf partout, même dans ton trou.")

    @commands.command(pass_context=True)
    async def pertedetemps(self,ctx):
        owner = self.bot.get_user(323111825975672862)
        await owner.send(f"``{ctx.author}`` à fait la commande ``pertedetemps`` dans le serveur ``{ctx.guild}``")
        await ctx.send("https://cdn.discordapp.com/attachments/691066689852407859/705906600979988594/Quelle_perte_de_temps_quelle_perte_denergie.mp4")

    @commands.command(pass_context=True)
    async def dorime(self,ctx):
        owner = self.bot.get_user(323111825975672862)
        await owner.send(f"``{ctx.author}`` à fait la commande ``dorime`` dans le serveur ``{ctx.guild}``")
        await ctx.send("Dorime https://www.youtube.com/watch?v=cmaVYAaaZvE")

def setup(bot):
    bot.add_cog(Memes(bot))
