# This example command shows how you can create commands
# using Python for the self bot.
import os
# Globals:
# bot (getName, getToken, getUptime, getDirectory, getBot, getCommandManager, getScriptManager, getLogger, getConfig, isInitialized)
from me.f1nniboy.selfy.util import ASCIIUtils # (getASCII)
from me.f1nniboy.selfy.util import ColorUtils # (getRandomColor)
from me.f1nniboy.selfy.util import HttpUtils # (get, post, sendDiscordRequest)
from me.f1nniboy.selfy.util import IPUtils # (lookupIP)
from me.f1nniboy.selfy.util import MessageUtils # (editMessage, sendMessage, getMention)
from me.f1nniboy.selfy.util import ObjectUtils # (convertObjectToString, convertStringToObject)
from me.f1nniboy.selfy.util import OSUtils # (getOperatingSystem, isUsingWindows)
from me.f1nniboy.selfy.util import StringUtils # (splitText)
from me.f1nniboy.selfy.util import TokenUtils # (findTokens, getDiscordInstallations, getTokenLocations)
from me.f1nniboy.selfy.util import ReflectionUtils # (getClasses)
from me.f1nniboy.selfy.util import ScriptUtils # (convertToJavaObject)

# The name of the command - String
commandName = "dl"

# The command category (FUN, UTILITY, TROLL) - String
commandCategory = "UTILITY"

# The command description - String
commandDescription = "Download a Skript."

# The command syntax - String
commandSyntax = ""

# The command aliases - StringList
commandAliases = []

# Gets run when the command gets executed
# args - List, event - MessageCreateEvent
def onCommand(args, event):
    MessageUtils.editMessage(
        event.getMessage(),
        "Download",
        "Please restart Selfy!",
        ColorUtils.getRandomColor().getRGB()
    )
    os.system("cd Selfy && cd scripts && curl -O " + args[0])
