import discord 
import respuestas
import os
from dotenv import load_dotenv

async def send_message(message, user_message, is_private):
    response = respuestas.get_response(user_message)
    await message.author.send(response) if is_private else await message.channel.send(response)
    
def run_discord_bot():
    load_dotenv()
    TOKEN = os.getenv('DISCORD_TOKEN')
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)
    
    @client.event
    async def on_ready():
        print(f'{client.user} Está vivo!!!!')
        
    @client.event
    async def on_message(message):
        if message.author == client.user:
            return
        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)
        
        print(f'{username} en {channel} dijo: {user_message}')
        
        if user_message[0] == '?':
            user_message = user_message[1:]
            await send_message(message, user_message, is_private = True)
        else:
            await send_message(message, user_message, is_private = False)
            
    
    client.run(TOKEN)