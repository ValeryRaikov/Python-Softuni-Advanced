# Structures for the mills game:

# Valid board positions:
POSITIONS = {
    # main diagonal:
    'a': (0, 0), 
    'b': (1, 1), 
    'c': (2, 2),
    'd': (4, 4), 
    'e': (5, 5),
    'f': (6, 6),
    
    # vertical line:
    'g': (0, 3),
    'h': (1, 3),
    'i': (2, 3),
    'j': (4, 3),
    'k': (5, 3),
    'l': (6, 3),
    
    # secondary diagonal:
    'm': (0, 6),
    'n': (1, 5),
    'o': (2, 4),
    'p': (4, 2),
    'q': (5, 1),
    'r': (6, 0),
    
    # horizontal line:
    's': (3, 0),
    't': (3, 1),
    'u': (3, 2),
    'v': (3, 4),
    'w': (3, 5),
    'x': (3, 6),
}

#                 primary positions    horizontal positions   vertical positions
KEY_POSITIONS = (('h', 't', 'k', 'w'), ('g', 'i', 'j', 'd'), ('s', 't', 'w', 'x'))

DIRECTIONS = (
    (0, -1), #left
    (0, 1),  #right
    (-1, 0), #up
    (1, 0),  #down
)