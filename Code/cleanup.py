remove = '().!,"-'

def cleanup(file):
    
  word_list = []      

  with open(file, "r") as file:
    for line in file:
      for word in line.split():
        word = word.lstrip(remove).rstrip(remove).strip('\n').lower()
        word_list.append(word)

  return word_list