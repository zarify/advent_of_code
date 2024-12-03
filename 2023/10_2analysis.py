from PIL import Image
from collections import deque

def flood_fill(x, y, old_color, new_color, image):
    width, height = image.size
    pixels = image.load()

    # Create a queue for BFS and insert the starting pixel
    queue = deque([(x, y)])

    while queue:
        x, y = queue.popleft()

        # Check if the current pixel has the old color
        if pixels[x, y] == old_color:
            # Change the color of the pixel
            pixels[x, y] = new_color

            # Add the neighboring pixels to the queue
            if x > 0:
                queue.append((x - 1, y))
            if x < width - 1:
                queue.append((x + 1, y))
            if y > 0:
                queue.append((x, y - 1))
            if y < height - 1:
                queue.append((x, y + 1))

# Load an image
image = Image.open("10_2.png")

# Perform flood fill by going around the perimeter of the image
for x in range(image.size[0]):
    flood_fill(x, 0, (255, 255, 255), (255, 0, 0), image)
    flood_fill(x, image.size[1] - 1, (255, 255, 255), (255, 0, 0), image)
for y in range(image.size[1]):
    flood_fill(0, y, (255, 255, 255), (255, 0, 0), image)
    flood_fill(image.size[0] - 1, y, (255, 255, 255), (255, 0, 0), image)
# flood_fill(0, 0, (255, 255, 255), (255, 0, 0), image)

# save the image
image.save("10_2_filled.png")

# now count all the white pixels remaining
white_pixels = 0
width, height = image.size
pixels = image.load()
for x in range(width):
    for y in range(height):
        if pixels[x, y] == (255, 255, 255):
            white_pixels += 1
print(white_pixels)
