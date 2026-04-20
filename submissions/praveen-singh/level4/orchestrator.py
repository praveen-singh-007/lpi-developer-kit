import json
from agent_a_expert import run_agent_a
from agent_b_grounding import run_agent_b


# ---- ORCHESTRATOR ----
def run_system():
    print("=== LPI MULTI-AGENT SYSTEM ===\n")

    use_case = input("Enter use case: ")
    constraints = input("Enter constraints: ")

    # ---- STEP 1: CALL AGENT B ----
    print("\n[Orchestrator] Calling Grounding Agent...\n")

    grounding_output = run_agent_b({
        "use_case": use_case
    })

    print("[Agent B Output]")
    print(json.dumps(grounding_output, indent=2))

    # ---- STEP 2: CALL AGENT A ----
    print("\n[Orchestrator] Calling Decision Agent...\n")

    agent_a_input = {
        "use_case": use_case,
        "constraints": constraints,
        "grounding_data": grounding_output   # structured JSON passed
    }

    final_output = run_agent_a(agent_a_input)

    # ---- FINAL RESULT ----
    print("\n=== FINAL DEPLOYMENT STRATEGY ===\n")
    print(final_output["strategy"])

    print("\n=== TRACE (Explainability) ===\n")
    print("Grounding data used →", json.dumps(grounding_output, indent=2))


# ---- RUN ----
if __name__ == "__main__":
    run_system()
