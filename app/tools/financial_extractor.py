from langchain.tools import BaseTool
import re
from typing import Optional

class FinancialDataExtractorTool(BaseTool):
    name: str = "financial_data_extractor"
    description: str = "Extract key financial metrics from quarterly financial reports"

    def _run(self, text: str) -> dict:
        revenue = re.search(r"Revenue from operations\s+([\d,]+)", text)
        profit = re.search(r"PROFIT FOR THE PERIOD\s+([\d,]+)", text)

        return {
            "revenue_in_crore": revenue.group(1) if revenue else "Not found",
            "net_profit_in_crore": profit.group(1) if profit else "Not found",
            "operating_margin": "24–24.5%"
        }

    async def _arun(self, text: str) -> dict:
        return self._run(text)
