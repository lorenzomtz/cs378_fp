import json
import os

if __name__ == "__main__" :
    if os.path.exists("./incorrect.json"):
        os.remove("./incorrect.json")
        count = 0
        count_incorrect = 0
    with open('./eval_output/eval_predictions.jsonl', 'r') as f:
        data = list(f)
        for e in data:
            count += 1
            el = json.loads(e)
            if el['predicted_answer'] not in el['answers']['text']:
                count_incorrect += 1
                with open('./incorrect.json', 'a+') as f:
                    json.dump(el, f, indent=4)
    print(count, count_incorrect, ((count-count_incorrect)/count))
