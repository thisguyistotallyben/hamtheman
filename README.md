# HamTheMan
HamTheMan (htm) is a Discord bot for various ham radio related things, including callsign lookups (globally with HamQTH), solar conditions, time, and a morse code translator.

## Prerequisites

### System
- Python: Python 3.10 or higher
- Discord: `pip3 install discord.py` OR `pip3 install -U discord.py` OR `python3 -m "pip" install discord.py`
- Requests: `pip3 install requests`

### API Keys

#### Discord Application
- Go to https://discordapp.com/developers/applications/
- Create a new application
- Note the client secret. You will need it later :)

#### HamQTH
- Go to https://hamqth.com
- Create an account

## Setup

- Copy and rename `config_default.json` to `config.json` and fill in the information inside
  - `discord key`: the client secret for your Discord bot
  - `owner id`: Your Discord ID (a long number you can find by right-clicking your name in a server and selecting the option "Copy ID")
  - `accent color`: The hex code (as a string) used for the embed accents. You can leave this alone for blue.
  - `hamqth`
    - `username` Your callsign
    - `password` Your HamQTH password
  - `oofs`: No need to touch this.

## Running HamTheMan
- Run `python3 hamtheman.py &` in a terminal (cmd, powershell, bash, whatever your OS has)
- **Note:** The `&` runs it in the background so you can close the terminal.
