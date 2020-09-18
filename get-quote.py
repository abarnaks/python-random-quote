import random

def primary():
  # print("Keep it logically awesome.")

  #reading all quotes inside file
  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()

  #generating quotes randomly from list
  last = len(quotes) - 1
  rnd = random.randint(0,last)

  print(quotes[rnd])
  #-1 for last value regardless of size
  #list size is 14 so last element index would be 13

if __name__== "__main__":
  primary()
