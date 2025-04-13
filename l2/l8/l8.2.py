def is_palindrome(text):
    changed_text = ''.join(char.lower() for char in text if char.isalnum())
    return changed_text == changed_text[::-1]
assert is_palindrome('A man, a plan, a canal: Panama')
assert is_palindrome('0P')==False
assert is_palindrome('a.')
assert is_palindrome('aurora')==False
print("ОК")