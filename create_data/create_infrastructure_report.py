from reportlab.pdfgen import canvas
import os

os.makedirs("data/pdfs", exist_ok=True)

pdf = canvas.Canvas("data/pdfs/Infrastructure_Report.pdf")

content = [
    "Infrastructure Report",
    "",
    "Server-1 CPU usage exceeded 90 percent.",
    "Database latency increased.",
    "Network traffic spike detected."
]

y = 800

for line in content:
    pdf.drawString(50, y, line)
    y -= 20

pdf.save()

print("Infrastructure_Report.pdf created")