Here is the link to my Level 3 AI Agent repository: https://github.com/praveen-singh-007/lpi-life-agent

### My AI Agent Implementation
I built a Python-based AI agent that directly communicates with the LPI MCP server via **JSON-RPC over stdio**.  
The agent deterministically queries three SMILE-related tools:

- `smile_overview` — retrieves the core SMILE methodology  
- `query_knowledge` — fetches query-specific contextual knowledge  
- `get_case_studies` — provides real-world examples  

The outputs from these tools are combined into a structured prompt and passed to a **local LLM (Ollama – qwen2.5:1.5b)**.  
The model is explicitly instructed to answer using only the provided context and cite tool sources, ensuring explainability.

---

### Evidence of Execution and Explainability
Below is the actual output from running the agent locally, demonstrating:

- Sequential tool execution  
- Integration of multiple LPI sources  
- Clear provenance tracking  

```text
[1/3] Querying SMILE overview...
[2/3] Searching knowledge base...
[3/3] Checking case studies...

Sending to LLM (Ollama)...

============================================================
  ANSWER
============================================================
SMILE methodology prioritizes impact over data in its digital twin implementation process. It involves creating a shared reality canvas for establishing where and when, defining the scope (as is to to be), validating hypotheses virtually, connecting physical sensors, sharing ontologies, and leveraging knowledge across time periods.

============================================================
  PROVENANCE (tools used)
============================================================
  [1] smile_overview (no args)
  [2] query_knowledge {"query": "What is SMILE methodology?"}
  [3] get_case_studies (no args)
