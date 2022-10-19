import os
import discord
import random
my_secret = os.environ['token1']
import flask 
import keep_alive
description = '''Wee woo'''
intents = discord.Intents.default()
intents.members = True
bot = discord.Bot(description=description,intents=intents)

@bot.event
async def on_ready():
	activity = discord.Game(name="Very Cool Bot", type=3)
	await bot.change_presence(status=discord.Status.idle, activity=activity)
	print('Logged in as')
	print(bot.user.name)
	print(bot.user.id)
	print('------')


@bot.slash_command(description="Adds two numbers cause clearly you are too dumb to do so")
async def add(ctx, left: int, right: int):
	"""Adds two numbers together."""
	await ctx.respond(left + right)

@bot.slash_command(description="Standard ping command")
async def ping(ctx):
    await ctx.respond(f"Pong! {round(bot.latency * 1000)}ms")

    

@bot.slash_command(description="Repeats a message many times")
async def repeat(ctx, times: int, content:str):
    """Repeats a message multiple times."""
    if times >= 70:
      return await ctx.respond("That is too much for me to handle! Try below 70.")
    elif times <= 0:
      return await ctx.respond("Give me number of times in positive")
    
      
    for i in range(times):
      await ctx.respond(content)

@bot.slash_command(description="Repeats a message once")
async def say(ctx,*,content):
    await ctx.respond(content)

@bot.slash_command(description="Asks a question to the almighty Magic 8 Ball(Eg: /ask am i a potato)")
async def ask(ctx, *, question):
  message = question.lower()
  list = ["will", "how", "why","is" ,
  "when", "where", "who", "whom","I","@","can","am","should","are","were","if","did","does","do","has","was"]
  bool = False
  for x in list:
    if x in message.split():
      bool = True
  if bool == False:
    return await ctx.respond("Invalid question format.")
    
  await ctx.respond(
	  random.choice([
	        "It is certain :8ball:", "It is decidedly so :8ball:",
	        "Without a doubt :8ball:", "Yes, definitely :8ball:",
	        "You may rely on it :8ball:", "As I see it, yes :8ball:",
	        "Most likely :8ball:", "Outlook good :8ball:", "Yes :8ball:",
	        "Signs point to yes :8ball:", "Reply hazy try again :8ball:",
	        "Ask again later :8ball:", "Better not tell you now :8ball:",
	        "Cannot predict now :8ball:", "Concentrate and ask again :8ball:",
	        "Don't count on it :8ball:", "My reply is no :8ball:",
	        "My sources say no :8ball:", "Outlook not so good :8ball:",
	        "Very doubtful :8ball:"
	    ]))



embed = discord.Embed(
    title="Magic 8 Ball",
    description=
    "This bot solves your questions and more. For more questions do ?help. Also be sure to invite the bot!"
)
embed.colour = 0x00FFFF
embed.set_image(
    url=
    "https://cdn.discordapp.com/attachments/437067256049172491/742326962160271380/image0.png"
)
embed.add_field(name="Bot Dev", value="Frost!#2042", inline=False)
embed2 = discord.Embed(
    title="Magic 8 Ball Help Page",
    description="Here is the list of commands for this server")
embed2.colour = 0x00FFFF
embed2.add_field(name="Help", value="Displays this command", inline=False)
embed2.add_field(
    name="About", value="Shows information about the bot ", inline=False)
embed2.add_field(name="Repeat", value="Repeats a phrase many times *Number of times comes first*", inline=False)
embed2.add_field(name="Ask", value="Asks Magic 8 Ball a question", inline=False)
embed2.add_field(name="Add", value="Adds numbers for you(When you are too dumb to do it yourself)", inline=False)
embed2.add_field(name="Choose", value="Chooses between two choices", inline=False)





@bot.slash_command(description="Just your average help command")
async def help(ctx):
	await ctx.respond(embed=embed2)


@bot.slash_command(description="Get to know the bot a bit")
async def about(ctx):
	await ctx.respond(embed=embed)
  
@bot.slash_command(description="Allows you to chose between multiple choices. Eg- /choose pizza pasta burger")
async def choose(ctx,*,choices):
  e=choices.split(" ")
  await ctx.respond(random.choice(e))
  
keep_alive.run()
bot.run(my_secret)
