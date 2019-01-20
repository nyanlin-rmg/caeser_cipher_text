def text_encryption(encrypt, key):
	encryption = ''
	try:
		encrypt = str(encrypt)
		key = int(key)
		if key > 25:
			key = 25
		elif key < 1:
			key = 1
		for enc in encrypt:
			number = 0
			number += ord(enc)
			if number == 32:
				number += 0
			elif number > 96 and number < 123:
				number += key
				if number > 122:
					number = (number - 122) + 96
			elif number > 64 and number < 91:
				number += key
				if number > 90:
					number = (number - 90 ) + 64
			encryption += chr(number)
		return encryption
	except ValueError:
		encryption += "Something wrong with your input"
		return encryption