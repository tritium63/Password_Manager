def Pass_Gen():
	import random, string
	x = ''.join(random.choices(string.ascii_letters + string.digits, k=16))
	print(x)