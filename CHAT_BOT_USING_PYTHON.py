"""
we can create chat-bot by using RANDOM MOdule of python
"""

import random

var_1 = ["hi","hello"]
var_2 = ["how are you","how are you doing","how is your health"]
var_3 = ["what is your name","how do i call you"]
var_4 = ["what is your programming language","which programming language you want to preferred"]
var_5 = ["what are your hobbies","what you do in your free time"]
var_6 = ["tell me your source code","your scripting code"]
var_7 = ["ok bye","bye"]
print("Hello,my name is Avnish, how may i help you","\n")
while 1:
    user_input = input("Talk With Me Here :")
    if user_input.lower() in var_1:
        bot = ["hello","hi"]
        print("Avnish :" + random.choice(bot))
    elif user_input.lower() in var_2:
        bot = ["I Am Fine","I Am Doing Good"]
        print("Avnish :" + random.choice(bot))
    elif user_input.lower() in var_3:
        bot = ["I Am Avnish","You can call me Avnish or a friend"]
        print("Avnish :" + random.choice(bot))

    elif user_input.lower() in var_4:
        bot = ["python programming language", "i made up by using python programming"]
        print("Avnish :" + random.choice(bot))
    elif user_input.lower() in var_5:
        bot = ["solve the peoples problem","guide the peoples"]
        print("Avnish :" + random.choice(bot))
    elif user_input.lower() in var_6:
        print("Avnish : sorry my owner 'avnish' not granted me permission to tell you this !!!!")
    elif user_input.lower() in var_7:
        break
    else:
        print("Avnish :sorry i am not able to understand your question")

