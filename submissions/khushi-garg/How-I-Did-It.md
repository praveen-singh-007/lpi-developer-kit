# How I Did It – Level 2 (Khushi Garg)

## Step 1: Cloned the Repository
I cloned the LPI Developer Kit repository to my local system using:
git clone https://github.com/g-khushi/lpi-developer-kit.git

Then I navigated into the project folder:
cd lpi-developer-kit

## Step 2: Installed Dependencies
I installed all required packages using:
npm install

This ensured that all necessary libraries were available for the project.

## Step 3: Built the Project
I built the project using:
npm run build

This step prepared the project for execution.


## Step 4: Ran the Test Client
I executed:
npm run test-client

This step tested whether the AI agent and tools were working properly.

## Step 5: Verified Output
The test client ran successfully and showed outputs for all tools:

[PASS] smile_overview  
[PASS] query_knowledge  
[PASS] get_case_studies  
[PASS] get_insights  
[PASS] list_topics  
[PASS] smile_phase_detail  
[PASS] get_methodology_step  

This confirmed that all tools were working correctly.

## Step 6: AI Model Setup
I used the LLaMA3 model via Ollama to run the AI locally without APIs.  
The model successfully generated responses related to digital twin concepts using SMILE methodology.


## Step 7: Understanding SMILE
Through this process, I understood how the SMILE methodology works:
- It structures AI responses into meaningful steps
- It helps in explaining real-world concepts like digital twins clearly
- It connects tools with AI-generated insights

## Conclusion
By successfully running the test client and verifying outputs, I confirmed that my local setup is working correctly.  
This completes Level 2 of the LPI Developer Kit.
