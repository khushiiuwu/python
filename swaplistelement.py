def swapList(list,pos1,pos2):
    list[pos1], list[pos2] = list[pos2], list[pos1]
    return list

List = [11,12,13,14,15,16]
print(List)

while True:
    try:
        pos1 = int(input("Enter the element 1 you want to swapped"))
        pos2 = int(input("Enter the element 2 you want to swapped"))

        if pos1 < 0 or pos1 > 6 & pos2< 0 or pos2 > 6:
            raise ValueError #will send it to the print message and back to the input option
        break
    except ValueError:
        print("The number must be in the range of 0-5.")
print(swapList(List, pos1, pos2))