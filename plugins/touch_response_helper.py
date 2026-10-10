# ba_meta require api 9

import babase
import bascenev1 as bs
from bascenev1lib.actor.spaz import Spaz


SPEED_MULTIPLIER = 1.15

_original_on_move = Spaz.on_move


def faster_on_move(self, x: float, y: float) -> None:
    _original_on_move(
        self,
        x * SPEED_MULTIPLIER,
        y * SPEED_MULTIPLIER,
    )


Spaz.on_move = faster_on_move


# ba_meta export babase.Plugin
class TouchResponseHelper(babase.Plugin):

    def on_app_running(self) -> None:
        babase.screenmessage(
            "Movement Boost 1.15x enabled",
            color=(0.4, 1.0, 0.4)
        )
        
