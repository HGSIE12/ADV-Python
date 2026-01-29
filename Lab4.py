import json

data = {
    "config": {
        "epochs": 5,
        "learning_rate": 0.01
    },
    "results": {
        "accuracy": 0.9,
        "loss": 0.1
    }
}

print("Config:", data["config"])

print("Results:", data["results"])

with open("results.json", "w") as f:
    json.dump(data, f, indent=4)