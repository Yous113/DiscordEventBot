
import discord
import lister

intents = discord.Intents.default()
# The intents that has to be True for the events to work
intents.message_content = True
intents.members = True
intents.reactions = True

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
    helpMessage = "Decide the date of your event by using '!SetEvent' followed by the title of the event"
    
    if contents == "!help":
      await message.channel.send(helpMessage)


    if contents.startswith("!SetEvent"):
      lister.title = contents[10:]
      firstreply = "Write some date you would like to hold the event: "+ lister.title +", use command '!Date' then write your dates and end with '!Done' (Remember ',' between every date)"
      # Create an object of the class event
      lister.title = lister.Event(lister.title, [])
      lister.setEvent = True
      await message.channel.send(firstreply)
      

    if contents.startswith("!Date") and contents.endswith("!Done") and lister.setEvent == True: 
          # The content after !Date
          con = contents[6:]
          # Removes !Done
          con = con.replace("!Done","")
          # Splits the dates
          dates = con.split(",")
          # Sets the eventDates(list) value of the class to the given dates
          lister.title.eventDates = dates
          await message.channel.send("React on the date that fit you best!")
          #for loop looks in the list of dates
          for date in dates:
            # sends a message of each date
            m = await message.channel.send(date)
            # Puts all of the message ids in a dictionary
            lister.ReactDict[m.id] = 0
          await message.channel.send("When the voting is finished use command '!SetDate' to determine the best date")
          lister.setEvent = False

    if contents.startswith("!SetDate"):
      # Checks if the dictionary is empty
      if len(lister.ReactDict) == 0:
        firstreply = "Write some date you would like to hold the event: "+ lister.title +", use command '!Date' then write your dates and end with '!Done' (Remember ',' between every date)"
        await message.channel.send(firstreply)
      else:
        # Looks for the biggest value in the dictionary
        max_value = max(lister.ReactDict.values())
        # looks at every key(id) in the dictionary and checks which key is = the max value(votes/reactions)
        max_key = [k for k, v in lister.ReactDict.items() if v == max_value]
        print(max_value)
        msg = await message.channel.fetch_message(max_key[0])
        # Clears the dictionary for the next event that is gonna be created
        lister.ReactDict.clear()
        await message.channel.send("The chosen date is " + msg.content + ". We Hope you will have a fun time!")
    
@client.event
async def on_reaction_add(reaction, user):
    message_id = reaction.message.id
    # Checks if the message that has been reacted to is in the dictionary
    if message_id in lister.ReactDict:
      lister.ReactDict[message_id] += 1

    # For debugging
    for (k, v) in lister.ReactDict.items():
      print(k, v)
    
@client.event
async def on_reaction_remove(reaction, user):
    message_id = reaction.message.id
    
    if message_id in lister.ReactDict:
        lister.ReactDict[message_id] -= 1

    # For debugging
    for (k, v) in lister.ReactDict.items():
      print(k, v)

token = get_token()
client.run(token)