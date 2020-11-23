#-------------------------------------------------------------------------------
# Name:			roleBot
# Purpose:		This bot is a discord bot
#				it's purpose is to help admin of a role play discord server
#				by adding some commands
#				This bot is divided in 4 parts (including this one)
#				This programme defines the bot name and imports discords api for an easier "compilation"
#
# Author:      Youllou
#
# Created:     20/11/2020
# Copyright:   (c) Youllou 2020
# Licence:     <your licence>
#-------------------------------------------------------------------------------



import discord
from discord.ext import commands


client = discord.Client()
roleBot = commands.Bot(command_prefix='!')