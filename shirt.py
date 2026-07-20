import sys
from PIL import Image, ImageOps

if len(sys.argv)<=2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv)>3:
    sys.exit("Too many command-line arguments")

elif not ((sys.argv[1].endswith("png") and sys.argv[2].endswith("png")) or (sys.argv[1].endswith("jpg") and sys.argv[2].endswith("jpg")) or (sys.argv[1].endswith("jpeg") and sys.argv[2].endswith("jpeg"))):
    sys.exit("Input and output have different extensions")

else:
    try:
        with Image.open(sys.argv[1]) as photo, Image.open("shirt.png") as shirt:
            fitted_photo = ImageOps.fit(photo, shirt.size)
        
            fitted_photo.paste(shirt, shirt)

            fitted_photo.save(sys.argv[2])

    except FileNotFoundError:
        sys.exit("Invalid input")
    
        
