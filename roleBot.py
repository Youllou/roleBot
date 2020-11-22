#-------------------------------------------------------------------------------
# Name:	       RoleBot
# Purpose:
#
# Author:      Youllou
#
# Created:     20/11/2020
# Copyright:   (c) Youllou 2020
# Licence:     <your licence>
#-------------------------------------------------------------------------------

# bot.py

#global imports
import os
import discord
from discord.ext import commands
import random

#define the bot
client = discord.Client()
roleBot = commands.Bot(command_prefix='!')

#define constant
__adventure__=("L'enferRe","Test")


#define global variable
cur_path = os.path.dirname(__file__)


@roleBot.command()
async def ping(ctx):
	await ctx.send('pong')

async def join(ctx,adventure: str = None):
	if adventure == None:
		await ctx.channel.send("You must choose an adventure to join")
	elif adventure not in __adventure__ :
		await ctx.channel.send("This adventure does not exist yet. Ask an MJ if he can create it")
	else :
		for i in ctx.guild.roles:
			if adventure == i.name :
				rl = i

		if rl in ctx.author.roles :
			await ctx.channel.send("You're already in this adventure.\nIf you wish to quit it use '!quit'")
		else :
			await ctx.author.add_roles(rl)
			await ctx.channel.send("Succesfully joined "+adventure)

@roleBot.command()
async def quit(ctx,adventure: str = None):
	if adventure == None:
		await ctx.channel.send("You must choose an adventure to quit")
	elif adventure not in __adventure__ :
			await ctx.channel.send("This adventure does not exist yet.\nYou can not quit an adventure that doesn't exist")
	else :
		for i in ctx.guild.roles:
			print("adventure : "+adventure+"\nrole : '"+i.name+"'")
			if adventure == i.name :
				rl = i

		if rl not in ctx.author.roles :
			await ctx.channel.send("You're not in this adventure.\nIf you wish to join it use '!join'")
		else :
			await ctx.author.remove_roles(rl)
			await ctx.channel.send("Succesfully quitted "+adventure)

@roleBot.command()
async def inventory(ctx,adventure: str = None,name: str = None):
	allinfo = []
	cpt = 0
	if adventure == None:
		for i in ctx.author.roles:
			for j in __adventure__:
				if i.name == j :
					tmp = j
					cpt+=1
		if cpt > 2 :
			await ctx.channel.send("You are in more than one adventure. Please specify the adventure")
		elif cpt < 1 :
			await ctx.channel.send("You are not in any adventure, join one to check your inventory")
		else :
			adventure=tmp
			print(adventure)

	if name == None:
		try :
			print("File : "+os.path.relpath("../"+adventure+"/Players/"+ctx.author.name+".csv",cur_path))
			info_user=open(os.path.relpath("../"+adventure+"/Players/"+ctx.author.name+".csv",cur_path),encoding="UTF-8")
			while 1:
				info = info_user.readline()
				if info =="":
					break
				else :
					allinfo+=[info.split("|")]
			print(allinfo)
			await ctx.channel.send("Here is what you have :")
			sentence = "```"
			for i in range(len(allinfo)):
				sentence += allinfo[i][0]+"|"+allinfo[i][1]
			sentence += "```"
			await ctx.channel.send(sentence)
		except FileNotFoundError:
			await ctx.channel.send("Your inventory has not been found\nAre you sure you are in this adventure ?\nYes ? then try to add your role name")
	else :
		try :
			print("File : "+str(os.path.relpath("../"+adventure+"/Players/"+name+".csv",cur_path)))
			info_user=open(os.path.relpath("../"+adventure+"/Players/"+name+".csv",cur_path),encoding='UTF-8')
			while 1:
				info = info_user.readline()
				if info =="":
					break
				else :
					allinfo+=[info.split("|")]
			print(allinfo)
			await ctx.channel.send("Here is what you have :")
			sentence = "```"
			for i in range(len(allinfo)):
				sentence += allinfo[i][0]+"|"+allinfo[i][1]
			sentence += "```"
			await ctx.channel.send(sentence)
		except FileNotFoundError:
			await ctx.channel.send("Your inventory has not been found\nAre you sure you are in this adventure ?")



		


roleBot.run("Token")
