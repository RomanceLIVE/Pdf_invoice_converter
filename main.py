import pandas as pd
import glob
# glob is useful here for lists with multiple files
from fpdf import FPDF
from pathlib import Path
# helps with using filepaths

filepaths = glob.glob("invoices/*.xlsx")
print(filepaths)

for filepath in filepaths:
    df = pd.read_excel(filepath, sheet_name="Sheet 1")
    pdf = FPDF(orientation="P", unit="mm", format="A4")
    pdf.add_page()
    filename = Path(filepath).stem
    # stem extract a property of the file
    # which here will be the name
    invoice_nr = filename.split("-")[0]
    pdf.set_font(family="Times", size=16, style="B")
    pdf.cell(w=50, h=8, txt=f"Invoice nr.{invoice_nr}")
    pdf.output(f"PDFS/{filename}.pdf")
    # f string useful here
    # because we generate files dynamically from multiple files


    # we create a pdf for each excel
    # that's the logic to use inside for loop

print(df)
#reminder prints are good to check step by step the output,
# but also actions done correctly