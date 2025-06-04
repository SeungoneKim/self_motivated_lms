import argparse
import os
import json

def main():
    parser = argparse.ArgumentParser(description="Merge JSON files in a directory into a Python list.")
    parser.add_argument("--directory", required=True, help="Directory containing JSON files")
    args = parser.parse_args()

    results = []
    
    for filename in os.listdir(args.directory):
        if filename.endswith(".json"):
            filepath = os.path.join(args.directory, filename)
            with open(filepath, "r", encoding="utf-8") as f:
                data = json.load(f)
                if isinstance(data, list):
                    results.extend(data)
                else:
                    results.append(data)

    score = 0
    for item in results:
        prediction = item["model_output"].split("</think>")[-1]
        if "\\boxed{" in item['answer']:
            if item['answer'] in prediction:
                score += 1
        else:
            if "\\boxed{"+item['answer']+"}" in prediction:
                score += 1
    print(f"Score: {str(int(score)/len(results))}")
    

if __name__ == "__main__":
    main()