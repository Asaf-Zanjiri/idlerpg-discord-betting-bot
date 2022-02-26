# Idlerpg Discord Betting Bot
I digged up my projects folder and found some cool stuff I made in 2020 / 2021. This one was from early 2021

Since it was an old project, the code is a bit messy, since I don't plan on doing anything with it I won't tidy up the code and make it more professional, but it should be good enough if you're looking for discord selfbot examles.


This selfbot works with the https://idlerpg.xyz/ discord bot.
If you dont know what a discord selfbot is, it basically automates messages/actions in your own discord account.


The bot uses a simple betting algorithm. If you lose, double down with the initial bet. Starting from 1, 2, 4, 8, and so on...
Since in the long run this will be bound to fail, I've also added a safe stop mechanism to reset the betting amount when the balance is around 1 forth of the intial betting balance.
The application prints in the console each bet, if it's a win or a lose, and the current balance.
When I first made it I left it overnight every night for almost a week and reached around $1m bot coins, so that was pretty cool.


To use this bot you first need to give your discord token to the bot (dw, I don't grab the discord token like other codes, you can look at the source code). Add it to settings\config.json in the code folder.


To start the bot type: `>flipbot start`
To stop the bot type: `>flipbot stop`
To see the help message type: `>HELP`
To nuke spam messages made by the bot type: `>purge X` Can't delete more than 10 messages in one go as a safety mechanism to avoid deleting actual messages


I don't have a screenshot of the bot console, but I took a screenshot of the bot in action - I only wrote `>flipbot start` and the bot typed the rest:
![Screenshot_1](https://user-images.githubusercontent.com/60044819/155860000-ce10d072-0a8e-4d64-8579-b9d79c6a75ae.png)
