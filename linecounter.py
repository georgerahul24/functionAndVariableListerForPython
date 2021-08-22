import webbrowser

import tabulate

totalcode = 0
totalblanklinecount = 0
totalcommentcounter = 0
totallines = 0


def function_paraser(name, filepath):
    file = open(filepath)
    data = file.read().splitlines()
    functions = []
    count = 0
    global totallines, totalblanklinecount, totalcode, totalcommentcounter
    blanklinecount = 0
    commentcounter = 0
    for line in data:
        line = line.rstrip().lstrip()
        if len(line) != 0 and line.startswith("#") == False:
            count += 1
            totalcode += 1
        elif len(line) == 0:
            blanklinecount += 1
            totalblanklinecount += 1
        elif line.startswith("#") == True:
            commentcounter += 1
            totalcommentcounter += 1
    functions.append([name, len(data), count, blanklinecount, commentcounter])

    totallines += len(data)
    return functions


import os
from pathlib import Path

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
        "Total Number of lines of code",
        "Written Code",
        "Blank lines",
        "Comments",
    ]
    filewritename = (
        f'{folderpath.split("/")[-1]} {datetime.date.today()} linecounter.txt'
    )
    fileresult = open(filewritename, "w", encoding="UTF-16")

    fileresult.writelines(
        tabulate.tabulate(
            headers=headers, tabular_data=result, tablefmt="fancy_grid", showindex=True
        )
    )
    fileresult.writelines(
        [
            f"\n\nTotal lines in project = {totallines}",
            f"\nTotal lines of code = {totalcode}",
            f"\nTotal blank lines = {totalblanklinecount}",
            f"\nTotal comments = {totalcommentcounter}",
        ]
    )
    webbrowser.open(filewritename)
