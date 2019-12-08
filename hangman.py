import random
wlist = ['python', 'java', 'kotlin', 'javascript']
choice = random.choice(wlist)
blank = choice
for i in range(0,len(choice)):
    blank = blank.replace(choice[i],"-")
while True:
  start = input('Type "play" to play the game, "exit" to quit: ')
  if start == 'exit':
    break
  elif start == 'play':
    print('H A N G M A N')

    lives = 8
    word_length = len(choice)
    used = []
    blank = list(blank)

    while lives > 0:
      if ''.join(blank) == choice:
        print('You guessed the word ' +''.join(blank) + '!')
        print('You survived!')
        break

      print()
      print(''.join(blank))
      
      guess = input('Input a letter: ')

      if guess in used:
        print('You already typed this letter')

      elif len(guess) != 1:
        print('You should print a single letter')  
      
      elif not (guess.isascii() and guess.islower()):
        print('It is not an ASCII lowercase letter')

      elif guess in choice:
        for i in range(word_length):
          if choice[i] == guess:
            blank[i] = guess
        used.append(guess)  

      else: 
          print('No such letter in the word')
          used.append(guess)
          lives -= 1


    if lives == 0:
      print('You are hanged!')
      print('')
  else:
    continue
