# hamtheman
HamTheMan (htm) is a Discord bot for various ham radio related things

## Getting started

Make sure you are running Python 3.6 or higher.

### Discord
First, you need the correct version of the Discord API for Python.

`python3 -m pip uninstall discord`

`python3 -m pip install -U https://github.com/Rapptz/discord.py/archive/rewrite.zip#egg=discord.py[voice]`

### API Keys
You then need an API key for your bot (https://discordapp.com/developers/applications/) and an account with HamQTH (https://hamqth.com).

Place the API key in a file called `discord.txt` and your callsign and password (each on a new line) in a file called `hamqth-login.txt`.
