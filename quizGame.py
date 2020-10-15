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
# CurrentQuestion=random.randint(0,4)
CurrentQuestion=1
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
  if NumberofQuestion >10:
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
  t.write(str(NumberofQuestion)+'. Most species: ',align='center', font=style)
  t.hideturtle()
  # writes first question 1


  t.goto(-400,360)
  t.write('A.Are larger than 1 foot in lengthe',align='left', font=style)
  t.hideturtle()
  # writes first answer choice

  t.goto(-400,330)
  t.write('B.Live in tropical regions', align='left', font=style)
  t.hideturtle()
  # writes second answer choice

  t.goto(-400,300)
  t.write('C.Live in temperate regions', align='left', font=style)
  t.hideturtle()
  # writes third answer choice 



  # GATHER USER INPUT
  screen.listen()
  screen.onkey(wronganswer,"a")
  screen.onkey(wronganswer,"A")
  screen.onkey(rightanswer,"b")
  screen.onkey(rightanswer,"B")
  screen.onkey(wronganswer,"c")
  screen.onkey(wronganswer,"C")
 # tells how to identify right vs wrong by telling which one I put first in the

def askquestion2():
  # Question 2
  t.penup()
  t.goto(0, 400)
  t.color('blue')
  style=('Courier', 20, 'bold')
  t.write(str(NumberofQuestion)+'. Viruses are denied a kingdom of their own beacause?',align='center', font=style)
  t.hideturtle()
  # writes first question 1

  t.goto(-400,360)
  t.write('A.They are too poorly understood',align='left', font=style)
  t.hideturtle()
  # writes first answer choice

  t.goto(-400,330)
  t.write('B.They are too small', align='left', font=style)
  t.hideturtle()
  # writes second answer choice

  t.goto(-400,300)
  t.write('C.Their genetics cannot be determined', align='left', font=style)
  t.hideturtle()
  # writes third answer choice 


  t.goto(-400,270)
  t.write('D.They are not organisms', align='left', font=style)
  t.hideturtle()
  # writes fourth answer choice

  # GATHER USER INPUT
  screen.listen()
  screen.onkey(wronganswer, "a")
  screen.onkey(wronganswer, "A")
  screen.onkey(wronganswer, "b")
  screen.onkey(wronganswer, "B")
  screen.onkey(wronganswer, "c")
  screen.onkey(wronganswer, "C")
  screen.onkey(rightanswer, "d")
  screen.onkey(rightanswer, "D")
  # tells how to identify right vs wrong by telling which one I put first in the first block of code that I introduced this exact topic

def askquestion3():
  # Question 3
  t.penup()
  t.goto(0, 400)
  t.color('blue')
  style=('Courier', 20, 'bold')
  t.write(str(NumberofQuestion)+'. In the current taxonomic system, families are groupes into?',align='center', font=style)
  t.hideturtle()
  # writes first question 1

  t.goto(-400,360)
  t.write('A.Classes',align='left', font=style)
  t.hideturtle()
  # writes first answer choice

  t.goto(-400,330)
  t.write('B.Phyla', align='left', font=style)
  t.hideturtle()
  # writes second answer choice

  t.goto(-400,300)
  t.write('C.Orders', align='left', font=style)
  t.hideturtle()
  # writes third answer choice 


  t.goto(-400,270)
  t.write('D.Divisions', align='left', font=style)
  t.hideturtle()
  

  t.goto(-400,240)
  t.write('E.Kingdoms', align='left', font=style)
  t.hideturtle()
  # writes fourth answer choice

  # GATHER USER INPUT
  screen.listen()
  screen.onkey(wronganswer, "a")
  screen.onkey(wronganswer, "A")
  screen.onkey(wronganswer, "b")
  screen.onkey(wronganswer, "B")
  screen.onkey(rightanswer, "c")
  screen.onkey(rightanswer, "C")
  screen.onkey(wronganswer, "d")
  screen.onkey(wronganswer, "D")
  screen.onkey(wronganswer, "d")
  screen.onkey(wronganswer, "D")
  screen.onkey(wronganswer, "e")
  screen.onkey(wronganswer, "E")
  # tells how to identify right vs wrong by telling which one I put first in the first block of code that I introduced this exact topic

def askquestion4():
  # Question 4
  t.penup()
  t.goto(0, 400)
  t.color('blue')
  style=('Courier', 20, 'bold')
  t.write(str(NumberofQuestion)+'. Currently, scientists have named approximatley _ species.',align='center', font=style)
  t.hideturtle()
  # writes first question 1

  t.goto(-400,360)
  t.write('A.100,000',align='left', font=style)
  t.hideturtle()
  # writes first answer choice

  t.goto(-400,330)
  t.write('B.500,000', align='left', font=style)
  t.hideturtle()
  # writes second answer choice

  t.goto(-400,300)
  t.write('C.1,000,000', align='left', font=style)
  t.hideturtle()
  # writes third answer choice 

  t.goto(-400,270)
  t.write('D.1,500,000', align='left', font=style)
  t.hideturtle()

  t.goto(-400,240)
  t.write('E.10,000,000', align='left', font=style)
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
  screen.onkey(wronganswer, "e")
  screen.onkey(wronganswer, "E")
  # tells how to identify right vs wrong by telling which one I put first in the first block of code that I introduced this exact topic



def askquestion5():
  # Question 5
  t.penup()
  t.goto(0, 400)
  t.color('blue')
  style=('Courier', 16, 'bold')
  
  t.write(str(NumberofQuestion)+'. Taxonomy is best described as:',align='center', font=style)
  t.hideturtle()
  # writes question 5

  t.goto(-600,360)
  t.write('A.A method of scientifically naming species that never changes',align='left', font=style)
  t.hideturtle()
  # writes first answer choice

  t.goto(-600,330)
  t.write('B.Classifying organisms by biological traits, w/occassional revision', align='left', font=style)
  t.hideturtle()
  # writes second answer choice

  t.goto(-600,300)
  t.write('C.Preparing, and stuffing the skins of animals with lifelike effect', align='left', font=style)
  t.hideturtle()
  # writes third answer choice 


  t.goto(-600,270)
  t.write('D.The study of animal skeletons', align='left', font=style)
  t.hideturtle()
  # writes fourth answer choice

  # GATHER USER INPUT
  screen.listen()
  screen.onkeypress(wronganswer, "a")
  screen.onkeypress(wronganswer, "A")
  screen.onkeypress(rightanswer, "b")
  screen.onkeypress(rightanswer, "B")
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
  t.write(str(NumberofQuestion)+'. Which of the following is a kingdom classification?',align='center', font=style) 
  t.hideturtle()
  # writes question 6

  t.goto(-400,360)
  t.write('A.Plants',align='left', font=style)
  t.hideturtle()
  # writes first answer choice

  t.goto(-400,330)
  t.write('B.Animals', align='left', font=style)
  t.hideturtle()
  # writes second answer choice

  t.goto(-400,300)
  t.write('C.A & B', align='left', font=style)
  t.hideturtle()
  # writes third answer choice 


  t.goto(-400,270)
  t.write('D.Prosit', align='left', font=style)
  t.hideturtle()
  # writes fourth answer choice

  # GATHER USER INPUT
  screen.listen()
  screen.onkeypress(wronganswer, "a")
  screen.onkeypress(wronganswer, "A")
  screen.onkeypress(wronganswer, "b")
  screen.onkeypress(wronganswer, "B")
  screen.onkeypress(rightanswer, "c")
  screen.onkeypress(rightanswer, "C")
  screen.onkeypress(wronganswer, "d")
  screen.onkeypress(wronganswer, "D")
  # tells how to identify right vs wrong by telling which one I put first in the first block of code that I introduced this exact topic


def askquestion7():
  # Question 7
  t.penup()
  t.goto(0, 400)
  t.color('blue')
  style=('Courier', 20, 'bold')
  t.write(str(NumberofQuestion)+'. Which one of the following is NOT covered under Taxonomy?',align='center', font=style)
  t.hideturtle()
  # write question 7
  t.goto(-400,360)
  t.write('A. Alpha Taxonomy',align='left', font=style)
  t.hideturtle()
  # writes first answer choice

  t.goto(-400,330)
  t.write('B. Beta Taxonomy', align='left', font=style)
  t.hideturtle()
  # writes second answer choice

  t.goto(-400,300)
  t.write('C. Delta Taxonomy', align='left', font=style)
  t.hideturtle()
  # writes third answer choice 


  t.goto(-400,270)
  t.write('D. Gamma Taxonomy', align='left', font=style)
  t.hideturtle()
  # writes fourth answer choice

  # GATHER USER INPUT
  screen.listen()
  screen.onkeypress(wronganswer, "a")
  screen.onkeypress(wronganswer, "A")
  screen.onkeypress(wronganswer, "b")
  screen.onkeypress(wronganswer, "B")
  screen.onkeypress(rightanswer, "c")
  screen.onkeypress(rightanswer, "C")
  screen.onkeypress(wronganswer, "d")
  screen.onkeypress(wronganswer, "D")
  # tells how to identify right vs wrong by telling which one I put first in the first block of code that I introduced this exact topic


def askquestion8():
  # Question 8
  t.penup()
  t.goto(0, 400)
  t.color('blue')
  style=('Courier', 20, 'bold')
  t.write(str(NumberofQuestion)+'. What is the term given to a duplicate specimen of the original type?',align='center', font=style)
  t.hideturtle()
  # writes question 1
  t.goto(-400,360)
  t.write('A.Lectotype',align='left', font=style)
  t.hideturtle()
  # writes first answer choice

  t.goto(-400,330)
  t.write('B.Holotype', align='left', font=style)
  t.hideturtle()
  # writes second answer choice

  t.goto(-400,300)
  t.write('C.Isotype', align='left', font=style)
  t.hideturtle()
  # writes third answer choice 


  t.goto(-400,270)
  t.write('D.Neotype', align='left', font=style)
  t.hideturtle()
  # writes fourth answer choice

  # GATHER USER INPUT
  screen.listen()
  screen.onkeypress(wronganswer, "a")
  screen.onkeypress(wronganswer, "A")
  screen.onkeypress(wronganswer, "b")
  screen.onkeypress(wronganswer, "B")
  screen.onkeypress(rightanswer, "c")
  screen.onkeypress(rightanswer, "C")
  screen.onkeypress(wronganswer, "d")
  screen.onkeypress(wronganswer, "D")
  # tells how to identify right vs wrong by telling which one I put first in the first block of code that I introduced this exact topic


def askquestion9():
  # Question 9
  t.penup()
  t.goto(0, 400)
  t.color('blue')
  style=('Courier', 20, 'bold')
  t.write(str(NumberofQuestion)+'. What is the definition of classification?',align='center', font=style)
  t.hideturtle()
  # writes question 9 

  t.goto(-400,360)
  t.write('A.To organize a variety of items',align='left', font=style)
  t.hideturtle()
  # writes first answer choice

  t.goto(-400,330)
  t.write('B.A group of similar and closley related items', align='left', font=style)
  t.hideturtle()
  # writes second answer choice

  t.goto(-400,300)
  t.write('C.A set or category of things having some property or attribute in common and differentiated from others by kind, type, or quality.', align='left', font=style)
  t.hideturtle()
  # writes third answer choice 


  t.goto(-400,270)
  t.write('D.Scientists who classify animals into groups', align='left', font=style)
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






