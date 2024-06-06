from discord.ext import commands
from discord.ui import Button, View
import discord
import random


intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix = "!", intents=intents)

#client = discord.Client(intents=intents)
#This is if we wanted to deal with client events and the like




class RPS_View(discord.ui.View):
    # int [1, 2, 3] for Rock, Paper, or Scissors (0 otherwise)
    optionValue : int = 0

    async def disable_all(self):
        for item in self.children:
            item.disabled= True
        await self.message.edit(view=self)

    async def on_timeout(self) -> None:
        await self.message.channel.send("timed out")
        await self.disable_all()


    @discord.ui.button(label="Rock")
    async def rock(self, interaction:discord.Interaction, button:Button):
        await interaction.response.send_message("You chose Rock")
        self.optionValue = 4
        print(self.optionValue)
        self.stop()
    @discord.ui.button(label="Paper")
    async def paper(self, interaction:discord.Interaction,button:Button):
        await interaction.response.send_message("You chose Paper")
        self.optionValue = 5
        print(self.optionValue)
        self.stop()
    @discord.ui.button(label="Scissors")
    async def scissors(self, interaction:discord.Interaction, button:Button):
        await interaction.response.send_message("You chose Scissors")
        self.optionValue = 6
        print(self.optionValue)
        self.stop()





async def RPS(challenger:discord.User, defender:discord.User):
    prompt = f"You've been challenged to Rock, Paper, Scissors by {challenger}"
    c_prompt = f"You have challenged {defender} to Rock, Paper, Scissors"

    embed = discord.Embed(title=prompt)
    c_embed = discord.Embed(title=c_prompt)
    await defender.send(embed=embed)
    await challenger.send(embed=c_embed)

    view = RPS_View(timeout=30)
    c_view = RPS_View(timeout=30)

    message = await defender.send(view=view)
    c_message = await challenger.send(view=c_view)
    view.message = message
    c_view.message = c_message
     
    await view.wait()
    await c_view.wait()

    await view.disable_all()
    await c_view.disable_all()


    if view.optionValue != 0 and c_view.optionValue != 0:
        if view.optionValue == 4 and c_view.optionValue == 5:
            result = f"Paper beats Rock, `{challenger}` Wins!"
        elif view.optionValue == 4 and c_view.optionValue == 6:
            result = f"Rock beats Scissors, `{defender}` Wins!"
        elif view.optionValue == 5 and c_view.optionValue == 6:
            result = f"Scissors beats Paper, `{challenger}` Wins!"
        elif view.optionValue == 5 and c_view.optionValue == 4:
            result = f"Paper beats Rock, `{defender}` Wins!"
        elif view.optionValue == 6 and c_view.optionValue == 4:
            result = f"Rock beats Scissors, `{challenger}` Wins!"
        elif view.optionValue == 6 and c_view.optionValue == 5:
            result = f"Scissors beats Paper, `{defender}` Wins!"
        else:
            result = "It was a draw!"
    else :
        result = "`Incomplete Game`"

    return result


#####BOT EVENTS#####

@bot.event
async def on_ready():
    print('----------------------')
    print('- we are now running -')
    print('----------------------')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    username = str(message.author)
    user_message = str(message.content)
    channel = str(message.channel)

    print(f'{username} said: "{user_message}" in ({channel})')
    await bot.process_commands(message)


#####BOT COMMANDS#####




@bot.command(pass_context = True)
async def challenge(ctx, user:discord.User, *, message=None):
    result = await RPS(ctx.author, user)
    await ctx.channel.send(result)


@bot.command()
async def roll(ctx, dice: str):
    #Rolls a dice in NdN format.
    try:
        rolls, limit = map(int, dice.split('d'))
    except Exception:
        await ctx.send('Format has to be in NdN!')
        return

    result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
    result = f"` {result} `"
    await ctx.send(result)

@bot.command()
@commands.is_owner()
async def shutdown(ctx):
    await ctx.send("`Shutting down...`")
    await bot.close()
    
from apikeys import TOKEN

bot.run(TOKEN)

