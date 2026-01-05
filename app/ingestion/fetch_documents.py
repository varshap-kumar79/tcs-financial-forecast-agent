from app.ingestion.pdf_parser import extract_text_from_pdf

def load_documents():
    return {
        "q2_call": extract_text_from_pdf("data/raw/Q2_FY25_call.pdf"),
        "q3_call": extract_text_from_pdf("data/raw/Q3_FY25_call.pdf"),
        "q3_financials": extract_text_from_pdf("data/raw/Q3_FY25_financials.pdf")
    }  
