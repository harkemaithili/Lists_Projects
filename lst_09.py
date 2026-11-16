
from functools import reduce

# RGB pixel values
pixels = [
    (255, 0, 0),
    (0, 255, 0),
    (0, 0, 255),
    (255, 255, 255),
    (50, 50, 50),
    (100, 100, 100)
]

# Convert RGB into grayscale
gray = list(map(
    lambda p: int(0.299*p[0] +
                  0.587*p[1] +
                  0.114*p[2]),
    pixels
))

print("Grayscale Values:")
print(gray)

# Count dark pixels
dark = list(filter(lambda x: x < 128, gray))

print("Dark Pixels:", len(dark))

# Average brightness
average = reduce(lambda a, b: a + b, gray) / len(gray)

print("Average Brightness:", round(average, 2))

# Binary conversion
binary = list(map(
    lambda x: 0 if x < 128 else 255,
    gray
))

print("\nBinary Values:")
print(binary)

# ASCII image
print("\nASCII IMAGE")

for pixel in binary:
    print("#" if pixel == 255 else ".", end=" ")

print()
