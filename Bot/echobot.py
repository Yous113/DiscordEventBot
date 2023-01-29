
import discord
import lister
import Classes

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
    title = ""
    setEvent = False
    helpMessage = "Decide the date of your event by using !SetEvent followed by the title of the event"
    
    
    
    if contents == "!help":
      
      await message.channel.send(helpMessage)

    if contents.startswith("!SetEvent"):
      title = contents[9:]
      firstreply = "Giv nogen datoer for eventet: " + title + " ,ved brug af kommando '!date' og afslut med '!done'"
      title = lister.Event(title, [])
      print(title.eventName)
      setEvent = True
      print(setEvent)
      await message.channel.send(firstreply)

    if contents.startswith("!Date") and contents.endswith("!Done") and setEvent == True: 
      con = contents[6:]
      con = con.replace("!Done","")
      dates = con.split(",")
      setEvent = False
      title.eventDates = dates
      print(setEvent)
      for date in dates:
        await message.channel.send(date)

    
      # sæt hver besked ind i en dictionary så vi kan tælle dens votes
      # sæt listen af datoer ind som værdi for event objektet

    

@client.event
async def on_raw_reaction_add(payload):
  message_id = payload.message_id
  
    


           
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



