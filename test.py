from compress import compress, decompress
from encryption import encrypt, decrypt, genKey

originData = b"hello!lliaaassasf"
data, seqdata, length = compress(originData)
result = (decompress(data, seqdata, length))

print(data)
print(seqdata)

print(originData.decode("ascii"))


key = genKey()
data, seqdata, length = encrypt(originData, key)
decrypted = decrypt(data, seqdata, length, key)

print(data)
print(decrypted.decode("ascii"))
