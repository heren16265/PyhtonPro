import random
def gen_pass(pass_length):


    elements = "+-/*!&$#?=@<>1234567890qwertyuıopğüasdfhgjklşizxcvbnmöç.*"
    password = ""

    for i in range(pass_length):
        password += random.choice(elements)

    return password