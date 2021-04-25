from enum import IntEnum
import os
folder = r"‪C:\Users\Lenovo\Desktop\Python\Hashtag Generator"
folder = folder.lstrip("\u202a")


with open(os.path.join(folder, "Hash.txt"), "r", encoding="UTF-8") as file:
    hashtag_all = set(file.read().split())

export_list = []
hint_list = ["moody", "dark", "portrait", "portret", "poland", "polska"]
hashtag_count = 0
menu_option = 0

Main_Menu = IntEnum("Main_Menu", "generate hintlist exit")

while True:
    print()
    menu_option = int(input("What do you wish to do?: 1) Genenerate hashtags 2) Show hint list 3) Exit"))

    if(menu_option == Main_Menu.generate):
        while hashtag_count < 30:
            print()
            print("Number of hashtags generated: ", hashtag_count)
            hashtag_count += get_number(get_phrase())
            
            if hashtag_count == 30:
                print("You have successfully chosen 30 hastags. They have been written to a text file.")
                with open(os.path.join(folder, "HashEXP.txt"), "w", encoding="UTF-8") as output:
                    for hashtag in export_list:
                        output.write(hashtag + " ")
                hashtag_count = 0
                break
            
            elif hashtag_count > 30:
                print("Too many hashtags. Try again.")
                
    elif(menu_option == Main_Menu.hintlist):
        print()
        print(hint_list)

    elif(menu_option == Main_Menu.exit):
        break

