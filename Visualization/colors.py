from colour import Color

DARK_GRAY = '#65696B'
LIGHT_GRAY = '#C4C5BF'
BLUE = '#0CA8F6'
DARK_BLUE = '#4204CC'
WHITE = '#FFFFFF'
BLACK = '#000000'
RED = '#F22810'
YELLOW = '#F7E806'
PINK = '#F50BED'
LIGHT_GREEN = '#05F50E'
PURPLE = '#BF01FB'

def generate_gradient(n):
    blue = Color('blue')
    colors = list(blue.range_to(Color('red'), n))

    res = [color.hex for color in colors]
    return res
generate_gradient(10)