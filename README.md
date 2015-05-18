# PinIt
Tired of typing an often used or long command? Pin it!


## What's PinIt ?
A simplistic way to collect, organize and fire actions.

It consists of only two kind of things:
* menus
* buttons

A button can do only two things:
* open another menu
* do an action

An action is a command executed on the owning command line.
This way you can hook programs, apps, scripts, tools, complicated calls,
browser+webpages ... whatever that can be executed on the command line.

The layout can be extended with a few clicks, with further nested submenus
and/or actions, be stored or even be scripted.


## Installation
PinIt was written using python3. So you should have it available on your system^^.
Either clone the repo `git clone https://github.com/84n4n4j03/pinit.git`
or download the [archive](https://github.com/84n4n4j03/pinit/archive/master.zip).


## Usage
In the root directory simply say `python pinit.py`
and a small GUI with colored buttons should open. Submenus open on mouse
hovering and can be pinned on mouse click. All menus are always on top. Open
the config menu to add new buttons.


## Tricks
### savedLayout.js
The layout is stored into a file named savedLayout.js. As the extension implies
it's human readable json and can be directly tweaked. When you start PinIt the
first time you'll get an empty menu. When you save it, it is stored next to the
main directory.
(Hint: this way it's outside the PinIt repo and can be stored with a parent
repo, in case you use PinIt as sub repo).
To start from scratch you can simply delete it and start pinit.
The structure is easy to understand and after you get used to it you can
quickly add, modify, and delete stuff.

You could even remove the configuration and storage capablities this way to
write protect a menu.

### Parameter
To use an action with different parameter simply add a "$" in front of a word
in the command. If you click the button another menu shows up to ask you for
the actual value. E.g.: `git checkout $branch` will ask you for the value
of `$branch`. Of course you can do this for multiple parameters.


## Limitations
I needed it on Windows machines, and some code related to window focussing
will not run on other platforms. Though this could easily be adapted (e.g.
by extracting a base class from `misc/windowmgr.py` and inherit both the existing
Windows implementation and your new target platform implementation, finally
add some logic to switch between both based on the platform you're running on).
