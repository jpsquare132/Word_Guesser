secret_word = input("Enter your secret word: ")

# Step 0: Use a loop to let the user have up to 3 tries at guessing.

  # Step 1: Prompt the user to input their guess and make the guess lowercase
  # YOUR CODE HERE
prediction=input("Enter your guess:")
guess=prediction.lower()
tries=3
correctness=0
while guess!=secret_word:
  correctness=correctness+1
  tries=tries-1
  if tries==0:
    print(f"Game over! The correct word is {secret_word}.")
    break
  if len(guess)<len(secret_word) and tries!=0:
    print(f"Sorry. That is incorrect. You have {tries} tries left. \nHint: Your guess is too short") 
  elif len(guess)>len(secret_word) and tries!=0:
    print(f"Sorry. That is incorrect. You have {tries} tries left. \nHint: Your guess is too long")
  elif len(guess)==len(secret_word):
    print(f"Sorry. That is incorrect. You have {tries} tries left. \nHint: Your guess is the correct length")
  prediction=input("Enter your guess:")
  guess=prediction.lower()

if guess==secret_word:
  correctness=correctness+1
  print(f"Correct! You got it in {correctness} tries!")


