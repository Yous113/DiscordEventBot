
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
          for date in dates:
            m = await message.channel.send(date)
            lister.ReactDict[m.id] = 0
          lister.setEvent = False

    if contents.startswith("!SetDate"):
      if len(lister.ReactDict) == 0:
        firstreply = "Giv nogen datoer for eventet: " + lister.title + ",ved brug af kommando '!date' og afslut med '!done'"
        await message.channel.send(firstreply)
      else:
        max_value = max(lister.ReactDict.values())
        max_key = [k for k, v in lister.ReactDict.items() if v == max_value]
        print(max_value)
        msg = await message.channel.fetch_message(max_key[0])
        await message.channel.send(msg.content)

    
@client.event
async def on_reaction_add(reaction, user):
    message = reaction.message
    message_id = reaction.message.id
    
    if message_id in lister.ReactDict:
      lister.ReactDict[message_id] = 0
      for r in message.reactions:
        lister.ReactDict[message_id] += r.count
    for (k, v) in lister.ReactDict.items():
      print(k, v)

token = get_token()
client.run(token)