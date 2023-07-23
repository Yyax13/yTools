BRANDING NEW VERSION 1.0.3

UPDATES:
``all banners now haven't the grey box``
``ASCII tool removed by copy``
``a new main code``
``delay line for line in main``


Install:

in kali:

```
$ sudo apt install git

$ git clone https://github.com/Yyax13/Rvng-tools
```

in termux

```
$ pkg i git && git clone https://github.com/Yyax13/Rvng-tools && cd Rvng-tools
```

usage:

in kali:

```
$ cd Rvng_tools

$ python main.py
```

in termux:

```
$ cd Rvng-tools

$ termux_setup_storage

$ python3 main.py
```

in 'Presets' paste, you can finder some presets (html, etc)

obs:
to use this tool without errors, in the termcolor archive (a python lib)
add ``''`` to the HIGHLIGHTS var, don't forget to change the number 48 in ``list(range(40, 48))`` to 49

the HIGHLIGHTS final code is:

```
HIGHLIGHTS = dict(
        list(zip([
            'on_grey',
            'on_red',
            'on_green',
            'on_yellow',
            'on_blue',
            'on_magenta',
            'on_cyan',
            'on_white',
            ''
            ],
            list(range(40, 49))
            ))
        )
```
