rules = [
    {"if": {"A", "B"}, "then": "C"},
    {"if": {"C", "D"}, "then": "E"}
]

facts = {"A", "B", "D"}

def forward_chaining(rules, facts):
    new_facts = set(facts)
    while True:
        added = False
        for rule in rules:
            if rule["then"] not in new_facts and rule["if"].issubset(new_facts):
                print(f"Inferred: {rule['then']} from {rule['if']}")
                new_facts.add(rule["then"])
                added = True
        if not added:
            break
    return new_facts

def backward_chaining(goal, rules, known_facts, depth=0):
    indent = "  " * depth
    if goal in known_facts:
        print(f"{indent}{goal} is already known.")
        return True
    for rule in rules:
        if rule["then"] == goal:
            print(f"{indent}Trying: {goal} via {rule}")
            if all(backward_chaining(subgoal, rules, known_facts, depth + 1) for subgoal in rule["if"]):
                known_facts.add(goal)
                print(f"{indent}Proved {goal}")
                return True
    print(f"{indent}Failed to prove {goal}")
    return False

print("=== Forward Chaining ===")
final_facts = forward_chaining(rules, facts)
print("Final facts:", final_facts)

print("\n=== Backward Chaining ===")
goal = "E"
print(f"Proving goal: {goal}")
result = backward_chaining(goal, rules, set(facts))
print(f"Goal {goal} is", "proved" if result else "not proved")
