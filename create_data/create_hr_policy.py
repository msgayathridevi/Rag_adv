from reportlab.pdfgen import canvas
import os

os.makedirs("data/pdfs", exist_ok=True)

pdf = canvas.Canvas("data/pdfs/HR_Policy.pdf")

content = [
    "HR Policy Document",
    "",
    "Employees receive 20 annual leave days.",
    "Remote work allowed 3 days per week.",
    "Medical insurance provided."
]

y = 800

for line in content:
    pdf.drawString(50, y, line)
    y -= 20

pdf.save()

print("HR_Policy.pdf created")