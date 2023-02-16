import configparser
import nextcord
from nextcord.ext import commands

config = configparser.ConfigParser()
config.read('config.ini')

intents = nextcord.Intents.default()
intents.members, intents.message_content = True, True

owner = config['CREDENTIAL']['owner']

client = commands.Bot()

@client.event
async def on_ready():
    print('Remote administration bot is now online.')

@client.message_command(name="Delete Message")
async def delete_message(interaction: nextcord.Interaction, message: nextcord.Message):
    if interaction.user.id == owner:
        await message.delete()
        await interaction.response.send_message("Message deleted.", ephemeral=True)
    else:
        await interaction.response.send_message("You don't have permission to use this command.", ephemeral=True)

@client.user_command(name="Kick User")
async def timeout_user(interaction: nextcord.Interaction, user: nextcord.User):
    if interaction.user.id == owner:
        await user.kick()
        await interaction.response.send_message("User kicked.", ephemeral=True)
    else:
        await interaction.response.send_message("You don't have permission to use this command.", ephemeral=True)

@client.user_command(name="Ban User")
async def timeout_user(interaction: nextcord.Interaction, user: nextcord.User):
    if interaction.user.id == owner:
        await user.ban()
        await interaction.response.send_message("User banned.", ephemeral=True)
    else:
        await interaction.response.send_message("You don't have permission to use this command.", ephemeral=True)

client.run(config['CREDENTIAL']['token'])