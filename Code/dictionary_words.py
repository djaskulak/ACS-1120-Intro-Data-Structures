import random, sys

def rand_sent(length):
  with open('/usr/share/dict/words') as f:
    words = f.readlines()
    words = [word.rstrip() for word in words]
    sent_len = random.choices(words, k=length)
    sentence = ''
    for i in sent_len:
      sentence += str(i) + ' '
    print(sentence)


if __name__ == '__main__':
  length = int(sys.argv[1])
  rand_sent(length)