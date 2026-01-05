from pydantic import BaseModel
from typing import List, Dict

class ForecastSchema(BaseModel):
    company: str
    period_analyzed: str
    financial_trends: Dict
    management_outlook: Dict
    risks: List[str]
    opportunities: List[str]
    forecast_summary: str
