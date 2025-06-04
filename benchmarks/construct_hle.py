from datasets import load_dataset
import json

init_data = load_dataset("cais/hle", split="test")
data = []
questions = []

for item in init_data:
    if item["image"] == "":
        data.append({
            "question": item["question"]+"\n\n"+"Please reason step by step, and put your final answer within \\boxed{} in the prompt.",
            "answer": item["answer"],
            "rationale": item["rationale"],
            "raw_subject": item["raw_subject"],
            "category": item["category"]
        })
        questions.append(item["question"])

with open("hle.json", "w") as f:
    json.dump(data, f, indent=4)