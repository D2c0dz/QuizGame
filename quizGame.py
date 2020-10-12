import turtle
import time
import random
# References used:
# https://docs.python.org/3/library/turtle.html
# https://github.com/wynand1004/Projects/blob/master/Space%20Arena/space_arena_18.py
# https://stackoverflow.com/questions/34033701/python-how-to-reset-the-turtle-graphics-window#:~:text=position%2C%20etc.)-,turtle.,window%20to%20it's%20original%20state.
#
# REQUIREMENTS: python3, python3-tkinter, turtle, screen resolution = 1280 x 1024
# Author: Darin Dhiman
# TO DO:
#   enter more questions (10 total), end quiz after 5 questions, randomize questions

# GLOBAL VARIABLES ---------------------------------------------------------------
CurrentQuestion=random.randint(0,4)
NumberofQuestion=1
# uses the screen feature which is avalible in the turtle library for the question to be written on
screen = turtle.Screen()
# ensures that the screen will be that many pixles in hieght and width
screen.setup(1280,1024)
# FUNCTIONS-----------------------------------------------------------------------
def rightanswer():
  # call when user enters
  t.goto(30,30) 
  t.color('green')
  style=('Courier', 20, 'bold')
  t.write('CORRECT!',align='right', font=style)
  time.sleep(3)
  nextquestion()



  # call when user enters wrong answers
def wronganswer():
  # goes to that part in the screen
  t.goto(-30,-30) 
  # sets color
  t.color('red') 
  # sets the font, font size and font color
  style=('Courier', 20, 'bold') 
  # starts writing    
  t.write('INCORRECT!',align='center', font=style)
  time.sleep(3)
  nextquestion()

def nextquestion():
# when user put their answer clear the screen and call the next question
  # clears the screen for the next question
  screen.clearscreen()
  
  global CurrentQuestion, NumberofQuestion, QuestionBank
  
  screen.bgpic("taxonomy.gif")

  print("CurrentQuestion="+str(CurrentQuestion))
  print("NumberofQuestion="+str(NumberofQuestion))
  # print(str(QuestionBank[CurrentQuestion]))
  # make sure to only ask 5 questions
  if NumberofQuestion >5:
  # contains instrustions for what to do if it has already asked 5 questions  
    t.penup()
    t.goto(-30,-30)  
    style=('Courier', 35, 'bold') 
    t.write('GOODBYE. THANKS FOR PLAYING!',align='center', font=style)
    time.sleep(7)
    exit()

  else:
    # calls the askquestion functions from the questionbank list
    QuestionBank[CurrentQuestion]()
    # contains instrustions for what to do if it has not yet asked 5 questions
    CurrentQuestion=CurrentQuestion+1
    NumberofQuestion=NumberofQuestion+1
    

def askquestion1():
  t.goto(-175,0)
  t.goto(255,0)
  # Question 1
  t.penup()
  t.goto(0, 400)
  t.color('blue')
  style=('Courier', 20, 'bold')
  t.write(str(NumberofQuestion)+'. ASKQUESTION1  ,?',align='center', font=style)
  t.hideturtle()
  # writes first question 1

  t.goto(-400,360)
  t.write('a.asdfasdfsadfasdf',align='left', font=style)
  t.hideturtle()
  # writes first answer choice

  t.goto(-400,330)
  t.write('b.adf', align='left', font=style)
  t.hideturtle()
  # writes second answer choice

  t.goto(-400,300)
  t.write('c.dcfvgbhnjm', align='left', font=style)
  t.hideturtle()
  # writes third answer choice 

  t.goto(-400,270)
  t.write('d.sdxfvgnjmkl', align='left', font=style)
  t.hideturtle()
  # writes fourth answer choice

  # GATHER USER INPUT
  screen.listen()
  screen.onkey(rightanswer,"a")
  screen.onkey(rightanswer,"A")
  screen.onkey(wronganswer,"b")
  screen.onkey(wronganswer,"B")
  screen.onkey(wronganswer,"c")
  screen.onkey(wronganswer,"C")
  screen.onkey(wronganswer,"d")
  screen.onkey(wronganswer,"D")
  # tells how to identify right vs wrong by telling which one I put first in the

def askquestion2():
  # Question 2
  t.penup()
  t.goto(0, 400)
  t.color('blue')
  style=('Courier', 20, 'bold')
  t.write(str(NumberofQuestion)+'. ASKQUESTION2  ,?',align='center', font=style)
  t.hideturtle()
  # writes first question 1

  t.goto(-400,360)
  t.write('a.sdfsfgerfghj',align='left', font=style)
  t.hideturtle()
  # writes first answer choice

  t.goto(-400,330)
  t.write('b.ghirghaswedrftgh', align='left', font=style)
  t.hideturtle()
  # writes second answer choice

  t.goto(-400,300)
  t.write('c.edgufewqsdfgbht', align='left', font=style)
  t.hideturtle()
  # writes third answer choice 


  t.goto(-400,270)
  t.write('d.sdxrfdgthjnmkl', align='left', font=style)
  t.hideturtle()
  # writes fourth answer choice

  # GATHER USER INPUT
  screen.listen()
  screen.onkey(rightanswer, "a")
  screen.onkey(rightanswer, "A")
  screen.onkey(wronganswer, "b")
  screen.onkey(wronganswer, "B")
  screen.onkey(wronganswer, "c")
  screen.onkey(wronganswer, "C")
  screen.onkey(wronganswer, "d")
  screen.onkey(wronganswer, "D")
  # tells how to identify right vs wrong by telling which one I put first in the first block of code that I introduced this exact topic

def askquestion3():
  # Question 3
  t.penup()
  t.goto(0, 400)
  t.color('blue')
  style=('Courier', 20, 'bold')
  t.write(str(NumberofQuestion)+'. ASKQUESTION3  ,?',align='center', font=style)
  t.hideturtle()
  # writes first question 1

  t.goto(-400,360)
  t.write('a.sdfsfgerfghj',align='left', font=style)
  t.hideturtle()
  # writes first answer choice

  t.goto(-400,330)
  t.write('b.ghirghaswedrftgh', align='left', font=style)
  t.hideturtle()
  # writes second answer choice

  t.goto(-400,300)
  t.write('c.edgufewqsdfgbht', align='left', font=style)
  t.hideturtle()
  # writes third answer choice 


  t.goto(-400,270)
  t.write('d.sdxrfdgthjnmkl', align='left', font=style)
  t.hideturtle()
  # writes fourth answer choice

  # GATHER USER INPUT
  screen.listen()
  screen.onkey(rightanswer, "a")
  screen.onkey(rightanswer, "A")
  screen.onkey(wronganswer, "b")
  screen.onkey(wronganswer, "B")
  screen.onkey(wronganswer, "c")
  screen.onkey(wronganswer, "C")
  screen.onkey(wronganswer, "d")
  screen.onkey(wronganswer, "D")
  # tells how to identify right vs wrong by telling which one I put first in the first block of code that I introduced this exact topic

def askquestion4():
  # Question 4
  t.penup()
  t.goto(0, 400)
  t.color('blue')
  style=('Courier', 20, 'bold')
  t.write(str(NumberofQuestion)+'. ASKQUESTION4  ,?',align='center', font=style)
  t.hideturtle()
  # writes first question 1

  t.goto(-400,360)
  t.write('a.fcvfvhjh',align='left', font=style)
  t.hideturtle()
  # writes first answer choice

  t.goto(-400,330)
  t.write('b.asdfghjbgfddsffsghjk', align='left', font=style)
  t.hideturtle()
  # writes second answer choice

  t.goto(-400,300)
  t.write('c.edthejego dfgrtghimnt', align='left', font=style)
  t.hideturtle()
  # writes third answer choice 


  t.goto(-400,270)
  t.write('d.aswdddfchjk', align='left', font=style)
  t.hideturtle()
  # writes fourth answer choice

  # GATHER USER INPUT
  screen.listen()
  screen.onkey(rightanswer, "a")
  screen.onkey(rightanswer, "A")
  screen.onkey(wronganswer, "b")
  screen.onkey(wronganswer, "B")
  screen.onkey(wronganswer, "c")
  screen.onkey(wronganswer, "C")
  screen.onkey(wronganswer, "d")
  screen.onkey(wronganswer, "D")
  # tells how to identify right vs wrong by telling which one I put first in the first block of code that I introduced this exact topic



def askquestion5():
  # Question 5
  t.penup()
  t.goto(0, 400)
  t.color('blue')
  style=('Courier', 20, 'bold')
  t.write(str(NumberofQuestion)+'. ASKQUESTION5  ,?',align='center', font=style)
  t.hideturtle()
  # writes question 5

  t.goto(-400,360)
  t.write('a.xc vbnjkmm,',align='left', font=style)
  t.hideturtle()
  # writes first answer choice

  t.goto(-400,330)
  t.write('b.aq zsdxcfgvhjkl', align='left', font=style)
  t.hideturtle()
  # writes second answer choice

  t.goto(-400,300)
  t.write('c.fdfgvbhjk', align='left', font=style)
  t.hideturtle()
  # writes third answer choice 


  t.goto(-400,270)
  t.write('d.fvggcdfgh', align='left', font=style)
  t.hideturtle()
  # writes fourth answer choice

  # GATHER USER INPUT
  screen.listen()
  screen.onkeypress(rightanswer, "a")
  screen.onkeypress(rightanswer, "A")
  screen.onkeypress(wronganswer, "b")
  screen.onkeypress(wronganswer, "B")
  screen.onkeypress(wronganswer, "c")
  screen.onkeypress(wronganswer, "C")
  screen.onkeypress(wronganswer, "d")
  screen.onkeypress(wronganswer, "D")
  # tells how to identify right vs wrong by telling which one I put first in the first block of code that I introduced this exact topic



def askquestion6():
  # Question 6
  t.penup()
  t.goto(0, 400)
  t.color('blue')
  style=('Courier', 20, 'bold')
  t.write(str(NumberofQuestion)+'. ASKQUESTION6  ,?',align='center', font=style) 
  t.hideturtle()
  # writes question 6

  t.goto(-400,360)
  t.write('a.xc  xccx v cvxv cfv c,',align='left', font=style)
  t.hideturtle()
  # writes first answer choice

  t.goto(-400,330)
  t.write('b. jhhhhlokklgfhj', align='left', font=style)
  t.hideturtle()
  # writes second answer choice

  t.goto(-400,300)
  t.write('c.fagdgfhgjik,lkhggfgdefgf', align='left', font=style)
  t.hideturtle()
  # writes third answer choice 


  t.goto(-400,270)
  t.write('d.asygfjdnjifsdfhgfujrfednvdfjiudujnmng', align='left', font=style)
  t.hideturtle()
  # writes fourth answer choice

  # GATHER USER INPUT
  screen.listen()
  screen.onkeypress(rightanswer, "a")
  screen.onkeypress(rightanswer, "A")
  screen.onkeypress(wronganswer, "b")
  screen.onkeypress(wronganswer, "B")
  screen.onkeypress(wronganswer, "c")
  screen.onkeypress(wronganswer, "C")
  screen.onkeypress(wronganswer, "d")
  screen.onkeypress(wronganswer, "D")
  # tells how to identify right vs wrong by telling which one I put first in the first block of code that I introduced this exact topic


def askquestion7():
  # Question 7
  t.penup()
  t.goto(0, 400)
  t.color('blue')
  style=('Courier', 20, 'bold')
  t.write(str(NumberofQuestion)+'. ASKQUESTION7  ,?',align='center', font=style)
  t.hideturtle()
  # write question 7
  t.goto(-400,360)
  t.write('a.qzsacf rdexwa,',align='left', font=style)
  t.hideturtle()
  # writes first answer choice

  t.goto(-400,330)
  t.write('b. dfjgufdhgndjx', align='left', font=style)
  t.hideturtle()
  # writes second answer choice

  t.goto(-400,300)
  t.write('c.wf yhtg6e4rf5,546y', align='left', font=style)
  t.hideturtle()
  # writes third answer choice 


  t.goto(-400,270)
  t.write('d.2e s c6hgty7ufvbvr gjjur', align='left', font=style)
  t.hideturtle()
  # writes fourth answer choice

  # GATHER USER INPUT
  screen.listen()
  screen.onkeypress(rightanswer, "a")
  screen.onkeypress(rightanswer, "A")
  screen.onkeypress(wronganswer, "b")
  screen.onkeypress(wronganswer, "B")
  screen.onkeypress(wronganswer, "c")
  screen.onkeypress(wronganswer, "C")
  screen.onkeypress(wronganswer, "d")
  screen.onkeypress(wronganswer, "D")
  # tells how to identify right vs wrong by telling which one I put first in the first block of code that I introduced this exact topic


def askquestion8():
  # Question 8
  t.penup()
  t.goto(0, 400)
  t.color('blue')
  style=('Courier', 20, 'bold')
  t.write(str(NumberofQuestion)+'. ASKQUESTION8  ,?',align='center', font=style)
  t.hideturtle()
  # writes question 1
  t.goto(-400,360)
  t.write('a.sofjmdkfmdskmd',align='left', font=style)
  t.hideturtle()
  # writes first answer choice

  t.goto(-400,330)
  t.write('b. sdjmfgndxjfnj', align='left', font=style)
  t.hideturtle()
  # writes second answer choice

  t.goto(-400,300)
  t.write('c.z,dfsnmihjughfsjudegbhvnjfb vf', align='left', font=style)
  t.hideturtle()
  # writes third answer choice 


  t.goto(-400,270)
  t.write('d.jdfgher vhjdsffbnvyhsdfgh', align='left', font=style)
  t.hideturtle()
  # writes fourth answer choice

  # GATHER USER INPUT
  screen.listen()
  screen.onkeypress(rightanswer, "a")
  screen.onkeypress(rightanswer, "A")
  screen.onkeypress(wronganswer, "b")
  screen.onkeypress(wronganswer, "B")
  screen.onkeypress(wronganswer, "c")
  screen.onkeypress(wronganswer, "C")
  screen.onkeypress(wronganswer, "d")
  screen.onkeypress(wronganswer, "D")
  # tells how to identify right vs wrong by telling which one I put first in the first block of code that I introduced this exact topic


def askquestion9():
  # Question 9
  t.penup()
  t.goto(0, 400)
  t.color('blue')
  style=('Courier', 20, 'bold')
  t.write(str(NumberofQuestion)+'. ASKQUESTION9  ,?',align='center', font=style)
  t.hideturtle()
  # writes question 9 

  t.goto(-400,360)
  t.write('a.xc  xccx v retgretrewg cfv c,',align='left', font=style)
  t.hideturtle()
  # writes first answer choice

  t.goto(-400,330)
  t.write('b. jhhreghj', align='left', font=style)
  t.hideturtle()
  # writes second answer choice

  t.goto(-400,300)
  t.write('c.ghjmk,o', align='left', font=style)
  t.hideturtle()
  # writes third answer choice 


  t.goto(-400,270)
  t.write('d.hfcnvx jkmbgu', align='left', font=style)
  t.hideturtle()
  # writes fourth answer choice

  # GATHER USER INPUT
  screen.listen()
  screen.onkeypress(rightanswer, "a")
  screen.onkeypress(rightanswer, "A")
  screen.onkeypress(wronganswer, "b")
  screen.onkeypress(wronganswer, "B")
  screen.onkeypress(wronganswer, "c")
  screen.onkeypress(wronganswer, "C")
  screen.onkeypress(wronganswer, "d")
  screen.onkeypress(wronganswer, "D")
  screen.onkeypress(nextquestion,"n")
  # tells how to identify right vs wrong by telling which one I put first in the first block of code that I introduced this exact topic


def askquestion10():
  screen.bgpic('taxfiles.gif')
  # Question 10
  t.penup()
  t.goto(0, 400)
  t.color('blue')
  style=('Courier', 20, 'bold')
  t.write(str(NumberofQuestion)+'. ASKQUESTION10  ,?',align='center', font=style)
  t.hideturtle()
  # writes question 10

  t.goto(-400,360)
  t.write('a.xc  xccx v cvxv cfv c,',align='left', font=style)
  t.hideturtle()
  # writes first answer choice

  t.goto(-400,330)
  t.write('b. jhhhhlokklgfhj', align='left', font=style)
  t.hideturtle()
  # writes second answer choice

  t.goto(-400,300)
  t.write('c.fagdgfhgjik,lkhggfgdefgf', align='left', font=style)
  t.hideturtle()
  # writes third answer choice 


  t.goto(-400,270)
  t.write('d.asygfjdnjifsdfhgfujrfednvdfjiudujnmng', align='left', font=style)
  t.hideturtle()
  # writes fourth answer choice

  # GATHER USER INPUT
  screen.listen()
  screen.onkeypress(rightanswer, "a")
  screen.onkeypress(rightanswer, "A")
  screen.onkeypress(wronganswer, "b")
  screen.onkeypress(wronganswer, "B")
  screen.onkeypress(wronganswer, "c")
  screen.onkeypress(wronganswer, "C")
  screen.onkeypress(wronganswer, "d")
  screen.onkeypress(wronganswer, "D")
  # tells how to identify right vs wrong by telling which one I put first in the first block of code that I introduced this exact topic
  



 

#MAIN PROGRAM---------------------------------------------------
# this is a list containing the different functions that ask the questions.
QuestionBank=[askquestion1, askquestion2, askquestion3, askquestion4, askquestion5, askquestion6, askquestion7, askquestion8, askquestion9, askquestion10] 
# creates an instance of turtle so it can write the question and answer options
t=turtle.Turtle()
# start asking questions 
nextquestion()
# runs the application in a loop
screen.mainloop()






