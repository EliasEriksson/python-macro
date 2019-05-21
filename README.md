# python-macro
Executes python scripts with specified keybinding.

You can chose to run python-macro from the command line or execute the run.py. 
If run.py is executed it will read the macros.json file for macros. If executed from terminal directly execute python macropython.py instead.

The function option is not required and does not pass args or kwargs to the function. Anything inside `if __name__ == "__main__"` will not be run as the script will be imported. In this case define a `main()` function.

# Examples:
Using the following macros.json file will execute the given python files with respective enviroment if their keybinding is pressed.
```
[
    {
        "binding": "lctrl rctrl",
        "environment": "python3",
        "script": "~/clean_downloads_folder.py",
        "function": ""
    },
    {
        "binding": "lctrl lshift alt a",
        "environment": "~/projects/project/venv/bin/python",
        "script": "~/projects/project/script.py",
        "function": "some_function"
    }
]
```

Same results are posible with the two following commands: \
`python macropython.py -b lctrl rctrl -e python3 -s ~/clean_downloads_folder.py` \
and \
`python macropython.py -b lctrl lshift alt a -e ~/projects/project/venv/bin/python -s ~/projects/project/script.py -f some_function`
