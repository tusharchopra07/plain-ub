import requests
from userbot import bot, CMD_HELP
from userbot.events import register

# Replace with the user ID or chat ID you want to send quotes to
TARGET_ID = "-1002216786187"

@register(incoming=True, disable_edited=True)
async def auto_quote(event):
    """Automatically send a quote to a specific user or chat."""
    if event.chat_id == int(TARGET_ID):
        response = requests.get("https://zenquotes.io/api/random")
        
        if response.status_code == 200:
            data = response.json()
            quote = data[0]['q']
            author = data[0]['a']
            await event.reply(f"Today's Quote:\n\n*{quote}*\n\nAuthor: {author}\n\nFollow @TheFreebiteQuote")
        else:
            await event.reply("Failed to fetch a quote.")

@register(outgoing=True, pattern="^.quote$")
async def fetch_quote(event):
    """Fetch a random quote and send it back."""
    response = requests.get("https://zenquotes.io/api/random")
    
    if response.status_code == 200:
        data = response.json()
        quote = data[0]['q']
        author = data[0]['a']
        await event.reply(f"**Today's Quote:**\n\n*{quote}*\n\n**Author:** {author}\n\nFollow @TheFreebiteQuote")
    else:
        await event.reply("Failed to fetch a quote.")

# Help command for the plugin
CMD_HELP.update({
    "quote": ".quote\nUsage: Fetches a random quote from Zen Quotes."
})
