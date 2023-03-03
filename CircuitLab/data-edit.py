import pandas as pd
import os.path as path

if __name__ == "__main__":
    file = input("Enter the file name: ")
    if path.exists(f"./lab_data/{file}.csv"):
        while True:
            # Show existing data
            df = pd.read_csv(f"./lab_data/{file}.csv")
            print(df.tail(5))
            # Get new row data
            row = ""
            for i in range(df.columns.size):
                value = input(f"Enter value for {df.columns[i]}: ")
                row += f"{value},"
            # Append new row to existing data
            df.loc[df.index.size] = row[:-1].split(",")
            # Save new data
            df.to_csv(f"./lab_data/{file}.csv", index=False)
            # Ask user if they want to add more data
            if input("Do you want to add more data? (Enter/y, n): ") == "n": break
    else:
        print("File does not exist")
        # Create new file
        columns = input("Enter the column names separated by commas: ").split(",")
        # Create new dataframe
        df = pd.DataFrame(columns=columns)
        while True:
            # Show existing data
            print(df.tail(5))
            # Get new row data
            row = ""
            for i in range(len(columns)):
                value = input(f"Enter value for {columns[i]}: ")
                row += f"{value},"
            df.loc[df.index.size] = row[:-1].split(",")
            # Save new data
            df.to_csv(f"./lab_data/{file}.csv", index=False)
            # Ask user if they want to add more data
            if input("Do you want to add more data? (Enter/y, n): ") == "n": break
