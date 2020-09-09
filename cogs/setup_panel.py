import discord
from discord.ext import commands

class Setup_panel(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def setup(self, ctx, arg1=None):
        if ctx.channel.permissions_for(ctx.author).administrator :
            if arg1 == None :
                logs = discord.utils.get(ctx.guild.channels, name="📢-logs")
                muterole = discord.utils.get(ctx.guild.roles, name="Muted")
                roomscategory = discord.utils.get(ctx.guild.categories, name="Custom rooms")
                embed = discord.Embed(
                    color = discord.Color.orange()
                )
                embed.set_author(name="Panel des fonctions de Winro :", icon_url="https://winro-bot.000webhostapp.com/images/minia.png")
                embed.add_field(name="Liste des fonctions :", value="Voici la listes des fonctions de Winro activées sur votre serveur :", inline=False)
                if logs != None :
                    embed.add_field(name="Sytème de logs [logs] :", value="Le système de logs de Winro est activé sur votre serveur ! ✅", inline=False)
                else :
                    embed.add_field(name="Sytème de logs [logs] :", value="Le système de logs de Winro n'est pas activé sur votre serveur ! ❎", inline=False)
                if muterole != None :
                    embed.add_field(name="Sytème de mute [mute] :", value="Le système de mute de Winro est activé sur votre serveur ! ✅", inline=False)
                else :
                    embed.add_field(name="Sytème de mute [mute] :", value="Le système de mute de Winro n'est pas activé sur votre serveur ! ❎", inline=False)
                if roomscategory != None :
                    embed.add_field(name="Sytème de salons privés [rooms] :", value="Le système de salons privés de Winro est activé sur votre serveur ! ✅", inline=False)
                else :
                    embed.add_field(name="Sytème de salons privés [rooms] :", value="Le système de salons privés de Winro n'est pas activé sur votre serveur ! ❎", inline=False)
                embed.add_field(name="Activer ou désactiver une fonction :", value="Vous souhaitez activer ou désactiver une de ces fonctions ? Faites !setup [fonction] pour l'activer ou la désactiver !", inline=False)
                embed.set_footer(text="Créé par WhitePixels#9953, * = facultatif")
                await ctx.send(embed=embed)
            else :
                if arg1 == "logs":
                    logs = discord.utils.get(ctx.guild.channels, name="📢-logs")
                    if logs != None: 
                        await logs.delete(reason="Fonction désactivée")
                        await ctx.send("Le système de logs de Winro est maintenant désactivé !")
                    else :
                        await ctx.guild.create_text_channel(name="📢-logs")
                        await ctx.send("Le système de logs de Winro est maintenant activé !")
                elif arg1 == "mute":
                    muterole = discord.utils.get(ctx.guild.roles, name="Muted")
                    if muterole != None: 
                        await muterole.delete(reason="Fonction désactivée")
                        await ctx.send("Le système de mute de Winro est maintenant désactivé !")
                    else :
                        await ctx.guild.create_role(name="Muted")
                        await ctx.send("Veuillez patienter...")
                        muterole = discord.utils.get(ctx.guild.roles, name="Muted")
                        for channel in ctx.guild.channels:
                            await channel.set_permissions(muterole, send_messages=False, read_messages=True)
                        await ctx.send("Le système de mute de Winro est maintenant activé !")
                elif arg1 == "rooms":
                    roomscategory = discord.utils.get(ctx.guild.categories, name="Custom rooms")
                    if roomscategory != None: 
                        await roomscategory.delete(reason="Fonction désactivée")
                        await ctx.send("Le système de salons privés de Winro est maintenant désactivé !")
                    else :
                        await ctx.guild.create_category("Custom rooms")
                        roomscategory = discord.utils.get(ctx.guild.categories, name="Custom rooms")
                        membres = discord.utils.get(ctx.guild.roles, name="@everyone")
                        membresoverwrite = discord.PermissionOverwrite(read_messages=False, send_messages=False)
                        await roomscategory.set_permissions(membres, overwrite=membresoverwrite)
                        await ctx.send("Le système de salons privés de Winro est maintenant activé !")
                else : 
                    await ctx.send("Cette fonction n'existe pas !")
        else : 
            await ctx.send("Vous n'avez pas la permission pour exécuter cette commande ! (Permission(s) requise(s) : administrateur)")

def setup(bot):
    bot.add_cog(Setup_panel(bot))


