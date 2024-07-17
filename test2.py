from PIL import Image
import numpy as np
from encryption import encrypt, keylen

key = np.arange(0, keylen) * (65535 / keylen)

image = np.array(Image.open("pfp.jpg"))


shape = image.shape
image = image.flatten()
imglen = image.size


def encryptImage(image):
  data, _, _ = encrypt(image, key)
  encryptedImage = ((data[:imglen] / 65535)*255)
  encryptedImage = Image.fromarray(
      encryptedImage.reshape(shape).astype("uint8"))

  return encryptedImage


encryptedImages = [encryptImage(image) for _ in range(0, 4)]


for i in range(0, len(encryptedImages)):
  encryptedImages[i].save(f"without-key{i}.png")
