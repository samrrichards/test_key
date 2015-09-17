letters = "ABCDEFGHIJKLMNO"
x = 0 

import random 

while x < 15:
	x += 1
	num = random.randint(0, len(letters) - 1)
	letter = letters[num]
	print str(x) + ". " + letter 
	letterList = list(letters)
	del(letterList[num])
	letters = "".join(letterList) 