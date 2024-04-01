# this is a code for palindrome in python
input_str=input("Enter a word")
chec_str=input_str[::-1]
if input_str == chec_str:
    print("its a palindrome")
else:
    print("its a not palindrome")
