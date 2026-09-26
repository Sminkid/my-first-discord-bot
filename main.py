import discord
import os 
from dotenv import load_dotenv, dotenv_values

load_dotenv() # Load environment variables from .env file

class Client (discord.Client):
    async def on_ready(self): #This function is called when the bot is ready to start working
        print(f'Logged on as {self.user}') # Print the bot's username

    async def on_message(self, message): #This function is called when a message is sent in a server the bot is in
        print(f'Message from {message.author}: {message.content}') # Print the message's author and content
        if message.author == self.user: # Check if the message was sent by the bot itself
            return # If it was, do nothing

        if message.content.startswith('hello') or message.content.startswith('hi'): # Check if the message starts with "!hello" or "!hi"
            await message.channel.send(f'Hello there, {message.author.mention}!') # Send "Hello!" in the same channel

        elif message.content.startswith('goodbye') or message.content.startswith('bye'): # Check if the message starts with "!goodbye" or "!bye"
            await message.channel.send(f'Goodbye, {message.author.mention}!') # Send "Goodbye!" in the same channel

    async def on_member_join(self, member): #This function is called when a new member joins the server
        channel = member.guild.system_channel # Get the system channel of the server
        if channel is not None: # Check if the system channel exists
            await channel.send(f'Welcome to the server, {member.mention}!') # Send a welcome message in the system channel

    async def on_reaction_add(self, reaction, user): #This function is called when a reaction is added to a message
        if user == self.user: # Check if the reaction was added by the bot itself
            return # If it was, do nothing

        if reaction.emoji == '👍': # Check if the reaction is a thumbs up
            await reaction.message.channel.send(f'{user.mention} you like what they said huh? :wink:') # Send a message in the same channel
intents = discord.Intents.default() # Create an instance of the Intents class with default settings
intents.message_content = True # Enable the message content intent

client = Client(intents=intents)
client.run(os.getenv('MY_TOKEN')) # Replace with your bot's token
