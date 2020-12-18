import numpy as np
#import matplotlib.pyplot as plt

NUMBER_OF_MOVES = 4

from game_functions import initialize_game, random_move, \
                            move_down, move_left,\
                            move_right, move_up,\
                            check_for_win, add_new_tile



def ai_move(board, searches_per_move, search_length):

    possible_first_moves = [move_left, move_up, move_down, move_right]
    first_move_scores = np.zeros(NUMBER_OF_MOVES)
    
    #SIMULATION PART
    for first_move_index in range(NUMBER_OF_MOVES):
        first_move_function =  possible_first_moves[first_move_index]
        board_with_first_move, first_move_made, first_move_score = first_move_function(board)

        if first_move_made:     #check if game is valid or not
            board_with_first_move = add_new_tile(board_with_first_move)
            first_move_scores[first_move_index] += first_move_score

        else:
            continue

        for _ in range(searches_per_move):
            move_number = 1
            search_board = np.copy(board_with_first_move)
            game_valid = True

            while game_valid and move_number < search_length:
                search_board, game_valid, score = random_move(search_board)
                if game_valid:
                    search_board = add_new_tile(search_board)
                    first_move_scores[first_move_index] += score
                    move_number += 1

    # SELECTION OF BEST SCORE        
    best_move_index = np.argmax(first_move_scores)
    best_move = possible_first_moves[best_move_index]
    search_board, game_valid, score = best_move(board)

    return search_board, game_valid

