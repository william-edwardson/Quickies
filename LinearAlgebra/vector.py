class Vector(object):
    def __init__(self, coordinates):
        try:
            # no blank initialisations
            if not coordinates:
                raise ValueError
            # set the coordinates and the dimension
            self.coordinates = tuple(coordinates)
            self.dimension = len(coordinates)
        # Value error
        except ValueError:
            raise ValueError('Cannot initialise with empty coordinates!')
        # Type error
        except TypeError:
            raise TypeError('The coordinates must be iterable')

# text output
def __str__(self):
    return 'Vector: {}'.format(self.coordinates)

# check for equality
def __eq__(self, v):
    return self.coordinates == v.coordinates