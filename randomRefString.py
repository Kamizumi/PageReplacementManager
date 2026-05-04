import random

def genRefString(length):
    emptyString = ""
    for i in range(length):
        emptyString += str(random.randint(0,7))
    return emptyString

for i in range(50):
    print(genRefString(30))