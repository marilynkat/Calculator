#  /$$$$$$            /$$                     /$$             /$$                        
# /$$__  $$          | $$                    | $$            | $$                        
#| $$  \__/  /$$$$$$ | $$  /$$$$$$$ /$$   /$$| $$  /$$$$$$  /$$$$$$    /$$$$$$   /$$$$$$ 
#| $$       |____  $$| $$ /$$_____/| $$  | $$| $$ |____  $$|_  $$_/   /$$__  $$ /$$__  $$
#| $$        /$$$$$$$| $$| $$      | $$  | $$| $$  /$$$$$$$  | $$    | $$  \ $$| $$  \__/
#| $$    $$ /$$__  $$| $$| $$      | $$  | $$| $$ /$$__  $$  | $$ /$$| $$  | $$| $$      
#|  $$$$$$/|  $$$$$$$| $$|  $$$$$$$|  $$$$$$/| $$|  $$$$$$$  |  $$$$/|  $$$$$$/| $$      
# \______/  \_______/|__/ \_______/ \______/ |__/ \_______/   \___/   \______/ |__/      
                                                                                  
import tkinter

calc = tkinter.Tk()
calc.title('Calculator')

#Addition function
def add():
    #Save value from textbox input
    inputValue=textbox.get("1.0","end-1c")

    #Place inputs that are separated by comma into list
    list = inputValue.split(',')
    num1 = int(list[0])
    num2 = int(list[1])
    result = num1 + num2

    #Clear textbox
    textbox.delete('1.0', tkinter.END)

    #Display result in textbox
    textbox.insert(tkinter.END, result)
    textbox.see(tkinter.END)

#Subtraction function
def subtract():
    #Save value from textbox input
    inputValue=textbox.get("1.0","end-1c")

    #Place inputs that are separated by comma into list
    list = inputValue.split(',')
    num1 = int(list[0])
    num2 = int(list[1])
    result = num1 - num2

    #Clear textbox
    textbox.delete('1.0', tkinter.END)

    #Display result in textbox
    textbox.insert(tkinter.END, result)
    textbox.see(tkinter.END)

#Divide function
def divide():
    #Save value from textbox input
    inputValue=textbox.get("1.0","end-1c")

    #Place inputs that are separated by comma into list
    list = inputValue.split(',')
    num1 = int(list[0])
    num2 = int(list[1])
    result = num1 // num2

    #Clear textbox
    textbox.delete('1.0', tkinter.END)

    #Display result in textbox
    textbox.insert(tkinter.END, result)
    textbox.see(tkinter.END)

#Multiplication function
def multiply():
    #Save value from textbox input
    inputValue=textbox.get("1.0","end-1c")

    #Place inputs that are separated by comma into list
    list = inputValue.split(',')
    num1 = int(list[0])
    num2 = int(list[1])
    result = num1 * num2

    #Clear textbox
    textbox.delete('1.0', tkinter.END)

    #Display result in textbox
    textbox.insert(tkinter.END, result)
    textbox.see(tkinter.END)

#Modulus function
def mod():
    #Save value from textbox input
    inputValue=textbox.get("1.0","end-1c")

    #Place inputs that are separated by comma into list
    list = inputValue.split(',')
    num1 = int(list[0])
    num2 = int(list[1])
    result = num1 % num2

    #Clear textbox
    textbox.delete('1.0', tkinter.END)

    #Display result in textbox
    textbox.insert(tkinter.END, result)
    textbox.see(tkinter.END)

#Exponent function
def exponentiate():
    #Save value from textbox input
    inputValue=textbox.get("1.0","end-1c")

    #Place inputs that are separated by comma into list
    list = inputValue.split(',')
    num1 = int(list[0])
    num2 = int(list[1])
    result = num1 ** num2

    #Clear textbox
    textbox.delete('1.0', tkinter.END)

    #Display result in textbox
    textbox.insert(tkinter.END, result)
    textbox.see(tkinter.END)

#GUI window dimensions
calc.geometry("220x220")

#Components
textbox = tkinter.Text(height=2,width=20)
button1 = tkinter.Button(calc, text="+", width=2, height=2, command=add)
button2 = tkinter.Button(calc, text="-", width=2, height=2, command=subtract)
button3 = tkinter.Button(calc, text="/", width=2, height=2, command=divide)
button4 = tkinter.Button(calc, text="x", width=2, height=2, command=multiply)
button5 = tkinter.Button(calc, text="%", width=2, height=2, command=mod)
button6 = tkinter.Button(calc, text="^", width=2, height=2, command=exponentiate)

#Display to GUI
textbox.pack()
button1.place(x=52, y=40)
button2.place(x=112, y=40)
button3.place(x=52, y=100)
button4.place(x=112, y=100)
button5.place(x=52, y=160)
button6.place(x=112, y=160)

calc.mainloop()