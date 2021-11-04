<<<<<<< HEAD
=======

>>>>>>> 7113bea14792dda2b333c0e38c019ac90456d5cf
import random, string
def Pass_Gen():
	x = ''.join(random.choices(string.ascii_letters + string.digits, k=16))
	return x