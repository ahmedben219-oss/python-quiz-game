from Logins import signup
from Logins import login
from Game import start_quiz


print("=" * 40)
print("WELCOME TO THE ULTIMATE QUIZ")
print("=" * 40)

print("1. Log In ")
print("2. Sign Up")
print("3. Quit")
choice = input(" Please Choose Option 1 or 2 To Sign Up or Log In:  ")

if choice == "1":
    login()
elif choice == "2":
    signup()
elif choice == "3":
    quit
else:
    print("thats not an option")