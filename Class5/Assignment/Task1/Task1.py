import os
import glob
import shutil
import pandas as pd

# Ensure the backup folder exists
backup_folder = "backup_folder"
if not os.path.exists(backup_folder):
    os.makedirs(backup_folder)

# Move CSV files to the backup folder
csv_files = glob.glob("*.csv")
for file in csv_files:
    shutil.move(file, backup_folder)
    print(f"Moved file: {file}")

# Function to export data in different formats
def export_data(df, filename, format):
    if format == "csv":
        df.to_csv(filename, index=False)
        print(f"Data exported to {filename} in CSV format.")
    elif format == "json":
        df.to_json(filename, orient="records")
        print(f"Data exported to {filename} in JSON format.")
    else:
        print("Unsupported format.")

# Sample DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
}

df = pd.DataFrame(data)

# Export data
export_data(df, "output.csv", "csv")
export_data(df, "output.json", "json")
