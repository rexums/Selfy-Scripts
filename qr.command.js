// The name of the command - String
commandName = "qrcode";

// The command category (FUN, UTILITY, TROLL) - String
commandCategory = "UTILITY";

// The command description - String
commandDescription = "Generate a QR Code from a string.";

// The command syntax - String
commandSyntax = "<URL>";

// The command aliases - StringList
commandAliases = [ "qr" ];

// The API which is used to generate the QR Code
api = "https://rex-api.rexjohannes.repl.co/qr/" + bot.getConfig().getConfigObjectByKey("rexAPI").getValue("") + "/?url=";

// Gets run when the command gets executed
// args - List, event - MessageCreateEvent
function onCommand(args, event) {
    response = HttpUtils.get(api + args[0].replaceAll(" ", "+"));

    MessageUtils.editMessage(
        event.getMessage(),
        "QR Code",
        "",
        ColorUtils.getRandomColor().getRGB(),
        response
    );
}