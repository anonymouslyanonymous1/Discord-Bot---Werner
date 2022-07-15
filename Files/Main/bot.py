import discord
from discord.ext import commands
import datetime
import asyncio
import random
from PIL import Image, ImageDraw, ImageFilter, ImageFont
import urllib.request
from io import BytesIO
import os
import sys


# client = discord.Client()
client = commands.Bot(command_prefix='.')

def restart_bot(): 
  os.execv(sys.executable, ['python'] + sys.argv)

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.command()
async def transfer(ctx, player_name):
    try:
        # await ctx.send(f"Ok so Player Name: {player_name}")
        first = discord.Embed(title = "Player Name", description = "Ok so, Player Name: " + player_name, colour = discord.Colour.dark_red())
        await ctx.send(embed = first)
        def check(m):
            return m.author.id == ctx.author.id
        await ctx.send("Player Age?")
        player_age = await client.wait_for('message', check=check)
        second = discord.Embed(title = "Player Age", description = "Ok so, Player Age: " + player_age.content, colour = discord.Colour.dark_red())
        await ctx.send(embed = second)

        await ctx.send("Provide a link for the image of the player with the aspect ratio 1:1, upload that image to [https://postimages.org/]")
        player_link = await client.wait_for('message', check=check)
        third = discord.Embed(title = "Player Image", description = "Ok so, Player Image: ", colour = discord.Colour.dark_red())
        third.set_image(url = player_link.content)
        await ctx.send(embed = third)
        

        await ctx.send("Provide a ***wikipedia link/postimage link*** of the logo of the club in which the player is currently in")
        current_club_link = await client.wait_for('message', check=check)
        fourth = discord.Embed(title = "Player's Current Club", description = "Noice, so Player's current club: ", colour = discord.Colour.dark_red())
        fourth.set_image(url = current_club_link.content)
        await ctx.send(embed = fourth)
        

        await ctx.send("Provide a ***wikipedia link/postimage link*** of the logo of the club to which the player is going to move to")
        future_club_link = await client.wait_for('message', check=check)
        fifth = discord.Embed(title = "Player's Future Club", description = "Noice, so Player's future club: ", colour = discord.Colour.dark_red())
        fifth.set_image(url = future_club_link.content)
        await ctx.send(embed = fifth)
        

        await ctx.send("Provide the current status of the deal eg: Rumours/ In Talks/ Confirmed")
        deal_status = await client.wait_for('message', check=check)
        sixth = discord.Embed(title = "Deal Status", description = "Ok so, Deal Status: " + deal_status.content, colour = discord.Colour.dark_red())
        await ctx.send(embed = sixth)

        await ctx.send("Please wait. The image is being processed <a:WindowsLoading:993886231895232602>")

        urllib.request.urlretrieve(player_link.content, "Main/images/player_img.jpg")
        urllib.request.urlretrieve(current_club_link.content, "Main/images/current_club.png")
        urllib.request.urlretrieve(future_club_link.content, "Main/images/future_club.png")


        base = Image.open('Main/base.jpg')
        player1 = Image.open("Main/images/player_img.jpg")
        player2 = player1.resize((1536, 1536))
        player2.save("Main/images/player_img1.jpg")
        player = Image.open("Main/images/player_img1.jpg")
        previous_clubo = Image.open("Main/images/current_club.png")
        next_clubo = Image.open("Main/images/future_club.png")
        prev_new = Image.open("Main/images/current_club.png")
        next_new = Image.open("Main/images/future_club.png")

        if previous_clubo.height != previous_clubo.width:
            prev_new = previous_clubo.resize((480, 655))
            prev_new.save('Main/images/previous_club1.png')
        elif previous_clubo.width != previous_clubo.height:
            prev_new = previous_clubo.resize((570, 300))
            prev_new.save('Main/images/previous_club1.png')
        else:
            prev_new = previous_clubo.resize((564, 564))
            prev_new.save('Main/images/previous_club1.png')

        previous_club = Image.open('Main/images/previous_club1.png')

        if next_clubo.height != next_clubo.width:
            next_new = next_clubo.resize((480, 655))
            next_new.save('Main/images/next_club1.png')
        elif next_clubo.width != next_clubo.height:
            next_new = next_clubo.resize((570, 300))
            next_new.save('Main/images/next_club1.png')
        else:
            next_new = next_clubo.resize((564, 564))
            next_new.save('Main/images/next_club1.png')

        next_club = Image.open('Main/images/next_club1.png')

        previous_club1 = previous_club.convert("RGBA")
        next_club1 = next_club.convert("RGBA")

        # rgba1 = previous_club.convert("RGBA")
        # rgba2 = next_club.convert("RGBA")
        # data1 = rgba1.getdata()
        # data2 = rgba2.getdata()

        # newData1 = []
        # for item in data1:
        #     if item[0] == 0 and item[1] == 0 and item[2] == 0:  # finding black colour by its RGB value
        #         # storing a transparent value when we find a black colour
        #         newData1.append((255, 255, 255, 0))
        #     else:
        #         newData1.append(item)  # other colours remain unchanged

        # newData2 = []
        # for item in data2:
        #     if item[0] == 0 and item[1] == 0 and item[2] == 0:  # finding black colour by its RGB value
        #         # storing a transparent value when we find a black colour
        #         newData2.append((255, 255, 255, 0))
        #     else:
        #         newData2.append(item)  # other colours remain unchanged

        # rgba1.putdata(newData1)
        # rgba2.putdata(newData2)
        # rgba1.save("previous_club", "PNG")
        # rgba2.save("next_club", "PNG")

        # previous_club1 = Image.open('previous_club')
        # next_club1 = Image.open('next_club')


        base_copy = base.copy()

        status = ImageDraw.Draw(base_copy)
        font1 = ImageFont.truetype("Main/coolvetica.ttf", 198)
        status.text((100, 2700), "Status: " + deal_status.content, (255, 255, 255), font=font1)

        name = ImageDraw.Draw(base_copy)
        # size = 200
        font2 = ImageFont.truetype("Main/coolvetica.ttf", 255)
        name.text((1760, 840), player_name, (255, 255, 255), font=font2)

        age = ImageDraw.Draw(base_copy)
        font3 = ImageFont.truetype("Main/coolvetica.ttf", 210)
        age.text((1760, 1100), "Age: " + player_age.content + "yrs", (255, 255, 255), font=font3)


        base_copy.paste(player, (138, 280))
        # base_copy.paste(previous_club1, (800, 1900), previous_club1)
        # base_copy.paste(next_club1, (1900, 1980), next_club1)


        if previous_club1.size == (480, 655):
            base_copy.paste(previous_club1, (800, 1900), previous_club1)
        elif previous_club1.size == (655, 480):
            base_copy.paste(previous_club1, (800, 1900), previous_club1)
        else:
            base_copy.paste(previous_club1, (716, 1983), previous_club1)

        if next_club1.size == (480, 655):
            base_copy.paste(next_club1, (1934, 1937), next_club1)
        elif next_club1.size == (655, 480):
            base_copy.paste(next_club1, (800, 1900), next_club1)
        else:
            base_copy.paste(next_club1, (1934, 1985), next_club1)

        base_copy.save('Main/generated_image.jpg', quality=95)

        await ctx.send(file = discord.File('Main/generated_image.jpg'))
    except:
        error = discord.Embed(title = "There was an error ❌", description = "We are looking into it.. Please wait for a few seconds or so and try again.<a:WindowsLoading:993886231895232602> ", colour = discord.Colour.dark_red())
        await ctx.send(embed = error)
        restart_bot()
        


client.run('token')