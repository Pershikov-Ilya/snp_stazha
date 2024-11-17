def palindrome(string):
    if not isinstance(string, str):
        if isinstance(string, (int, float)):
            string = str(string)
        else:
            return False
    result = [char.lower() for char in string if char.isalnum()]
    return result == result[::-1]


print(palindrome("A man, a plan, a canal -- Panama"))
print(palindrome("Madam, I'm Adam!"))
print(palindrome(333))
print(palindrome("555dfd550"))
print(palindrome("Abracadabra"))
