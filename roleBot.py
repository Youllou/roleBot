#-------------------------------------------------------------------------------
# Name:			roleBot
# Purpose:		This bot is a discord bot
#				it's purpose is to help admin of a role play discord server
#				by adding some commands
#				This bot is divided in 4 parts (including this one)
#				This programme is the reunificator of the 3 other and also launch the bot
#
# Author:      Youllou
#
# Created:     20/11/2020
# Copyright:   (c) Youllou 2020
# Licence:     <your licence>
#-------------------------------------------------------------------------------



from deff import *
from player import *

@roleBot.command()
async def help(ctx):
	await ctx.author.create_dm()
	await ctx.author.send("""roleBot is divided in some parts
							 Use '!help_player' to have the player's commands
							 Use'!help_GM' to have the Game master's commands""")


roleBot.run("Token")
