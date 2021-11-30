def say_hi(name):
    print("Hello " + name)

say_hi("Mike")

def cube(num):
    return num*num*num

result = cube(4)
print(result)

is_male = True
is_tall = True
if is_male and is_tall:
    print("You are a tall male")
elif is_male and not(is_tall):
    print("you are a short male")
elif not(is_male) and is_tall:
    print("you are not male but tall")
else:
    print("You are either not male or not tall or both")

secret_word = "giraffe"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False

while guess != secret_word and not(out_of_guesses):
  if guess_count < guess_limit:
    guess = input("Enter guess: ")
    guess_count += 1
  else:
      out_of_guesses = True

if out_of_guesses:
    print("Out of guesses, YOU LOSE!")
else:
    print ("You Win!")