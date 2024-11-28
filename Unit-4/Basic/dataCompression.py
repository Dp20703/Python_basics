# import zlib
# s="it's fun to learn python"
# print(len(s))
# t=zlib.compress(s)
# len(t)
# print(len(t))

import gzip
s="it's fun to learn python"
print(len(s))
t=gzip.compress(s)
len(t)
print(len(t))

