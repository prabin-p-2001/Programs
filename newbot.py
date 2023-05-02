bot_template = "BOT : {0}"
user_template = "USER : {0}"

# Define a function that sends a message to the bot:
def send_message(message):
    # Print user_template including the user_message
    print(user_template.format(message))
    # Get the bot's response to the message
    response = respond(message)
    # Print the bot template including the bot's response.
    print(bot_template.format(response))

# Define a function that receives a message and returns a response based on some rules:
def respond(message):
    # Concatenate the user's message to the end of a standard bot greeting
    bot_message = "Hello, " + message
    # Return the result
    return bot_message

# Test the bot by sending a message
send_message("Hi there!")
