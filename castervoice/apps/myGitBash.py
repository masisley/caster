#
# This file is a command-module for Dragonfly.
# (c) Copyright 2008 by Christo Butcher
# Licensed under the LGPL, see <http://www.gnu.org/licenses/>
#
"""
Command-module for git

"""
#---------------------------------------------------------------------------

from dragonfly import (Grammar, Mimic, Function)

from castervoice.lib import control
from castervoice.lib import settings
from castervoice.lib.dfplus.additions import IntegerRefST
from castervoice.lib.dfplus.merge import gfilter
from castervoice.lib.dfplus.merge.mergerule import MergeRule
from castervoice.lib.dfplus.state.short import R
from castervoice.lib.context import AppContext
from castervoice.lib.actions import (Key, Text)
from castervoice.lib.dfplus.merge.ccrmerger import CCRMerger

class MyGitBashRule(MergeRule):
    pronunciation = "my git bash"
    mwith = CCRMerger.CORE
    mapping = {
        "status":
            R(Key("g, i, t, space, s, t, a, t, u, s")+Key("enter"), rdescript="GIT: Status"),
        "checkout":
            R(Text("git checkout "), rdescript="GIT: Check Out"),
        "fetch":
            R(Text("git fetch ")+Key("enter"), rdescript="GIT: Fetch"),
        "pull":
            R(Text("git pull ")+Key("enter"), rdescript="GIT: Pull"),
        "list":
            R(Text("dir")+Key("enter"), rdescript="GIT: List"),
             
        "get":              Text( "git " ),
        "open project":     R(Text("vsmsbuild sources.proj")+Key("enter"), rdescript="vsmsbuild"),
        "force push":       R(Text( "git push -f" )+Key("enter"), rdescript="GIT: Force Push"),
        "build":      R(Text( "build" )+Key("enter"), rdescript="Build: local"),
        "build rec":        R(Text( "buildreq" )+Key("enter"), rdescript="Build: remote"),
        "build signed":     R(Text( "buildreq -s" )+Key("enter"), rdescript="Build: remote"),
        "build package":     R(Text( "buildreq -s -p" )+Key("enter"), rdescript="Build: remote"),
        "NPM Start":     R(Text( "npm start" )+Key("enter"), rdescript="NPM: start"),

        "open (Flow portal | portal) admin":      R(Key("cw-p"), rdescript="Conemu: Open Portal"),
        "open (Flow portal | portal)":      R(Key("cw-i"), rdescript="Conemu: Open Portal User"),
        "open (Flow RP | RP) admin":          R(Key("cw-r"), rdescript="Conemu: Open RP"),
        "open (Flow RP | RP)":     R(Key("cw-u"), rdescript="Conemu: Open RP User"),
        "open Caster":      R(Key("cw-c"), rdescript="Conemu: Open Caster"),
        "Next tab":      R(Key("w-tab"), rdescript="Conemu: Next tab"),
        "switch tab [<n>]":      R(Key("w-tab"), rdescript="Conemu: Next tab"),
        "Close tab":      R(Key("wa-delete"), rdescript="Conemu: Close tab"),

        "checkout masisley":         R(Text( "git checkout masisley/" ), rdescript="GIT: Check Out"),
        "checkout new":         R(Text( "git checkout -b masisley/" ), rdescript="GIT: Check Out"),
        "checkout master":         R(Text( "git checkout master" ) + Key("enter"), rdescript="GIT: Check Out Master"),
        "(get push | push) Set up stream":R(Text( "git push --set-upstream origin masisley/" ), rdescript="GIT: Push"),
        "(get Rebase| rebase) Master":              R(Text( "git rebase master" ) + Key("enter"),  rdescript="GIT: Rebase master"),
        "pull origin master":             R(Text( "git pull origin master" )+Key("enter"), rdescript="GIT: Pull"),
        
        "kill":             R(Text( "taskkill /f /IM " ), rdescript="Taskkill"),
        "findster":             R(Text( "findstr /spin  *" )+Key("left")+Key("left"), rdescript="findstr"),
        "CLS":             R(Text( "cls" )+Key("enter"), rdescript="Clear screen"),
        "clear build":             R(Text( "cls" )+Key("enter")+Text("build")+Key("enter"), rdescript="Clear build"),
    }
    extras = [
        IntegerRefST("n", 1, 10),
    ]
    defaults = {"n": 0}


#---------------------------------------------------------------------------

context = AppContext(executable="\\sh.exe") | \
          AppContext(executable="\\bash.exe") | \
          AppContext(executable="\\cmd.exe") | \
          AppContext(executable="\\mintty.exe") | \
          AppContext(executable="\\ConEmu.exe") | \
          AppContext(executable="\\ConEmu64.exe") | \
          AppContext(executable="\\ConEmuC64.exe") | \
          AppContext(executable="\\powershell.exe")

if settings.SETTINGS["apps"]["gitbash"]:
    if settings.SETTINGS["miscellaneous"]["rdp_mode"]:
        control.nexus().merger.add_global_rule(MyGitBashRule())
    else:
        control.nexus().merger.add_app_rule(MyGitBashRule(), context)
