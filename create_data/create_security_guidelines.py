from reportlab.pdfgen import canvas
import os

os.makedirs("data/pdfs", exist_ok=True)

pdf = canvas.Canvas("data/pdfs/Security_Guidelines.pdf")

content = [
    "Security Guidelines",
    "",
    "MFA is mandatory.",
    "Password rotation every 90 days.",
    "Access logs must be monitored."
]

y = 800

for line in content:
    pdf.drawString(50, y, line)
    y -= 20

pdf.save()

print("Security_Guidelines.pdf created")