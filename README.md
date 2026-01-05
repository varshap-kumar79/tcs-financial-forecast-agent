# Financial Forecasting Agent for TCS

## Project Overview (What & Why)

This project implements an **AI-first, agentic financial forecasting system** for **Tata Consultancy Services (TCS)** using **FastAPI** and a tool-based agent design inspired by **LangChain**.

The goal is to move beyond simple Q&A and demonstrate an AI agent that can:
- Analyze recent **quarterly financial reports**
- Process **earnings call transcripts**
- Extract structured financial signals
- Perform **qualitative, document-grounded reasoning**
- Generate a **forward-looking business outlook forecast**

The system intentionally produces a **qualitative forecast**, not a numerical financial model, aligning with real-world financial analysis practices.

---

## Architecture Explanation

The application follows a **modular, agent-driven architecture**:

1. **API Layer**
   - FastAPI service exposing a single analytical endpoint: `POST /forecast`

2. **Agent Layer**
   - Orchestrates multi-step reasoning
   - Coordinates specialized tools
   - Synthesizes insights into a unified forecast

3. **Tool Layer**
   - Financial data extraction tool
   - Qualitative RAG-based analysis tool

4. **Persistence Layer**
   - Logs requests and responses to a MySQL-compatible database
   - Implements graceful degradation if database access is unavailable

**High-level flow:**
- Documents → Tools → Agent Reasoning → Structured JSON → Database Logging

---

## Agent & Tool Design

### FinancialDataExtractorTool

**Purpose**  
Extracts key financial signals from quarterly financial reports.

**Responsibilities**
- Identify revenue direction (growth / stability)
- Identify margin direction (pressure / improvement)
- Capture high-level financial performance indicators

**Design Choice**
- Focuses on **directional trends**, not precise numerical forecasting
- Avoids speculative extrapolation beyond reported results

---

### QualitativeAnalysisTool (RAG-based)

**Purpose**  
Analyzes earnings call transcripts to extract qualitative insights.

**What it identifies**
- Management sentiment
- Forward-looking commentary
- Key risks and opportunities

**Approach**
- Transcript text is chunked and embedded
- Semantic search retrieves relevant sections
- Retrieved content is synthesized into qualitative insights

---

### Forecast Agent (Orchestrator)

The agent performs **multi-step reasoning** by:
1. Invoking the financial extraction tool
2. Invoking the qualitative analysis tool
3. Combining outputs from both tools
4. Producing a coherent business outlook forecast
5. Returning results in a predictable JSON structure

---

## AI Stack

- **LLM:** flan-t5-large
- **Embeddings:** all-MiniLM-L6-v2
- **Vector Database:** FAISS
- **PDF Parsing:** PyPDF
- **Agent Framework:** LangChain-inspired tool orchestration
- **Backend Framework:** FastAPI
- **Database:** MySQL (with graceful fallback)

---

## Guardrails & Evaluation Strategy

To ensure reliability and correctness:

- Low-temperature generation for deterministic outputs
- Tool-based access to documents (no free-form hallucination)
- Document-grounded synthesis only
- Conservative, finance-appropriate language
- Structured JSON output for predictable responses

---

## Forecast Scope: Qualitative vs Numeric Modeling

The forecast is intentionally **qualitative, high-level, and conservative**.

### What the Forecast Includes
- Directional revenue trends
- Margin movement (pressure or improvement)
- Management sentiment and outlook
- Strategic risks and opportunities
- Deal pipeline and business momentum

### What Is Intentionally Excluded
The system does **not** attempt to predict:
- Exact revenue numbers
- Exact margin percentages
- Segment-wise financial breakdowns
- Forward-looking financial projections

This design avoids hallucination and ensures all insights remain grounded in management disclosures and reported results.

### Light Numeric Grounding
When explicitly stated in source documents, the agent may reference:
- Approximate constant currency growth ranges (e.g., ~4–5%)
- Large deal pipeline indicators (e.g., $10B+ TCV)
- Sequential margin improvement trends

These references are **contextual**, not predictive.

---

### Output Format (Structured JSON)

### Example response from `POST /forecast`:

- ```json
{
  "company": "Tata Consultancy Services (TCS)",
  "period_analyzed": "Q2 & Q3 FY25",
  "financial_trends": {
    "revenue_trend": "Stable growth with Q3 constant currency growth of approximately 4–5%",
    "margin_trend": "Sequential margin improvement driven by operational efficiencies"
  },
  "management_outlook": "Cautiously optimistic with a strong deal pipeline exceeding $10B in TCV",
  "risks": [
    "Macroeconomic uncertainty",
    "Short-term margin pressure"
  ],
  "opportunities": [
    "AI-led digital transformation",
    "Large enterprise deal wins"
  ],
  "forecast_summary": "TCS is expected to deliver steady performance with cautious optimism in the upcoming quarter."
}


### Run 
- Activate environment  -> source venv/bin/activate
- Atart AIP server -> uvicorn app.main:app --reload
- Verify the service -> http://127.0.0.1:8000/docs
- database -> forecast_logs
