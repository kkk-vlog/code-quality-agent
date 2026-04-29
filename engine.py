from analyzers.lint_analyzer import LintAnalyzer
from analyzers.complexity_analyzer import ComplexityAnalyzer
from analyzers.ai_reviewer import AIReviewer
from reports.report_builder import ReportBuilder

class CodeQualityAgent:

    def __init__(self, repo_path: str):
        self.repo_path = repo_path

        self.analyzers = [
            LintAnalyzer(),
            ComplexityAnalyzer(),
            AIReviewer()
        ]

    def run(self):
        results = []

        for analyzer in self.analyzers:
            result = analyzer.analyze(self.repo_path)
            results.append(result)

        report = ReportBuilder(results)
        return report
