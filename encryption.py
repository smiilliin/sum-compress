from compress import keySum, keys, compress, decompress
import numpy as np

keyArray = []

for i in keySum:
  for j in keys:
    keyArray.append(i + j)
    keyArray.append(i - j)
keyArray = np.array(list(set(keyArray)))
keylen = keyArray.shape[0]


def genKey():
  key = np.arange(0, 65536, 1)
  np.random.shuffle(key)
  return key[0:keylen]


def encrypt(data, key):
  data, seqdata, length = compress(data)

  for i, b in enumerate(data):
    data[i] = key[np.where(keyArray == b)[0][0]]
  return data, seqdata, length


def decrypt(data, seqdata, length, key):
  for i, b in enumerate(data):
    data[i] = keyArray[np.where(key == b)[0][0]]
  return decompress(data, seqdata, length)
