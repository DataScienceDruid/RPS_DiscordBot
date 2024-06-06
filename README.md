# RPS_DiscordBot
## Overview 
Discord is an instant messaging/voice call application that allows for building online community spaces called "servers".
This python script is a discord "bot" which is an automated user that other users can interact with when in a server. 
By beginning messages with the appropriate prefix and issuing a valid command the bot can challenge another user to a game of "Rock, Paper, Scissors".
Then once issued the challenge each user is sent a personal message by the bot where they are prompted to press the button for their choice of Rock, Paper, or Scissors. Then the result of the game is sent back in whatever text-channel the challenge was issued. (If a user does not click on an option within the time alloted the game is null and the bot sends a timed-out message in the original text channel).

This requires the `discord` python library and another python file in the same directory "apikeys.py" which contains the constant "TOKEN" containing a string for your bots access token. 
