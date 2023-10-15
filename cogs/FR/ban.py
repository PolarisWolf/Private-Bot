import discord
from discord.ext import commands
class Ban(discord.Cog):
    def __init__(self, bot):
        super().__init__()
        self.bot = bot
    @commands.command(name="ban",description="Permet de bannir un membre")
    async def ban(self, ctx, member: discord.Member=None, *, reason="Aucune raison fournie"):
        if not ctx.author.guild_permissions.ban_members:
            return await ctx.send("Vous n'avez pas la permission de bannir un membre")
        if not member:
            return await ctx.reply("Synthaxe: `$ban <membre> [<raison>]`")
        try:
            await member.ban(reason=reason)
        except:
            return await ctx.reply("Je n'ai pas la permission de bannir ce membre")
        await ctx.send(f"{member} a bien été banni")
        try:
            await member.send(f"Tu as été banni de {ctx.guild.name} pour {reason} par {ctx.author}")
        except:
            pass

def setup(bot):
    bot.add_cog(Ban(bot))