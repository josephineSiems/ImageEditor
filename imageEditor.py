from PIL import Image, ImageEnhance, ImageFilter
import os
import sys
from pathlib import Path


def main():
    path = './Photo_In'
    pathOut = '/Photo_Out'
    for filename in os.listdir(path):
        img = Image.open(f"{path}/{filename}")

        if len(sys.argv) > 1:
            if (sys.argv[1] == 'contour'):
                edit = img.filter(ImageFilter.CONTOUR)
            elif (sys.argv[1] == 'blur'):
                edit = img.filter(ImageFilter.BLUR)
            elif (sys.argv[1] == 'saturation'):
                if len(sys.argv) > 2 :
                    factor = int(sys.argv[2])
                else:
                    factor = 2
                    print("You can add a number after saturation, to choose the intensity. The standard is 2.")
                enhancer = ImageEnhance.Color(img)
                edit = enhancer.enhance(factor)   
        else:
            print("Please add an argument like 'contour','blur' or 'saturation'\n You can add a number after saturation, to choose the intensity.")
            return None
        
        clean_name = os.path.splitext(filename)[0]
        counter = 0
        clean_name_edited = f'{clean_name}_edited.png'
        print(f".{pathOut}/{clean_name_edited}")

    
        while(Path(f".{pathOut}/{clean_name_edited}").is_file()):
            print("hi! " + str(counter))
            counter += 1
            clean_name_edited = f'{clean_name}_edited{counter}.png'


        edit.save(f'.{pathOut}/{clean_name_edited}')

if __name__ == "__main__":
    main()