# Troublshooting - Version 4
# - Questions may lead to a supplementary question (efficiently)

# The decision tree of questions that are available!
questions = {
    "start" : {
        "q" : "Is your device a mobile phone?",
        "t" : "signal_start",
        "f" : None
        },
    "signal_start" : {
        "q" : "Does your phone have signal?",
        "t" : "dropped_start",
        "f" : "Uh oh, you're a muppet.  Put the SIM card in then!"
        },
    "dropped_start" : {
        "q" : "Have you dropped your phone?",
        "t" : "dropped_water",
        "f" : None
        },
    "dropped_water" : {
        "q" : "Did you drop your phone in water?",
        "t" : "dropped_water_time",
        "f" : "dropped_screen"
        },
    "dropped_water_time" : {
        "q" : "Was the phone submerged in water for longer than 5 minutes?",
        "t" : "Turn it off and leave it in a jar of rice for at least 3 days.",
        "f" : "Turn it off and leave it in a jar of rice overnight"
        },
    "dropped_screen" : {
        "q" : "Has the screen broken?",
        "t" : "You'll need to have the screen replaced.",
        "f" : None
        }
}

# This function will request user input and validate it's YES or NO.
# Alternative inputs will be accepted as appropriate.
# This function will then return TRUE or FALSE respectively.
def inputYN():
    trueResponses = ["Y", "YES", "1"]
    falseResponses = ["N", "NO", "0", ""]
    
    while True:
        answer = input("YES or NO: >> ").upper()

        if answer in trueResponses:
            return True
        elif answer in falseResponses:
            return False

    return None

def hasSubQuestion(question, outcome="t"):
    global questions

    return (question[outcome] in questions)

##questions = [
##    ["Does your phone have signal?", "Your SIM card must be inserted."],
##    ["Have you dropped your phone?", "What a muppet.  You'll need to get that fixed."],
##    ["Has your phone suffered water damage?", "A jar of rice will fix that!"]
##]

print("Welcome to the generic trouble shooter for a mobile phone.")

question = questions["start"]
while question != None:
    print(question["q"])

    if inputYN():
        if hasSubQuestion(question, "t"):
            question = questions[question["t"]]
        else:
            print(question["t"])
            input()
            exit(0)
    else:
        if hasSubQuestion(question, "f"):
            question = questions[question["f"]]
        else:
            question = None

print("Uh oh, we have no solution.  Go back to your vendor!")
