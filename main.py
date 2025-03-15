import discord
import google.generativeai as genai
from discord import app_commands
from discord.ext import commands
import os

# Load your Gemini API key
GEMINI_API_KEY = os.environ.get('GEMINI_API_KEY')
genai.configure(api_key=GEMINI_API_KEY)

# Bot setup
TOKEN = os.environ.get('BOT_TOKEN')
GUILD_ID = discord.Object(id=1349752551049793710)

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

# Register Slash Command (Scoped to One Server)
@bot.tree.command(name="ask", description="Ask Gemini AI a question!", guild=GUILD_ID)
@app_commands.describe(question="What do you want to ask Gemini?")
async def ask(interaction: discord.Interaction, question: str):
    await interaction.response.defer()  # Defer response if it takes time

    try:
        # Correct API call using genai
        model = genai.GenerativeModel("gemini-1.5-pro")
        response = model.generate_content(question)

        # Extract the response correctly
        answer = response.text if hasattr(response, "text") else "I couldn't find an answer."
        await interaction.followup.send(f"**Q:** {question}\n**A:** {answer}")

    except Exception as e:
        await interaction.followup.send("⚠️ Error fetching response. Try again later.")
        print(f"Error: {e}")

# Sync commands only for the specified server
@bot.event
async def on_ready():
    await bot.tree.sync(guild=GUILD_ID)
    print(f"✅ Logged in as {bot.user} in {GUILD_ID.id}")

bot.run(TOKEN)
