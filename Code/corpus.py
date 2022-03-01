import requests
import sys

#------------------------------------------------------------------------

# url and personal API key
DIFFBOT_API_URL = 'http://api.diffbot.com/v3/article'
DIFFBOT_DEV_TOKEN = '4005c11318c9d5b2665622894985b4fb'

#------------------------------------------------------------------------

# function to extract lyrics from azlyrics
def get_lyrics(url):
  # parameters required by the API
  params = {
    'token': DIFFBOT_DEV_TOKEN,
    'url': url,
    'discussion': 'false'
  }

  request = requests.get(DIFFBOT_API_URL, params)
  obj = request.json()['objects'][0]
  file = obj['text']

  return file

def create_corpus(file):
  output_file = open('./data/sample.txt', 'w')

  corpus = ''

  for line in file:
    line_url = line.strip()
    lyrics = get_lyrics(line_url)
    corpus += lyrics

  return output_file.write(corpus)
  

#------------------------------------------------------------------------

if __name__ == '__main__':
  input_file = open(sys.argv[1])

  text_file = get_lyrics(input_file)
  create_corpus(text_file)
  