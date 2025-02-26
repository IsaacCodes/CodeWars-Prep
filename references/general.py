#This "program" is not intended to be run
#It is just for copy pasting code snippets
from sys import exit
exit()


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


#Increase recursion limit (1000 by defualt)
from sys import setrecursionlimit
setrecursionlimit(1500)


#Convert lists to dicts using zip or comprehension
keys = ["a", "b", "c"]
values = ["one", "two", "three"]
dict1 = dict(zip(keys, values))
dict2 = {keys[i] : values[i] for i in range(len(keys))}


#Custom sorting (ex. sort integer-strings by magnitude)
list1 = ["1", "34", "-100", "900", "5", "-343"]
sorted(list1, key=lambda x: abs(int(x)))

#Custom sorting using a comparison instead of value function
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


#Converts lists and strings to a dictionary-like counter
from collections import Counter
first = "abcd"
second = "acdb"
#For isntace, checking for anagrams (all the same elements + counts)
is_anagram = Counter(first) == Counter(second)


#Checks if all list items are unqiue
list1 = [1, 2, 3, 4, 4, 5]
all_unqiue = len(list1) == len(set(list1))


#Convert decimal to binary, octal, or hexadecimal
#String outputs are prefixed with 2 digit identifiers
n = 1000
bin_n = bin(n) # '0b1111101000'
oct_n = oct(n) # '0o1750'
hex_n = hex(n) # '0x3e8'

#Convert to base 10 from base b
b = 16
dec_n = int("3e8", b) # 1000

#Convert to a custom base output as a list ignorning sign
#Numbers can then be replaced as nessecary (ex. 11 -> "A")
def n_to_base(n, base):
  n = abs(n)
  if n == 0:
    return [0]
  
  digits = []
  while n > 0:
    digits.append(n % base)
    n //= base
  
  return digits[::-1]


n = 3
#Fill the number with 0's to the left until n digits
print("12".zfill(3)) # '012'

#Fill the number with 0's to the right after the decimal place until n digits
print(f"{12:.{n}f}") # '12.000'


#Date conversion from string to datetime object
# %Y is year, %m is month, %d is day
from datetime import datetime
time_str = "2024-8-20"
time_t = datetime.strptime(time_str, "%Y-%m-%d")