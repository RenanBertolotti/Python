from enum import Enum,auto


class Directions(Enum):
    #right = auto()
    right = 0
    left = 1
    up = 2
    down = 3


def move(direction):
    if not isinstance(direction, Directions):
        raise ValueError("Cannot move in this direction")

    return f"Moving {direction.name}"


print(move(Directions.right))
print(move(Directions.left))
print(move(Directions.up))
print(move(Directions.down))