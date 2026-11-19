# Practical 3: Code Explanation & Viva Guide
## 🩺 Rule-Based Expert System (Forward & Backward Chaining)

---

### 🎯 Aim of the Practical
To implement a medical diagnosis **Rule-Based Expert System** using both **Forward Chaining** (data-driven) and **Backward Chaining** (goal-driven) inference mechanisms.

---

### 🧩 Chunk-by-Chunk Code Breakdown

#### 🔹 Chunk 1: Knowledge Base Representation
```python
rules = [
    (["Fever", "Cough"], "Flu"),
    (["Flu", "BodyPain"], "ViralInfection"),
    (["ViralInfection"], "Medicine"),
    (["Sneezing"], "Cold"),
    (["Cold"], "Rest")
]
```
- **What it does:**
  - Defines the **Knowledge Base** as a collection of `IF-THEN` production rules.
  - Each rule is structured as a tuple: `(premises_list, conclusion)`.
  - For example: `IF Fever AND Cough THEN Flu`.

---

#### 🔹 Chunk 2: Forward Chaining (Data-Driven Inference)
```python
def forward_chaining(facts):
    inferred = set(facts)
    changed = True
    while changed:
        changed = False
        for premises, conclusion in rules:
            if all(p in inferred for p in premises) and conclusion not in inferred:
                inferred.add(conclusion)
                print(f"Rule Fired: {premises} -> {conclusion}")
                changed = True
    return inferred
```
- **What it does:**
  - Starts with known initial facts (`inferred = set(facts)`).
  - Iterates repeatedly through all rules in the knowledge base:
    1. `all(p in inferred for p in premises)` checks if **every** required premise of a rule is currently satisfied.
    2. `conclusion not in inferred` prevents duplicate firing of the same rule.
    3. When a rule fires, its conclusion is added to the facts set, and `changed = True` tells the loop to keep checking for newly enabled rules.
  - Stops when no new rules can be fired (`changed == False`).
- **Viva Examiner Tip:**
  - *Examiner:* "Why is Forward Chaining called 'data-driven'?"
  - *Answer:* Because it begins with bottom-level raw data/facts and drives forward toward unknown conclusions.

---

#### 🔹 Chunk 3: Backward Chaining (Goal-Driven Recursive Inference)
```python
def backward_chaining(goal, facts, visited=None):
    if visited is None:
        visited = set()
    if goal in facts:
        return True
    if goal in visited:
        return False
    visited.add(goal)
    for premises, conclusion in rules:
        if conclusion == goal:
            if all(backward_chaining(p, facts, visited) for p in premises):
                print(f"Goal '{goal}' proved via rule premises {premises}")
                return True
    return False
```
- **What it does:**
  - Starts with a target hypothesis/goal (e.g., `"Medicine"`).
  - **Base Case 1:** `if goal in facts:` $\rightarrow$ Goal is an already confirmed initial fact, returns `True`.
  - **Base Case 2:** `if goal in visited:` $\rightarrow$ Prevents infinite loops in cyclic rule graphs.
  - **Recursive Step:** Finds rules that can conclude the goal (`conclusion == goal`). Then recursively checks if all premises (`p`) of that rule can themselves be proven from the known facts.
- **Viva Examiner Tip:**
  - *Examiner:* "Why is Backward Chaining called 'goal-driven'?"
  - *Answer:* Because it begins with a top-level goal/hypothesis and works backward down the chain to check whether facts exist to support it.

---

#### 🔹 Chunk 4: Driver Execution
```python
if __name__ == "__main__":
    facts = {"Fever", "Cough", "BodyPain"}

    print("--- Forward Chaining ---")
    print("Inferred Facts:", forward_chaining(facts))

    print("\n--- Backward Chaining ---")
    goal = "Medicine"
    print(f"Is goal '{goal}' proved?:", backward_chaining(goal, facts))
```
- **Output:**
  - Forward chaining deduces: `Flu` $\rightarrow$ `ViralInfection` $\rightarrow$ `Medicine`.
  - Backward chaining verifies: `Medicine` is confirmed `True`.

---

### 🎤 Top Viva Questions & Instant Answers for Practical 3

**Q1: What are the three main components of an Expert System?**
1. **Knowledge Base:** Stores domain rules and facts.
2. **Inference Engine:** Applies reasoning (forward/backward chaining) to derive decisions.
3. **User Interface / Explanation Facility:** Interacts with the user and explains why a conclusion was reached.

**Q2: When should Forward Chaining be used vs Backward Chaining?**
- Use **Forward Chaining** when you have a lot of incoming data and want to see what conclusions follow (e.g., monitoring, fault detection, alarms).
- Use **Backward Chaining** when you have a specific hypothesis to verify or diagnose (e.g., medical diagnosis, debugging code).

**Q3: What is Conflict Resolution in Rule-Based Systems?**
- When multiple rules can fire at the same time, Conflict Resolution decides which rule fires first (e.g., by rule priority, specificity, or recency).
