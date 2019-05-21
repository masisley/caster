from dragonfly import (Grammar, Dictation, Repeat)

from castervoice.lib import control
from castervoice.lib import settings
from castervoice.lib.dfplus.additions import IntegerRefST
from castervoice.lib.dfplus.merge import gfilter
from castervoice.lib.dfplus.merge.mergerule import MergeRule
from castervoice.lib.dfplus.state.short import R
from castervoice.lib.context import AppContext
from castervoice.lib.actions import (Key, Text)


class MyVisualStudioRule(MergeRule):
    pronunciation = "my visual studio"

    mapping = {
        "search solution [explorer]":   R(Key("c-semicolon"), rdescript="Visual Studio: Search Solution Explorer"),
        "sync":                         R(Key("c-lbracket, s"), rdescript="Visual Studio: Search Solution Explorer"),

        "references":                   R(Key("c-r, c-f"), rdescript="Visual Studio: Find all references"),
        "hierarchy":                    R(Key("c-k, c-t"), rdescript="Visual Studio: Show hierarchy"),
        "definition":                   R(Key("f12"), rdescript="Visual Studio: Go to definition"),
        "nexta [<n>]":                  R(Key("ac-pgdown"), rdescript="Visual Studio: Next Tab") * Repeat(extra="n"), 
        "prexta [<n>]":                 R(Key("ac-pgup"), rdescript="Visual Studio: Previous Tab") * Repeat(extra="n"),
        "Go back [<n>]":                R(Key("c-minus"), rdescript="Visual Studio: Go Back") * Repeat(extra="n"),
        "Go forward [<n>]":             R(Key("cs-minus"), rdescript="Visual Studio: Go Forward") * Repeat(extra="n"),
        "Goot":                         R(Key("c-t"), rdescript="Visual Studio: Go To") * Repeat(extra="n"),
        "Goot this":                    Key("right, c-left") + Key("cs-right") * Repeat(extra="n") + Key("c-c, c-t, c-v"),

        "find everywhere":
            R(Key("cs-f"), rdescript="Find Everywhere"),
        "rename":                       R(Key("c-r, c-r"), rdescript="Visual Studio: Rename"),
        "save all":                     R(Key("cs-s"), rdescript="Visual Studio: Save all"),
        "suggestion":                   R(Key("a-enter"), rdescript="Visual Studio: Alt enter"),
        "stoosh this":                  R(Key("right, c-left, cs-right, c-c"), rdescript="Visual Studio: stoosh this"),
        "clearly":                      R(Key("end, s-home, s-home, del, del"), rdescript="Visual Studio: clear line"),
    }
    extras = [
        Dictation("text"),
        Dictation("mim"),
        IntegerRefST("n", 1, 1000),
    ]
    defaults = {"n": 1, "mim": ""}


#---------------------------------------------------------------------------

context = AppContext(executable="devenv")
grammar = Grammar("My Visual Studio", context=context)

if settings.SETTINGS["apps"]["visualstudio"]:
    if settings.SETTINGS["miscellaneous"]["rdp_mode"]:
        control.nexus().merger.add_global_rule(MyVisualStudioRule())
    else:
        rule = MyVisualStudioRule(name="myvisualstudio")
        gfilter.run_on(rule)
        grammar.add_rule(rule)
        grammar.load()
