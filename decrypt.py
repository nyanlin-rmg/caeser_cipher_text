def text_decryption(decrypt, key):

	decryption = ''
	try:
		decrypt = str(decrypt)
		key = int(key)

		if key > 25:
			key = 25
		elif key < 1:
			key = 1
		for dec in decrypt:
			number = 0

			number += ord(dec)

			if number == 32:
				number += 0

			if number > 96 and number < 123:
				number -= key
				if number < 97:
					number = (number + 122) - 96

			elif number > 64 and number < 91:
				number -= key
				if number < 65:
					number = (number + 90) - 64

			decryption += chr(number)
		return decryption
	except ValueError:
		decryption = "Something wrong with your input!"
		return decryption