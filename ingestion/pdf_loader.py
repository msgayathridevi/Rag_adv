from pathlib import Path
from pypdf import PdfReader


def load_pdfs(pdf_folder="data/pdfs"):
    documents = []

    for pdf_file in Path(pdf_folder).glob("*.pdf"):

        reader = PdfReader(str(pdf_file))

        text = ""

        for page in reader.pages:
            page_text = page.extract_text()

            if page_text:
                text += page_text + "\n"

        documents.append(
            {
                "content": text,
                "source": pdf_file.name,
                "source_type": "pdf"
            }
        )

    return documents