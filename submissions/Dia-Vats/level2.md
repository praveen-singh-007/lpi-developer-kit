# Level 2 submission - Dia Vats


## Test Client Output
```
=== LPI Sandbox Test Client ===

[LPI Sandbox] Server started — 7 read-only tools available
Connected to LPI Sandbox

Available tools (7):
  - smile_overview: Get an overview of the S.M.I.L.E. methodology
  - smile_phase_detail: Deep dive into a specific SMILE phase.
  - query_knowledge: Search the LPI knowledge base
  - get_case_studies: Browse or search anonymized case studies
  - get_insights: Get digital twin implementation advice
  - list_topics: Browse all available topics
  - get_methodology_step: Get step-by-step guidance 

[PASS] smile_overview({})
[PASS] smile_phase_detail({"phase":"reality-emulation"})
[PASS] list_topics({})
[PASS] query_knowledge({"query":"explainable AI"})
[PASS] get_case_studies({})
[PASS] get_case_studies({"query":"smart buildings"})
[PASS] get_insights({"scenario":"personal health digital twin","tier":"free"})
[PASS] get_methodology_step({"phase":"concurrent-engineering"})

=== Results ===
Passed: 8/8
Failed: 0/8

All tools working. Your LPI Sandbox is ready.
```


## Track A: S.M.I.L.E. Methodology Reflection & LLM Output

I **chose** to run the **mistral** model locally via Ollama because it balanced speed and performance for local execution.  
Gemma4:e2b was too slow on my system, so I switched to a lighter model.  
It handled SMILE prompt effectively without needing cloud models.

**Model Output:**

"1. Modeling  
We create digital models of physical assets like machines or buildings. This helps us understand and predict behavior.
2. Simulation  
We run simulations on these models to test behavior under different conditions and predict issues.
3. Integration  
We connect models with real-world sensor data so the digital twin reflects the actual system state.
4. Leverage  
We use the digital twin to optimize operations, predict maintenance, train staff, and improve design.
We use the digital twin to optimize operations, predict maintenance, train staff, and improve design."

---

**SMILE Reflection:**

1. It starts with understanding the real-world problem first, not with data or models.  
2. It is structured in clear phases where each step builds on the previous one.  
3. It prioritizes problem definition and system connection over technical complexity.

---

