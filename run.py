from macropython import PyMacro
import json


def main():
    with open("macros.json") as f:
        macros = json.load(f)

    for macro in macros:
        macro["binding"] = macro["binding"].split(" ")
    PyMacro(macros).run()


if __name__ == "__main__":
    main()
