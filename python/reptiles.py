from typing import List

from puzzle import Part, Tile, Puzzle


class LizardPart(Part):
    BlueHead = 0
    BlueTail = 1
    OrangeHead = 2
    OrangeTail = 3
    BlackHead = 4
    BlackTail = 5
    GreenHead = 6
    GreenTail = 7


deck: List[Tile] = [
    Tile([LizardPart.BlueHead, LizardPart.BlueTail, LizardPart.OrangeTail, LizardPart.BlackTail]),
    Tile([LizardPart.GreenTail, LizardPart.BlueHead, LizardPart.GreenTail, LizardPart.BlackTail]),
    Tile([LizardPart.OrangeHead, LizardPart.GreenHead, LizardPart.BlueHead, LizardPart.BlackTail]),
    Tile([LizardPart.BlackTail, LizardPart.BlueHead, LizardPart.GreenHead, LizardPart.BlackHead]),
    Tile([LizardPart.BlueTail, LizardPart.GreenHead, LizardPart.OrangeTail, LizardPart.OrangeTail]),
    Tile([LizardPart.BlackHead, LizardPart.GreenTail, LizardPart.BlueTail, LizardPart.GreenHead]),
    Tile([LizardPart.GreenHead, LizardPart.BlackHead, LizardPart.OrangeHead, LizardPart.GreenTail]),
    Tile([LizardPart.BlueHead, LizardPart.OrangeHead, LizardPart.OrangeHead, LizardPart.BlackTail]),
    Tile([LizardPart.OrangeTail, LizardPart.BlueTail, LizardPart.OrangeHead, LizardPart.BlackHead]),
]

Puzzle().solve(deck)
