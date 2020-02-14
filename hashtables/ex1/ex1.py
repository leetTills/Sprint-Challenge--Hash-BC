#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    """
    YOUR CODE HERE
    """

     
    for i in range(length):
        item = weights[i]
        hash_table_insert(ht, key = item, value = i)

    
    for i in range(length):
        item = weights[i]
        if item < limit:
           
            match = limit - item
            match_i = hash_table_retrieve(ht, match)
            
            if match_i is None:
                continue
            elif match_i >= 0 and match_i != i:
                if match_i >= i:
                    return (match_i, i)
                else:
                    return (i, match_i)

    return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
