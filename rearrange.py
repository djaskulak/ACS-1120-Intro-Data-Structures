import random

def rearrange(str):
  rand_list = str.split(' ')
  random.shuffle(rand_list)
  return rand_list


if __name__ == '__main__':
    rearranged = rearrange(input())
    print(' '.join(rearranged))
