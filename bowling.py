def score(game):
    '''Get overall score of game from string.
    Args:
        game: rolls
    Returns: result/score'''
    if game[-3].lower() == 'x':
        return how_to_count(game, len(game) - 2)  # discounting extra rolls that are strikes
    else:
        return how_to_count(game, len(game))


def how_to_count(game, length):
    '''Get the values of the rolls in the game and adds them into overall score.
    Args:
        game: rolls
        length: the number of rolls to evaluate)
    Returns: score'''
    result = 0
    for i in range(length):
        if game[i] == '/':  # get a (10+next score) but discount previous roll
            result += get_value(game[i]) + get_value(game[i+1]) - get_value(game[i-1])
        elif game[i].lower() == 'x':  # get (10+next two rolls)
            result += get_value(game[i]) + get_value(game[i+1]) + get_value(game[i+2])
            if game[i+2] == '/':
                result -= get_value(game[i+1])
        else:
            result += get_value(game[i])
    return result


def get_value(char):
    '''Get the values of individual rolls/characters in string
    Args:
        char: char to be examined in game string
    Returns: int value'''
    if char in str([i for i in range(1, 10)]):
        return int(char)
    elif char.lower() == 'x' or char == '/':
        return 10
    elif char == '-':
        return 0
    else:
        raise ValueError()
