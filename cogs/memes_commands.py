import discord
import discord.utils 
from discord.ext import commands

class Memes(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def toz(self, ctx):
        await ctx.send("Tu crois que c'est du respect ça mon garçon ?")

    @commands.command(pass_context=True)
    async def arouf(self, ctx):
        await ctx.send("Arouf partout, même dans ton trou.")

    @commands.command(pass_context=True)
    async def pertedetemps(self,ctx):
        await ctx.send("https://cdn.discordapp.com/attachments/691066689852407859/705906600979988594/Quelle_perte_de_temps_quelle_perte_denergie.mp4")

    @commands.command(pass_context=True)
    async def dorime(self,ctx):
        await ctx.send("Dorime https://www.youtube.com/watch?v=cmaVYAaaZvE")

def setup(bot):
    bot.add_cog(Memes(bot))
