# #  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable, hash_table_insert)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(length)

    temp_length = 0
    arr = []

    while temp_length < length:
        diff = limit - weights[temp_length]
        for (i, v) in enumerate(weights):
            hash_table_insert(ht, v, i)
            if diff == weights[i] and temp_length != i:
                arr.append(i)

        temp_length += 1

    if len(arr) == 0:
        return None
    return arr


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
