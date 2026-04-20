# How I Actually Built It

## The Big Picture

I wrote a Python agent that talks to the LPI (Life Programmable Interface) sandbox. It takes a question, figures out which tools to call, runs them, and stitches their answers together into something structured and useful.

---

## My Step-by-Step Approach

### 1. Figuring Out the LPI Setup

- Spent some time exploring the LPI Developer Kit to see what tools were available.
- Realized the tools aren't exposed through the test client — they run via a Node.js server at `dist/src/index.js`.
- Noticed that all communication follows JSON-RPC patterns.

### 2. Writing the Agent

- Built a single Python script (`agent.py`) that handles:
  - Reading user input
  - Deciding which tools make sense
  - Launching the Node server and calling tools via subprocess
  - Mashing the results together

### 3. Connecting the Tools

- Picked two tools to work with:
  - `smile_overview` → explains the SMILE methodology
  - `get_case_studies` → pulls real-world examples
- Set up subprocess communication:
  - Started the Node server with `subprocess.Popen`
  - Sent JSON-RPC commands through stdin
  - Read responses from stdout

### 4. Fixing Protocol Headaches

**What broke initially:**
- I was calling `test-client.js` instead of the real server
- Forgot to send the initialization message

**How I fixed it:**
- Switched to `dist/src/index.js`
- Added this required handshake:
  ```json
  {"jsonrpc": "2.0",
          "method": "notifications/initialized"}
  ```
## 5. Digging Into Nested Responses
Tool outputs came back deeply nested:

```json
{
  "result": {
    "content": [
      { "type": "text", "text": "actual content here" }
    ]
  }
}
```
So I had to extract with:

python
result: ```["content"][0]["text"]```

## 6. Making Results Actually Relevant
The problem:
get_case_studies returned examples from multiple industries — not just healthcare.

My fix:
Changed the tool arguments to be more specific:

python
```{"query": "healthcare digital twin"}```
Then manually filtered the response to pull only the healthcare-related parts.

## 7. Assembling the Final Answer

Kept summarization simple — trimmed text instead of splitting sentences (so headings didn't break)

Combined three pieces:

- SMILE methodology summary  
- Healthcare case study  
- Short analysis + conclusion  

---

## What Went Wrong (And How I Fixed It)

### 1. Wrong Tool Executable
**Issue:** Used `test-client.js` at first  

**Result:** Got test logs, no real data  

**Fix:** Switched to the actual server file  

---

### 2. Path and Directory Problems
**Issue:** Node process couldn't find server files  

**Fix:** Explicitly set working directory:

```python
cwd = "lpi-developer-kit"
```

## 3. Empty Outputs
**Issue:** Bad JSON parsing + incomplete stdout reads

**Fix:** Used process.communicate() and proper response parsing

## 4. Irrelevant Case Studies
**Issue:** Tool returned everything, not just what I asked for

**Fix:** Added domain-specific filtering after receiving the response

## What I Learned
- For tool-based agents, data flow and integration matter more than model complexity

- Getting the environment right (paths, working directory, build step) is half the battle

- You have to parse structured responses carefully — no shortcuts

- Using multiple tools dramatically improves answer quality

- Tools often return broad results, so post-filtering is essential

## Where I Ended Up
The agent now:

- Uses multiple tools in one flow

- Pulls real data from the live LPI server

- Processes and filters results intelligently

- Outputs structured, relevant answers
