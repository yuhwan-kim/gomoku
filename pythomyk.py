import numpy as np
board_size = 15
board_array = np.zeros([board_size, board_size])

turns = board_size * board_size

for i in range(turns):

    if i / 2 - - 0:
        position = input('Black Turn:')

        sub_p = position.split(' ')
        pos_X = int(sub_p[0])
        pos_Y = int(sub_p[1])

        board_array[pos_Y, pos_X] = 1

    else:
        position = input('White Turn:')

        sub_p = position.split(' ')
        pos_X = int(sub_p[0])
        pos_Y = int(sub_p[1])

        board_array[pos_Y, pos_X] = 2

    print(board_array)



