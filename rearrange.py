import random, sys

input_str = sys.argv[1:]

def rearrange(str):
  rand_list = str.split(' ')
  random.shuffle(rand_list)
  output = ''
  for i in len(rand_list):
    output += str(i) + ' '
  return output

if __name__ == '__main__':
  print(rearrange(str(input_str)))
