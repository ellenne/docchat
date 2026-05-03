import fitz  # PyMuPDF


def extract_text_from_pdf(pdf_bytes: bytes) -> list[dict]:
    """
    Extract text from a PDF, page by page.

    Returns: [{"page": 1, "text": "..."}, ...]
    Page-level granularity helps with citation later.
    """
    doc = fitz.open(stream=pdf_bytes, filetype="pdf")
    pages = []
    for page_num, page in enumerate(doc, start=1):
        text = page.get_text()
        if text.strip():  # skip blank pages
            pages.append({"page": page_num, "text": text})
    doc.close()
    return pages