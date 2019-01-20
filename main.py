from encrypt import text_encryption
from decrypt import text_decryption

char = True
while char:
	ans = ''
	while not(ans.upper() == 'D' or ans.upper() == 'E'):
		ans = input("\nEnter 'E' for encryption (or) Enter 'D' for decryption: ")
	text = input("Enter text: ")
	key  = input("Enter key: ")
	if ans.upper() == 'E':
		result = text_encryption(text, key)
	else:
		result = text_decryption(text, key)

	print(result)

	do_more = input("Do you want to continue?(Y/N)")
	if do_more.upper() == 'Y':
		char = True
	else:
		char = False