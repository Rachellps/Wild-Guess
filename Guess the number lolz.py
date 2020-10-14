import random
import time

corr_num = random.randint(1, 100)
num_g = 0

while True:
    user_str = input("Make your guess: ").strip()
    if user_str.isdigit():
        user_num = int(user_str)
    else:
        print("Please lar, please key in digit")
        continue
    
    num_g = num_g + 1
    
    if user_num == corr_num:
        print("You are damn right!")
        break

    elif user_num > corr_num:
        print("too much liao lar")

    else:
        print("too little, add more!")
    
time.sleep(1)
print("Number of guess is", num_g)
time.sleep(1)
print("Bye, you smart ass!")
