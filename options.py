class Options():
    # also figure out a way to make this code easier to update ig
    # 1 - reveal invites (don't obfuscate them)
    # 2 - ping the target on mod events

    def __init__(self, value):
        self.reveal_invites: value & 0b01 == 0b01
        self.ping_target: value & 0b10 == 0b10