import argparse
from agent.engine import CodeQualityAgent

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo", required=True)
    args = parser.parse_args()

    agent = CodeQualityAgent(args.repo)
    report = agent.run()

    print(report.summary())

if __name__ == "__main__":
    main()
