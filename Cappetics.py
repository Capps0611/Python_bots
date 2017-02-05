import discord
import os
from discord.ext import commands

#MjU2MDk4ODEzNDczNzE4Mjcy.CyyM8A.pFa1uLujdn5U3vtEV9tK7dxrhfo = token
#espeak "#{event.user.username} has connected" -w connected.wav     : cmd to get speech file
#use os.system() for terminal commands

if not discord.opus.is_loaded():
    discord.opus.load_opus('opus')

phonetics_enabled = False
cur_mems = []
new_mems = []
first_run = True
voice = None

description = '''A bot that plays phonetics when a user connects/disconnects to a voice channel!'''
bot = commands.Bot(command_prefix='!', description=description)

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)

@bot.event
async def on_voice_state_update(before,after):
	#print(before.voice_channel)
	global phonetics_enabled
	global voice
	if phonetics_enabled == True:
		b4_channel = before.voice_channel
		channel = after.voice_channel
		bot_channel = voice.channel
		if b4_channel != bot_channel and channel == bot_channel:
			nam = "\""+after.name+" has connected\""
			cmd = "espeak %s -w connected.wav" %nam
			os.popen(cmd)
			os.wait()
			player = voice.create_ffmpeg_player("/root/connected.wav")
			player.start()
		elif before.voice_channel == bot_channel and after.voice_channel != bot_channel:
			nam = "\""+after.name+" has disconnected\""
			cmd = "espeak %s -w disconnected.wav" %nam
			os.popen(cmd)
			os.wait()
			player = voice.create_ffmpeg_player("/root/disconnected.wav")
			player.start()

@bot.command(pass_context=True)
async def phonetics_off(ctx):
	global voice
	global phonetics_enabled
	if voice is not None:
		if voice.is_connected():
			await voice.disconnect()
			voice = None
			await bot.say("Phonetics disabled!")
			phonetics_enabled = False

@bot.command(pass_context=True)
async def phonetics_on(ctx):
	channel = ctx.message.author.voice_channel
	global phonetics_enabled
	global voice
	if channel is None:
		mem = ctx.message.author
		await bot.say("Hey "+mem.name+" try getting into a voice channel next time!")
	else:
		if voice is not None:
			if voice.is_connected():
				await voice.move_to(channel)
				await bot.say("Phonetics enabled")
				phonetics_enabled = True
			else:
				voice = await bot.join_voice_channel(channel)
				await bot.say("Phonetics enabled")
				phonetics_enabled = True
		else:
			voice = await bot.join_voice_channel(channel)
			await bot.say("Phonetics enabled")
			phonetics_enabled = True



@bot.command(pass_context=True)
async def test(ctx):
	global voice
	channel = ctx.message.author.voice_channel #gets channel
	voice = await bot.join_voice_channel(channel) #sets up audio player
	player = voice.create_ffmpeg_player("/root/Novel.wav")#creates audio player
	player.start()#plays audio



bot.run('MjU2MDk4ODEzNDczNzE4Mjcy.CyyM8A.pFa1uLujdn5U3vtEV9tK7dxrhfo')
