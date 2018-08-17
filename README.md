# hamtheman
HamTheMan (htm) is a Discord bot for various ham radio related things.

The most up-to-date version is in the `rewrite` branch, and is currently suitable for running.

## Getting started

### Discord
First, you need the correct version of the Discord API.

`python3 -m pip uninstall discord`

`python3 -m pip install -U https://github.com/Rapptz/discord.py/archive/rewrite.zip#egg=discord.py[voice]`

## Noteworthy stuff
You need a text file titled '.discordkey.txt' and a Discord key inside it to run the bot.

Also, you will need a hamqth.com account with your callsign and password (each on a new line) in a file titled '.onlinelookup-login.txt'.  Otherwise, it will throw a LookupVerificationError.
