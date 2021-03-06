BPYTHON(1)                 bpython                 BPYTHON(1)

NAME
       bpython  - a fancy {curtsies, curses, urwid} interface
       to the Python interactive interpreter

SYNOPSIS
       bpython [options] [file [args]]

       bpython-curses [options] [file [args]]

       bpython-urwid [options] [file [args]]

DESCRIPTION
       The idea is to provide the user with all the  features
       in-line,  much  like  modern  IDEs,  but  in a simple,
       lightweight package that can be run in a terminal win‐
       dow.

       In-line syntax highlighting.
              Hilights commands as you type!

       Readline-like  autocomplete with suggestions displayed
       as you type.
              Press tab to complete expressions when  there's
              only one suggestion.

       Expected parameter list.
              This  displays  a  list  of  parameters for any
              function you call. It uses the inspect  module,
              then tries pydoc.

       Rewind.
              This  is a bit misleading, but it code that has
              been  entered  is  remembered,  and  when   you
              Rewind,  it pops the last line and re-evaluates
              the  entire  code.  This  is  error-prone,  and
              mostly  useful  for  defining classes and func‐
              tions.

       Pastebin code/write to file.
              This posts the current  buffer  to  a  pastebin
              (bpaste.net) or writes it to a file.

       Flush curses screen to stdout.
              Unlike  other  curses  apps,  bpython dumps the
              screen data to stdout when you quit, so you see
              what  you've  done in the buffer of your termi‐
              nal.

OPTIONS
       The long and short forms of options, shown here as al‐
       ternatives,  are equivalent.  If bpython sees an argu‐
       ment it does not know, execution  falls  back  to  the
       regular Python interpreter.

       The following options are supported by all frontends:

       --config=<config>
              Use <config> instead of default config file.

       -h, --help
              Show the help message and exit.

       -i, --interactive
              Drop  to  bpython  shell after running file in‐
              stead of exiting. The PYTHONSTARTUP file is not
              read.

       -q, --quiet
              Do not flush the output to stdout.

       -V, --version
              Print bpython's version and exit.

       In  addition  to  the above options, bpython also sup‐
       ports the following options:

       -L, --log
              Write   debugging   messages   to   the    file
              bpython.log. Use -LL for more verbose logging.

       -p file, --paste=file
              Paste in the contents of a file at startup.

       In  addition to the common options, bpython-urwid also
       supports the following options if  Twisted  is  avail‐
       able:

       -r <reactor>, --reactor=<reactor>
              Use  Twisted's  <reactor>  instead  of  urwid's
              event loop.

       --help-reactors
              Display a list of available Twisted reactors.

       -p <plugin>, --plugin=<plugin>
              Execute a twistd plugin. Use twistd  to  get  a
              list  of  available plugins. Use -- to pass op‐
              tions to the plugin.

       -s <port>, --server=<port>
              Run an eval server on port <port>. This  option
              forces the use of a Twisted reactor.

KEYS
       bpython's    keys    are   fully   configurable.   See
       http://docs.bpython-interpreter.org/configuration.html#keyboard

FILES
       $XDG_CONFIG_HOME/bpython/config

       Your    bpython    config.   See   sample-config   (in
       /usr/share/doc/bpython/examples on Debian) for various
       options you can use, or read bpython-config(5).

KNOWN BUGS
       See  http://github.com/bpython/bpython/issues/  for  a
       list of known issues.

SEE ALSO
       bpython-config(5), python(1)

AUTHOR
       bpython was  written  by  Robert  Anthony  Farrell  <‐
       robertanthonyfarrel@gmail.com>  and his bunch of loyal
       followers.

       This manual page was written by Jørgen Pedersen Tjernø
       <jorgen@devsoft.no>,  for  the Debian project (but may
       be used by others).

COPYRIGHT
       2008-2020 Bob Farrell, Andreas Stuehrk et al.

 0.18                    Jan 04, 2020              BPYTHON(1)
