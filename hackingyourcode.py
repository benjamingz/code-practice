import time
answer = input("What's the password? ")
while True:
    if answer.upper() == "FART" :
        print("Access Granted.")
        print("Loading secret information....")
        time.sleep(30)
        print("error :(")
        break
    else :
        print("Incorrect Password")
        answer = input()
