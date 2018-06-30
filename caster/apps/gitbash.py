#
# This file is a command-module for Dragonfly.
# (c) Copyright 2008 by Christo Butcher
# Licensed under the LGPL, see <http://www.gnu.org/licenses/>
#
"""
Command-module for git

"""
#---------------------------------------------------------------------------

from dragonfly import (Grammar, AppContext, Mimic, Key, Text, Function)

from caster.lib import control
from caster.lib import settings
from caster.lib.dfplus.additions import IntegerRefST
from caster.lib.dfplus.merge import gfilter
from caster.lib.dfplus.merge.mergerule import MergeRule
from caster.lib.dfplus.state.short import R


def _apply(n):
    if n != 0:
        Text("stash@{" + str(int(n)) + "}").execute()


class GitBashRule(MergeRule):
    pronunciation = "git bash"

    mapping = {
        "initialize repository":
            Text("git init") + Key("enter"),
        "add":
            R(Key("g, i, t, space, a, d, d, space, dot, enter"),
              rdescript="GIT: Add All"),
        "status":
            R(Key("g, i, t, space, s, t, a, t, u, s, enter"), rdescript="GIT: Status"),
        "commit":
            R(Key(
                "g, i, t, space, c, o, m, m, i, t, space, minus, a, m, space, apostrophe, apostrophe, left"
            ),
              rdescript="GIT: Commit"),
        "bug fix commit <n>":
            R(Mimic("commit") + Text("fixes #%(n)d ") + Key("backspace"),
              rdescript="GIT: Bug Fix Commit"),
        "reference commit <n>":
            R(Mimic("commit") + Text("refs #%(n)d ") + Key("backspace"),
              rdescript="GIT: Reference Commit"),
        "checkout":
            R(Text("git checkout "), rdescript="GIT: Check Out"),
        "branch":
            R(Text("git branch") + Key("enter"), rdescript="GIT: Branch"),
        "remote":
            R(Text("git remote "), rdescript="GIT: Remote"),
        "merge":
            R(Text("git merge "), rdescript="GIT: Merge"),
        "merge tool":
            R(Text("git mergetool") + Key("enter"), rdescript="GIT: Merge Tool"),
        "fetch":
            R(Text("git fetch") + Key("enter"), rdescript="GIT: Fetch"),
        "(get push | push)":
            R(Text("git push") + Key("enter"), rdescript="GIT: Push"),
        "pull":
            R(Text("git pull") + Key("enter"), rdescript="GIT: Pull"),
        "CD up":
            R(Text("cd ..") + Key("enter"), rdescript="GIT: Up Directory"),
        "CD":
            R(Text("cd "), rdescript="GIT: Navigate Directory"),
        "list":
            R(Text("ls") + Key("enter"), rdescript="GIT: List"),
        "make directory":
            R(Text("mkdir "), rdescript="GIT: Make Directory"),
        "undo [last] commit":
            R(Text("git reset --soft HEAD~1") + Key("enter"),
              rdescript="GIT: Undo Commit"),
        "(undo changes | reset hard)":
            R(Text("git reset --hard") + Key("enter"),
              rdescript="GIT: Undo or Reset Since Last Commit"),
        "stop tracking [file]":
            R(Text("git rm --cached FILENAME"), rdescript="GIT: Stop Tracking"),
        "preview remove untracked":
            R(Text("git clean -nd") + Key("enter"),
              rdescript="GIT: Preview Remove Untracked"),
        "remove untracked":
            R(Text("git clean -fd") + Key("enter"), rdescript="GIT: Remove Untracked"),
        "visualize":
            R(Text("gitk") + Key("enter"), rdescript="GIT: gitk"),
        "visualize file":
            R(Text("gitk -- PATH"), rdescript="GIT: gitk Single File"),
        "visualize all":
            R(Text("gitk --all") + Key("enter"), rdescript="GIT: gitk All Branches"),
        "exit":
            R(Text("exit") + Key("enter"), rdescript="GIT: Exit"),
        "stash":
            R(Text("git stash") + Key("enter"), rdescript="GIT: Stash"),
        "stash apply [<n>]":
            R(Text("git stash apply") + Function(_apply), rdescript="GIT: Stash Apply"),
        "stash list":
            R(Text("git stash list") + Key("enter"), rdescript="GIT: Stash List"),
        "stash branch":
            R(Text("git stash branch NAME"), rdescript="GIT: Stash Branch"),
        "cherry pick":
            R(Text("git cherry-pick "), rdescript="GIT: Cherry Pick"),
        "abort cherry pick":
            R(Text("git cherry-pick --abort"), rdescript="GIT: Abort Cherry Pick"),
        "GUI | gooey":
            R(Text("git gui") + Key("enter"), rdescript="GIT: gui"),

        # Begin My customizations #
        "get":              Text( "git " ),
        "open project":     R(Text("vsmsbuild sources.proj")+Key("enter"), rdescript="vsmsbuild"),
        "force push":       R(Text( "git push -f" )+Key("enter"), rdescript="GIT: Force Push"),
        "build":      R(Text( "build" )+Key("enter"), rdescript="Build: local"),
        "build rec":        R(Text( "buildreq" )+Key("enter"), rdescript="Build: remote"),
        "build signed":     R(Text( "buildreq -s" )+Key("enter"), rdescript="Build: remote"),
        "NPM Start":     R(Text( "npm start" )+Key("enter"), rdescript="NPM: start"),

        "open portal":      R(Key("cw-p"), rdescript="Conemu: Open Portal"),
        "open RP":          R(Key("cw-r"), rdescript="Conemu: Open RP"),
        "open RP user":     R(Key("cw-u"), rdescript="Conemu: Open RP User"),
        "open Caster":      R(Key("cw-c"), rdescript="Conemu: Open Caster"),
        "Next tab":      R(Key("w-tab"), rdescript="Conemu: Next tab"),

        "checkout masisley":         R(Text( "git checkout masisley/" ), rdescript="GIT: Check Out"),
        "checkout new":         R(Text( "git checkout -b masisley/" ), rdescript="GIT: Check Out"),
        "(get push | push) Set up stream":R(Text( "git push --set-upstream origin masisley/" ), rdescript="GIT: Push"),
        "get Rebase Master":              R(Text( "git rebase master" ), rdescript="GIT: Rebase master"),
        "pull origin master":             R(Text( "git pull origin master" )+Key("enter"), rdescript="GIT: Pull"),
        
        "task kill":             R(Text( "taskkill /f /IM " ), rdescript="Taskkill"),
        # End   My customizations #
        "blame":
            R(Text("git blame PATH -L FIRSTLINE,LASTLINE"), rdescript="GIT: Blame"),
        "gooey blame":
            R(Text("git gui blame PATH"), rdescript="GIT: GUI Blame"),
        "search recursive":
            R(Text("grep -rinH \"PATTERN\" *"), rdescript="GREP: Search Recursive"),
        "search recursive count":
            R(Text("grep -rinH \"PATTERN\" * | wc -l"),
              rdescript="GREP: Search Recursive Count"),
        "search recursive filetype":
            R(Text("find . -name \"*.java\" -exec grep -rinH \"PATTERN\" {} \\;"),
              rdescript="GREP: Search Recursive Filetype"),
        "to file":
            R(Text(" > FILENAME"), rdescript="Bash: To File"),
    }
    extras = [
        IntegerRefST("n", 1, 10000),
    ]
    defaults = {"n": 0}

#---------------------------------------------------------------------------

context = AppContext(executable="\\sh.exe")
context2 = AppContext(executable="\\bash.exe")
context3 = AppContext(executable="\\cmd.exe")
context4 = AppContext(executable="\\mintty.exe")
context5 = AppContext(executable="\\ConEmu64.exe")

grammar = Grammar("MINGW32", context=(context | context2 | context3 | context4 | context5))

if settings.SETTINGS["apps"]["gitbash"]:
    if settings.SETTINGS["miscellaneous"]["rdp_mode"]:
        control.nexus().merger.add_global_rule(GitBashRule())
    else:
        rule = GitBashRule(name="git bash")
        gfilter.run_on(rule)
        grammar.add_rule(rule)
        grammar.load()
