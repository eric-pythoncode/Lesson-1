import random 

def password(length = 12):
    lowercase = "abcdefghijklmnopqrstuvxyz"
    uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    num = "1234567890"
    special = "?><$%*#!.,@"
    allcharacters = lowercase + uppercase + num + special
    password = random.choices(allcharacters, k = length)
    random.shuffle(password)
    return "".join(password)

passcode = password(12)
print(f"\nGenerated password: {passcode}")