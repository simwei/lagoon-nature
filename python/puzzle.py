from enum import Enum

from typing import List, Union


class Part(Enum):
    def partner(self):
        if self.value % 2 == 0:
            return self.__class__(self.value + 1)
        else:
            return self.__class__(self.value - 1)


class Tile(List[Part]):
    #   0
    # 3   1
    #   2
    def __init__(self, list):
        super().__init__(list)
        assert len(list) == 4


def rotate(tile: Tile) -> Tile:
    return Tile([tile[3]] + tile[:3])


def rotations(tile: Tile) -> List[Tile]:
    result = []
    for i in range(0, 4):
        result.append(tile)
        tile = rotate(tile)
    return result


class Puzzle(List[Union[Tile, None]]):
    def __init__(self):
        super().__init__()

    def solution_print(self):
        assert len(self) == 9

        def pretty_print_part(part: Part):
            return part.name

        def pretty_print_tile(tile: Tile) -> str:
            return "Tile: " + " ".join(map(pretty_print_part, tile), )

        print("Found Solution:\n",
              "\n ".join(map(pretty_print_tile, self)))

    def check(self, tile):
        if len(self) in [0]:
            return True
        if len(self) in [1, 2]:
            if self[-1][1] == tile[3].partner():
                return True
            return False
        if len(self) in [3, 6]:
            if self[-3][2] == tile[0].partner():
                return True
            return False
        else:  # len(self) in [4, 5, 7, 8]:
            if self[-1][1] == tile[3].partner():
                if self[-3][2] == tile[0].partner():
                    return True
            return False

    def insert_rec(self, tiles: List[Tile]):
        if len(tiles) == 0:
            self.solution_print()
            return

        for tile in tiles:
            _tiles = tiles.copy()
            _tiles.remove(tile)
            for rotatedTile in rotations(tile):
                if self.check(rotatedTile):
                    length = len(self)
                    self.append(rotatedTile)
                    self.insert_rec(_tiles)
                    self.remove(rotatedTile)
                    assert len(self) == length

    def solve(self, deck: List[Tile]):
        self.insert_rec(deck)
