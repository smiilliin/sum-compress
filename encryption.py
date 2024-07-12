from compress import keySum, keys, compress, decompress
import numpy as np

keyArray = []


def dictKey(key):
  return {value: index for index, value in enumerate(key)}


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
  result = []
  keySize = len(key)
  dictKeyArray = dictKey(keyArray)

  indicies = [(dictKeyArray[b]+offset) %
              keySize for offset, b in enumerate(data)]

  result = key[indicies]
  return result, seqdata, length


def decrypt(data, seqdata, length, key):
  result = []
  key = dictKey(key)

  indicies = [(key[b]-offset) %
              keylen for offset, b in enumerate(data)]

  result = keyArray[indicies]

  return decompress(result, seqdata, length)
