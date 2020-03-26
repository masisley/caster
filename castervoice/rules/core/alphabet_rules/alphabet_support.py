from dragonfly import Choice

from castervoice.lib.actions import Key, Text


def caster_alphabet():
    return {
        "arch"    : "a",
        "brov"    : "b",
        "char"    : "c",
        "delta"   : "d",
        "echo"    : "e",
        "foxy"    : "f",
        "goof"    : "g",
        "hotel"   : "h",
        "India"   : "i",
        "julia"   : "j",
        "kilo"    : "k",
        "Lima"    : "l",
        "Mike"    : "m",
        "Novakeen": "n",
        "oscar"   : "o",
        "prime"   : "p",
        #"Quebec"  : "q",
        "Romeo"   : "r",
        "Sierra"  : "s",
        "tango"   : "t",
        "uniform" : "u",
        "victor"  : "v",
        "whiskey" : "w",
        "x-ray"   : "x",
        "yankee"  : "y",
        "Zulu"    : "z",
        #"air"     : "a",
        "bat"    : "b",
        "cap"    : "c",
        "drum"   : "d",
        "each"    : "e",
        "Fist"    : "f",
        #"gust"    : "g",
        "harp"   : "h",
        "sit"   : "i",
        "jury"   : "j",
        "kin"    : "k",
        "look"    : "l",
        #"made"    : "m",
        "near": "n",
        "odd"   : "o",
        "pit"   : "p",
        "quinn"  : "q",
        "red"   : "r",
        "sun"  : "s",
        "trap"   : "t",
        "urge" : "u",
        "vest"  : "v",
        "whale" : "w",
        "plex"   : "x",
        "yank"  : "y",
        "Zip"    : "z",
        "zero"  : "0",
        "one"  : "1",
        "torque"  : "2",
        "three"  : "3",
        "fairn"  : "4",
        "five"  : "5",
        "six"  : "6",
        "seven"  : "7",
        "eight"  : "8",
        "nine"  : "9",
    }


def get_alphabet_choice(spec):
    return Choice(spec, caster_alphabet())


def letters(big, dict1, dict2, letter):
    '''used with alphabet.txt'''
    d1 = str(dict1)
    if d1 != "":
        Text(d1).execute()
    if big:
        Key("shift:down").execute()
    letter.execute()
    if big:
        Key("shift:up").execute()
    d2 = str(dict2)
    if d2 != "":
        Text(d2).execute()


def letters2(big, letter):
    if big:
        Key(letter.capitalize()).execute()
    else:
        Key(letter).execute()


'''for fun'''


def elite_text(text):
    elite_map = {
        "a": "@",
        "b": "|3",
        "c": "(",
        "d": "|)",
        "e": "3",
        "f": "|=",
        "g": "6",
        "h": "]-[",
        "i": "|",
        "j": "_|",
        "k": "|{",
        "l": "|_",
        "m": r"|\/|",
        "n": r"|\|",
        "o": "()",
        "p": "|D",
        "q": "(,)",
        "r": "|2",
        "s": "$",
        "t": "']['",
        "u": "|_|",
        "v": r"\/",
        "w": r"\/\/",
        "x": "}{",
        "y": "`/",
        "z": r"(\)"
    }
    text = str(text).lower()
    result = ""
    for c in text:
        if c in elite_map:
            result += elite_map[c]
        else:
            result += c
    Text(result).execute()
