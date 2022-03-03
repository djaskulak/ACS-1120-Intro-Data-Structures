from dictogram import Dictogram
from cleanup import cleanup
from tokens import tokenize
import random

class Markov(Dictogram):
  def __init__(self, word_list, order):
    super(Markov, self).__init__()
    self.word_list = word_list
    self.dict = {}
    self.n_markov_dict = self.create_chain(order)
  
  def create_chain(self, order):
    index = order

    while (index+2) < (len(self.word_list) - order):
      w1 = self.word_list[index]
      w2 = self.word_list[index + 1]
      w3 = self.word_list[index + 2]

      tup = (w1, w2)

      if tup not in self.dict:
        self.dict[tup] = Dictogram() 
      
      self.dict[tup].add_count(w3)
  
      index += 1

    return self.dict

  def walk_chain(self):
    # empty string that will become our sentence 
    sentence_str = ''
    # start at a random index in the list
    start = random.randint(0, len(self.word_list))
    # word at the random index
    word = self.word_list[start]
    next_word = self.word_list[start+1]
    current_tup = (word, next_word)

    sentence_str += ' ' + word

    while len(sentence_str) < 140:
      current_tup = (current_tup[1], next_word)
      sentence_str += ' ' + next_word
      if current_tup in self:
        next_word = self.dict[current_tup].sample()
      else: 
        i = random.randint(0, len(self.word_list))
        next_word = self.word_list[i]

    return sentence_str

if __name__ == '__main__':
  chain = Markov(cleanup('./corpus.txt'), 2)
  print(chain.walk_chain(), 2)