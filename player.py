#-------------------------------------------------------------------------------
# Name:			player
# Purpose:		This bot is a discord bot
#				it's purpose is to help admin of a role play discord server
#				by adding some commands
#				This bot is divided in 4 parts (including this one)
#				This part is the player part. Here you will find all the commands usefull for the player
#
# Author:      Youllou
#
# Created:     20/11/2020
# Copyright:   (c) Youllou 2020
# Licence:     <your licence>
#-------------------------------------------------------------------------------


#local import
from deff import*


#define constant

#define global variable




@roleBot.command()
async def help_player(ctx):
	"""
		This command gives all the player's command in dm to the user
	"""
	await ctx.author.create_dm()
	await ctx.author.send("""As a player you can do those commands :
							 !join `adventure` makes you join an adventure
							 !quit `adventure` makes you quit an adventure (the argument is optionnal)
							 !inventory `adventure` gives your inventory (the argument is optionnal)""")


@roleBot.command()
async def join(ctx,adventure: str = None):
	"""
		This command makes the user join an adventure 
	"""
	__adventure__=os.listdir('../'+ctx.guild.name)
	print(__adventure__)

	if adventure == None:
		await ctx.channel.send("You must choose an adventure to join")
	elif adventure not in __adventure__ :
		await ctx.channel.send("This adventure does not exist yet. Ask a GM if he can create it")
	else :
		for i in ctx.guild.roles:
			if adventure == i.name :
				adventure = i

		if adventure in ctx.author.roles :
			await ctx.channel.send("You're already in this adventure.\nIf you wish to quit it use '!quit'")
		else :
			try :
				os.mkdir(os.path.relpath("../"+ctx.guild.name+"/"+adventure.name+"/Players/"+str(ctx.author.id),cur_path))
			except OSError:
				print("os error when creating dir during !join")
				await ctx.channel.send("They were an error during directory creation\nMaybe if you try again ??\nIf it keep happening please contact an @admin")
			else :
				f=open(os.path.relpath("../"+ctx.guild.name+"/"+adventure.name+"/Players/"+str(ctx.author.id)+"/Inventory.csv",cur_path),"w")
				f.write("id |name")
				f.close()
				await ctx.author.add_roles(adventure)
				await ctx.channel.send("Succesfully joined "+adventure.name)



@roleBot.command()
async def quit(ctx,adventure: str = None):
	"""
		This command makes the user quit an adventure
	"""
	__adventure__=os.listdir('../'+ctx.guild.name)
	print(__adventure__)

	if adventure == None:
		await ctx.channel.send("You must choose an adventure to quit")
	elif adventure not in __adventure__ :
			await ctx.channel.send("This adventure does not exist yet.\nYou can not quit an adventure that doesn't exist")
	else :
		for i in ctx.guild.roles:
			if adventure == i.name :
				adventure = i

		if adventure not in ctx.author.roles :
			await ctx.channel.send("You're not in this adventure.\nIf you wish to join it use '!join'")
		else :
			try :
				shutil.rmtree(os.path.relpath("../"+ctx.guild.name+"/"+adventure.name+"/Players/"+str(ctx.author.id),cur_path))
			except OSError :
				print("os error when deleting dir during !quit")
				await ctx.channel.send("They were an error during directory suppression\nMaybe if you try again ??\nIf it keep happening please contact an @admin")
			else :
				await ctx.author.remove_roles(adventure)
				await ctx.channel.send("Succesfully quitted "+adventure.name)



@roleBot.command()
async def inventory(ctx,adventure: str = None):
	"""
		This command gives the inventory of the user for an adventure
	"""
	__adventure__=os.listdir('../'+ctx.guild.name)
	print(__adventure__)

	#define some variables
	allinfo = []
	cpt = 0

	#seeking if the user specified an adventure 
	#if not, the bot look in the user's roles, if he detect only one adventure he select this one, else he ask the user to specify
	#if yes, the bot select the adventure specified
	if adventure == None:
		for i in ctx.author.roles:
			for j in __adventure__:
				if i.name == j :
					tmp = j
					cpt+=1
		if cpt >= 2 :
			await ctx.channel.send("You are in more than one adventure. Please specify the adventure")
		elif cpt < 1 :
			await ctx.channel.send("You are not in any adventure, join one to check your inventory")
		else :
			adventure=tmp

	try :
		#searching for the file
		f=open(os.path.relpath("../"+ctx.guild.name+"/"+adventure+"/Players/"+str(ctx.author.id)+"/Inventory.csv",cur_path),"r",encoding="UTF-8")
	except FileNotFoundError:
		#output if not found
		await ctx.channel.send("Your inventory has not been found\nAre you sure you are in this adventure ?\nYes ? then try to add your role name")
	else :
		while 1:
			info = f.readline()
			if info =="":
				break
			else :
				allinfo+=[info.split("|")]
		#output if found
		sentence = "```"
		for i in range(len(allinfo)):
			sentence += allinfo[i][0]+"|"+allinfo[i][1]
		sentence += "```"
		await ctx.channel.send("Here is what you have for "+adventure+" :")
		await ctx.channel.send(sentence)