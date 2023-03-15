import pandas as pd
import os.path as path

if __name__ == "__main__":
    file = input("Enter the file name: ")
    if path.exists(f"./lab_data/{file}.txt"):
        with open(f"./lab_data/{file}.txt", "r", encoding="utf-8") as f:
            data = f.read().splitlines()
            # Convert to dataframe
            col = int(input("Enter the number of column(s): "))
            headers = data[:col]
            data = data[col:]
            df = pd.DataFrame(columns=headers)
            for index, entry in enumerate(data):
                try:
                    df.iloc[index//col, index%col] = entry.strip()
                except IndexError:
                    df.loc[index//col] = [None] * col
                    df.iloc[index//col, index%col] = entry.strip()
            # Save dataframe to csv
            df.to_csv(f"./lab_data/{file}.csv", index=False, encoding="utf-8")
    else:
        print("File does not exist")
