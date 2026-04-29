from agent.engine import CodeQualityAgent

if __name__ == "__main__":
    agent = CodeQualityAgent(repo_path="./demo_repo")
    report = agent.run()

    print("\n=== Code Quality Report ===")
    print(report.summary())
