from PIL import Image
from crop_image import crop_image, resize_image, rotate_image

def main():
    image_path = input("Enter image path:")
  
  #Error Handling for file not found
    try:
        img = Image.open(image_path) # python attempts to find and open the file
    except FileNotFoundError:   # an inbuilt exception class in python
        print("Error: Image not found!")# this only runs if the file doesn't exist
        return                          # exit the program if file not found
    
    #SHOW ORIGINAL IMAGE FIRST
    print("Original image opened")
    img.show()
    
    while True: #main menu
        print("\n--- Mini Image Editor ---")
        print("1. Crop Image")
        print("2. Resize Image")
        print("3. Rotate Image")
        print("4. Save Image")
        print("0. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            img = crop_image(img)
        elif choice == '2':
            img = resize_image(img)
        elif choice == '3':
            img = rotate_image(img)
        elif choice == '4':
            filename = input("Enter output filename:")
            img.save(filename)
            print("Image saved successfully!")
        elif choice == '0':
            print("Exiting Editor, Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")
            continue

        #Post-action menu --- making edits permanent(write to the computer's disk)
        while True:
            print("\nWhat would you like to do next?")
            print("1. Save image")
            print("2. Continue editing")
            print("0. Exit")

            next_choice = input("Choose an option: ")

            if next_choice == "1":
                filename = input("Enter output filename:")
                img.save(filename)
                print("Image saved successfully!")

                #Reload saved image to continue editing
                img = Image.open(filename)
                break
            elif next_choice == "2":
                break
            elif next_choice == "0":
                print("Exiting editor")
                return
            else:
                print("Invalid choice")



if __name__ == "__main__":
    main()



  
