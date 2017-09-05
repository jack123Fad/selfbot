import discord
from discord.ext import commands

class cog:
  def __init__(self, bot):
    self.bot = bot

  @commands.command()
  async def echo(self, *, text):
    """Repeat after me!"""
    await self.bot.say(text)
    
  @commands.command()
  async def die(self):
    await self.bot.say('hello')
    
  @commands.command(pass_context=True)
  async def test(self, ctx, arg1, arg2, *, therest):
    await self.bot.say('1: {}, 2:{}, The rest: {}'.format(arg1, arg2, therest))

  @commands.command(pass_context=True)
  async def echohelp(self):
    em = discord.Embed(title="Echo Help",description="Visit https://echo.xtclabs.net/ to learn about the basic things Echo can do \nVisit https://ars.xtclabs.net/ to learn about the ever-evolving ARS. \nVisit https://github.com/proxikal/Echo to see Echo 1.0 Documentation!", color=0x00FFFF)
    em.set_author(name = "4JR",  icon_url = "https://discordapp.com/api/v6/users/180314310298304512/avatars/eb45214491b879d0db62a8165148a311.jpg")
    await self.bot.say(embed=em)
    
  @commands.command(pass_context=True)
  async def status(self, *, text):
    await bot.say(text)
    if text == 'online':
       await bot.change_presence(status=discord.Status.online, afk=True)
       await bot.say('Set your status to online')
    if text == 'idle':
       await bot.change_presence(status=discord.Status.idle, afk=True)
       await bot.say('Set your status to idle')
    if text == 'dnd':
       await bot.change_presence(status=discord.Status.dnd, afk=True)
       await bot.say('Set your status to DND')
    if text == 'invis':
       await bot.change_presence(status=discord.Status.invisible, afk=True)
       await bot.say('Set your status to invisible')

    

    
  #async def on_message(self, message):
    #if message.author != self.bot.user:
      #return
    #if message.content.startswith('hi'):
      #await self.bot.add_reaction(message, '👌')
    
def setup(bot):
  bot.add_cog(cog(bot))