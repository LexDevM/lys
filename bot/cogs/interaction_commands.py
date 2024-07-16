import discord
from discord.ext import commands
from discord import ui
import random

class InteractionCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.CommandNotFound):
            emoji = '🤔'
            mensaje = f"{emoji} No puedo encontrar este comando."
            
            # Crear un embed para el mensaje
            embed = discord.Embed(description=mensaje, color=discord.Color.yellow())
            
            # Crear un botón para descartar el mensaje
            view = discord.ui.View()
            button = discord.ui.Button(label="Descartar mensaje", style=discord.ButtonStyle.grey)
            
            async def button_callback(interaction):
                await interaction.message.delete()
            
            button.callback = button_callback
            view.add_item(button)
            
            # Enviar el mensaje con el embed y el botón
            await ctx.send(embed=embed, view=view, ephemeral=True)

    @commands.command()
    async def ayuda(self, ctx, *args):
        if not args:
            embed = discord.Embed(title="Comandos Disponibles", color=discord.Color.blue())
            embed.add_field(name="!poll", value="Crea una encuesta. Uso: !poll <pregunta> <opción1> <opción2> ...", inline=False)
            embed.add_field(name="!ochoball", value="Pregunta a la bola 8 mágica. Uso: !ochoball <tu pregunta>", inline=False)
            await ctx.send(embed=embed)
        else:
            await ctx.send(f"No hay ayuda disponible para '{' '.join(args)}'")

    @commands.command()
    async def poll(self, ctx, *, args):
    # Dividir los argumentos en pregunta y opciones
        parts = args.split("|")
        if len(parts) < 3:
            await ctx.send("Formato incorrecto. Usa: !poll ¿Tu pregunta? | opción1 | opción2 ...")
            return

        question = parts[0].strip()
        options = [opt.strip() for opt in parts[1:]]

        if len(options) > 10:
            await ctx.send("Puedes proporcionar un máximo de 10 opciones.")
            return

        reactions = ['1️⃣', '2️⃣', '3️⃣', '4️⃣', '5️⃣', '6️⃣', '7️⃣', '8️⃣', '9️⃣', '🔟']
        description = []
        for x, option in enumerate(options):
            description.append(f'\n{reactions[x]} {option}')
        embed = discord.Embed(title=question, description=''.join(description))
        react_message = await ctx.send(embed=embed)
        for reaction in reactions[:len(options)]:
            await react_message.add_reaction(reaction)

    @commands.command(name='ochoball')
    async def ochoball(self, ctx, *, question):
        responses = [
            "Es cierto.", "Definitivamente es así.", "Sin duda.",
            "Sí, definitivamente.", "Puedes confiar en ello.", "Como yo lo veo, sí.",
            "Probablemente.", "Las perspectivas son buenas.", "Sí.",
            "Las señales apuntan a que sí.", "Respuesta confusa, intenta de nuevo.",
            "Pregunta de nuevo más tarde.", "Mejor no decirte ahora.",
            "No puedo predecirlo ahora.", "Concéntrate y pregunta de nuevo.",
            "No cuentes con ello.", "Mi respuesta es no.", "Mis fuentes dicen que no.",
            "Las perspectivas no son muy buenas.", "Muy dudoso."
        ]
        await ctx.send(f"Pregunta: {question}\nRespuesta: {random.choice(responses)}")

async def setup(bot):
    await bot.add_cog(InteractionCommands(bot))