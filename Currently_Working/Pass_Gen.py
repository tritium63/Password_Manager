import random, string
def Pass_Gen():
	x = ''.join(random.choices(string.ascii_letters + string.digits, k=16))
	return x