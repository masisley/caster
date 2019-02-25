'''
Created on Sep 1, 2015

@author: synkarius
'''
from dragonfly import Repeat, Function, Dictation, Choice, MappingRule

from castervoice.lib import context, navigation, alphanumeric, textformat, text_utils
from castervoice.lib import control
from castervoice.lib.actions import Key, Mouse
from castervoice.lib.dfplus.additions import IntegerRefST
from castervoice.lib.dfplus.merge.ccrmerger import CCRMerger
from castervoice.lib.dfplus.merge.mergerule import MergeRule
from castervoice.lib.dfplus.state.actions import AsynchronousAction, ContextSeeker
from castervoice.lib.dfplus.state.actions2 import UntilCancelled
from castervoice.lib.dfplus.state.short import L, S, R
from dragonfly.actions.action_mimic import Mimic
from castervoice.lib.ccr.standard import SymbolSpecs

_NEXUS = control.nexus()


class NavigationNon(MappingRule):
    mapping = {
        "<direction> <time_in_seconds>":
            AsynchronousAction(
                [L(S(["cancel"], Key("%(direction)s"), consume=False))],
                repetitions=1000,
                blocking=False),
        "erase multi clipboard":
            R(Function(navigation.erase_multi_clipboard, nexus=_NEXUS),
              rdescript="Erase Multi Clipboard"),
        "find":
            R(Key("c-f"), rdescript="Find"),
        "find next [<n>]":
            R(Key("f3"), rdescript="Find Next")*Repeat(extra="n"),
        "find prior [<n>]":
            R(Key("s-f3"), rdescript="Find Prior")*Repeat(extra="n"),
        "find everywhere":
            R(Key("cs-f"), rdescript="Find Everywhere"),
        "replace":
            R(Key("c-h"), rdescript="Replace"),
        "(F to | F2)":
            R(Key("f2"), rdescript="Key: F2"),
        "(F six | F6)":
            R(Key("f6"), rdescript="Key: F6"),
        "(F nine | F9)":
            R(Key("f9"), rdescript="Key: F9"),
        "[show] context menu":
            R(Key("s-f10"), rdescript="Context Menu"),
        "squat":
            R(Function(navigation.left_down, nexus=_NEXUS), rdescript="Mouse: Left Down"),
        "kick mid":
            R(Function(navigation.middle_click, nexus=_NEXUS),
              rdescript="Mouse: Middle Click"),
        "psychic":
            R(Function(navigation.right_click, nexus=_NEXUS),
              rdescript="Mouse: Right Click"),
        "shift right click":
            R(Key("shift:down") + Mouse("right") + Key("shift:up"),
              rdescript="Mouse: Shift + Right Click"),
        "curse <direction> [<direction2>] [<nnavi500>] [<dokick>]":
            R(Function(navigation.curse), rdescript="Curse"),
        "scree <direction> [<nnavi500>]":
            R(Function(navigation.wheel_scroll), rdescript="Wheel Scroll"),
        "colic":
            R(Key("control:down") + Mouse("left") + Key("control:up"),
              rdescript="Mouse: Ctrl + Left Click"),
        "garb [<nnavi500>]":
            R(Mouse("left") + Mouse("left") + Function(
                navigation.stoosh_keep_clipboard,
                nexus=_NEXUS),
              rdescript="Highlight @ Mouse + Copy"),
        "drop [<nnavi500>]":
            R(Mouse("left") + Mouse("left") + Function(
                navigation.drop_keep_clipboard,
                nexus=_NEXUS,
                capitalization=0,
                spacing=0),
              rdescript="Highlight @ Mouse + Paste"),
        # My edits #
        "shift click":
            R(Key("shift:down") + Mouse("left") + Key("shift:up"),
              rdescript="Mouse: Shift + Left Click"),
        "(queue this | select this)":       R(Key("right, c-left, cs-right"), rdescript="Select this"),
        "(copy this)":       R(Key("right, c-left, cs-right, c-c"), rdescript="Copy this"),
        "Stab [<n>]": R(Key("s-tab"), rdescript="Shift tab") * Repeat(extra="n"),
        "(soap | calm) [<n>]":                  R(Key("pgup"), rdescript="Page Up") * Repeat(extra="n"),
        "(dope | peace) [<n>]":                  R(Key("pgdown"), rdescript="Page Down") * Repeat(extra="n"),        
        # End my edits #

        "sure spark":
            R(Key("c-v"), rdescript="Simple Paste"),
        "undo [<n>]":
            R(Key("c-z"), rdescript="Undo")*Repeat(extra="n"),
        "redo [<n>]":
            R(Key("c-y"), rdescript="Redo")*Repeat(extra="n"),
        "refresh":
            R(Key("c-r"), rdescript="Refresh"),
        "maxiwin":
            R(Key("w-up"), rdescript="Maximize Window"),
        "move window":
            R(Key("a-space, r, a-space, m"), rdescript="Move Window"),
        "window (left | lease) [<n>]":
            R(Key("w-left"), rdescript="Window Left")*Repeat(extra="n"),
        "window (right | ross) [<n>]":
            R(Key("w-right"), rdescript="Window Right")*Repeat(extra="n"),
        "monitor (left | lease) [<n>]":
            R(Key("sw-left"), rdescript="Monitor Left")*Repeat(extra="n"),
        "monitor (right | ross) [<n>]":
            R(Key("sw-right"), rdescript="Monitor Right")*Repeat(extra="n"),
        "desktop (left | lease) [<n>]":
            R(Key("cw-left"), rdescript="Desktop Left")*Repeat(extra="n"),
        "desktop (right | ross) [<n>]":
            R(Key("cw-right"), rdescript="Desktop Right")*Repeat(extra="n"),
        "(next | prior) window":
            R(Key("ca-tab, enter"), rdescript="Next Window"),
        "switch (window | windows)":
            R(Key("ca-tab"), rdescript="Switch Window")*Repeat(extra="n"),
        "next tab [<n>]":
            R(Key("c-pgdown"), rdescript="Next Tab")*Repeat(extra="n"),
        "prior tab [<n>]":
            R(Key("c-pgup"), rdescript="Previous Tab")*Repeat(extra="n"),
        "close tab [<n>]":
            R(Key("c-w/20"), rdescript="Close Tab")*Repeat(extra="n"),
        "elite translation <text>":
            R(Function(alphanumeric.elite_text), rdescript="1337 Text"),
    }

    extras = [
        Dictation("text"),
        Dictation("mim"),
        IntegerRefST("n", 1, 50),
        IntegerRefST("nnavi500", 1, 500),
        Choice("time_in_seconds", {
            "super slow": 5,
            "slow": 2,
            "normal": 0.6,
            "fast": 0.1,
            "superfast": 0.05
        }),
        navigation.get_direction_choice("direction"),
        navigation.get_direction_choice("direction2"),
        navigation.TARGET_CHOICE,
        Choice("dokick", {
            "kick": 1,
            "psychic": 2
        }),
        Choice("wm", {
            "ex": 1,
            "tie": 2
        }),
    ]
    defaults = {
        "n": 1,
        "mim": "",
        "nnavi500": 1,
        "direction2": "",
        "dokick": 0,
        "text": "",
        "wm": 2
    }


class Navigation(MergeRule):
    non = NavigationNon
    pronunciation = CCRMerger.CORE[1]

    mapping = {
    # "periodic" repeats whatever comes next at 1-second intervals until "cancel" is spoken or 100 tries occur
        "periodic":
            ContextSeeker(forward=[L(S(["cancel"], lambda: None),
            S(["*"], lambda fnparams: UntilCancelled(Mimic(*filter(lambda s: s != "periodic", fnparams)), 1).execute(),
            use_spoken=True))]),
    # VoiceCoder-inspired -- these should be done at the IDE level
        "fill <target>":
            R(Key("escape, escape, end"), show=False) +
            AsynchronousAction([L(S(["cancel"], Function(context.fill_within_line, nexus=_NEXUS)))],
            time_in_seconds=0.2, repetitions=50, rdescript="Fill" ),
        "jump in":
            AsynchronousAction([L(S(["cancel"], context.nav, ["right", "(~[~{~<"]))],
            time_in_seconds=0.1, repetitions=50, rdescript="Jump: In"),
        "jump out":
            AsynchronousAction([L(S(["cancel"], context.nav, ["right", ")~]~}~>"]))],
            time_in_seconds=0.1, repetitions=50, rdescript="Jump: Out"),
        "jump back":
            AsynchronousAction([L(S(["cancel"], context.nav, ["left", "(~[~{~<"]))],
            time_in_seconds=0.1, repetitions=50, rdescript="Jump: Back"),
        "jump back in":
            AsynchronousAction([L(S(["cancel"], context.nav, ["left", "(~[~{~<"]))],
            finisher=Key("right"), time_in_seconds=0.1, repetitions=50, rdescript="Jump: Back In" ),

    # keyboard shortcuts
        'save':
            R(Key("c-s"), rspec="save", rdescript="Save"),
        'shock [<nnavi50>]':
            R(Key("enter"), rspec="shock", rdescript="Enter")* Repeat(extra="nnavi50"),

        "(<mtn_dir> | <mtn_mode> [<mtn_dir>]) [(<nnavi500> | <extreme>)]":
            R(Function(text_utils.master_text_nav), rdescript="Keyboard Text Navigation"),

        "shift click":
            R(Key("shift:down") + Mouse("left") + Key("shift:up"),
              rdescript="Mouse: Shift Click"),
    
        "stoosh [<nnavi500>]":
            R(Function(navigation.stoosh_keep_clipboard, nexus=_NEXUS), rspec="stoosh", rdescript="Copy"),
        "cut [<nnavi500>]":
            R(Function(navigation.cut_keep_clipboard, nexus=_NEXUS), rspec="cut", rdescript="Cut"),
        "spark [<nnavi500>] [(<capitalization> <spacing> | <capitalization> | <spacing>) (bow|bowel)]":
            R(Function(navigation.drop_keep_clipboard, nexus=_NEXUS), rspec="spark", rdescript="Paste"),

        "splat [<splatdir>] [<nnavi10>]":
            R(Key("c-%(splatdir)s"), rspec="splat", rdescript="Splat") * Repeat(extra="nnavi10"),
        "deli [<nnavi50>]":
            R(Key("del/5"), rspec="deli", rdescript="Delete") * Repeat(extra="nnavi50"),
        "clear [<nnavi50>]":
            R(Key("backspace/5:%(nnavi50)d"), rspec="clear", rdescript="Backspace"),
        SymbolSpecs.CANCEL:
            R(Key("escape"), rspec="cancel", rdescript="Cancel Action"),


        "shackle":
            R(Key("home/5, s-end"), rspec="shackle", rdescript="Select Line"),
        "(tell | tau) <semi>":
            R(Function(navigation.next_line), rspec="tell dock", rdescript="Complete Line"),
        "duple [<nnavi50>]":
            R(Function(navigation.duple_keep_clipboard), rspec="duple", rdescript="Duplicate Line"),
        "Kraken":
            R(Key("c-space"), rspec="Kraken", rdescript="Control Space"),

    "shin dope [<nnavi50>]":         R(Key("s-pgdown"), rdescript="Select page down") * Repeat(extra="nnavi50"), 
    "shin soap [<nnavi50>]":           R(Key("s-pgup"), rdescript="Select page up") * Repeat(extra="nnavi50"),

    "kick":
        R(Function(navigation.left_click, nexus=_NEXUS),
            rdescript="Mouse: Left Click"),
    "(kick double|double kick|slam)":
        R(Function(navigation.left_click, nexus=_NEXUS)*Repeat(2),
        rdescript="Mouse: Double Click"),
    "bench":
        R(Function(navigation.left_up, nexus=_NEXUS), rdescript="Mouse: Left Up"),

    # text formatting
        "set [<big>] format (<capitalization> <spacing> | <capitalization> | <spacing>) (bow|bowel)":
            R(Function(textformat.set_text_format), rdescript="Set Text Format"),
        "clear castervoice [<big>] formatting":
            R(Function(textformat.clear_text_format), rdescript="Clear Caster Formatting"),
        "peek [<big>] format":
            R(Function(textformat.peek_text_format), rdescript="Peek Format"),
        "(<capitalization> <spacing> | <capitalization> | <spacing>) (bow|bowel) <textnv> [brunt]":
            R(Function(textformat.master_format_text), rdescript="Text Format"),
        "[<big>] format <textnv>":
            R(Function(textformat.prior_text_format), rdescript="Last Text Format"),
        "<word_limit> [<big>] format <textnv>":
            R(Function(textformat.partial_format_text), rdescript="Partial Text Format"),

        "hug <enclosure>":
            R(Function(text_utils.enclose_selected), rdescript="Enclose text "),
        "dredge":
            R(Key("a-tab"), rdescript="Alt-Tab"),

    "tit <textnv>":  R(Function(textformat.custom_format_text, capitalization2=2, spacing2=0), rdescript="Text Format"),
    "tin <textnv>": R(Function(textformat.custom_format_text, capitalization2=2, spacing2=1), rdescript="Text Format"),

    "lit <textnv>": R(Function(textformat.custom_format_text, capitalization2=5, spacing2=0), rdescript="Text Format"),
    "lin <textnv>": R(Function(textformat.custom_format_text, capitalization2=5, spacing2=1), rdescript="Text Format"),

    "sit <textnv>": R(Function(textformat.custom_format_text, capitalization2=4, spacing2=0), rdescript="Text Format"),
    "shout <textnv>": R(Function(textformat.custom_format_text, capitalization2=1, spacing2=1), rdescript="Text Format"),
    "camel <textnv>": R(Function(textformat.custom_format_text, capitalization2=3, spacing2=1), rdescript="Text Format"),

    }

    extras = [
        IntegerRefST("nnavi10", 1, 11),
        IntegerRefST("nnavi50", 1, 50),
        IntegerRefST("nnavi500", 1, 500),
        Dictation("textnv"),
        Choice(
            "enclosure", {
                "prekris": "(~)",
                "angle": "<~>",
                "curly": "{~}",
                "brax": "[~]",
                "thin quotes": "'~'",
                'quotes': '"~"',
            }),
        Choice("capitalization", {
            "yell": 1,
            "tie": 2,
            "Gerrish": 3,
            "sing": 4,
            "laws": 5
        }),
        Choice(
            "spacing", {
                "gum": 1,
                "gun": 1,
                "spine": 2,
                "snake": 3,
                "pebble": 4,
                "incline": 5,
                "dissent": 6,
                "descent": 6
            }),
        Choice("semi", {
            "dock": ";",
            "doc": ";",
            "sink": ""
        }),
        Choice("word_limit", {
            "single": 1,
            "double": 2,
            "triple": 3,
            "Quadra": 4
        }),
        navigation.TARGET_CHOICE,
        navigation.get_direction_choice("mtn_dir"),
        Choice("mtn_mode", {
            "shin": "s",
            "queue": "cs",
            "fly": "c",
        }),
        Choice("extreme", {
            "Wally": "way",
        }),
        Choice("big", {
            "big": True,
        }),
        Choice("splatdir", {
            "lease": "backspace",
            "ross": "delete",
        }),
    ]

    defaults = {
        "nnavi500": 1,
        "nnavi50": 1,
        "nnavi10": 1,
        "textnv": "",
        "capitalization": 0,
        "spacing": 0,
        "mtn_mode": None,
        "mtn_dir": "right",
        "extreme": None,
        "big": False,
        "splatdir": "backspace",
    }


control.nexus().merger.add_global_rule(Navigation())
