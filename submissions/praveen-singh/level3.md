# Level 3 Submission — Praveen Singh

## Project: Explainable Knowledge Agent (LPI)

**Repository:** https://github.com/praveen-singh-007/lpi-life-agent
**Code** https://github.com/praveen-singh-007/lpi-life-agent/agent.py
**A2A Card**  https://github.com/praveen-singh-007/lpi-life-agent/agent.json

---

## What This Project Does

This is a Level 3 agent built on the Life Programmable Interface (LPI). Instead of just calling one tool, it picks multiple tools based on the user's question, runs them, processes their results, and then puts together a clean, structured answer.

---

## Tools Integrated

- `smile_overview` → explains the SMILE methodology  
- `get_case_studies` → fetches real-world implementation examples  

---

## Step-by-Step Workflow

1. Accepts a user question (e.g., something about healthcare)  
2. Chooses two relevant tools to answer it  
3. Sends JSON-RPC requests to the LPI server  
4. Gets structured data back from each tool  
5. Parses the responses and pulls out the useful text  
6. Filters case studies to keep only healthcare-related ones  
7. Merges everything into one final answer  

---

## Key Capabilities

- Coordinates multiple tools in one flow  
- Dynamically adjusts tool arguments as needed  
- Uses JSON-RPC communication via subprocess calls  
- Produces a structured final response (summary + analysis + conclusion)  
- Filters results by domain (e.g., healthcare only)  

---

## Example Query

```text
How are digital twins being used in healthcare today?
```

## Example Output (Summary)

- Overview of the SMILE framework

- A healthcare case study focused on continuous patient twinning

- Analysis connecting the methodology to the actual application

## Level 3 Requirements Met
  ✅ Uses more than one tool
  
  ✅ Combines outputs from different tools
  
  ✅ Processes and restructures tool responses
  
  ✅ Delivers a meaningful, final answer
  
  ✅ Shows reasoning across tool outputs

## Implementation Notes
- Talks to the real LPI server (dist/src/index.js), not a mock client

- Filters case studies to match the user's domain

- Built with Python + Node.js (LPI runtime)

## Going Beyond the Instructions
**What I added on my own**
- Filtered tool outputs to return only healthcare-relevant case studies instead of dumping everything.

- Modified tool arguments (e.g., used "healthcare digital twin") to make results more relevant instead of blindly passing the raw query.

- Manually parsed nested JSON-RPC responses (result → content → text).

- Used the actual LPI server with explicit initialization instead of the test client.

**What I'd improve next time**
- Abstract the tool-calling logic into a reusable client separate from the agent logic.

- Add explicit reasoning traces to show why each tool was chosen and how outputs were merged.

- Improve summarization with consistent structure (Challenge → Approach → Outcome) instead of truncation.

- Make tool selection adaptive rather than rule-based.
