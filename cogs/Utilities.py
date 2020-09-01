import discord
import sys
import random
import time
import datetime
from discord.ext import commands

class Utilities(commands.Cog):

    def __init__(self, client):
        self.client = client
    
    @commands.Cog.listener()
    async def on_ready(self):
        time.sleep(0.2)
        print('Utilities.py')
        time.sleep(0.2)
        print(20 * '~')

    @commands.command(aliases = ['invite', 'add', 'Add'])
    async def Invite(self, ctx):
        member = ctx.message.author
        mem = member.Mention
        embed= discord.Embed(
            colour=(0x629632)
        )

        embed.set_author(name="Guardian Deer", icon_url="https://cdn.discordapp.com/avatars/606855758612660327/98b13ab2d31342848754caa909a653da.png?size=1024")
        embed.add_field(name="Invite link sent to:", value=str(mem), inline=False)
        embed.set_footer(text="More Features Coming Soon! We're still in Alpha™")

        await ctx.channel.send(embed=embed)
        embed2= discord.Embed(
            colour=(0x629632)
        )

        embed2.set_author(name="Guardian Deer", icon_url="https://cdn.discordapp.com/avatars/606855758612660327/98b13ab2d31342848754caa909a653da.png?size=1024")
        embed2.add_field(name="Here's an Invite Link!", value='https://discord.com/oauth2/authorize?client_id=695320805315182723&scope=bot&permissions=125014', inline=False)
        embed2.set_footer(text="More Features Coming Soon! We're still in Alpha™")
        await member.send(embed=embed2)


    @commands.command(aliases=["Changelog", "log", "Log", "release", "Release", "Version", "version"])
    async def changelog(self, ctx):
        embed= discord.Embed(
            colour=(0x629632),
            title="P.A.R.R.O.T. V.1.3.1_1/09/20 (4f7704b)"
        )

        embed.set_author(name="Guardian Deer", icon_url="https://cdn.discordapp.com/avatars/606855758612660327/98b13ab2d31342848754caa909a653da.png?size=1024")
        embed.add_field(name="What's New?", value="Added: Gaming commands >Roll and >Coinflip\nFurther additions to the Social Extension\n>Uptime so you can see how long it has been since the last restart", inline=False)
        embed.add_field(name="Changes:", value="Added >Help Gaming to the Utilities Extension.", inline=False)
        embed.add_field(name="Removed:", value="Nothing...", inline=False)
        embed.add_field(name="What's Next?", value="More Social & Gaming Related Commands.\nLogging for deleted and edited messages.\n>Suggestions (DM's only)\nRandomised time-based profile statuses!\n>FAQ command alongside >Ask", inline=False)
        embed.set_footer(text="More Features Coming Soon! We're still in Alpha™")

        await ctx.send(embed=embed)

    @commands.command(aliases=["credits", "Cred", "cred"])
    async def Credits(self, ctx):
        embed= discord.Embed(
            colour=(0x629632),
            title="Credits!"
        )

        embed.set_author(name="Guardian Deer", icon_url="https://cdn.discordapp.com/avatars/606855758612660327/98b13ab2d31342848754caa909a653da.png?size=1024")
        embed.add_field(name="Description:", value="These are the primary contributors to the Guardian Bot who are credited below.", inline=False)
        embed.add_field(name="Beowulf#1863", value="Role: Owner\n Primary developer of the Guardian Deer bot, as well as manager for the GitHub and Heroku dependencies.", inline=False)
        embed.add_field(name="Mathew!#1404", value="Role: Assistant Developer\n Assistant in developing new code modules and features, as well as DeBugging broken code.", inline=False)
        embed.set_footer(text="More Features Coming Soon! We're still in Alpha™")

        await ctx.send(embed=embed)  

    @commands.command(aliases=["listerr", "Errors", "errors", "Error"])
    async def error(self, ctx):
        embed= discord.Embed(
            colour=(0x629632),
            title="Known Errors:"
        )

        embed.set_author(name="Guardian Deer", icon_url="https://cdn.discordapp.com/avatars/606855758612660327/98b13ab2d31342848754caa909a653da.png?size=1024")
        embed.add_field(name="#000", value="Unknown Errors.", inline=False)
        embed.add_field(name="#001", value="Missing Permissions.", inline=False)
        embed.add_field(name="#002", value="Missing Required Arguments.", inline=False)
        embed.add_field(name="#003", value="Coding Limitations.", inline=False)
        embed.add_field(name="#004", value="Precautionary Limitations.", inline=False)
        embed.add_field(name="#005", value="Command Does Not Exist.", inline=False)
        embed.add_field(name="#006", value="Unable To Complete Request.", inline=False)
        embed.set_footer(text="More Features Coming Soon! We're still in Alpha™")

        await ctx.send(embed=embed)


    @commands.command(aliases=['help'])
    async def Help(self, ctx, *, module:str):
        if module == "Utilities" or module == "utilities":
            embed= discord.Embed(
                colour=(0x629632),
                title="Utility Commands:"
            )

            embed.set_author(name="Guardian Deer", icon_url="https://cdn.discordapp.com/avatars/606855758612660327/98b13ab2d31342848754caa909a653da.png?size=1024")
            embed.add_field(name=">Ping", value="This command returns the current ping of the bot in milliseconds.", inline=False)
            embed.add_field(name=">Purge", value="Deletes a specified number of previous messages. \n Useage: >purge [# of Messages]", inline=False)
            embed.add_field(name=">Uptime", value="Returns the uptime of the bot!", inline=False)
            embed.set_footer(text="More Features Coming Soon! We're still in Alpha™")

            await ctx.send(embed=embed)
            return
        elif module == "Moderation" or module == "moderation":
            embed2= discord.Embed(
                colour=(0x629632),
                title="Moderation Commands:"
            )

            embed2.set_author(name="Guardian Deer", icon_url="https://cdn.discordapp.com/avatars/606855758612660327/98b13ab2d31342848754caa909a653da.png?size=1024")
            embed2.add_field(name=">Ban", value="The Guardian will ban the specified user for a specified reason.\n Usage: >ban [User Mention] [Ban reason]", inline=False)
            embed2.add_field(name=">Kick", value="The Guardian will kick the specified user for a specified reason.\n Usage: >kick [User Mention] [Kick reason]", inline=False)
            embed2.add_field(name=">Unban", value="The Guardian will unban the desired user.\n Useage: >unban [User ID]", inline=False)
            embed2.set_footer(text="More Features Coming Soon! We're still in Alpha™")

            await ctx.send(embed=embed2)
            return
        elif module == "Social" or module == "social":
            embed2= discord.Embed(
                colour=(0x629632),
                title="Social Commands:"
            )

            embed2.set_author(name="Guardian Deer", icon_url="https://cdn.discordapp.com/avatars/606855758612660327/98b13ab2d31342848754caa909a653da.png?size=1024")
            embed2.add_field(name=">Hug", value="Allows you to hug another user.\n Usage: >hug [User Mention]", inline=False)
            embed2.add_field(name=">Cuddle", value="Allows you to cuddle another user.\n Usage: >cuddle [User Mention]", inline=False)
            embed2.add_field(name=">Boop", value="Allows you to boop another user.\n Usage: >boop [User Mention]", inline=False)
            embed2.add_field(name=">Flop", value="Allows you to flop on another user.\n Usage: >flop [User Mention]", inline=False)
            embed2.set_footer(text="More Features Coming Soon! We're still in Alpha™")

            await ctx.send(embed=embed2)
            return
        elif module == "dev" or module == "debug":
            embed2= discord.Embed(
                colour=(0x629632),
                title="Developer Commands:"
            )

            embed2.set_author(name="Guardian Deer", icon_url="https://cdn.discordapp.com/avatars/606855758612660327/98b13ab2d31342848754caa909a653da.png?size=1024")
            embed2.add_field(name=">Error", value="Lists the meanings of all known error codes.", inline=False)
            embed2.add_field(name=">Changelog", value="Opens the latest change log.", inline=False)
            embed2.add_field(name=">Credits", value="Opens the credits page.", inline=False)
            embed2.set_footer(text="More Features Coming Soon! We're still in Alpha™")

            await ctx.send(embed=embed2)
            return

        elif module == "Gaming" or module == "gaming":
            embed2= discord.Embed(
                colour=(0x629632),
                title="Gaming Commands:"
            )

            embed2.set_author(name="Guardian Deer", icon_url="https://cdn.discordapp.com/avatars/606855758612660327/98b13ab2d31342848754caa909a653da.png?size=1024")
            embed2.add_field(name=">Roll", value="Rolls the dice!\n Usage: >roll [Number of Dice]d[Number of Sides on Dice]", inline=False)
            embed2.add_field(name=">Coinflip", value="Flips a coin for you!\n 1 in 6000 chance of landing on it's side!", inline=False)
            embed2.set_footer(text="More Features Coming Soon! We're still in Alpha™")

            await ctx.send(embed=embed2)
            return

        else:
            embed2= discord.Embed(
                colour=(0x629632),
                title="An error has occured..."
            )

            embed2.set_author(name="Guardian Deer", icon_url="https://cdn.discordapp.com/avatars/606855758612660327/98b13ab2d31342848754caa909a653da.png?size=1024")
            embed2.add_field(name="That Command Does Not Exist...", value="Error: #005", inline=False)
            embed2.set_footer(text="More Features Coming Soon! We're still in Alpha™") 
            await ctx.send(embed=embed2)   

    @Help.error
    async def help_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            embed= discord.Embed(
                colour=(0x629632),
                title="Help Commands:"
            )

            embed.set_author(name="Guardian Deer", icon_url="https://cdn.discordapp.com/avatars/606855758612660327/98b13ab2d31342848754caa909a653da.png?size=1024")
            embed.add_field(name=">Help", value="This command returns this embed.", inline=False)
            embed.add_field(name=">Help Utilities", value="This command returns help info for the Guardian's Utility commands.", inline=False)
            embed.add_field(name=">Help Moderation", value="This command returns help info for the Guardian's Moderation commands.", inline=False)
            embed.add_field(name=">Help Social", value="This command returns help info for the Guardian's Social commands.", inline=False)
            embed.add_field(name=">Help Gaming", value="This command returns help info for the Guardian's Gaming commands.", inline=False)
            embed.add_field(name=">Help Dev", value="This command returns help info for the Guardian's Developer commands.\nNote: These commands are simply related to information about the Development process of Guardian Deer.", inline=False)
            embed.set_footer(text="More Features Coming Soon! We're still in Alpha™")

            await ctx.send(embed=embed)



def setup(client):
    client.add_cog(Utilities(client))