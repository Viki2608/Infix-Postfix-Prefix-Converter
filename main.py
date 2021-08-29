from tkinter import *
from pythonds import Stack
window = Tk()

OPERATORS = set(['+', '-', '*', '/', '(', ')', '^'])  # set of operators
PRIORITY = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}  # dictionary having priorities


def infix_to_postfix():
    infix_input = infix_entry.get()  # input expression

    stack = []  # initially stack empty

    output = ''  # initially output empty

    for ch in infix_input:

        if ch not in OPERATORS:  # if an operand then put it directly in postfix expression

            output += ch

        elif ch == '(':  # else operators should be put in stack

            stack.append('(')

        elif ch == ')':

            while stack and stack[-1] != '(':
                output += stack.pop()

            stack.pop()

        else:
            while stack and stack[-1] != '(' and PRIORITY[ch] <= PRIORITY[stack[-1]]:
                output += stack.pop()

            stack.append(ch)

    while stack:
        output += stack.pop()

    print(output)
    postfix_result.config(text=output)


def prefix_to_postfix():
    stack = []

    operators = set(['+', '-', '*', '/', '^'])

    # Reversing the order
    s = prefix_entry.get()
    s=s[::-1]

    # iterating through individual tokens
    for i in s:

        # if token is operator
        if i in operators:

            # pop 2 elements from stack
            a = stack.pop()
            b = stack.pop()

            # concatenate them as operand1 +
            # operand2 + operator
            temp = a + b + i
            stack.append(temp)

        # else if operand
        else:
            stack.append(i)

    # printing final output
    print(*stack)
    postfix_result.config(text=stack)


def isOperator(x):
    if x == "+":
        return True

    if x == "-":
        return True

    if x == "/":
        return True

    if x == "*":
        return True

    return False


# Convert postfix to Prefix expression


def postfix_to_prefix():
    post_exp = postfix_entry.get()
    s = []

    # length of expression
    length = len(post_exp)

    # reading from right to left
    for i in range(length):

        # check if symbol is operator
        if isOperator(post_exp[i]):

            # pop two operands from stack
            op1 = s[-1]
            s.pop()
            op2 = s[-1]
            s.pop()

            # concat the operands and operator
            temp = post_exp[i] + op2 + op1

            # Push string temp back to stack
            s.append(temp)

        # if symbol is an operand
        else:

            # push the operand to the stack
            s.append(post_exp[i])

    ans = ""
    for i in s:
        ans += i
    print(ans)
    prefix_result.config(text=ans)


def infix_to_prefix():
    infix_input = infix_entry.get()[::-1]
    stack = []
    output = ''
    for ch in infix_input:
        if ch not in OPERATORS:  # if an operand then put it directly in postfix expression
            output += ch
        elif ch == '(':  # else operators should be put in stack
            stack.append('(')
        elif ch == ')':
            while stack and stack[-1] != '(':
                output += stack.pop()

            stack.pop()
        else:

            while stack and stack[-1] != '(' and PRIORITY[ch] <= PRIORITY[stack[-1]]:
                output += stack.pop()

            stack.append(ch)
    while stack:
        output += stack.pop()

    result=output[::-1]

    prefix_result.config(text=result)


def prefix_to_infix():
    prefix=prefix_entry.get()

    stack = []

    i = len(prefix) - 1
    while i >= 0:
        if not isOperator(prefix[i]):

            # symbol is operand
            stack.append(prefix[i])
            i -= 1
        else:

            # symbol is operator
            str = "(" + stack.pop() + prefix[i] + stack.pop() + ")"
            stack.append(str)
            i -= 1
    infix_result.config(text=stack[-1])


def is_operand(x):
    return (x >= 'a' and x <= 'z') or (x >= 'A' and x <= 'Z')


def postfix_to_infix():
    exp = postfix_entry.get()
    s = []

    for i in exp:

        # Push operands
        if is_operand(i):
            s.insert(0, i)

        else:
            op1 = s[0]
            s.pop(0)
            op2 = s[0]
            s.pop(0)
            s.insert(0, "(" + op2 + i +op1 + ")")

    infix_result.config(text=s)





window.title("Prefix Postfix Infix Converter")
window.minsize(width=500, height=400)
window.config(padx =10,pady =10,bg="#261C2C")

Infix = Label(text="Infix")
Infix.grid(row=0, column=0)
Infix.config(padx=20, pady=20,bg="#261C2C",fg="white")

infix_entry = Entry()
infix_entry.grid(row=0,column=1)
infix_entry.config(width=50)

prefix = Label(text="prefix")
prefix.grid(row=1, column=0)
prefix.config(padx=20, pady=20,bg="#261C2C",fg="white")

prefix_entry = Entry()
prefix_entry.grid(row=1,column=1)
prefix_entry.config(width=50)

postfix = Label(text="postfix")
postfix.grid(row=2, column=0)
postfix.config(padx=20, pady=20,bg="#261C2C",fg="white")

postfix_entry = Entry()
postfix_entry.grid(row=2,column=1)
postfix_entry.config(width=50)

postfix_result = Label(text='0')
postfix_result.config(width=50)
postfix_result.grid(row=7,column=1)
postfix_result.config(padx=20,pady=20,bg="#261C2C",fg="white")

prefix_result = Label(text='0')
prefix_result.config(width=50)
prefix_result.grid(row=8,column=1)
prefix_result.config(padx=20,pady=20,bg="#261C2C",fg="white")

infix_result = Label(text='0')
infix_result.config(width=50)
infix_result.grid(row=9,column=1)
infix_result.config(padx=20,pady=20,bg="#261C2C",fg="white")

infix_to_postfix_button = Button(text="Infix to Postfix", command=infix_to_postfix)
infix_to_postfix_button.grid(row=3,column =0)
infix_to_postfix_button.config(padx=10,pady=10)
prefix_to_postfix_button = Button(text = "Prefix to Postfix", command=prefix_to_postfix)
prefix_to_postfix_button.grid(row=4,column =0)
prefix_to_postfix_button.config(padx=10,pady=10)
postfix_to_prefix_button = Button(text = "Postfix to Prefix", command=postfix_to_prefix)
postfix_to_prefix_button.grid(row=5,column =0)
postfix_to_prefix_button.config(padx=10,pady=10)
postfix_to_infix_button = Button(text="Postfix to Infix", command=postfix_to_infix)
postfix_to_infix_button.grid(row=5,column =1)
postfix_to_infix_button.config(padx=10,pady=10)
infix_to_prefix_button = Button(text="Infix to Prefix", command=infix_to_prefix)
infix_to_prefix_button.grid(row=3,column =1)
infix_to_prefix_button.config(padx=10,pady=10)
prefix_to_infix_button = Button(text="Prefix to Infix", command=prefix_to_infix)
prefix_to_infix_button.grid(row=4,column =1)
prefix_to_infix_button.config(padx=10,pady=10)

postfix = Label(text="Postfix Expression : ")
postfix.grid(row=7,column=0)
postfix.config(padx=20,pady=20,bg="#261C2C",fg="white")
postfix = Label(text="Prefix Expression : ")
postfix.grid(row=8,column=0)
postfix.config(padx=20,pady=20,bg="#261C2C",fg="white")
postfix = Label(text="Infix Expression : ")
postfix.grid(row=9,column=0)
postfix.config(padx=20,pady=20,bg="#261C2C",fg="white")

window.mainloop()