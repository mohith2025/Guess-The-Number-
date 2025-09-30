import random
secret_number = int(random.randint(1,20))
print(secret_number)
print("Welcome to Number Guessing Game!")
print("You need to guess the correct number between 1 and 20.")
print("If your guess is lower or higher, hints will be given.")
guess_num = int(input("Guess the number b/w 1 to 20: "))

max_attempts = 5
i = 1

while i <= max_attempts :
    if guess_num == secret_number :
        guess_num = print(f"Attempt {i}/{max_attempts}, correct guess!")
        break
    elif guess_num < secret_number:
        print(f"Too Low! {max_attempts - i} chances remaining.")
        guess_num = int(input("Guess the number b/w 1 to 20: "))

    else:
        print(f"Too High! {max_attempts - i} chances remaining.")
        guess_num = int(input("Guess the number b/w 1 to 20: "))
    i+=1

else:
    print(f"Out of attempts! The correct answer was {secret_number}.")
