from pyfiglet import Figlet, FigletFont
import random
import sys

fonts=FigletFont.getFonts()
figlet=Figlet() # important line

if len(sys.argv) == 1:
    user_font=random.choice(fonts)
    figlet.setFont(font=user_font)

elif len(sys.argv) == 3:
    flag = sys.argv[1]
    font_name = sys.argv[2]

    if flag in ["-f", "--font"] and font_name in fonts:
        figlet.setFont(font=font_name)
    else:
        sys.exit("Invalid usage")
    
else:
    sys.exit("Invalid usage")

user_input = input("Input: ")
print(figlet.renderText(user_input))