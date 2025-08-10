import pandas as pd
from fpdf import FPDF

# Step 1: Load your CSV file
csv_path = r"C:\Users\janha\Desktop\jateen\task\reserch.csv"
data = pd.read_csv(csv_path)

# Step 2: Create a PDF
class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 14)
        self.cell(0, 10, 'Research Footnotes Report', ln=True, align='C')
        self.ln(5)

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Page {self.page_no()}', align='C')

    def add_footnote(self, number, text):
        self.set_font('Arial', 'B', 11)
        self.multi_cell(0, 8, f'[{number}]')  # <-- no ln argument
        self.set_font('Arial', '', 11)
        self.multi_cell(0, 8, f'{text}\n')

# Step 3: Add content to PDF
pdf = PDF()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.add_page()

# Add each footnote
for _, row in data.iterrows():
    pdf.add_footnote(row['Number'], row['Footnote'])

# Step 4: Output PDF
output_path = r"C:\Users\janha\Desktop\jateen\task\Research_Footnotes_Report.pdf"
pdf.output(output_path)

print(f"✅ PDF generated successfully at:\n{output_path}")
