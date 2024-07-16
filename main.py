from turtle import Turtle,Screen
import random

screen = Screen()


###################### challenge - Turtle Race ######################

screen.setup(width = 500, height = 400)
userBet = screen.textinput(title = "Make your bet", prompt = "Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

race = False
all_turtle_object = []

a = 0 
for y in range(-80, 121, 40):
  t = Turtle(shape = "turtle")
  t.color(colors[a])
  a= a+1
  t.penup()
  t.setposition(x = -230, y = y)
  all_turtle_object.append(t)

if userBet:
  race = True

while race == True:
  for i in all_turtle_object:
    random_range = random.randint(0, 10)
    i.forward(random_range)
    if i.xcor() > 220:
      race = False
      winning_t_color = i.pencolor()

      if userBet == winning_t_color:
        print(f"You won! {winning_t_color} turtle won the race.")
      else:
        print(f"You lost! {winning_t_color} turtle won the race.")

    
  

screen.exitonclick()