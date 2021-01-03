arr = [91,4,64,78]
pieces = [[78],[4,64],[91]]


def canFormArray():
    output = False
    length = len(arr)
    for index in range(0, length):

        used_piece = None
        for piece in pieces:
            if (piece[0] == arr[index]):
                # if it matches
                len_piece = len(piece)

                sliced_arr = arr[index : index+len_piece]

                if (sliced_arr != piece):
                    return False

                used_piece = piece
                index += len_piece - 1

        print(used_piece)
        if (used_piece != None):
            pieces.remove(used_piece)

    print(pieces)


canFormArray()

if (pieces == []):
    print(True)
else:
    print(False)





