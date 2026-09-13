import random
def start_quiz(username, high_score):
    quiz = open("questions.txt").read().split("---") # opens and splits the whole txt file into the questions on their own
    random.shuffle(quiz) 
    score = 0
    print("\n")
    print("Login Succesful, Let's Get Ready To Play")
    print("\n")


    for x in quiz[:10]:
        questions = x.split("And your answer is: ")
        User_Answer = input(questions[0]).upper()
        FullAnswerText = questions[1]
        answer = FullAnswerText.split("Answer is ")[-1].strip()
        print(f"You answered {User_Answer} | Correct Answer is {answer}")
        if User_Answer == answer:
            print("correct")
            score += 1
        else:
            print("wrong")
            score += 0

    print("Your final score is: ",score)
    if score > high_score:
        print("Congratulations on your new high score of ",score)
        update_high_score(username, score)

def update_high_score(username, score):
    lines_updated = []
    high_scoreData = open("logins.txt").read().split("\n")
    for lines in high_scoreData:
        if lines.strip() == "":
            continue
        parts = lines.split(",")
        if username == parts[0]:
            new_line = parts[0] + "," + parts[1] + "," + str(score)
        else:
            new_line = lines
        lines_updated.append(new_line)
    with open("logins.txt", "w") as f:
        for line in lines_updated:
            f.write(line + "\n")



