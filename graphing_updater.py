import tkinter as tk
import matplotlib.pyplot as plt
import numpy as np
import matplotlib
matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter.font as tkFont
from tkinter import StringVar, Label

'''
A basic visualization of how changing coefficients and exponents can affect the curvature of a graph.
'''

class GraphUtil(tk.Frame):
   def __init__(self, master=None):
      tk.Frame.__init__(self, master)
      self.create_canvas()



   def create_canvas(self):
      figure = plt.figure(figsize=(4.5, 4.5))
      axes = figure.add_axes([0.15, 0.15, 0.65, 0.56])
      canvas = FigureCanvasTkAgg(figure, master=main)
      canvas.get_tk_widget().grid(row=7, column=0, columnspan=4)

      x = np.arange(-5, 5, 0.005)
      initial_func = x
      axes.plot(x, initial_func)



      self.graph_button=tk.Button(master=main, text="Plot", command=lambda: self.update_graph(canvas, axes),
                                  height=2, width=5)
      self.graph_button.grid(row=6, column=0, columnspan=4)
      self.input_button=tk.Entry(master=main)
      self.input_button.grid(row=4, column=2)
      self.input_button2=tk.Entry(master=main)
      self.input_button2.grid(row=3, column=2)
      self.text=tk.Label(text="As you increase the exponent, the graph becomes flatter on the x-axis. ")
      self.text.grid(row=8, column=0, columnspan=4)
      self.text2 = tk.Label(text="As you increase the coefficient, "
                                 "the graph becomes less flat, seen by the function's range increasing.")
      self.text2.grid(row=9, column=0, columnspan=4)

      self.label1=StringVar()
      self.label1.set("Enter coefficient: ")
      self.label11=Label(main, textvariable=self.label1, height=4)
      self.label11.grid(row=3, column=1)
      self.label2=StringVar()
      self.label2.set("Enter exponent: ")
      self.label22=Label(main, textvariable=self.label2, height=4)
      self.label22.grid(row=4, column=1)


      self.uptext=tk.Label(text="Visualizing Curve Flattening", font=fontStyle)
      self.uptext.grid(row=0, column=0, columnspan=4)
      self.uptext2=tk.Label(text="With Changing Exponents and Coefficients", font=fontStyle)
      self.uptext2.grid(row=1, column=0, columnspan=4)
      self.blank=tk.Label(text="", font=fontStyle)
      self.blank.grid(row=2, column=1)
      self.blank2=tk.Label(text="", font=fontStyle)
      self.blank2.grid(row=5, column=1)
      self.blank3=tk.Label(text="", font=fontStyle)
      self.blank3.grid(row=10, column=1)


   def update_graph(self, canvas, axes):
      new_num = self.input_button.get()
      new_coef = self.input_button2.get()

      if new_coef == '':
         new_coef = 1

      if new_num == '':
         new_num = 1

      new_num = int(new_num)
      new_coef = int(new_coef)

      axes.clear()

      new_coef_1 = new_coef

      if new_coef == 1:
         new_coef_1 = ''

      string_print = "%sx^%s" % (new_coef_1, new_num)



      for num in range(10):
         value = np.arange(0, 5, 0.005)
         def func(x):
            # Troubleshooting: un-comment the following --> print(x**new_num)
            return new_coef * x ** new_num

         axes.plot(value, func(value))
         axes.legend([string_print])
         canvas.draw()

main = tk.Tk()
main.wm_title("Visualizing Curve Flattening")
fontStyle = tkFont.Font(family="Lucida Grande", size=30)
app=GraphUtil(master=main)
app.mainloop()







