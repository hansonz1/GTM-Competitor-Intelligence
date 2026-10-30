# GTM Competitive Intelligence — Case Study

## Executive Summary
Competitive intelligence often suffers from cross-functional coordination challenges and information lag. This delay can leave positioning and sales messaging outdated when competitors introduce new capabilities. This project uses GitHub Actions to schedule and orchestrate the workflow. I implemented Python scripts to collect changelog updates and compare historical snapshots. Finally, integrate Gemini to assess potential GTM impact and generate evidence-aware recommendations. I validated the cloud monitoring pipeline and cross-run snapshot persistence with real data; then used a hypothetical competitor update to generate the structured JSON Battlecard.

## Business Problem
The traditional workflow requires continuous monitoring of competitors' product updates, an analysis from PMMs or competitive intelligence teams, passing findings to marketing teams to adjust positioning changes, and eventually give updated sales enablement materials to the sales team. This process is time-consuming and prone to errors, which may lead to information lag and coordination challenges.

Sometimes, even when an update is detected, it's hard to immediately evaluate its impact on business due to the different target customers and value propositions. An improvement in one competitor's capabilities does not necessarily threaten another company's differentiation when their target customers and value propositions differ. Without contextual analysis, GTM teams may overreact to updates with limited relevance, spending unnecessary time revising positioning or sales messaging. Conversely, missing a relevant competitor update may leave GTM teams relying on outdated differentiation claims and potentially affect sales efficiency. 

## Solution & Architecture
To turn this idea into a working prototype, I first used Python to collect product updates from Folk's changelog page, then built a snapshot comparison system that automatically detects if there's an update of the Changelog page compared against historical snapshots. When new updates are detected, then it leads to Gemini to assess potential GTM impact, identify evidence gaps, and recommend actionable next-steps based on Attio's ICP, differentiation context, and value proposition. I used GitHub Actions to orchestrate and schedule the entire pipeline and output a structured JSON Battlecard.

## Engineering Decisions
### Decision 1: Snapshot-Based Change Detection
To create a snapshot, I used BeautifulSoup to extract headlines from Folk's changelog page, and then extracted update titles against historical snapshots to identify new titles. However, changes to an existing update's body content may go undetected if its headline remains unchanged. Furthermore, creating the comparison before the integration into Gemini API avoids unnecessary AI token spend and repetitive API calls. Ideally on the first run, it will create the baseline version snapshot and it will compare subsequent snapshots against the baseline in the future.

### Decision 2: Evidence-Aware AI Analysis
Gemini provides a powerful foundation for the AI analysis. However, we still need to be cautious about the reliability of the conclusions. Denpend solely on product announcements does not give Gemini a real user example, thus, it may miss actual product capabilities and customer experiences. Therefore, I designed the output schema to include confidence, evidence_gaps, and evidence_status in the report. These fields help PMMs understand uncertainty and identify what requires further verification. This can help the PMMs to avoid prematurely changing their positioning or sales messaging, leading them to conduct further research to validate if the change is really influential.

### Decision 3: GitHub Actions & Snapshot Persistence
Manual daily execution could be annoying. So I chose to use GitHub Actions to automate a daily scheduled task. Using GitHub Cache to store historical snapshots enables change detection across separate workflow runs. However, the GitHub Actions may only be more suitable to early stage deployment because cached data can expire or be evicted.

## Testing & Results
No-Change Test: I tested the collector against Folk's live changelog, successfully extracting 92 update titles and detecting zero new updates. The analyzer skipped the Gemini API call as expected.
Positive Path Test: I created a synthetic test fixture (a mock competitor's update) to test the Gemini Analyzer, and the system successfully generated a structured JSON Battlecard.
Cross-Run Snapshot Persistence: I validated that GitHub Actions could preserve and restore historical snapshots. This allows the system to compare and detect updates across separate workflow runs.
Test Limitation: The synthetic update I used in the previous test is hypothetical and does not represent a verified product announcement.

## GTM Insights & Learnings
Throughout the process, I learned that a company's feature parity does not necessarily mean its value parity. Value parity is emphasizing more on where the company sits in the industry, what marketing strategies they use, and what value they are prodiving their customers.

I also realized that even in the powerful AI era like today, an AI-generated report should always include evidence guardrails and human review. Especially when involving a strategy approach of the company, powerful artificial intelligence can support strategic decision-making, but human judgment and evidence verification remain essential.

Most importantly, I learned so much about Python Automations, API Integrations, and Cloud Workflows during the process. I also learned that clearly defined requirements and constraints are essential when collaborating with AI during development.