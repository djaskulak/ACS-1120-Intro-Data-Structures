def histogram_dict(source_text):
  with open(source_text) as f:
    words = f.read().lower()
    words = [word.rstrip() for word in words]

    special_chars = '''!()-[]{};:'"\…,<>./?@#$%‼^&*_~”„“‥\n'''

    histogram = {}

    for word in words:
      for letter in word: 
        if letter in special_chars:
          word = word.replace(letter, "")
      if word in histogram.keys():
        histogram[word] += 1
      else:
        histogram[word] = 1
    return histogram

def unique_words(histogram):
  print("This text has " + str(len(histogram)) + " unique words in it!")
  return len(histogram)

def frequency(word, histogram):
  frequency = 0
  for key in histogram:
    if key == word:
      frequency = histogram[key]
  return frequency


if __name__ == '__main__':
  histogram = histogram_dict('code/sherlock.txt')
  print(histogram)