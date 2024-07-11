from compress import compress, decompress

originData = b"hello!lliaaassasf"
data, seqdata, length = compress(originData)
result = (decompress(data, seqdata, length))

print(data)
print(seqdata)

print(originData.decode("ascii"))
