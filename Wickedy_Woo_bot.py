import discord
import os
from discord.ext import commands
import re
import urllib.request





description = '''Bot for the guild Wickedy Woo on Winterhoof!'''
bot = commands.Bot(command_prefix='!', description=description)
voice = None
#Pastes the last 8 Raid Logs to chat!
@bot.command(pass_context=True)
async def WW_logs(ctx):
	site = urllib.request.urlopen('https://www.warcraftlogs.com/guilds/reportslist/57022')
	source = site.read()

	final_source = source.decode("utf8")
	site.close()
	logs_re = re.compile(r'<td><a href="(.+)">(\w.+)<\/a>')
	logs = logs_re.findall(final_source)

	i = 0
	for aLog in logs:
		log_link = aLog[0]
		log_name = aLog[1]
		complete_log = log_name+': https://www.warcraftlogs.com'+log_link
		if i == 8:
			break
		i = i+1
		await bot.say(complete_log)

#Displays Raid Days/Times
@bot.command(pass_context=True)
async def WW_Raid_Days(ctx):
	await bot.say('Wickedy Woo\'s Raid Days are:')
	await bot.say('Tuesday & Wednesday @ 7:30pm EST - 10:30pm EST')


#Displays Wickedy Woo Staff
@bot.command(pass_context=True)
async def WW_Staff(ctx):
	await bot.say('Guild Master: Capps')
	await bot.say('Grand Woofficers: Ctdemonet, Rageapples, Yikesa')
	await bot.say('Woofficers: Krazzed, Trollgwild, Disaa, Precedent, Beebop, Alecto, Crysus, Yartch, Schottky, Tribalpopoki')
	await bot.say('Raid Leader: Capps')


#Displays Wickedy Woo Twitch Streams!
@bot.command(pass_context=True)
async def WW_Streamers(ctx):
	await bot.say('Capps- https://www.twitch.tv/Capps_tv')
	await bot.say('Disaa - https://www.twitch.tv/hevisdead')
	await bot.say('Capps & Disaa - http://multitwitch.tv/capps_tv/hevisdead')


#Displays All commands the bot can do!
@bot.command(pass_context=True)
async def WW_Commands(ctx):
	await bot.say('List of Commands:')
	await bot.say('!WW_Logs - List link to past 8 raid logs in chat!')
	await bot.say('!WW_Staff - Lists the GM & Officers of Wickedy Woo!')
	await bot.say('!WW_Raid_Days - Lists Wickedy Woo\'s Raid Days/Times!')
	await bot.say('!WW_Streamers - Lists Wickedy Woo\'s Twitch streams!')
	await bot.say('!WW_Bot_Info - Displays bot welcome text!')
#	await bot.say('!WW_Radio *youtube link* - Plays the audio from the youtube clip!')
	await bot.say('Have a command request? I\'ll see what I can do!')

#@bot.command(pass_context=True)
#async def WW_Radio(ctx):
#	global voice
#	channel = ctx.message.author.voice_channel #gets channel
#	msg = ctx.message.content
#	print(msg)
#	song_re = re.compile(r'!WW_Radio ')
#	song = re.sub(song_re, '', msg)
#	print(song)
#	if channel is None:
#		mem = ctx.message.author
#		await bot.say("Hey "+mem.name+" try getting into a voice channel next time!")
#	else:
#		if voice is not None:
#			cur_channel = voice.channel
#			if channel != cur_channel:
#				voice = await bot.move_to(channel)
#				player = await voice.create_ytdl_player(song)
#				player.volume = 0.1
#				player.start()
#			elif channel == cur_channel:
#				player = await voice.create_ytdl_player(song)
#				player.volume = 0.1
#				player.start()
#		else:
#			voice = await bot.join_voice_channel(channel)
#			player = await voice.create_ytdl_player(song)
#			player.volume = 0.1
#			player.start()



@bot.command(pass_context=True)
async def soundboard(ctx):
	await bot.say('Here are the current soundboard commands:')
	await bot.say('!join - joins the bot to your voice channel')
	await bot.say('!disconnect - disconnects the bot from voice channels')
	await bot.say('Current Clips: !tg - !no - !exist - !so_mean - !angry_kitty - !thats_fine - !kitty_laugh - !wipe - !get_there_first')
	await bot.say('!wes_what - !deep_breath - !shut_up_pre - !one_tank - !omg_tg - !burn_him')
	await bot.say('More clips to follow, it takes awhile to transfer everything, I am only one person')


@bot.command(pass_context=True)
async def tg(ctx):
	global voice
	channel = ctx.message.author.voice_channel #gets channel
	if channel is None:
		mem = ctx.message.author
		await bot.say("Hey "+mem.name+" try getting into a voice channel next time!")
	else:
		if voice is not None:
			cur_channel = voice.channel
			if channel != cur_channel:
				voice = await bot.move_to(channel) #sets up audio player
				player = voice.create_ffmpeg_player("/root/Good_job_dude.wav")#creates audio player
				player.start()#plays audio
			elif channel == cur_channel:
				player = voice.create_ffmpeg_player("/root/Good_job_dude.wav")#creates audio player
				player.start()#plays audio
		else:
			voice = await bot.join_voice_channel(channel) #sets up audio player
			player = voice.create_ffmpeg_player("/root/Good_job_dude.wav")#creates audio player
			player.start()#plays audio

@bot.command(pass_context=True)
async def disconnect(ctx):
	global voice
	if voice is not None:
		if voice.is_connected():
			await voice.disconnect()
			voice = None

@bot.command(pass_context=True)
async def join(ctx):
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

#Soundboard stuffzzz below here!

@bot.command(pass_context=True)
async def no(ctx):
	global voice
	channel = ctx.message.author.voice_channel
	if channel is None:
		mem = ctx.message.author
		await bot.say("Hey "+mem.name+" try getting into a voice channel next time!")
	else:
		if voice is not None:
			cur_channel = voice.channel
			if channel != cur_channel:
				voice = await bot.move_to(channel)
				player = voice.create_ffmpeg_player("/root/Soundboard/Answer_is_no.wav")
				player.start()
			elif channel == cur_channel:
				player = voice.create_ffmpeg_player("/root/Soundboard/Answer_is_no.wav")
				player.start()
		else:
			voice = await bot.join_voice_channel(channel)
			player = voice.create_ffmpeg_player("/root/Soundboard/Answer_is_no.wav")
			player.start()

@bot.command(pass_context=True)
async def exist(ctx):
	global voice
	channel = ctx.message.author.voice_channel
	if channel is None:
		mem = ctx.message.author
		await bot.say("Hey "+mem.name+" try getting into a voice channel next time!")
	else:
		if voice is not None:
			cur_channel = voice.channel
			if channel != cur_channel:
				voice = await bot.move_to(channel)
				player = voice.create_ffmpeg_player("/root/Soundboard/Ceased_to_exist.wav")
				player.start()
			elif channel == cur_channel:
				player = voice.create_ffmpeg_player("/root/Soundboard/Ceased_to_exist.wav")
				player.start()
		else:
			voice = await bot.join_voice_channel(channel)
			player = voice.create_ffmpeg_player("/root/Soundboard/Ceased_to_exist.wav")
			player.start()

@bot.command(pass_context=True)
async def so_mean(ctx):
	global voice
	channel = ctx.message.author.voice_channel
	if channel is None:
		mem = ctx.message.author
		await bot.say("Hey "+mem.name+" try getting into a voice channel next time!")
	else:
		if voice is not None:
			cur_channel = voice.channel
			if channel != cur_channel:
				voice = await bot.move_to(channel)
				player = voice.create_ffmpeg_player("/root/Soundboard/Its_So_Mean.wav")
				player.start()
			elif channel == cur_channel:
				player = voice.create_ffmpeg_player("/root/Soundboard/Its_So_Mean.wav")
				player.start()
		else:
			voice = await bot.join_voice_channel(channel)
			player = voice.create_ffmpeg_player("/root/Soundboard/Its_So_Mean.wav")
			player.start()

@bot.command(pass_context=True)
async def angry_kitty(ctx):
	global voice
	channel = ctx.message.author.voice_channel
	if channel is None:
		mem = ctx.message.author
		await bot.say("Hey "+mem.name+" try getting into a voice channel next time!")
	else:
		if voice is not None:
			cur_channel = voice.channel
			if channel != cur_channel:
				voice = await bot.move_to(channel)
				player = voice.create_ffmpeg_player("/root/Soundboard/Fuck_arrrg.wav")
				player.start()
			elif channel == cur_channel:
				player = voice.create_ffmpeg_player("/root/Soundboard/Fuck_arrrg.wav")
				player.start()
		else:
			voice = await bot.join_voice_channel(channel)
			player = voice.create_ffmpeg_player("/root/Soundboard/Fuck_arrrg.wav")
			player.start()

@bot.command(pass_context=True)
async def thats_fine(ctx):
	global voice
	channel = ctx.message.author.voice_channel
	if channel is None:
		mem = ctx.message.author
		await bot.say("Hey "+mem.name+" try getting into a voice channel next time!")
	else:
		if voice is not None:
			cur_channel = voice.channel
			if channel != cur_channel:
				voice = await bot.move_to(channel)
				player = voice.create_ffmpeg_player("/root/Soundboard/yeah_thats_fine.wav")
				player.start()
			elif channel == cur_channel:
				player = voice.create_ffmpeg_player("/root/Soundboard/yeah_thats_fine.wav")
				player.start()
		else:
			voice = await bot.join_voice_channel(channel)
			player = voice.create_ffmpeg_player("/root/Soundboard/yeah_thats_fine.wav")
			player.start()

@bot.command(pass_context=True)
async def kitty_laugh(ctx):
	global voice
	channel = ctx.message.author.voice_channel
	if channel is None:
		mem = ctx.message.author
		await bot.say("Hey "+mem.name+" try getting into a voice channel next time!")
	else:
		if voice is not None:
			cur_channel = voice.channel
			if channel != cur_channel:
				voice = await bot.move_to(channel)
				player = voice.create_ffmpeg_player("/root/Soundboard/Ct_Laugh.wav")
				player.start()
			elif channel == cur_channel:
				player = voice.create_ffmpeg_player("/root/Soundboard/Ct_Laugh.wav")
				player.start()
		else:
			voice = await bot.join_voice_channel(channel)
			player = voice.create_ffmpeg_player("/root/Soundboard/Ct_Laugh.wav")
			player.start()

@bot.command(pass_context=True)
async def wipe(ctx):
	global voice
	channel = ctx.message.author.voice_channel
	if channel is None:
		mem = ctx.message.author
		await bot.say("Hey "+mem.name+" try getting into a voice channel next time!")
	else:
		if voice is not None:
			cur_channel = voice.channel
			if channel != cur_channel:
				voice = await bot.move_to(channel)
				player = voice.create_ffmpeg_player("/root/Soundboard/Zero_%_wipe_fuck.wav")
				player.start()
			elif channel == cur_channel:
				player = voice.create_ffmpeg_player("/root/Soundboard/Zero_%_wipe_fuck.wav")
				player.start()
		else:
			voice = await bot.join_voice_channel(channel)
			player = voice.create_ffmpeg_player("/root/Soundboard/Zero_%_wipe_fuck.wav")
			player.start()

@bot.command(pass_context=True)
async def get_there_first(ctx):
	global voice
	channel = ctx.message.author.voice_channel
	if channel is None:
		mem = ctx.message.author
		await bot.say("Hey "+mem.name+" try getting into a voice channel next time!")
	else:
		if voice is not None:
			cur_channel = voice.channel
			if channel != cur_channel:
				voice = await bot.move_to(channel)
				player = voice.create_ffmpeg_player("/root/Soundboard/gets_there_first.wav")
				player.start()
			elif channel == cur_channel:
				player = voice.create_ffmpeg_player("/root/Soundboard/gets_there_first.wav")
				player.start()
		else:
			voice = await bot.join_voice_channel(channel)
			player = voice.create_ffmpeg_player("/root/Soundboard/gets_there_first.wav")
			player.start()

@bot.command(pass_context=True)
async def wes_what(ctx):
	global voice
	channel = ctx.message.author.voice_channel
	if channel is None:
		mem = ctx.message.author
		await bot.say("Hey "+mem.name+" try getting into a voice channel next time!")
	else:
		if voice is not None:
			cur_channel = voice.channel
			if channel != cur_channel:
				voice = await bot.move_to(channel)
				player = voice.create_ffmpeg_player("/root/Soundboard/Wes_What_are_you_doing.wav")
				player.start()
			elif channel == cur_channel:
				player = voice.create_ffmpeg_player("/root/Soundboard/Wes_What_are_you_doing.wav")
				player.start()
		else:
			voice = await bot.join_voice_channel(channel)
			player = voice.create_ffmpeg_player("/root/Soundboard/Wes_What_are_you_doing.wav")
			player.start()

@bot.command(pass_context=True)
async def deep_breath(ctx):
	global voice
	channel = ctx.message.author.voice_channel
	if channel is None:
		mem = ctx.message.author
		await bot.say("Hey "+mem.name+" try getting into a voice channel next time!")
	else:
		if voice is not None:
			cur_channel = voice.channel
			if channel != cur_channel:
				voice = await bot.move_to(channel)
				player = voice.create_ffmpeg_player("/root/Soundboard/take_a_deep_breath.wav")
				player.start()
			elif channel == cur_channel:
				player = voice.create_ffmpeg_player("/root/Soundboard/take_a_deep_breath.wav")
				player.start()
		else:
			voice = await bot.join_voice_channel(channel)
			player = voice.create_ffmpeg_player("/root/Soundboard/take_a_deep_breath.wav")
			player.start()

@bot.command(pass_context=True)
async def shut_up_pre(ctx):
	global voice
	channel = ctx.message.author.voice_channel
	if channel is None:
		mem = ctx.message.author
		await bot.say("Hey "+mem.name+" try getting into a voice channel next time!")
	else:
		if voice is not None:
			cur_channel = voice.channel
			if channel != cur_channel:
				voice = await bot.move_to(channel)
				player = voice.create_ffmpeg_player("/root/Soundboard/shut_up_pre.wav")
				player.start()
			elif channel == cur_channel:
				player = voice.create_ffmpeg_player("/root/Soundboard/shut_up_pre.wav")
				player.start()
		else:
			voice = await bot.join_voice_channel(channel)
			player = voice.create_ffmpeg_player("/root/Soundboard/shut_up_pre.wav")
			player.start()

@bot.command(pass_context=True)
async def one_tank(ctx):
	global voice
	channel = ctx.message.author.voice_channel
	if channel is None:
		mem = ctx.message.author
		await bot.say("Hey "+mem.name+" try getting into a voice channel next time!")
	else:
		if voice is not None:
			cur_channel = voice.channel
			if channel != cur_channel:
				voice = await bot.move_to(channel)
				player = voice.create_ffmpeg_player("/root/Soundboard/one_tank.wav")
				player.start()
			elif channel == cur_channel:
				player = voice.create_ffmpeg_player("/root/Soundboard/one_tank.wav")
				player.start()
		else:
			voice = await bot.join_voice_channel(channel)
			player = voice.create_ffmpeg_player("/root/Soundboard/one_tank.wav")
			player.start()

@bot.command(pass_context=True)
async def omg_tg(ctx):
	global voice
	channel = ctx.message.author.voice_channel
	if channel is None:
		mem = ctx.message.author
		await bot.say("Hey "+mem.name+" try getting into a voice channel next time!")
	else:
		if voice is not None:
			cur_channel = voice.channel
			if channel != cur_channel:
				voice = await bot.move_to(channel)
				player = voice.create_ffmpeg_player("/root/Soundboard/omg_tg.wav")
				player.start()
			elif channel == cur_channel:
				player = voice.create_ffmpeg_player("/root/Soundboard/omg_tg.wav")
				player.start()
		else:
			voice = await bot.join_voice_channel(channel)
			player = voice.create_ffmpeg_player("/root/Soundboard/omg_tg.wav")
			player.start()

@bot.command(pass_context=True)
async def burn_him(ctx):
	global voice
	channel = ctx.message.author.voice_channel
	if channel is None:
		mem = ctx.message.author
		await bot.say("Hey "+mem.name+" try getting into a voice channel next time!")
	else:
		if voice is not None:
			cur_channel = voice.channel
			if channel != cur_channel:
				voice = await bot.move_to(channel)
				player = voice.create_ffmpeg_player("/root/Soundboard/burn_him.wav")
				player.start()
			elif channel == cur_channel:
				player = voice.create_ffmpeg_player("/root/Soundboard/burn_him.wav")
				player.start()
		else:
			voice = await bot.join_voice_channel(channel)
			player = voice.create_ffmpeg_player("/root/Soundboard/burn_him.wav")
			player.start()

bot.run('MjQ4MjEwODgxNzg2MTUwOTEz.Cw0b7A.o3EnOGtkGuHMmN9TPuNGm8vRxvU')

