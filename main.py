import pandas as pd
import glob
# glob is useful here for lists with multiple files

filepaths = glob.glob("invoices/*.xlsx")
print(filepaths)

for filepath in filepaths:
    df = pd.read_excel(filepath, sheet_name="Sheet 1")
print(df)
#reminder prints are good to check step by step the output,
# but also actions done correctly