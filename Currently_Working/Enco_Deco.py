import base64

def encode(st):
    b = bytes(st)
    return base64.b64encode(b)
def decode(b):
    return base64.b64decode(b).decode()
