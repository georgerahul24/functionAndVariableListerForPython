import webbrowser

import tabulate


def function_paraser(name, filepath):
    file = open(filepath)
    data = file.read().splitlines()
    functions = []
    for linenumber in range(len(data)):
        line = data[linenumber]
        if line.lstrip().startswith("def"):
            nested = bool(line.startswith(" "))
            line = line.replace("def", "").rstrip().lstrip()
            functions.append([name, line, linenumber + 1, nested])

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
    headers = ["sl no", "filename", "function name", "linenumber", "nested"]
    filewritename =  os.getcwd()+f'\\history\\{folderpath.split("/")[-1]} {datetime.date.today()} function lister.txt'
    os.makedirs(os.getcwd() + "\\history") if not Path(os.getcwd() + "\\history").is_dir() else print("Directory found")
    fileresult = open(filewritename, "w", encoding="UTF-16")
    fileresult.writelines(
        tabulate.tabulate(
            headers=headers, tabular_data=result, tablefmt="fancy_grid", showindex=True
        )
    )
    fileresult.close()
    webbrowser.open(filewritename)
