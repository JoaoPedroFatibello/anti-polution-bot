import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='/', intents=intents)

@bot.event
async def on_ready():
    print(f'logged in as {bot.user} (ID: {bot.user.id})')

@bot.command()
async def trash(ctx, *, wht: str):
    if wht == "plastico":
        await ctx.send("O lixo plástico deve ser colocado no recipiente amarelo.")
    elif wht == "papel":
        await ctx.send("O lixo papel deve ser colocado no recipiente azul.")
    elif wht == "vidro":
        await ctx.send("O lixo vidro deve ser colocado no recipiente verde.")
    elif wht == "metal":
        await ctx.send("O lixo metal deve ser colocado no recipiente cinza.")
    elif wht == "organico":
        await ctx.send("O lixo orgânico deve ser colocado no recipiente marrom.")
    elif wht == "eletronico":
        await ctx.send("O lixo eletrônico deve ser levado a um ponto de coleta especializado.")
    elif wht == "reciclavel":
        await ctx.send("O lixo reciclável deve ser separado e colocado no recipiente adequado para reciclagem ou levado a um ponto de coleta de reciclagem.")
    else:
        await ctx.send("Tipo de lixo desconhecido. Por favor, informe um tipo válido (plastico, papel, vidro, metal).")


bot.run('seu token')
