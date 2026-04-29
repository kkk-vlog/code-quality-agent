from radon.complexity import cc_visit
import os

class ComplexityAnalyzer:

    def analyze(self, repo_path):
        results = []

        for root, _, files in os.walk(repo_path):
            for file in files:
                if file.endswith(".py"):
                    path = os.path.join(root, file)
                    with open(path, "r", encoding="utf-8") as f:
                        code = f.read()
                        blocks = cc_visit(code)

                        for block in blocks:
                            results.append({
                                "file": path,
                                "name": block.name,
                                "complexity": block.complexity
                            })

        return {
            "type": "complexity",
            "data": results
        }
