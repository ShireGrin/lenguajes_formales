regex_integer_in_range = r"^([1-9][0-9]{5})$"	# Do not delete 'r'.
regex_alternating_repetitive_digit_pair = r"([0-9])(?=[0-9]\1)"	# Do not delete 'r'.

# Lo de arriba es el único "código" que se escribió, HackerRank solo pide eso, el resto del código se agrega automáticamente.

import re
P = input()

print (bool(re.match(regex_integer_in_range, P)) 
and len(re.findall(regex_alternating_repetitive_digit_pair, P)) < 2)
