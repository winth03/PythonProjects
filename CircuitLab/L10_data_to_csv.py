import pandas as pd
import os.path as path

file = "L10_data"
with open(f"./lab_data/{file}.txt", "r", encoding="utf-8") as f:
    data = f.read().splitlines()
    # Convert to dataframe
    col = ["V2 [V]", "Ib [A]", "Ic [A]", "Vbe [V]", "Vbc [V]", "Vce [V]"]
    df = pd.DataFrame(columns=col)
    for entry in data:
        if entry.endswith("V"):
            df.loc[len(df)] = [float(entry[:-1]), None, None, None, None, None]
        elif entry.startswith("Ib"):
            df.iloc[-1, 1] = float(entry[4:].strip())
        elif entry.startswith("Ic"):
            df.iloc[-1, 2] = float(entry[4:].strip())
        elif entry.startswith("Vbe"):
            df.iloc[-1, 3] = float(entry[5:].strip())
        elif entry.startswith("Vbc"):
            df.iloc[-1, 4] = float(entry[5:].strip())
        elif entry.startswith("Vce"):
            df.iloc[-1, 5] = float(entry[5:].strip())

    # Save dataframe to csv
    df.to_csv(f"./lab_data/{file}.csv", index=False, encoding="utf-8")
