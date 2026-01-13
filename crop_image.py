from PIL import Image  # Grab Image module so that you can use its tools from Python Image Library(PIL)
#Key points to note:
 # 1.Return keyword below is used for task sharing helping in data flow i.e img crop -> resize -> rotate

# 1) Crop image using user input
def crop_image(img):
    
# crop area(user input): (left, upper, right, lower)
    print("Enter crop area coordinates:")
    left = int(input("left: "))
    upper = int(input("upper: "))
    right = int(input("right: "))
    lower = int(input("lower: "))

    if right <= left or lower <= upper:
        print("Error: Invalid crop coordinates.")
        return img

# crop image
    img = img.crop((left, upper, right, lower))
    img.show()
    print("Image cropped.") 
    return img
    
   
# 2) Resize image(User Input)
def resize_image(img):

    width = int(input("New width: "))
    height = int(input("New height: "))
# Resize image
    img = img.resize((width, height))
    img.show()
    print("Image resized successfully!")
    return img

# 3) Rotate Image(user input)
def rotate_image(img):
   
    angle = int(input("Enter rotation angle: "))
    img = img.rotate(angle, expand = True) # expand = true means image os preserved and canvas grows larger
    img.show()
    print("Image rotated successfully!")
    return img

