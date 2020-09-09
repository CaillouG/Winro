import discord 
import os
from discord.ext import commands

class Autorole_commands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member):
        if os.path.isfile(f"./cogs/autorole/{member.guild.id}.txt")==True:
            rolefile = open(f"./cogs/autorole/{member.guild.id}.txt", "r")
            rolename = rolefile.read()
            role = discord.utils.get(member.guild.roles, name=rolename)
            await member.add_roles(role)

    @commands.command(pass_context=True)
    async def autorole(self, ctx, arg1=None):
        if ctx.channel.permissions_for(ctx.author).administrator :
            if arg1 == None :
                embed = discord.Embed(
                    color = discord.Color.orange()
                )
                embed.set_author(name="Auto-rôle :", icon_url="http://winro.rf.gd/images/minia.png")
                if os.path.isfile(f"./cogs/autorole/{ctx.guild.id}.txt") == False:
                    embed.add_field(name="Information :", value="L'auto-rôle n'est pas activé sur votre serveur ❌. \nFaites ``w!autorole [role]`` pour automatiquement atribuer un rôle au nouveaux membres", inline=False)
                else :
                    rolefile = open(f"./cogs/autorole/{ctx.guild.id}.txt", "r")
                    rolename = rolefile.read()
                    embed.add_field(name="Information :", value=f"L'auto est activer pour le rôle ``{rolename}`` sur votre serveur ✅. \nFaites ``w!autorole remove`` si vous voulez le désactiver", inline=False)
                embed.set_footer(text="Créé par WhitePixels#9953, * = facultatif")
                await ctx.send(embed=embed)
            elif arg1 == "remove":
                if os.path.isfile(f"./cogs/autorole/{ctx.guild.id}.txt") == False:
                    await ctx.send("L'auto-rôle n'est pas activé sur votre serveur ! Faites ``w!autorole`` pour plus d'informations")
                else :
                    os.remove(f"./cogs/autorole/{ctx.guild.id}.txt")
                    await ctx.send("L'auto-rôle est maintenant désactivé sur votre serveur !")
            else :
                if discord.utils.get(ctx.guild.roles, name=arg1):
                    rolefile = open(f"./cogs/autorole/{ctx.guild.id}.txt", "a")
                    rolefile.write(arg1)
                    rolefile.close()
                    await ctx.send(f"L'auto-rôle est maintenant activé pour le rôle ``{arg1}`` !")
                else :
                    await ctx.send("Veuillez indiquer un rôle qui existe !")
        else :
            await ctx.send("Vous n'avez pas la permission pour exécuter cette commande ! (Permission(s) requise(s) : administrateur)")

def setup(bot):
    bot.add_cog(Autorole_commands(bot))