from typing import Union
from pynput.keyboard import Key, KeyCode
from pynput import keyboard
from pathlib import Path
import argparse
import os


class PyMacro:
    def __init__(self, macros: list):
        self.key_map = {"shift": Key.shift, "ctrl": Key.ctrl, "alt": Key.alt, "lctrl": Key.ctrl_l,
                        "rctrl": Key.ctrl_r, "lshift": Key.shift_l, "rshift": Key.shift_r,
                        "alt gr": Key.alt_gr, "altgr": Key.alt_gr}
        self.held = set()
        self.macros = [self.load(macro) for macro in macros]

    def load(self, macro: dict):
        binding = set()
        script = Path(macro["script"]).stem
        env = macro["environment"]
        f = macro["function"]

        for key in macro["binding"]:
            if key in self.key_map:
                binding.add(self.key_map[key])
            else:
                binding.add(KeyCode.from_char(key))
        if f:
            return {"binding": binding,
                    "system_call": f'{env} -c "from {script} import {f}; {f}()"'}
        else:
            return {"binding": binding,
                    "system_call": f'{env} -c "import {script}"'}

    def press(self, key: Union[Key, KeyCode]):
        self.held.add(key)
        for macro in self.macros:
            if all(k in self.held for k in macro["binding"]):
                os.system(macro["system_call"])

    def release(self, key: Union[Key, KeyCode]):
        try:
            self.held.remove(key)
        except KeyError:
            pass

    def run(self):
        with keyboard.Listener(self.press, self.release) as listener:
            listener.join()


def main():
    parser = argparse.ArgumentParser(
        description='"pybind" a script that binds a script to a keybinding')
    parser.add_argument("--binding", "-b", type=str, nargs="+",
                        help="You keybind to launch your script.")
    parser.add_argument("--environment", "-e", type=str,
                        help='Your venv, is set to "python" if left empty.')
    parser.add_argument("--script", "-s", type=str,
                        help="Your python file where your function is located.")
    parser.add_argument("--function", "-f", type=str,
                        help="Your functions name in your file (no parentheses).")
    args = parser.parse_args()
    key_manager = PyMacro([vars(args)])
    key_manager.run()


if __name__ == "__main__":
    main()
