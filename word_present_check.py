txt_file = input("Enter the location of txt to check:\t")
try:
    with open(txt_file,"r") as rode:
        readlines= rode.readlines()
        
        ask = input("Enter the word/sentence to check weather there is present or not:\t").upper()
        valid_present=False
        #To read each lines
        print("First checking through sentence>..............\n")
        for lines in readlines:
            if ask in lines:
                print(f"Your input \"{ask}\" is present in \"{txt_file}\"\n")
                valid_present=True
                break
            else :
                words = lines.split(' ')
                for word in words:
                    if ask in word.upper():
                        print("Now going through each words>..............\n")
                        print(f"Your word \"{ask} \" is present in \"{txt_file}\"\n")
                        valid_present=True
                        break
                if not valid_present:    
                        input_split = (ask.split(" "))
                        for input_split0 in input_split:
                            if input_split0 in words:
                                print("Now going through each words again>.............\n")
                                print(f"Your word \"{input_split0} \" is present in \"{txt_file}\"\n")
                                valid_present=True
                                break


        if not valid_present:print(f"No there is no \"{ask}\" in file {txt_file}")

except Exception as e:
    print(f"Sorry No file Found as {txt_file}")
                
input("presss enter to end:   ")    
    