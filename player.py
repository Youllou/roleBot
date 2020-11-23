#-------------------------------------------------------------------------------
# Name:		   user_roleBot
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


#global imports
import os
from deff import*
import random


#define constant
__adventure__=("L'enferRe","Test")


#define global variable
cur_path = os.path.dirname(__file__)



@roleBot.command()
async def help_player(ctx):
	"""
		This command gives all the player's command in dm to the user
	"""
	await ctx.author.create_dm()
	await ctx.author.send("""As a player you can do those commands :
							 !join `adventure` `name` makes you join an adventure (the arguments are optionnal)
							 !quit `adventure` `name` makes you quit an adventure (the arguments are optionnal)
							 !inventory `adventure` `name` gives your inventory (the arguments are optionnal)""")


@roleBot.command()
async def join(ctx,adventure: str = None,name: str = None):
	"""
		This command makes the user join an adventure 
	"""
	if adventure == None:
		await ctx.channel.send("You must choose an adventure to join")
	elif adventure not in __adventure__ :
		await ctx.channel.send("This adventure does not exist yet. Ask an MJ if he can create it")
	else :
		for i in ctx.guild.roles:
			if adventure == i.name :
				adventure = i

		if adventure in ctx.author.roles :
			await ctx.channel.send("You're already in this adventure.\nIf you wish to quit it use '!quit'")
		else :
			if name == None :
				try :
					os.mkdir(os.path.relpath("../"+adventure.name+"/Players/"+ctx.author.name,cur_path))
				except OSError:
					print("os error when creating dir during !join")
					await ctx.channel.send("They were an error during directory creation\nMaybe if you try again ??\nIf it keep hapening please contact an admin")
				else :
					f=open(os.path.relpath("../"+adventure.name+"/Players/"+ctx.author.name+"/Inventory.csv",cur_path),"w")
					f.write("id |name")
					f.close()
					await ctx.author.add_roles(adventure)
					await ctx.channel.send("Succesfully joined "+adventure.name)
			else :
				try :
					os.mkdir(os.path.relpath("../"+adventure.name+"/Players/"+name),cur_path)
				except OSError:
					print("os error when creating dir during !join")
					await ctx.channel.send("They were an error during directory creation\nMaybe if you try again ??\nIf it keep hapening please contact an admin")
				else :
					f=open(os.path.relpath("../"+adventure.name+"/Players/"+name+"/Inventory.csv",cur_path),"w")
					f.write("id |name")
					f.close()
					await ctx.author.add_roles(adventure)
					await ctx.channel.send("Succesfully joined "+adventure.name)
	



@roleBot.command()
async def quit(ctx,adventure: str = None):
	"""
		This command makes the user quit an adventure
	"""
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
			await ctx.author.remove_roles(adventure)
			await ctx.channel.send("Succesfully quitted "+adventure.name)



@roleBot.command()
async def inventory(ctx,adventure: str = None,name: str = None):
	"""
		This command gives the inventory of the user for an adventure
	"""

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

	#seeking if the user specified a name
	#(this is usefull if users have a different name in the role play tho, for now, it gives the opportunity to everyone to see everyone's inventory)
	#as for the adventure if no name is given, the bot will search with the user name if nothing found he will ask to specify
	#if specified he will search with the name given
	if name == None:
		try :
			#searching for the file
			f=open(os.path.relpath("../"+adventure+"/Players/"+ctx.author.name+"/Inventory.csv",cur_path),"r",encoding="UTF-8")
			while 1:
				info = f.readline()
				if info =="":
					break
				else :
					allinfo+=[info.split("|")]
			#output if found
			await ctx.channel.send("Here is what you have :")
			sentence = "```"
			for i in range(len(allinfo)):
				sentence += allinfo[i][0]+"|"+allinfo[i][1]
			sentence += "```"
			await ctx.channel.send(sentence)
		except FileNotFoundError:
			#output if not found
			await ctx.channel.send("Your inventory has not been found\nAre you sure you are in this adventure ?\nYes ? then try to add your role name")
	else :
		try :
			f=open(os.path.relpath("../"+adventure+"/Players/"+name+"/Inventory.csv",cur_path),"r",encoding='UTF-8')
			while 1:
				info = f.readline()
				if info =="":
					break
				else :
					allinfo+=[info.split("|")]
			await ctx.channel.send("Here is what you have :")
			sentence = "```"
			for i in range(len(allinfo)):
				sentence += allinfo[i][0]+"|"+allinfo[i][1]
			sentence += "```"
			await ctx.channel.send(sentence)
		except FileNotFoundError:
			await ctx.channel.send("Your inventory has not been found\nAre you sure you are in this adventure ?")