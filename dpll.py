def dpll(clauses, assignment):
    if not clauses:
        return assignment
    if any(not c for c in clauses):
        return None
    for c in clauses:
        if len(c) == 1:
            lit = c[0]
            new_clauses = [[l for l in clause if l != -lit] for clause in clauses if lit not in clause]
            result = dpll(new_clauses, {**assignment, abs(lit): lit > 0})
            if result:
                return result
            return None
    literals = {l for c in clauses for l in c}
    for lit in literals:
        if -lit not in literals:
            new_clauses = [clause for clause in clauses if lit not in clause]
            result = dpll(new_clauses, {**assignment, abs(lit): lit > 0})
            if result:
                return result
    lit = next(l for c in clauses for l in c)
    for val in [lit, -lit]:
        new_clauses = [[l for l in clause if l != -val] for clause in clauses if val not in clause]
        result = dpll(new_clauses, {**assignment, abs(val): val > 0})
        if result:
            return result
    return None

clauses = [[1, 2], [-1, -2]]
result = dpll(clauses, {})
print("Satisfiable" if result else "Unsatisfiable", result)
