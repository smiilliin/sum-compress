from itertools import combinations

key = [2**i for i in range(0, 16)]

keyPeer = list(combinations(key, 2))
keySum = [i+j for i, j in keyPeer]


def findPeer(x):
  return keyPeer[keySum.index(x)]


def findFromKey(x):
  return key.index(x)


def fourbitArray(x):
  x = bytearray(x)
  result = []
  fourbitMask = 0b1111

  for i in x:
    result.append(i >> 4)
    result.append(i & fourbitMask)
  return result


def fromFourbitArray(x):
  result = []

  for i in range(1, len(x), 2):
    result.append((x[i-1] << 4) | x[i])
  return bytes(result)


def compress(x):
  x = fourbitArray(x)
  x.extend([0 for _ in range((3-(len(x) % 3)) % 3)])

  data = []
  seqdata = []
  for i in range(2, len(x), 3):
    A = x[i-2]
    B = x[i-1]
    C = x[i]

    comseq = True
    abseq = True

    if A == B:
      comseq = False
      B = (B+1) % 16
    else:
      abseq = (A < B)

    A = key[A]
    B = key[B]
    C = key[C]

    S = A+B+C
    Z = A+B-C

    seqdata.append((comseq, abseq))
    data.append(S)
    data.append(Z)

  return data, seqdata, len(x)


def decompress(data, seqdata, length):
  result = []
  for i, seq in enumerate(seqdata):
    S = data[i * 2]
    Z = data[i * 2+1]
    comseq, abseq = seq

    C = (S - Z)/2
    AB = S - C
    peer = findPeer(AB)
    A = min(peer[0], peer[1])
    B = max(peer[0], peer[1])

    if not abseq:
      tmp = B
      B = A
      A = tmp

    if comseq:
      result.append(findFromKey(A))
      result.append(findFromKey(B))
      result.append(findFromKey(C))
    else:
      result.append(findFromKey(A))
      result.append((findFromKey(B)-1) % 16)
      result.append(findFromKey(C))

  return fromFourbitArray(result[0:length])
