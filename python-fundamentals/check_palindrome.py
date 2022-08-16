def check_palindrome(word):
	new_word = word[::-1]

	if new_word == word:
		return True
	return False

status = check_palindrome("malayalam")

if status:
	print("word is palindrome")
else:
	print("word is not palindrome")