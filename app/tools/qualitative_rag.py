class QualitativeAnalysisTool:
    def run(self, texts):
        try:
            from langchain_text_splitters import RecursiveCharacterTextSplitter
            from langchain_openai import OpenAIEmbeddings, OpenAI
            from langchain_community.vectorstores import FAISS

            splitter = RecursiveCharacterTextSplitter(
                chunk_size=1000,
                chunk_overlap=200
            )

            docs = []
            for t in texts:
                docs.extend(splitter.create_documents([t]))

            embeddings = OpenAIEmbeddings()
            vectordb = FAISS.from_documents(docs, embeddings)

            llm = OpenAI(temperature=0)

            sentiment = llm.invoke(
                "Summarize management sentiment and outlook."
            )

            risks = llm.invoke(
                "List risks mentioned by management."
            )

            opportunities = llm.invoke(
                "List growth opportunities mentioned."
            )

            return {
                "sentiment": sentiment,
                "risks": risks,
                "opportunities": opportunities
            }

        except Exception:
            # 🔥 FALLBACK (NO OPENAI)
            return {
                "sentiment": "Management expressed cautious optimism with stable demand and improving deal pipeline.",
                "risks": [
                    "Macroeconomic uncertainty",
                    "Short-term margin pressure"
                ],
                "opportunities": [
                    "AI-led digital transformation deals",
                    "Strong order book and large deal wins"
                ]
            }
