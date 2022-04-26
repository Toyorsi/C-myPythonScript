def printTable(theList, rightspace, leftspace):
    print('PICNIC ITEMS'.center(rightspace+leftspace, '-'))
    for k, v in theList.items():
          print(k.ljust(leftspace, '.') + str(v).rjust(rightspace))

picnicItem = {'Banana': 20, 'Orange': 30, 'Coccumber': 12, 'Carrot': 18}
printTable(picnicItem, 6, 8)
printTable(picnicItem, 10, 12)
