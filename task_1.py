# Troublshooting - Version 2.1
# - Each question to accept either YES or NO answer
# - - Accept a range of suitable inputs.

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

print("Welcome to the generic trouble shooter for a mobile phone.")

print("Does your phone have signal?")
if inputYN():
    print("Your SIM card must be inserted.")
    input()
    exit(0)
    
print("Have you dropped your phone?")
if inputYN():
    print("What a muppet.  You'll need to get that fixed.")
    input()
    exit(0)

print("Has your phone suffered water damage?")
if inputYN():
    print("A jar of rice will fix that!")
    input()
    exit(0)

print("Uh oh, we have no solution.  Go back to your vendor!")
