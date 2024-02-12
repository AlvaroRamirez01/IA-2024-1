import discord 
import respuestas

async def send_message(message, user_message, is_private):
    response = respuestas.get_response(user_message)
    await message.author.send(response) if is_private else await message.channel.send(response)
    
def run_discord_bot():
    TOKEN = 'MTIwNDg1NDU2MjM2ODkxMzQ0OA.G5dlQV.bqf-em5XfA-AmacH4o3FyiDuZKW2w0M2DWhQUY'
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