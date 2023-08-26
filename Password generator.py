import random
alpha = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()"

while True:
    plen = int(input("Enter the desired length of the password: "))
    for i in range(0,1):
        password = ""
        for j in range(0, plen):
            a = random.choice(alpha)
            password = password + a
        print("Here is your random password : " , password)
    break
