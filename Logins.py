from Game import start_quiz
def signup():
    while True:
        lines = open("logins.txt").read().split("\n")
        user = input("Please create a username: ")
        username_taken = False
        for line in lines:
            if line.strip() == "":
                continue
            parts = line.split(",")
            username = parts[0]
            if user == username:
                username_taken = True
        if username_taken:
            print("Sorry that username is taken")
        else:
            break
    print("Username",user, "is available!")
    password = input("Please enter a password, Don't forget it: ")
    new_line = user.strip() + "," + password.strip() + ",0\n"

    with open("logins.txt", "a") as New_Account:
        New_Account.write(new_line)

def login():
    print("\n")
    print("Welcome Back, please sign in below")
    print("\n")
    user = input("Please input your username: ")
    password = input("Please enter your password: ")
    lines1 = open("logins.txt").read().split("\n")
    for lines in lines1:
        if lines.strip() == "":
            continue
        parts = lines.split(",")
        if user == parts[0].strip() and password == parts[1].strip():
            start_quiz(user, int(parts[2]) )
            return

    print("Incorrect Username Or Password")
    return None, None
