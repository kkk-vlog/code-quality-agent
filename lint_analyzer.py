import subprocess

class LintAnalyzer:

    def analyze(self, repo_path):
        try:
            result = subprocess.run(
                ["flake8", repo_path],
                capture_output=True,
                text=True
            )
            return {
                "type": "lint",
                "issues": result.stdout.splitlines()
            }
        except Exception as e:
            return {"type": "lint", "error": str(e)}
