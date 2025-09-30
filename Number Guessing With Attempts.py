import random
secret_number = int(random.uniform(1,20))
print("Welcome to number Guessing Game,\nyou are supposed to guess the correct number,\nif your number is less than given number it shows too low, vice versa")
guess_num = int(input("Guess the number b/w 1 to 20: "))

a = guess_num
# b = a
i = 1
while a True and range(i,5):
    if guess_num == secret_number :
        print(f"{guess_num} correct guess!",f"you found in {i} attempts")
        break
    elif guess_num < secret_number:
        print("Too Low",f" only {5-i} chances remaining")
        guess_num = int(input("retry with a new number : "))
        # a = b
    elif guess_num > secret_number:
        print(f"Too High, only {5-i} chances left")
        guess_num = int(input("retry with a new number : "))
        #b = guess_num
    i+=1
else:
    print(f"The answer was {secret_number}")

