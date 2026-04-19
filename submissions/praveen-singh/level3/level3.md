Here is the link to my Level 3 AI Agent repository:
https://github.com/praveen-singh-007/lpi-smile-agent

### Evidence 1: Real Response from LPI Tools
My code actively calls the LPI tools by spawning the Node.js server as a subprocess and sending JSON-RPC requests. Here is the actual raw text returned by the `smile_overview` tool when my code calls it, proving the connection works:

> # S.M.I.L.E. — Sustainable Methodology for Impact Lifecycle Enablement
> Benefits-driven digital twin implementation methodology focusing on impact before data.

### Evidence 2: Explainability (Provenance)
Explainability isn't just a feature in my agent, it's structurally forced. The agent prints a dedicated provenance block at the end of every execution so the user knows exactly where the data came from. Here is the exact output:

PROVENANCE (tools used)
[1] smile_overview (no args)
[2] query_knowledge ({"query": "What is SMILE methodology?"})
[3] get_case_studies (no args)

### Evidence 3: Explainability in Action
Explainability is deeply integrated into the LLM's response. When prompted, the agent uses inline citations to trace its logic back to the tools. Here is an example of what it says when asked to explain a recommendation:

**User Question:** "Why do you recommend starting with Reality Emulation?"
**Agent Answer:** "I recommend starting with Reality Emulation because it is the foundational Phase 1 of the SMILE methodology, which focuses on creating a shared reality canvas before investing heavily in sensors **[Tool 1: smile_overview]**. According to the methodology steps, this phase takes days to weeks and helps establish 'where and when' **[Tool 2: get_methodology_step]**. Furthermore, the 'Smart Heating for Municipal Schools' case study shows that skipping this alignment leads to disjointed data silos later on **[Tool 3: get_case_studies]**."  

**Update:** I have also implemented an Auto-Discovery Path Hunter in my agent so it can be cloned and run universally by reviewers or automated bots without pathing errors.

### Evaluation Questions Answered

**What choices did you make that weren't in the instructions? What would you do differently next time?**
The most critical choice I made outside the standard instructions was implementing an "Auto-Discovery Path Hunter" for the LPI MCP server. Because I built the agent in a completely separate repository to maintain clean modularity, the standard relative pathing (`..`) broke. 

Initially, I hardcoded my local path, but I realized: an automated evaluation bot won't manually set an environment variable, and if it tries to run my code, it will crash. Knowing that CI/CD pipelines typically clone repositories adjacent to each other in a workspace, I wrote a custom `find_lpi_server()` function. It checks for an environment variable first, then intelligently scans adjacent parent directories to accommodate the automated bot's workspace, and finally falls back to a local path. This guarantees the code won't break during automated evaluation or human review.

Next time, to make deployment even more seamless, I would package the agent inside a Docker container using a docker-compose network to connect to the LPI server, eliminating file-path hunting altogether. I would also add an A2A Agent Card dynamically so the agent could integrate directly into the LifeAtlas mesh.
