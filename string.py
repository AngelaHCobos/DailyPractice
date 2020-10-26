'''You are given two strings, A and B. Return whether A can be shifted some number of times to get B.

Eg. A = abcde, B = cdeab should return true because A can be shifted 3 times to the right to get B. A = abc and B= acb should return false.'''

def is_shifted(a, b):
  start_position = 1
  current_string = a[start_position:] + a[:start_position]
  while current_string != a:
    current_string = a[start_position:] + a[:start_position]
    print(current_string)
    start_position +=1
    if current_string == b:
      return True
  return False


def is_shifted(a,b)

  
print(is_shifted('fghdfhf', 'fghdfhf'))
# True
 