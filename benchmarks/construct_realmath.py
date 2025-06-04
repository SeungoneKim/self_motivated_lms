from datasets import load_dataset
import json
import random

data = []
questions = []
for s in ["Math_arXiv","CS_arXiv","Math_StackExchange"]:
    init_data = load_dataset("ethz-spylab/RealMath", split=s)
    

    for item in init_data:    
        data.append({
            # "question": "Please reason step by step, and put your final answer within \\boxed{} in the prompt.\n\nQuestion: "+item["question"]+"\n\nContext: "+item["context"]+"\n\n",
            "question": item["question"]+"\n\n"+"Please reason step by step, and put your final answer within \\boxed{} in the prompt.",
            "context": item["context"],
            "answer": item["answer"],
            "theorem": item["theorem"]
        })
        questions.append(item["question"])

    with open("realmath.json", "w") as f:
        json.dump(data, f, indent=4)