from typing import Tuple

import numpy as np

# Tile graphics structured
graphic_dt = np.dtype(
    [
        ("ch", np.int32), #Unicode
        ("fg", "3B"), #3 Bytes for RGB
        ("bg", "3B")
    ]
)

tile_dt = np.dtype(
    [
        ("walkable", np.bool),
        ("transparent", np.bool),
        ("dark", graphic_dt), #Graphics for when not in fov
        ("light", graphic_dt) #Grapchics for when in fov
     ]
)

def new_tile(
    walkable: int,
    transparent: int,
    dark: Tuple[int, Tuple[int, int, int], Tuple[int, int, int]],
    light: Tuple[int, Tuple[int, int, int], Tuple[int, int, int]],
) -> np.ndarray:
    return np.array((walkable, transparent, dark, light), dtype=tile_dt)

#SHROUD for unexplored and unseen tiles. Also has sick aim.
SHROUD = np.array((ord(" "), (255, 255, 255), (0, 0, 0)), dtype=graphic_dt)

floor = new_tile(
    walkable=True,
    transparent=True,
    dark=(ord("."), (200, 200, 200), (50, 50, 150)),
    light=(ord("."), (255, 255, 255), (200, 180, 50)),
)

wall = new_tile(
    walkable=False,
    transparent=False,
    dark=(ord("#"), (200, 200, 200), (0, 0, 100)),
    light=(ord("#"), (255, 255, 255), (130, 110, 50))
)