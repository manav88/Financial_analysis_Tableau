import pandas as pd
import glob
import os

os.makedirs('data3', exist_ok=True)

data_folder = "data/"


file_list = glob.glob(data_folder + "*.xls") 

all_frames = []


for file in file_list:
    print(file)
    if file=="data/indname.xls":
        
        continue
    else:
        df = pd.read_excel(file, skiprows=7,sheet_name='Industry Averages')
        print(df.columns[0])
        if df.columns[0]!='Industry Name':
            print("here")
            df.columns=df.loc[0]
            df=df.drop(0)
        filename = os.path.basename(file)  
        new_file_path = os.path.join('data2/', filename)  # Create the new file path
        df.to_excel(new_file_path, index=False,engine='openpyxl')
        print("files saved successfully")
        all_frames.append(df)
    


# Save the merged DataFrame to a new Excel file
# merged_df.to_excel("merged_data.xlsx", index=False)
