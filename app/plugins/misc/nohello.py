import asyncio
from datetime import datetime, timedelta
from pyrogram import Client, filters

# Define a dictionary to store the last message timestamps
last_message_time = {}

# Define greetings to respond to
greetings = {"hello", "hy"}

async def check_and_respond(client, message):
    user_id = message.from_user.id
    text = message.text.lower().strip()

    # If the message is in the greetings set and has no extra text
    if text in greetings:
        current_time = datetime.utcnow()
        last_time = last_message_time.get(user_id, None)
        
        # If it's the first message or last message was more than 5 minutes ago
        if last_time is None or (current_time - last_time) >= timedelta(minutes=5):
            # Schedule the response
            await asyncio.sleep(5 * 60)  # Wait for 5 minutes
            # Check again if no new message has been received
            if last_message_time.get(user_id, None) == last_time:
                await client.send_message(chat_id=message.chat.id, text="/hy")

    # Update the last message time
    last_message_time[user_id] = datetime.utcnow()

# Create the Pyrogram Client
app = Client("my_bot")

# Define a message handler
@app.on_message(filters.text & ~filters.private)
async def message_handler(client, message):
    await check_and_respond(client, message)

# Run the bot
app.run()
