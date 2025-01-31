from sys import exit
if 1 == 1:
  exit()
#This "program" is not intended to be run. It is just for copy pasting code snippets


#Open file. Add .strip() to remove surrounding whitespace if needed
with open("input.txt") as f:
  txt = f.read()

#Alphabet
alpha = "abcdefghijklmnopqrstuvwxyz"
#or
import string #Also contains other useful strings
print(string.ascii_lowercase)

#Switch rows + columns (transpose 2d list)
#Rows and columns must be of same len, otherwise lowest len is used
list1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
list2 = [list(elem) for elem in list(zip(*list1))]
#Use itertools.zip_longest to take longest len instead of shortest.
from itertools import zip_longest
list3 = [[1, 2], [4, 5, 6], [7, 8], [10, 11, 12]]
list4 = [list(elem) for elem in list(zip_longest(*list3, fillvalue=-1))]


#Increase recursion limit, 1000 by defualt
from sys import setrecursionlimit
setrecursionlimit(1500)

#Pair of lists to dict, extra items ignored
keys = ["a", "b", "c"]
values = ["one", "two", "three"]
dict = dict(zip(keys, values))

#Custom sort, ex. sort int-strings by magnitude
list1 = ["1", "34", "-100", "900", "5", "-343"]
sorted(list1, key=lambda x: abs(int(x)))

#Custom sort using comparison not value function
#Useful in certain cases with tie breakers or not easily numericized values
from functools import cmp_to_key
list1 = ["1", "34", "-100", "900", "5", "-343"]
def comparison(v1, v2):
  v1, v2 = abs(int(v1)), abs(int(v2))
  if v1 > v2:
    return 1
  elif v1 < v2:
    return -1
  else:
    return 0
list2 = sorted(list1, key=cmp_to_key(comparison))

#Anagram (same contents for both lists/strings)
from collections import Counter
first = "abcd"
second = "acdb"
is_anagram = Counter(first) == Counter(second)

#All unique
list1 = [1, 2, 3, 4, 4, 5]
all_unqiue = len(list1) == len(set(list1))

#Exponential growth / compound intrest formula
#Base number, intrest rate, times compounded, compounds per time
p, r, t, n = 9035, 0.31, 10, 1
a = p * (1 + r/n)**(n*t)

#Convert bases, 2 digit identifier added to start
n = 1000
bin_n = bin(n)
hex_n = hex(n)
oct_n = oct(n)
dup_n = int(bin_n[2:], 2)

#Convert to custom base (output as a list), ignores signs
def n_to_base(n, base):
  n = abs(n)
  if n == 0:
    return [0]
  
  digits = []
  while n > 0:
    digits.append(n % base)
    n //= base
  
  return digits[::-1]

#Zfill right side
def zfillright(n, zeros):
  return str(n).split(".")[0] + "." + str(n).split(".")[1].ljust(zeros, "0")
zfillright(1.2, 2)
#Left zfill
str(34).zfill(4)
