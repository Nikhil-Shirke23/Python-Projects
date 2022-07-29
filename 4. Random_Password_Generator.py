import random
import string

print("\t\t ====== Welcome to our Random Password Generator ======\n")

lower_cases = string.ascii_lowercase
upper_cases = string.ascii_uppercase
digits = string.digits
symbols = "@#_.$"

combine = lower_cases + upper_cases + digits + symbols
length = 9
x = random.sample(combine, length)
password = "".join(x)
print("Your Password is: ", password)