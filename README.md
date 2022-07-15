# Graphical Transfer Update Generator
#### Video Demo:  <https://youtu.be/2MLYqgUf0K8>
#### Description: Werner is a Discord bot, that generates graphical transfer updates using the given information.

# Required Information
#### Werner requires 3 images and few 3 text-replies, the ***3 images being***: 
> The player's image

> The player's current club

> The player's future club (according to the transfer news)
#### and the ***3 text replies being***:
> The player's name

> The player's age

> The deal's current status
#### using all that information, Werner would generate the transfer update image.

# Libraries that I used
#### Two main libraries that I used were:
- Pillow
- Discord.py 

### Reason behind using __Discord.py__:
#### I used Discord.py to lay the code Discord bot functionalities' foundation. It allowed me to login into my Discord bot, take input from users on Discord and then tie those input with my rest of the code

### Reason behind using __Pillow__:
#### Pillow is the key reason why this bot was possible, Pillow allowed me to take that Discord user's input and combine all of that to produce the final image.

# Folder Structure Breakdown
- There's a __Files__ folder
    - In which is another folder named __Main__:
        1. There resides my bot.py file, *the main file*
        2. The base image, *using which pillow would work*
        3. A truetype font file, *which pillow would use to type text on the image.*
        4. An image file named __generated_image__, *this is the image that pillow produced*
        5. Lastly there's another folder image:
            - Where lies all the downloaded images from user's input

# Code Dissection
#### The code basically has two parts
1. To connect the code to Discord's portal, *making the bot and taking in input etc*
2. Image manipulation, *the juicy part*

- 1) In this bit,
    - I connect my code to the Discord portal through the given token
    - Ask for user input
    - Make embeds, *stylised messages of Discord*
    - Store those user input in a variable
    - Send the produced image on Discord

- 2) Here using the pillow module,
    - I open the base image, and user's inputted images
    - Convert the png files of the user to the *RGBA* mode
    - Paste those images on the base image
    - Write text on the image according to the user's text-replies
    - Save the produced image and forward it to Discord.py

# How to start off
1. First of all, type `.transfer player_name` where player_name is the name of the player for whom you are creating the transfer update.
2. Then the bot would ask for the player's age, where you would type in the player's age.
3. Then the bot would ask you to input an *online image* of the player
4. Then it would ask for an *online image* of player's current club's logo
5. Then it would ask for an *online image* of the player's future club's logo
6. And finally it would prompt you for the transfer's current status.

#### And after inputting information for all those prompts, the bot would generate an image within a short amount of time.

# Want to use the code with your own bot??
#### Just go to the very last line of code and from there change the token value with your generated token value, *one you got from the Discord developer portal.*


