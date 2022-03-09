import discord
import random
import os
from os.path import join, dirname
from dotenv import load_dotenv
import asyncio

client = discord.Client()

@client.event
async def on_ready():
    print(f"loguei com o {client.user} mano beleza?")

    activities = [
      "calando boquinhas desde 21/02/2022",
      "fica xiu mano, to te vendo",
      "eu não quero conversar com você cara, some",
      "cope + ratio + didn't ask",
      "puta que pariu que cara chato",
      "https://bit.ly/36jQxzk"
    ]

    while True:
      await client.change_presence(status=discord.Status.idle, activity=discord.Game(random.choice(activities)))
      await asyncio.sleep(12)

@client.event
async def on_message(message):
  
  global liberado

  try: liberado
  except NameError: liberado = True

  if message.author == client.user:
    return

  if message.channel.id == "465617696763936769":
    
    if message.author.id == 258041633789050881:
      if message.content.lower().startswith("para com isso"):
        if liberado == False:
          await message.channel.send("beleza chefia tá liberado")
          liberado = True
        return
    else:
      print("nem era o luke falando, então foda-se")

    if message.author.id == 258041633789050881:  
      if message.content.lower().startswith("coloca eles no chinelo"):
        if liberado == True:
          await message.channel.send("é pra já kkkkkkkkkk")
          liberado = False
          return
    else:
      print("nem era o luke falando, então foda-se")

    if message.content.lower().startswith("qual teu ping"):
      await message.channel.send(f"Tô pingando uns **{round(client.latency * 1000)}ms** agora")
      return

    if liberado == False:

      frases = [
      "na minha epoca as pessoas não falavam, fica xiu",
      "vai dar meia hora de bunda com o relógio parado",
      "eu não quero conversar com você cara, some",
      "você só fala mano meu deus",
      "<https://bit.ly/36jQxzk>",
      "minha vontade é encher a sua boca na porrada",
      "CALA A BOCA PORRAAAAAAAAAAAAAAAAAAAAAAAAAA",
      "mano, acho que tu ja percebeu que eu quero que tu cale a porra da boca",
      "aooooo vai toma no cu google CALA A BOCA",
      "VOCÊ NÃO PODE SE AJUDAR A CALAR A BOCA?",
      "vai ser contratado pro vasco se continuar falando mlk, para logo",
      "uiuiui, um sistema unificado pras universidades, CALA A PORRA DA BOCA NINGUEM LIGA",
      "que corte de cabelo dahora mano, KKKKKKKKKKKKKKKKK AGORA TE CALA",
      "deu até ânsia de tanto que tu fala mlk, fica xiu",
      "mano tu parece o voyager 3, PARA, DE, FALAR",
      "tu tem problema mlk só pode",
      "kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk seu inútil, CALA A PORRA DA BOCA",
      "pindamonhangabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
      "🤫🤫🤫🤫🤫🤫🤫🤫",
      "parou?",
      "vai dormir caralho, tu tem que calar a porra da boca",
      "paraaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
      "meu deeeeeeeeeeeeeeeus vai arrumar algo pra fazer seu vagabundo inútil",
      "porra de rolê cosmico caralho, kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk"
      ]

      await message.delete()
      await message.channel.send(f"{message.author.mention}, {random.choice(frases)}")
      return
  else:
    print("detectei uma mensagem no canal errado, entao foda-se")


dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

token = str(os.environ.get("TOKEN"))

client.run(token)
