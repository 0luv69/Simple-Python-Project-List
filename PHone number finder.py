print("\nThis program is dedicated to find your number's company \n\t\tEither [Ncell/ Namesta]")
access = "Y"
while (access == "Y"):
    number = int(input("\nEnter your 10 diget number\t"))
    division0 = str(number)
    division1 = division0[2]
    division2 = int(division1)
    if division2 == 4 or division2 == 5 or int(division0[1]) ==7:
        print("The number that you have entered is of NAMESTA")    
    elif division2== 1 or division2==2 or division2==0:
        print("the number that you have entered is NCELL ")
    else:
        print("The number that you entered is new number of ntc or wrong number")
    access = input('Do you want to continue the press y or else type n').upper()        

exit = input('Press enter to exit')    



