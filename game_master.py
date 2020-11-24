#-------------------------------------------------------------------------------
# Name:			game_master
# Purpose:		This bot is a discord bot
#				it's purpose is to help admin of a role play discord server
#				by adding some commands
#				This bot is divided in 4 parts (including this one)
#				This part is the game master part. Here you will find all the commands usefull for the game master
#
# Author:      Youllou
#
# Created:     20/11/2020
# Copyright:   (c) Youllou 2020
# Licence:     <your licence>
#-------------------------------------------------------------------------------


from deff import *




@roleBot.command()
async def help_GM(ctx):
	"""
		This command gives all the Game Master's command in dm to the user
	"""
	await ctx.author.create_dm()
	await ctx.author.send("""As a Game Master you can do those commands :
							 !create `adventure` creates an adventure and makes you the owner
							 !delete `adventure` deletes an adventure which of you are the owner (the argument is optionnal)
							 !kick `name` `adventure` kicks a player from an adventure (his inventory will be deleted, adventure is optionnal)""")




@roleBot.command()
async def create(ctx, adventure: str = None):

	__adventure__=os.listdir('../'+ctx.guild.name)
	print(__adventure__)
	
	all_good = 1
	path = os.path.relpath("../"+ctx.guild.name+"/"+adventure,cur_path)

	if adventure == None :
		await ctx.channel.send("You must give a name tou your adventure")
	else :
		if adventure in __adventure__:
			await ctx.channel.send("This adventure already exists. You must give a different name to your adventure")
		else :
			try :
				os.mkdir(path)
			except OSError :
				print("os error when creating dir during !create main dir")
				await ctx.channel.send("They were an error during directory creation\nMaybe if you try again ??\nIf it keep happening please contact an @admin")
			else :
				for i in ["/Story","/Maps","/NPC","/Players"] :
					try :
						os.mkdir(os.path.relpath(path,cur_path)+i)
					except OSError :
						print("os error when creating dir during !create "+i)
						await ctx.channel.send("They were an error during directory creation\nMaybe if you try again ??\nIf it keep happening please contact an @admin")
						all_good = 0

				if all_good == 1:
					await ctx.guild.create_role(name=adventure)
					await ctx.channel.send(adventure+" was created")

@roleBot.command()
async def delete(ctx, adventure: str = None):

	__adventure__=os.listdir('../'+ctx.guild.name)
	print(__adventure__)

	if adventure == None:
		await ctx.channel.send("This function is not implemented yet.\nPlease add the name of the adventure you want to delete")
	else :
		if adventure in __adventure__:

			try :
				shutil.rmtree(os.path.relpath("../"+ctx.guild.name+"/"+adventure,cur_path))
			except OSError:
				print("os error when deleting dir during !delete")
				await ctx.channel.send("They were an error during directory suppression\nMaybe if you try again ??\nIf it keep happening please contact an @admin")
			else :
				for i in ctx.guild.roles:
					if i.name == adventure:
						rl = i
				await rl.delete()
				await ctx.channel.send("Succesfully deleted "+adventure)
		else :
			await ctx.channel.send("Hmmm... It seems that this adventure does not exists...\nAre you sure it's its name ?")



