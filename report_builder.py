class ReportBuilder:

    def __init__(self, results):
        self.results = results

    def summary(self):
        output = []

        for r in self.results:
            if r["type"] == "lint":
                output.append(f"[Lint] Issues: {len(r.get('issues', []))}")
            elif r["type"] == "complexity":
                high = [x for x in r["data"] if x["complexity"] > 10]
                output.append(f"[Complexity] High Risk Functions: {len(high)}")
            elif r["type"] == "ai_review":
                output.append(f"[AI Review] Files Reviewed: {len(r['data'])}")

        return "\n".join(output)
