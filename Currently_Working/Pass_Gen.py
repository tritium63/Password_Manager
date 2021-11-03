<<<<<<< HEAD
def Pass_Gen():
	import random, string
=======
import random, string
def Pass_Gen():
>>>>>>> aditya_personal
	x = ''.join(random.choices(string.ascii_letters + string.digits, k=16))
	return x