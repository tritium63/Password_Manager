import random
def PassGen():
    P=""
    for i in range(16):
        P+=chr(random.randrange(33,126))
    print(P)
# PassGen()