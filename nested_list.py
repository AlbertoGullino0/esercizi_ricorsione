def count_leaf_nodes(input_list):
    #terminale
    if len(input_list) == 0:
        return 0
    #non terminale
    else:
        counter = 0
        for element in input_list:
            #controllo se è una lista
            #se è una lista contiamo i suoi elementi con una ricorsione
            if type(element) == list:
                counter += count_leaf_nodes(element)
            #altrimenti incrementiamo di 1 il counter
            else:
                counter += 1
        return counter

if __name__ == '__main__':
    input_list =  ['Adam', ['Bob', ['Chet', 'Cat'], 'Barb', 'Bert'], 'Alex', ['Bea', 'Bill'], 'Ann']
    print(count_leaf_nodes(input_list)) #we expect 10
def count_leaf_nodes(input_list):
    #terminale
    if len(input_list) == 0:
        return 0
    # non terminale
    else:
        counter = 0
        for element in input_list:
            #check if element is a list
            # if it is a list, we count its elements
            # with a recursion
            if type(element) == list:
                counter += count_leaf_nodes(element)
            # else, we add +1
            else:
                counter += 1
        return counter


if __name__ == '__main__':
    names = ['Adam', ['Bob', ['Chet', 'Cat'], 'Barb', 'Bert'], 'Alex', ['Bea', 'Bill'], 'Ann']
    print(count_leaf_nodes(names)) #we expect 10