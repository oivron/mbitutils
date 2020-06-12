"""
Module speech.
"""


def translate(words):
    """Translate text string to phonemes.
    Returns a string.
    """
    return ""


def  pronounce(*args):
    """Pronounce the phonemes in a string. Either:
    speech.pronounce(phonemes)
    Or:
    speech.pronounce(phonemes, pitch, speed, throat, mouth)
    Pitch, speed, throat and mouth should have a value between 0 and 255.
    """


def say(*args):
    """Say the English words in the string. Either:
    speech.say(words)
    Or:
    speech.say(words, speed, pitch, throat, mouth)
    where pitch, speed, throat and mouth should have a value between 0 and 255.
    """


def sing(*args):
    """Sing the phonemes contained in a string. Either:
    speech.sing(phonemes)
    Or:
    speech.sing(phonemes, pitch, speed, throat, mouth)
    where pitch, speed, throat and mouth should have a value between 0 and 255.
    """
