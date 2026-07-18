import json

with open("responses.json", "r", encoding="utf-8") as file:
    rules = json.load(file)


def get_response(message):
    message = message.lower().strip()

    for rule in rules:
        for pattern in rule["patterns"]:
            if pattern.lower() in message:
                return rule["response"]

    return "Sorry, I don't understand your question."
