def clean_string(s):
    return s.replace(" ", "").lower() #first it will remove space and then lower function will convert into lowercases

def is_palindrome(s):
    if len(s) <= 1:  #  checking single character or empty string
        return True
    if s[0] == s[-1]:     #checking the first and last character are same or 
        return is_palindrome(s[1:-1])
    else:
        return False
string = input("Enter a string: ")
modified_string = clean_string(string)
if is_palindrome(modified_string):
    print(modified_string,"Is a Palindrome.")
else:
    print(modified_string,"Not a palindrome.")

