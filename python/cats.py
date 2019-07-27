from typing import List

from puzzle import Part, Tile, Puzzle


class CatPart(Part):
    PantherHead = 0
    PantherTail = 1
    LionHead = 2
    LionTail = 3
    TigerHead = 4
    TigerTail = 5
    GepardHead = 6
    GepardTail = 7


deck: List[Tile] = [
    Tile([CatPart.GepardTail, CatPart.TigerTail, CatPart.LionHead, CatPart.TigerHead]),
    Tile([CatPart.GepardHead, CatPart.LionTail, CatPart.PantherHead, CatPart.GepardTail]),
    Tile([CatPart.PantherTail, CatPart.PantherHead, CatPart.GepardTail, CatPart.TigerHead]),
    Tile([CatPart.LionTail, CatPart.LionHead, CatPart.TigerTail, CatPart.GepardHead]),
    Tile([CatPart.PantherTail, CatPart.LionHead, CatPart.PantherHead, CatPart.GepardTail]),
    Tile([CatPart.TigerHead, CatPart.GepardHead, CatPart.LionTail, CatPart.TigerHead]),
    Tile([CatPart.TigerTail, CatPart.TigerTail, CatPart.LionHead, CatPart.PantherHead]),
    Tile([CatPart.GepardHead, CatPart.PantherTail, CatPart.LionTail, CatPart.PantherTail]),
    Tile([CatPart.PantherHead, CatPart.LionTail, CatPart.GepardHead, CatPart.TigerHead]),
]

Puzzle().solve(deck)
