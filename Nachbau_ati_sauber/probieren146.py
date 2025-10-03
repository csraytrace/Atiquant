from fpdf import FPDF

# === Dateinamen anpassen ===
input_file = "probieren145_master.py"  # Hier Name deines .py Files eintragen!
output_pdf = "Formfaktor.pdf"  # Name für das PDF

pdf = FPDF(orientation='L', unit='mm', format='A4')  # Querformat!
pdf.add_page()
pdf.set_font("Courier", size=7)   # Viel kleiner!
pdf.set_auto_page_break(auto=True, margin=8)

# Zeilenumbruch, falls zu lang
max_line_len = 180  # Bis zu 180 Zeichen in kleiner Schrift im Querformat

with open(input_file, "r", encoding="utf-8") as f:
    for line in f:
        l = line.rstrip('\n')
        # Lange Zeilen umbrechen:
        while len(l) > max_line_len:
            pdf.cell(0, 4, l[:max_line_len], ln=1)
            l = l[max_line_len:]
        pdf.cell(0, 4, l, ln=1)

pdf.output(output_pdf)
print(f"PDF gespeichert als: {output_pdf}")
