# ba_meta require api 9

import babase


# ba_meta export babase.Plugin
class MovementHelper(babase.Plugin):

    def on_app_running(self) -> None:
        babase.screenmessage(
            "Movement Helper enabled",
            color=(0.4, 1.0, 0.4)
        )
