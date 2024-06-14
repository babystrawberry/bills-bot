from discord.ext import commands
import discord
from bills import bill_finder

BOT_TOKEN = "MTI1MDE1NDM0ODg1MjQxNjYxMg.GYaIxq.I9R_cTd8yjqiP7dAVlDr2Lzq4W6417R_p0ZBe4" #not real

intents = discord.Intents.default()
intents.message_content = True
client = commands.Bot(command_prefix='/', intents=intents)

@client.event
async def on_ready():
    print(f'Logged on as {client.user}!')
    await client.tree.sync()
@client.tree.command(name="bill", description="Retrieves bill info")
async def bill(ctx: discord.Interaction, bill_number:str):
    bill = bill_finder(bill_number)
    if bill != []:
        response = discord.Embed(title=bill[0], url=bill[4], description=bill[1], color=0xFF5733)
        response.add_field(name="Sponsors", value=bill[3], inline=False)
        response.add_field(name="Committee", value=bill[2], inline=False)
        await ctx.response.send_message(embed = response)
    else:
        await ctx.response.send_message("No bill found :(")




client.run(BOT_TOKEN)