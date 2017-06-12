# Troublshooting - Version 1
# - Series of troubleshooting questions asked

print("Welcome to the generic trouble shooter for a mobile phone.")

print("Does your phone have signal?")
answer = input(">> ")
if answer.upper() == "YES":
    print("Your SIM card must be inserted.")
    input()
    exit(0)
    
print("Have you dropped your phone?")
answer = input(">> ")
if answer.upper() == "YES":
    print("What a muppet.  You'll need to get that fixed.")
    input()
    exit(0)

print("Has your phone suffered water damage?")
answer = input(">> ")
if answer.upper() == "YES":
    print("A jar of rice will fix that!")
    input()
    exit(0)

print("Uh oh, we have no solution.  Go back to your vendor!")
