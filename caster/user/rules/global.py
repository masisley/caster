from dragonfly import *

from caster.lib import control
from caster.lib.dfplus.merge.mergerule import MergeRule
from caster.lib.dfplus.state.short import R
from caster.lib.dfplus.additions import IntegerRefST

class MyGlobal(MergeRule):
  pronunciation = "my global"

  mapping = {
    "select find this [<n>]":   Key("right, c-left") + Key("cs-right") * Repeat(extra="n") + Key("c-c, cs-f, c-v, enter"),
    "find this":   Key("c-c, cs-f, c-v, enter"),
  }
  extras = [
    IntegerRefST("n",1, 10),
  ]
  defaults ={"n": 1}

control.nexus().merger.add_global_rule(MyGlobal())