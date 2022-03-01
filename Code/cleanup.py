remove = '().!,"'

def cleanup(file):
    
  words = []      

  with open(file, "r") as file:
    for line in file:
      for word in line.split():
        word = word.lstrip(remove).rstrip(remove).strip('\n').replace('-', ' ').lower()
        words.append(word)

  return words