from PIL import Image

#Open the image
image = Image.open("pic2.jpg")

# crop area: (left, upper, right, lower)
cropped_image = image.crop((100,100,2500,2500))

# Save the cropped image
cropped_image.save("cropped_output.jpg", quality = 95)
cropped_image.show()

print("cropping complete!")
print((cropped_image.size))