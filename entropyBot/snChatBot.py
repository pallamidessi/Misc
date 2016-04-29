from math import log, sqrt, pow
import random
letter_frequencies_en = {
                    'a':0.08167, 
                    'b':0.01492, 
                    'c':0.02782, 
                    'd':0.04253, 
                    'e':0.12702, 
                    'f':0.02228, 
                    'g':0.02015, 
                    'h':0.06094, 
                    'i':0.06966, 
                    'j':0.00153, 
                    'k':0.00772, 
                    'l':0.04025, 
                    'm':0.02406, 
                    'n':0.06749, 
                    'o':0.07507, 
                    'p':0.01929, 
                    'q':0.00095, 
                    'r':0.05987, 
                    's':0.06327, 
                    't':0.09056, 
                    'u':0.02758, 
                    'v':0.00978, 
                    'w':0.02361, 
                    'x':0.00150, 
                    'y':0.01974, 
                    'z':0.00074 
                    }

def create_frequencies(text):
  freq = {}
  
  for character in text:
    freq[character] = freq.get(character, 0.0) + 1

  for key, value in freq.iteritems():
    freq[key] = value / len(text)

  return freq

def rmse(freq_1, freq_2):
  error = 0
  count = 0
  for key, value in freq_1.iteritems():
      if key in freq_2:
          error += pow(freq_2[key] - value, 2)
          count += 1

  if count != 0 and error > 0: 
    error = sqrt(error / count)
    
  return error

def rouletteSelection(distribution):
  rand = random.random()
  rouletteHeight = 0.0
  
  for key, value in distribution.iteritems():
      if rand >= rouletteHeight and rand <= rouletteHeight + value:
        return key
      rouletteHeight += value

def generate_from_dist(distribution, n):
  generated_text = ""
  for i in range(0, n - 1):
    generated_text += rouletteSelection(distribution)
  
  return generated_text

def shannon_entropy(freq):
  entropy = 0;
  for key, value in freq.iteritems():
      entropy += value * log(1 / value, 2)

  return entropy
  
text_simple = "This is a simple text sample"
text_stupid = "oooooaaaaa"
entropy_simple = shannon_entropy(create_frequencies(text_simple))
entropy_stupid = shannon_entropy(create_frequencies(text_stupid)) 
print "RMSE:", rmse(create_frequencies(text_simple), letter_frequencies_en)
text_from_dist = generate_from_dist(letter_frequencies_en, 500)
print "RMSE:", rmse(create_frequencies(text_from_dist), letter_frequencies_en)
print entropy_simple
print entropy_stupid 
