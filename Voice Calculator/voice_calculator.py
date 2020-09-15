'''
This is a numerical calculator which is voice enabled, intended for the visually impaired.
You can enter numerical calculations with multiple terms, and it works through the order of operations correctly. 
v1.0 - Voice-controlled calculator with support for basic four-function calculators, exponents, and parenthesis.
CURRENT: v1.1 - Fixed a bug with the mathematical calculations, and simplified it slightly.
'''

import sys
import math
import tkinter as tk
import operator

#TODO: Add functionality for larger numbers and nested parenthesis.

'''
How to Run:
You will need the speechrecognition, pyttsx3, and pyaudio modules.
You will be prompted to speak, but wait until "speak" appears in the console until you start speaking.
Currently, the calculator doesn't support nested parenthesis and may run into an error with large exponents, 
but it can run most numerical calculations aside from that.
For example, try saying "six times four divded by parenthesis two plus three parenthesis". The program should output 4.8. 
Have Fun!
'''

try:
   import speech_recognition as sr
except ImportError:
   print("No module named speech_recognition found.")
try:
   import pyttsx3
except ImportError:
   print("No module named pyttsx3 found.")
try:
   from googlesearch import search
except ImportError:
   print("No module named google found.")

engine = pyttsx3.init()
engine.setProperty('rate', 195)
engine.setProperty('volume', 0.8)
voices = engine.getProperty('voices')
voice_id = 'com.apple.speech.synthesis.voice.daniel' #Voice can be changed to fit preference.
engine.setProperty('voice', voice_id)

recording = sr.Recognizer()
mic = sr.Microphone()

with sr.Microphone() as source:
   engine.say("Hello. What do you want me to solve?")
   engine.runAndWait()
   print('speak')
   recording.adjust_for_ambient_noise(source)
   audio = recording.listen(source)
   user_input = recording.recognize_google(audio)

def convert_math_op(input_list):
   list = input_list

   tracker = -1
   for item in list:
      tracker += 1
      try:
         float(item)
         if float(item):
            list[tracker] = float(list[tracker])
      except ValueError:
         pass

   min_tracker = -1
   for item in list:
      min_tracker += 1
      if item != list[-1]:
         print(item)
         if not isinstance(item, float):
            print(item)
            print(min_tracker)
            if not isinstance(list[min_tracker+1], float):
               if list[min_tracker+1] != "(":
                  engine.say("That isn't a valid mathematical operation. Please Try Again.")
                  engine.runAndWait()
                  sys.exit(0)
   if isinstance(list[-1], str):
      if not list[-1] == ")":
         engine.say("That isn't a valid mathematical operation. Please Try Again.")
         engine.runAndWait()
         sys.exit(0)

   return list

u = user_input
u = u.split( )

tracker0 = -1
for item in u:
   tracker0 += 1
   if item == "x":
      u[tracker0] = "*"

uf = []

for item in u:
   try:
      float(item)
      if float(item):
         uf.append(float(item))
   except ValueError:
      if len(item) > 1:
         if item == "minus":
            item = '-'
            uf.append(item)
         elif item == "plus":
            item = '+'
            uf.append(item)
         elif item == "power of":
            item = "^"
            uf.append(item)
         elif item == "powerof":
            item = "^"
            uf.append(item)
         else:
            r = [str(x) for x in item]
            for value in r:
               try:
                  float(value)
                  if float(value):
                     uf.append(float(value))
               except ValueError:
                  uf.append(value)
      else:
         uf.append(item)

if isinstance(uf[0], str):
   if uf[0] != "(":
      engine.say("That is not a valid mathematical operation. Please Try Again.")
      engine.runAndWait()

print(uf)
uz = uf.copy()

uf = convert_math_op(uf)

def determine_operator(input):
   operations = {
      "+": operator.add,
      "-": operator.sub,
      "*": operator.mul,
      "/": operator.truediv,
      "^": operator.pow
   }
   oper = operations[input]

   return oper

def find_occurence(input, list):
   list = list
   result = []

   off = -1
   while True:
      try:
         off = list.index(input, off+1)
      except ValueError:
         return result
      result.append(off)

def do_math(input):
   list = input
   if list[0] == "(":
      list = list[1:-1]
   local_tracker = -1
   for value in list:
      local_tracker += 1
      try:
         int(value)
      except ValueError:
         q = determine_operator(value)
         list[local_tracker] = q

   print(list)

   #Order of Operations

   exp = find_occurence(operator.pow, list)
   for index in exp:
      ans = list[int(index) - 1] ** list[int(index) + 1]
      list[index-1:index+2] = [ans]

   print(list)
   mul = find_occurence(operator.mul, list)
   div = find_occurence(operator.truediv, list)
   muldiv = mul + div
   muldiv.sort()
   q = True
   if not muldiv:
      q = False
   while q == True:
      index = muldiv[0]
      if index in mul:
         ans = list[int(index) - 1] * list[int(index) + 1]
         list[index - 1:index + 2] = [ans]
      if index in div:
         ans = (list[int(index) - 1] / list[int(index) + 1])
         list[index - 1:index + 2] = [ans]
      list = list

      mul = find_occurence(operator.mul, list)
      div = find_occurence(operator.truediv, list)
      muldiv = mul + div
      muldiv.sort()
      muldiv = muldiv

      if not muldiv:
         q = False

   add = find_occurence(operator.add, list)
   sub = find_occurence(operator.sub, list)
   addsub = add + sub
   addsub.sort()
   r = True
   if not addsub:
      r = False
   while r == True:
      index = addsub[0]
      if index in add:
         ans = list[int(index) - 1] + list[int(index) + 1]
         list[index - 1:index + 2] = [ans]
      if index in sub:
         ans = (list[int(index) - 1] - list[int(index) + 1])
         list[index - 1:index + 2] = [ans]
      list = list

      add = find_occurence(operator.add, list)
      sub = find_occurence(operator.sub, list)
      addsub = add + sub
      addsub.sort()
      addsub = addsub

      if not addsub:
         r = False

   return list

tracker = -1

par = find_occurence("(", uf)
print(par)
run = True

if not par:
   run = False

while run == True:
   item = par[0]
   tracker = item
   tracker2 = tracker - 1
   for item in uf[::]:
      tracker2 += 1
      if item == ")":
         print(tracker)
         print(tracker2)
         res = do_math(uf[tracker:tracker2])
         uf[tracker:tracker2] = [res]

   par = find_occurence("(", uf)

   if not par:
      run = False

tracker3 = -1
for item in uf:
   tracker3 += 1
   if isinstance(item, list):
      z = [float(x) for x in item]
      f = z[0]
      uf[tracker3] = f

def check_mul(input):
   new_list = input

   def find_next(list):
      list = list
      tot = []

      track = -1
      max = len(list)-1
      for item in list:
         track += 1
         if track != max:
            if isinstance(item, float):
               if isinstance((list[track+1]), float):
                  tot.append(track)

      return tot

   mult = find_next(input)
   run = True
   if not mult:
      run = False
   while run == True:
      item = mult[0]
      ans = new_list[item] * new_list[item + 1]

      new_list[item:item+2] = [ans]

      mult = find_next(input)
      if not mult:
         run = False

   return new_list


print(check_mul(uf))
uf = check_mul(uf)
print(do_math(uf))

answer = uf[0]
if answer.is_integer():
   answer = int(answer)

print(answer)
answer = str(answer)

dict = {
   "x": "times",
   "*": "times",
   "X": "times",
   "+": "plus",
   "-": "minus",
   "/": "divided by",
   "(": "parenthesis",
   ")": "parenthesis"
}

user_result = []

for item in uz:
   if isinstance(item, float):
      if item.is_integer():
         user_result.append(str(int(item)))
   elif isinstance(item, str):
      user_result.append(dict[item])

user_init = ' '.join(user_result)
print(user_init)

engine.say("The answer to " + user_init + " is " + str(answer))
engine.runAndWait()

















