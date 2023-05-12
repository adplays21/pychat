import random

# Define some predefined responses
greetings = ["hi", "hello", "hey", "howdy", "greetings"]
farewells= ["bye", "goodbye", "see you", "take care"]
conversations=["how are you?","how are you","how you doing?"]
conversations1=["what is your name"]
conversations2=['what is your gender','are you a male or female','m or f']
conversations3=['what is your fav color','what is your favourite colour']
conversations4=['who is your creator',"who created you",'who designed you']
# Define a function to generate a random response
def get_random_response(responses):
    return random.choice(responses)

# Main chat loop
while True:
    # Get user input
    user_input = input("You: ").lower()

    # Check for greetings
    if user_input in greetings:
        bot_response = get_random_response(["Hello!", "Hi there!", "Hey!"])
    # Check for farewells
    elif user_input in farewells:
        bot_response = get_random_response(["Goodbye!", "See you later!", "Take care!"])
    #Check for random conversations 
    elif user_input in conversations:
        
     bot_response=get_random_response(["i am doing good lately,what about you?","i am good,i hope you are doiing well too"]) 

    elif user_input in conversations1:
        bot_response=get_random_response(["I am a self designed chat box named pychat"]) 
    elif user_input in conversations2:
        bot_response=get_random_response(["i am  a robot "])
    elif user_input in conversations3:
        bot_response=get_random_response(["i don't have any sepcific color choice but my creator loves black"])
    elif user_input in conversations4:
        bot_response=get_random_response(['i have been designed and implemented by mr Adan'])
    # Respond with a default message
    else:
        bot_response = get_random_response(["I'm sorry, I didn't understand that.I haven't been prepared for this task abruptly", "Could you please rephrase that?"])
  # Print the bot's response
    print("Bot:", bot_response)