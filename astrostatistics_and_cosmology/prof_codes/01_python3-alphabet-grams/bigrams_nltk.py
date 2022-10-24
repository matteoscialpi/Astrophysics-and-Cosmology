# use pip3 install --user nltk to install nltk
from nltk import ngrams
from nltk import FreqDist
#from nltk.util import ngrams    
import numpy as np
import sys


def compute_freq(filename):

  #Needs python3.5
  from pathlib import Path
 
  #REGEX
  import re

  txt = Path(filename).read_text()
  txt = txt.replace('\n', '') #transform newline into spaces

  #Print sample of text
  print(txt[:100])
 
  #All lowercase
  txt = txt.lower()

  #Keeps only alphabet and spaces
  txt = re.sub(r'[^a-zA-Z ]', '', txt)
  
  monograms = ngrams(txt, 1)
  monograms_freq = FreqDist(monograms)

  bigrams = ngrams(txt, 2)
  bigrams_freq = FreqDist(bigrams)
  
  return (monograms_freq.N(), monograms_freq, bigrams_freq.N(), bigrams_freq)

if __name__=='__main__':

  filename = sys.argv[1]

  #filename = "anna_karenina_project_gutenberg_pg1399.txt"
  Nmono, px_dict, Nbi, pxy_dict = compute_freq(filename)
  
  
  letters=np.array(["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"," "])
  len_letters = len(letters)
  
  #px_marginal = np.zeros(len_letters)
  #py_marginal = np.zeros(len_letters)
  
  # Check frequency of letters recovered
  print("Monogram frequency")
  total_sum = 0.
  px = np.empty(len_letters)
  
  for key,value in px_dict.items():
  
    #DEBUG
    #print(key,value/Nmono)
  
    total_sum += value/Nmono
    idx = np.where(letters == key[0])
    px[idx] = value/Nmono
    
    
  print()
  
  #Check if \sum{px} == 1
  print("Sum P(x) = ", total_sum)
  print("P(x) = ", px)
  #DEBUG
  print(f"{total_sum} == ", np.sum(px), " ???")
  
  
  print()
  print() 
  
  
  print("Bigram frequency")
  
  px_marginal = np.zeros(len_letters)
  py_marginal = np.zeros(len_letters)
  
  for key,value in pxy_dict.items():
  
    #DEBUG
    #print(key,value/Nbi)
    
    #Marginal px
    idx = np.where(letters == key[0])
    px_marginal[idx] += value/Nbi
    
    #Marginal py
    idy = np.where(letters == key[1])
    py_marginal[idy] += value/Nbi
  
    #DEBUG
    #print("key[0] = ", key[0])
    #print("idx = ", idx)
    
  for i in np.arange(len_letters):
    print(f"px = {px[i]}; px_marginal = {px_marginal[i]}; py_marginal = {py_marginal[i]}")
  
  
