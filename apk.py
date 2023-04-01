import tkinter as tk

class App:
  def __init__(self, master):
    self.master = master
    master.title("Hello World")

    self.label = tk.Label(master, text="Hello World!")
    self.label.pack()

    self.greet_button = tk.Button(master, text="Greet", command=self.greet)
    self.greet_button.pack()

    self.close_button = tk.Button(master, text="Close", command=master.quit)
    self.close_button.pack()

  def greet(self):
    print("Hello!")

root = tk.Tk()
app = App(root)
root.mainloop()