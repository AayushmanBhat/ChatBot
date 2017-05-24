import re
from tkinter import *
import speech_recognition as sr
from gtts import gTTS
import os
import json
from introductionState import myfunc1
from orderState import myfunc2
from suggestionstate import myfunc3
from reviewstate import myfunc4
from confirmstate import myfunc5



state=1
statedict={0:"--",1:"introduction",2:"ordering",3:"reviewing",4:"cancellation",5:"checkout",6:"confirmation",7:"suggestion7"}


def get_state():
    return statedict[state]

def update_state(user_input):
    #update the status
    return
def tts(callback):
    tts = gTTS(text=callback, lang='en')
    tts.save("good.mp3")
    os.system("mpg321 good.mp3")

def stt():
    r = sr.Recognizer()
    with sr.Microphone() as source:
              print("Say something!")
              audio = r.listen(source)

    try:
              
              print("Google Speech Recognition thinks you said " + r.recognize_google(audio))
              print(r.recognize_google(audio))
              label = Label(frame, text="User: "+r.recognize_google(audio),bg="red")
              input_user.set('')
              label.pack()
              generate_reply(r.recognize_google(audio))   
    except sr.UnknownValueError:
              print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
              print("Google Speech Recognition service is offline".format(e))

    
#load_dataset()
window = Tk()
input_user = StringVar()
b1=Button(window,text="Text to Speech",command=tts)
b2=Button(window,text="Speech to Text",command=stt)
b1.pack(side=BOTTOM)
b2.pack(side=BOTTOM)
input_field = Entry(window, text=input_user)
input_field.pack(side=BOTTOM, fill=X)

def myfunction(event):
    canvas.configure(scrollregion=canvas.bbox("all"),width=400,height=400)

def enter_pressed(event):
    global state
    input_get = input_field.get()
    print(input_get)
    label = Label(frame, text="User: "+input_get,bg="red")
    input_user.set('')
    label.pack()
    print("part1")
    if state==1:
              txt,state=myfunc1(input_get)
    elif state==2:
              
	      txt,state=myfunc2(input_get)
              
    elif state==3:
	      txt,state=myfunc4(input_get)
    
    elif state==6:
	      txt,state=myfunc5(input_get)
    else:
	      txt,state=myfunc3(input_get)
    
    print(state)
  
    generate_reply(txt)
    return "break"

def generate_reply(txt):
    
    label = Label(frame, text="Bot("+get_state()+"): "+txt,bg="blue")
    callback=txt
    tts(txt)
    update_state(txt)
    label.pack()

frame = Frame(window, width=600, height=600)
frame.pack_propagate(False) # prevent frame to resize to the labels size

canvas=Canvas(frame)
myscrollbar=Scrollbar(frame,orient="vertical",command=canvas.yview)
canvas.configure(yscrollcommand=myscrollbar.set)

myscrollbar.pack(side="right",fill="y")
canvas.create_window((0,0),window=frame,anchor='nw')
frame.bind("<Configure>",myfunction)
input_field.bind("<Return>", enter_pressed)
frame.pack()

window.mainloop()
