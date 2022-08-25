
    largest = -1
    smallest = None
    while True:
        num = input('enter a number:')
        if num == 'done':
            break
        try:
            inum = int(num)
        except:
            print('Invalid input')
            continue
        if  smallest is None:
            smallest = inum
        elif inum < smallest:
            smallest = inum
        elif inum > largest:
            largest = inum

    print('Maximum is', largest)
    print('Minimum is', smallest)
