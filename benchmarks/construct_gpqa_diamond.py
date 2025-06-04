from datasets import load_dataset
import json
import random

init_data = load_dataset("hendrydong/gpqa_diamond_mc", split="test")
data = []
questions = []

for item in init_data:    
    data.append({
        "question": item["problem"],
        "answer": item["solution"],
        "domain": item["domain"]
    })
    questions.append(item["problem"])

with open("gpqa_diamond.json", "w") as f:
    json.dump(data, f, indent=4)