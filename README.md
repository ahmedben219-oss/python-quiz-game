PYTHON QUIZ GAME

This is a terminal based quiz game made in python with several different features, including user accounts, randomized questions and a high score system.

HOW TO MAKE THE GAME WORK:
- RUN TitlePage.py


FEATURES - 
- Account System, users have to sign up and log in, in order to play the game so that we can save the game. Their usernames and passwords are then saved in a text file and when they log in we check against the file in which we have their logins.
- Randomized quiz, in my questions.txt file, we have a database filled with around 30 questions in which we choose 10 for the user to answer and the list is randomized anyway so it'll never be the same questions in a row.
- File-based Data Handling, Their usernames, passwords and high scores are saved in a text file in which we check against when we do update their high score or even when we grab and randomize questions for our user to answer. 

PROJECT STRUCTURE
- TitlePage.py = This is the main starting point of the game, it displays the menu and directs you to sign in
- Logins.py = This file handles the account creation, opening up the file and writing new accounts or simply just checking against it when you are trying to Sign in
- Game.py =  This is the main game file for the quiz, allows it to keep score while also getting the questions for user to answer and checking if they're right
- Questions.txt = This is where the questions are stored.

WHAT I LEARNT:
- For me it allowed me to strengthen even further my understanding of data handling, working with bugs in my code around file reading/writing and being able to connect multiple files together.In general it was a good boost to test my understanding of python.