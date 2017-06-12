# Troublshooting - Version 3
# - Questions may lead to a solution (more efficient)

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

# The decision tree of questions that are available!
questions = [
    ["Does your phone have signal?", "Your SIM card must be inserted."],
    ["Have you dropped your phone?", "What a muppet.  You'll need to get that fixed."],
    ["Has your phone suffered water damage?", "A jar of rice will fix that!"]
]

print("Welcome to the generic trouble shooter for a mobile phone.")

for question in questions:
    print(question[0])

    if inputYN():
        print(question[1])
        input()
        exit(0)

print("Uh oh, we have no solution.  Go back to your vendor!")
