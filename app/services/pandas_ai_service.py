import pandasai as pai
import os

class PandasAIService:
    def __init__(self, data_path: str = 'data/pop.csv'):
        self.api_key = os.getenv('PANDASAI_KEY')
        if not self.api_key:
            raise ValueError(
                "AI API key not found in environment variables")
        pai.api_key.set(self.api_key)

        self.data_path = data_path
        self._load_data()

    def _load_data(self):
        try:
            self.df = pai.read_csv(self.data_path)
        except FileNotFoundError:
            raise Exception(f"Data file not found at {self.data_path}")

    def ask_question(self, question: str) -> str:
        try:
            response = self.df.chat(prompt=question)
            return str(response)
        except Exception as e:
            raise Exception(f"Error processing question: {str(e)}")

    def get_data_preview(self):
        return {
            "columns": list(self.df.columns),
            "sample": self.df.head().to_dict(orient='records')
        }