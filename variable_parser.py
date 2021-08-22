import webbrowser

import tabulate


def function_paraser(name, filepath):
    file = open(filepath)
    data = file.read().splitlines()
    functions = []
    for linenumber in range(len(data)):
        line = data[linenumber]
        if "=" in line and line.lstrip().startswith("#") == False:
            reserved = False
            reservedwords = [
                "==",
                "if",
                "print",
                "def",
                "Label",
                "Button",
                "config",
                ".bind",
                "tkinterlib.initialise",
                ".grid",
                "fg",
                "bg",
                "bd",
                "partial",
                "text",
                "font",
                ".pack",
                ".place",
            ]
            for word in reservedwords:
                if word in line:
                    reserved = True
                    break
            if reserved == False:
                line = line.rstrip().lstrip().split("=")
                variablename = line[0]
                variablevalue = line[1]
                functions.append([name, variablename, variablevalue, linenumber + 1])

    return functions


import os
from pathlib import Path

# get path of the current file os.getcwd
# convert it into path use path(os.getcwd) use is_file() to check if it is a file
result = []


def index(pathn):
    try:
        for name in os.listdir(pathn):

            filename = os.path.join(pathn, name)
            filepath = Path(filename)
            if filepath.is_file() == True:
                if name.endswith(".py"):
                    result.extend(function_paraser(name, filepath))

            elif name.startswith(".") == False and name.startswith("__") == False:
                try:
                    index(filepath)
                except Exception as e:
                    print(e)

    except Exception as e:
        print(e)


if __name__ == "__main__":
    from tkinter import filedialog
    import datetime

    folderpath = filedialog.askdirectory()
    index(folderpath)
    headers = [
        "sl no",
        "filename",
        "variable name",
        "variable value",
        "linenumber",
    ]
    filewritename = (
        f'{folderpath.split("/")[-1]} {datetime.date.today()} variable lister.txt'
    )
    fileresult = open(filewritename, "w", encoding="UTF-16")
    fileresult.writelines(
        tabulate.tabulate(
            headers=headers, tabular_data=result, tablefmt="fancy_grid", showindex=True
        )
    )
    webbrowser.open(filewritename)
