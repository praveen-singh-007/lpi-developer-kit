# How I Did It — Level 2

## What I Did

<!-- WRITE THIS YOURSELF — the README says AI-generated write-ups count against you -->
<!-- Delete these comments and write in your own words. Example structure below: -->

1. Forked and cloned the lpi-developer-kit repo
2. Ran `npm install` and `npm run build` to set up the project
3. Ran `npm run test-client` — all 8 tests passed (7 tools, one tested twice)
4. Installed Ollama and pulled the qwen2.5:1.5b model
5. Ran the example agent (`examples/agent.py`) which connects to the LPI MCP server and feeds results to Ollama
6. Captured all outputs for my submission

## What Problems I Hit

<!-- Write about actual problems you encountered. Some ideas: -->
<!-- - Did you have Node.js version issues? -->
<!-- - Did Ollama fail to connect at first? -->
<!-- - Did the agent script point to wrong paths? -->

## What I Learned

<!-- Write about what you genuinely didn't know before. For example: -->
<!-- - What MCP is and how it works (stdio-based tool calling) -->
<!-- - How Ollama runs LLMs locally without cloud APIs -->
<!-- - What the SMILE methodology is about -->
