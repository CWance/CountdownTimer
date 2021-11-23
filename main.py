import time
import turtle
import os

#makes the screen that pops up
from tkinter import messagebox

wn = turtle.Screen()
wn.title(" Final Countdown Timer")
wn.bgcolor("black")
wn.screensize()
wn.setup(width=400, height=200)
wn.tracer()

#displays the timer
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.goto(0, 0)
pen.penup()
pen.hideturtle()

def countdown():
    #opens a pop up to enter an input
    enter_time = turtle.textinput("Enter the time in seconds: ", "")
    t = int(enter_time)
    while t:
        #converts the input to minutes and seconds
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        if t == 28:
            #changes the color of the timer
            pen.color("red")
            #plays a soundbite when it gets to the time
            os.system('aplay last_countdown.wav&')
        #removes the pen
        pen.clear()
        #adds the pen
        pen.write("{}".format(timer), align="center", font=("Courier", 60, "normal"))

        time.sleep(1)
        t -= 1
    #displays the ending message, stopping the screen from closing
    messagebox.showinfo("", "Timer completed")


countdown()