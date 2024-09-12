from ub_core import bot, filters
import time

# Dictionary to store the last message timestamp for each user
user_last_message_time = {}

@bot.on_message(filters.text)
async def nohello_response(client, message):
    user_id = message.from_user.id  # Get the user's ID
    current_time = time.time()  # Get the current time in seconds

    # Normalize the message text
    text = message.text.strip().lower()
    
    # Check if the message is exactly "hello" or "hy"
    if text in ["hello", "hy"]:
        # Check if the user has sent a message in the last 5 minutes (300 seconds)
        last_message_time = user_last_message_time.get(user_id, 0)
        
        if current_time - last_message_time >= 300:  # 5 minutes
            await message.reply("/hy")
    
    # Update the last message time for the user
    user_last_message_time[user_id] = current_time
