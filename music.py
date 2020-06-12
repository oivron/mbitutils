"""
Module music.
"""


DADADADUM = "DADADADUM"
ENTERTAINER = "ENTERTAINER"
PRELUDE = "PRELUDE"
ODE = "ODE"
NYAN = "NYAN"
RINGTONE = "RINGTONE"
FUNK = "FUNK"
BLUES = "BLUES"
BIRTHDAY = "BIRTHDAY"
WEDDING = "WEDDING"
FUNERAL = "FUNERAL"
PUNCHLINE = "PUNCHLINE"
PYTHON = "PYTHON"
BADDY = "BADDY"
CHASE = "CHASE"
BA_DING = "BA_DING"
WAWAWAWAA = "WAWAWAWAA"
JUMP_UP = "JUMP_UP"
JUMP_DOWN = "JUMP_DOWN"
POWER_UP = "POWER_UP"
POWER_DOWN = "POWER_DOWN"


def play(*args):
    """Plays a melody or a tune. Either:
    music.play(music.BIRTHDAY)
    or one of the other built-in melodies.
    Or:
    music.play(tune)
    where tune is a list of notes, its octave and its duration.
    "C2:4" is the note C in octave number 2 to be played for a duration of 4.
    """
    

def pitch(frequency, duration):
    """Plays a pitch of frequency for a number of milliseconds."""
    

def stop():
    """Stops all music playback.
    """
