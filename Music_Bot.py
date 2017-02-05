import discord
import os
from discord.ext import commands
import re
import urllib.request

description = '''Music bot that plays youtube audio clips in discord!!'''
bot = commands.Bot(command_prefix='!', description=description)
voice = None

#Displays All commands the bot can do!
@bot.command(pass_context=True)
async def Music_Commands(ctx):
	await bot.say('List of Commands:')
	await bot.say('!WW_Radio *youtube link* - Plays the audio from the youtube clip!')
	await bot.say('!Stop - Stops playback and disconnects the bot!')
	await bot.say('!Music_Join - Makes the music bot join your channel!')
	await bot.say('Have a command request? I\'ll see what I can do!')


@bot.command(pass_context=True)
async def WW_Radio(ctx):
	global voice
	channel = ctx.message.author.voice_channel #gets channel
	msg = ctx.message.content
	print(msg)
	song_re = re.compile(r'!WW_Radio ')
	song = re.sub(song_re, '', msg)
	opts = {'default_search' : 'auto', 'quiet': True,}
		
	print(song)
	if channel is None:
		mem = ctx.message.author
		await bot.say("Hey "+mem.name+" try getting into a voice channel next time!")
	else:
		
		if voice is not None:
			is_playing = True
			cur_channel = voice.channel
			if channel != cur_channel:
				voice = await bot.move_to(channel)
				player = await voice.create_ytdl_player(song)
				player.volume = 0.1
				player.start()
			elif channel == cur_channel:
				player = await voice.create_ytdl_player(song)
				player.volume = 0.1
				player.start()
		else:
			voice = await bot.join_voice_channel(channel)
			player = await voice.create_ytdl_player(song)
			player.volume = 0.1
			player.start()

@bot.command(pass_context=True)
async def stop(ctx):
	global voice
	global is_playing
	if voice is not None:
		if voice.is_connected():
			await voice.disconnect()
			voice = None
			is_playing = False

@bot.command(pass_context=True)
async def Music_Join(ctx):
	channel = ctx.message.author.voice_channel
	global voice
	if channel is None:
		mem = ctx.message.author
		await bot.say("Hey "+mem.name+" try getting into a voice channel next time!")
	else:
		if voice is not None:
			if voice.is_connected():
				await voice.move_to(channel)
			else:
				voice = await bot.join_voice_channel(channel)
		else:
			voice = await bot.join_voice_channel(channel)

bot.run('Token Goes here')
