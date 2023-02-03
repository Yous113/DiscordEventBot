
import discord
import lister

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

TOK_FILE = "Token.txt"



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
          for date in dates:
            await message.channel.send(date)
            lister.mesDict[message.id] = 0
          lister.setEvent = False

    if contents.startswith("!SetDate"):
      max_value = max(lister.mesDict.values())
      max_key = [k for k, v in lister.mesDict.items() if v == max_value]
      await message.channel.edit(max_key)

    
@client.event
async def on_reaction_add(reaction, user):
    message = reaction.message
    message_id = reaction.message.id
    
    for r in message.reactions:
       if message_id in lister.mesDict:
        lister.mesDict[message_id] = r.count    
    


    # create a dictionary to store the count of each emoji
#    emoji_counts = {}
 #   for r in message.reactions:
  #      emoji_counts[str(r.emoji)n] = r.count

    # format the emoji counts into a string
   # count_str = "\n".join([f"{emoji}: {count}" for emoji, count in emoji_counts.items()])
    #await message.edit(content=f"Reaction count:\n{count_str}")
          

    
      # sæt hver besked ind i en dictionary så vi kan tælle dens votes
           
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



