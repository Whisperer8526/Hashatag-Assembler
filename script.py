with open("Hash.txt", "r", encoding="UTF-8") as hashtagsAll:
    hashtagsUnique = set(hashtagsAll.read().split())

hashtagList = []
hintList = ["moody", "dark", "portrait", "portret", "poland", "polska"]
hashtagCount = 0
menuChoice = 0

Main_Menu = IntEnum("Main_Menu", "generate hintlist exit")

while True:
    print()
    menuChoice = int(input("What do you wish to do?: 1) Genenerate hashtags 2) Show hint list 3) Exit"))

    if(menuChoice == Main_Menu.generate):
        while hashtagCount < 30:
            print()
            print("Number of hashtags generated: ", hashtagCount)
            hashtagCount += how_many_hashtags(choose_phrase())
            
            if hashtagCount == 30:
                print("You have successfully chosen 30 hastags. They have been written to a text file.")
                with open("HashEXP.txt", "w", encoding="UTF-8") as hashtagsExport:
                    for hashtag in hashtagList:
                        hashtagsExport.write(hashtag + " ")
                hashtagCount = 0
                break
            
            elif hashtagCount > 30:
                print("Too many hashtags. Try again.")
                
    elif(menuChoice == Main_Menu.hintlist):
        print()
        print(hintList)

    elif(menuChoice == Main_Menu.exit):
        break
