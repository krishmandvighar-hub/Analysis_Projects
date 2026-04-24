'''
LIST = []

CHOOSE ANY OPTION (1 FOR ADD, 2 FOR REMOVE, 3 FOR UPDATE, 4 FOR CLEAR ITEMS )

1-- ENTER ANY ADD ITEM
2. -- ENTER ANY INDEX NUMBER FOR REMOVE
3. -- ENTER ANY INDEX NUMBER FOR UPDATE
	-- ENTER NEW ITEMS
    
 4. ALL CLEAR ITEMS
- PLZ CHOOSE RIGHT OPTION
'''


LIST = []

while True:
    print("1 FOR ADD, 2 FOR REMOVE, 3 FOR UPDATE, 4 FOR CLEAR ITEMS 5 show list 6 exit")
    num=int(input("CHOSE ANY FROM THESE: "))
    match num:
        case 1:
            num1=int(input("chose how many you wanted to add: "))
            for x in range(0,num1):
                list1=input("enter item name: ")
                LIST.append(list1)
        case 2:
            if len(LIST) == 0:
                print("No item to remove")
            else: 
                list2=input("enter remove name: ")
                LIST.remove(list2)
        case 3:
            if len(LIST) == 0:
                print("No item to update")
            else :   
                index=int(input("enter index: "))
                if 0<= index < len(LIST):
                    add=input("enter replace item name: ")
                    LIST[index] = add

        case 4:
            LIST.clear()
        
        case 5:
            print("MY LIST",LIST)
        case 6:
            print("BYE.. ")
            break
        case _:
            print("invalid")
        
    
        









        
