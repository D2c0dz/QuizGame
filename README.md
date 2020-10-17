# QuizGame

Anyone can use my quizGame program.  It is a quizzing engine that they could customize to meet their needs.  It could be used to prepare for a test, or just to create a fun quiz game.

# Game Requirements:
In order to run my quiz game program following are required:
 * Python Libraries: 
   * Turtle (may require Tkinter, depending on your setup)
   * Random
   * Time
 * Monitor that supports a screen resolution of 1280 x 1024
 * Python3

# How the Game is coded:
There are some global variables that need to be used by the functions to keep track of things:
   * Score, this global variable will start at 0 and increment by 1 everytime someone gets an answer correct.
   * NumberofQuestion, this global variable will cause the first question to be labled as question 1 and will increment by 1 each time someone answers a question
   * CurrentQuestion, this global variable will store a number of index to pull from the QuestionBank[]. It will increment by 1 every time someone answers a question.
   * The QuestionBank[] global variable contains is a list of all of the question function names
  
The main section of the code will actually start the program, as everything else is mostly functions to use.

# Functions:
   * Each question is its own function, for example Question1()
   * NextQuestion()
        * this function clears the screen when each question has been answered and asks the next question which is decided by CurrentQuestion variable. It also contains an if statement so that it dosen't ask all the questions listed in the QuestionBank[], and when 5 questions are asked it will end the game and display the score and say goodbye
   * askquestion1(), askquestion2(), ... - these contain the question text, prints the question, and has logic to check for the right answer 
   * rightanswer() - this function contains instructions on what to-do if the player gets the answer right
   * wronganswer() - this function contains instructions on what to-do if the player gets the answer wrong

# Playing the Quiz Game:
This app can be downloaded for free on github. To run the code on terminal you will need to type in "cd QuizGame" and hit enter. Then type "python3 quizGame.py". In order to play this game, you can press the letter on the keyboard that is the same letter as the answer you think is correct. It will automatically move on to the next question after that.
