
import discord
import lister

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
    lister.setEvent = False
    lister.title = ""


@client.event
async def on_message(message):
    contents = message.content
    helpMessage = "Decide the date of your event by using !SetEvent followed by the title of the event"
    
    
    
    if contents == "!help":
      
      await message.channel.send(helpMessage)

    if contents.startswith("!SetEvent"):
      lister.title = contents[9:]
      firstreply = "Giv nogen datoer for eventet: " + lister.title + " ,ved brug af kommando '!date' og afslut med '!done'"
      lister.title = lister.Event(lister.title, [])
      lister.setEvent = True
      await message.channel.send(firstreply)
      

    if contents.startswith("!Date") and contents.endswith("!Done") and lister.setEvent == True: 
          con = contents[6:]
          con = con.replace("!Done","")
          dates = con.split(",")
          lister.title.eventDates = dates
          print(lister.setEvent)
          for date in dates:
            await message.channel.send(date)
            lister.mesDict[message.id] = date
          lister.setEvent = False
          
          

    
      # sæt hver besked ind i en dictionary så vi kan tælle dens votes

    

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



