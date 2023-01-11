
import discord

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

TOK_FILE = "token.txt"


def get_token():
  tokfile = open(TOK_FILE, 'r')
  token = tokfile.read()
  tokfile.close()
  return token

@client.event
async def on_ready():
    print("Connected!")


@client.event
async def on_message(message):
    contents = message.content
    
    if contents == "!help":
      helpMessage = "Decide the date of your event by using !SetEvent followed by the title of the event"
      await message.channel.send(helpMessage)

    if contents.startswith("!SetEvent"):
      title = contents[9:]
      firstreply = "Giv nogen datoer for eventet: " + title + " ,ved brug af kommando '!date' og afslut med '!done'"
      await message.channel.send(firstreply)
    

@client.event
async def on_raw_reaction_add(payload):
  message_id = payload.message_id
  if payload.emoji.name == "":
    vote =+ 1
    
  

           
token = get_token()
client.run(token)

# Bruger: !SetEvent "Title"
# Bot: Giv nogen datoer ved brug af kommando "!date" og afslut med "!done"
# Bruger: !date ..... !done
# Bot: Reager på den dato, som er bedst for jer
# Bot: Dato 1
# Bot: Dato 2
# Bot: Dato 3
# Bot: Når votering er færdig skriv "!BestemDato"
# Bruger: !BestemDato
# Bot: "Title" foregår i dato 1

