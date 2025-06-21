import pandas as pd
import glob
import os

os.makedirs('data3', exist_ok=True)

data_folder = "data/"

# Use glob to find all Excel files in the folder
file_list = glob.glob(data_folder + "*.xls") 

all_frames = []

# Loop through each file path and read it into a DataFrame
for file in file_list:
    print(file)
    if file=="data/indname.xls":
        #print("h")
        continue
    else:
        df = pd.read_excel(file, skiprows=7,sheet_name='Industry Averages')
        print(df.columns[0])
        if df.columns[0]!='Industry Name':
            print("here")
            df.columns=df.loc[0]
            df=df.drop(0)
        filename = os.path.basename(file)  # Extract the file name
        new_file_path = os.path.join('data2/', filename)  # Create the new file path
        df.to_excel(new_file_path, index=False,engine='openpyxl')
        print("files saved successfully")
        all_frames.append(df)
    
# merged_df = pd.merge(all_frames,on="Industry Name" ,how="outer")

# Optionally, specify a sheet name to read from each file
# merged_df = pd.concat([pd.read_excel(file, sheet_name="Sheet1") for file in file_list], ignore_index=True)

# Save the merged DataFrame to a new Excel file
# merged_df.to_excel("merged_data.xlsx", index=False)
