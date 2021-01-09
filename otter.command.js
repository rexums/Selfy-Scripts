// This example command shows how you can create commands
// using JavaScript for the self bot.

// Globals:
// bot - Bot (getName, getToken, getUptime, getDirectory, getBot, getCommandManager, getScriptManager, getLogger, getConfig, isInitialized)

// The name of the command - String
var commandName = "otter";

// The command category (FUN, UTILITY, OTHER) - String
var commandCategory = "FUN";

// The command description - String
var commandDescription = "Send cool Otter images.";

// The command syntax - String
var commandSyntax = "";

// The command aliases - StringList
commandAliases = [];

// Gets run when the command gets executed
// args - List, event - MessageCreateEvent
function onCommand(args, event) {
    response = HttpUtils.get("https://otter.api.rex-bot.ga");
    
    MessageUtils.editMessage(
        event.getMessage(),
        "Otter",
        "",
        ColorUtils.getRandomColor().getRGB(),
        response
    );
}