import os
import glob
import pandas as pd
print(os.getcwd())

all_filenames = [f'id_kota_{i+1}.csv' for i in range(38)]
print(all_filenames)
combined_csv = pd.concat([pd.read_csv(f) for f in all_filenames ])

combined_csv.to_csv( "nilai.csv", index=False, encoding='utf-8-sig')