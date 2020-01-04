#collatz
#from automate the boring stuff
def collatz(number):
  if number % 2 == 0:
    return(number // 2)
  else:
    return((3 * number + 1))

while True:
  try:
    num = int(input('Please enter a number:\n'))
    while num != 1:
      num = collatz(num)
      print(num)
  except:
    print('Enter an integer damnit')
