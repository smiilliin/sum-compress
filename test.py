from PIL import Image
from compress import compress, decompress
from encryption import dictKey, encrypt, decrypt, genKey
import numpy as np
import matplotlib.pyplot as plt

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


image = np.array(Image.open("pfp.jpg"))
shape = image.shape
image = image.flatten()
imglen = image.size

data, seqdata, length = encrypt(image, key)
decrypted = decrypt(data, seqdata, length, key)
encryptedImage = ((data[:imglen] / 65535)*255)
encryptedImage = Image.fromarray(encryptedImage.reshape(shape).astype("uint8"))
decryptedImage = Image.fromarray(np.array(bytearray(decrypted)).reshape(shape))

fig, axes = plt.subplots(1, 2, figsize=(10, 5))

axes[0].imshow(encryptedImage)
axes[0].axis('off')
axes[0].set_title('Encrypted Image')

axes[1].imshow(decryptedImage)
axes[1].axis('off')
axes[1].set_title('Decrypted Image')

plt.show()
