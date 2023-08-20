# Discord Event Planner Bot

This is a school project that involves creating a Discord bot to help plan and organize events. The bot uses the Discord API and the `discord.py` library.

## Getting Started

1. Clone the repository or download the code files to your local machine.

2. Ensure you have Python 3 installed on your system.

3. Install the required dependencies by running the following command in your terminal:

   ```bash
   pip install discord.py
4. Create a file named token.txt in the same directory as the code and paste your Discord bot token inside the file.

5. invite the bot to your Discord server by generating an OAuth2 URL with the appropriate permissions and adding it to your server.

## Usage
1. Run the main.py file to start the bot.
2. Invite the bot to your Discord server.
3. Use the following commands to interact with the bot:
   - '!Help': Display a help message with instructions on how to use the bot.
   - '!SetEvent' [event title]: Start setting up a new event. Replace [event title] with the desired title of the event.
   - '!Date' [date1, date2, ...] !Done: Set potential dates for the event. Replace [date1, date2, ...] with a list of comma-separated dates.
   - React to the messages with the potential dates to vote for the best date.
   - '!SetDate': Determine the best date based on the votes and announce it.
## Features:
- Event Creation: Use the '!SetEvent' command to start setting up a new event by providing a title.
- Date Selection: Use the '!Date' command to set potential dates for the event. End the list with '!Done'.
- Voting: Participants can react to the potential date messages to vote for their preferred dates.
- Date Selection: Use the '!SetDate' command to determine the best date based on the votes.

## Example:
1. User types: '!SetEvent' Study Group
2. Bot responds: "Write some dates you would like to hold the event: Study Group, use command '!Date' then write your dates and end with '!Done' (Remember ',' between every date)"
3. User types: '!Date' August 25, August 26, August 27 '!Done'
4. Bot announces: "React on the date that fits you best!"
5. Participants react to the potential dates.
6. User types: '!SetDate'
7. Bot determines the best date based on votes and announces it.
