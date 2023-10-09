import sys
print(sys.path)

import re
text = 'My phone number is 43567654, the country code is 57, my lucky number is 17'
result = re.findall('[0-9]+', text)
print(result)

import time
timestamp = time.time()
local = time.localtime()
result= time.asctime()
print(result)

import collections
numbers = [2,4,5,6,3,34,5,76,3,23,4,6,53,123,3,342,32,3,2,2,3,3,3,4,1]
counters = collections.OrderedDict(numbers)
print(counters)