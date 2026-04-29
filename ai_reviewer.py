import os
from openai import OpenAI

class AIReviewer:

    def __init__(self):
        self.client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    def analyze(self, repo_path):
        summary = []

        for root, _, files in os.walk(repo_path):
            for file in files:
                if file.endswith(".py"):
                    path = os.path.join(root, file)
                    with open(path, "r", encoding="utf-8") as f:
                        code = f.read()[:2000]

                        response = self.client.chat.completions.create(
                            model="gpt-4o-mini",
                            messages=[
                                {"role": "system", "content": "你是代码审查专家"},
                                {"role": "user", "content": f"请审查以下代码:\n{code}"}
                            ]
                        )

                        summary.append({
                            "file": path,
                            "review": response.choices[0].message.content
                        })

        return {
            "type": "ai_review",
            "data": summary
        }
