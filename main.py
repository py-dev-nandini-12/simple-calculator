from tkinter import *

window = Tk()
window.title("Calculator")
# window.config(width =300 ,height = 400)
window.config(pady=70, padx=20)
# StringVar() is the variable class
# we create an instance of this class
text_input = StringVar()

# globally declare the operator variable
operator = ''


# Function to update expression
# in the text entry box
def click(numbers):  # define the button(btn)click function
    global operator
    # concatenation of string
    operator += str(numbers)
    # update the expression by using set method
    text_input.set(operator)


def equal_press():
    global operator
    # eval function evaluate the expression
    # and str function convert the result
    # into string
    result = str(eval(operator)) #here eval() evaluates an expression like 3+4 when = is clicked
    text_input.set(result)
    # operator=""


def clear():
    global operator
    operator = ""
    text_input.set(operator)

# create the text entry box for  # showing the expression

display = Entry(font=('arial', 20, 'bold'), textvariable=text_input, bd=30, insertwidth=4,
                bg="blue").grid(columnspan=4)


def create_button(text, column, row, padx, pady, fg, command):
    button = Button(text=text, padx=padx, pady=pady, fg=fg, command=command)
    button.grid(column=column, row=row)
    return button


# ------------------------0-------------------------------------------#
zero = create_button("0", row=5, column=0, padx=14, pady=14, fg="black", command=lambda: click(0))
# ----------------------------------------------------------------#
one = create_button("1", row=4, column=2, padx=14, pady=14, fg="black", command=lambda: click(1))
two = create_button("2", row=4, column=1, pady=14, padx=14, fg="black", command=lambda: click(2))
three = create_button("3", row=4, column=0, pady=14, padx=14, fg="black", command=lambda: click(3))
# -----------------------------------------------------------------#
four = create_button("4", row=3, column=2, pady=14, padx=14, fg="black", command=lambda: click(4))
five = create_button("5", row=3, column=1, pady=14, padx=14, fg="black", command=lambda: click(5))
six = create_button("6", row=3, column=0, pady=14, padx=14, fg="black", command=lambda: click(6))
# ------------------------------------------------------------------#
seven = create_button("7", row=2, column=2, pady=14, padx=14, fg="black", command=lambda: click(7))
eight = create_button("8", row=2, column=1, pady=14, padx=14, fg="black", command=lambda: click(8))
nine = create_button("9", row=2, column=0, pady=14, padx=14, fg="black", command=lambda: click(9))
# ----------------------------------------------------------------#
decimal = create_button(".", row=5, column=1, padx=14, pady=14, fg="black", command=lambda: click('.'))
equal = create_button("=", row=5, column=2, padx=14, pady=14, fg="black", command=equal_press)
c = create_button("C", row=1, column=2, pady=14, padx=14, fg="black", command=clear)
# -------------------------operator---------------------------------------#
divide = create_button("/", row=1, column=1, pady=15, padx=15, fg="black", command=lambda: click('/'))
multiply = create_button("*", row=1, column=0, pady=14, padx=14, fg="black", command=lambda: click('*'))
minus = create_button("-", row=2, column=3, pady=14, padx=14, fg="black", command=lambda: click("-"))
add = create_button("+", row=3, column=3, pady=14, padx=14, fg="black", command=lambda: click("+"))

window.mainloop()
