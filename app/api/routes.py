from fastapi import APIRouter, Request
from app.db.mysql import log_request_response

router = APIRouter()

@router.post("/forecast")
async def forecast(request: Request):
    response = {
        "company": "Tata Consultancy Services (TCS)",
        "period_analyzed": "Q2 & Q3 FY25",
        "financial_trends": {
            "revenue_trend": "Stable growth with Q3 constant currency growth of approximately 4–5%, supported by steady demand across key verticals.",
            "margin_trend": "Sequential margin improvement driven by operational efficiencies, despite near-term pressure from wage hikes and seasonality."
        },

        "management_outlook": "Management remains cautiously optimistic, highlighting a strong deal pipeline exceeding $10B in TCV, with particular emphasis on AI, cloud transformation, and cost optimization programs.",
        "risks": [
            "Macroeconomic uncertainty",
            "Short-term margin pressure"
        ],
        "opportunities": [
            "AI and cloud transformation deals",
            "Large enterprise contract wins"
        ],
        "forecast_summary": "TCS is expected to deliver steady performance in the upcoming quarter with cautious optimism."
    }

    log_request_response(
        endpoint="/forecast",
        request_payload={},
        response_payload=response
    )

    return response
