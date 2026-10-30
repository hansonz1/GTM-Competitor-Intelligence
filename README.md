## Project Title: 
GTM Competitive Intelligence & Sales Analysis

## Value Proposition:
This project is an AI-powered system designed for product marketing and GTM leaders. Using Attio as a case study, it monitors competitor's product updates with evidenced analysis of potential impact and recommendations, and assists the Product Marketing Managers (PMM) to make more efficient and informed positioning decisions. 

## Problem Statement:
The traditional workflow requires a close track of competitors' product updates, an analysis from PMMs or competitive intelligence teams, pass on to the marketing team to adjust positioning changes, and eventually give updated sales enablement materials to the sales team. This process is time-consuming and prone to errors, which may lead to outdated marketing strategy and inaccurate sales messaging.  

If the update is delayed, or the process is taking too much time, then the sales representatives cannot give more precise sales messaging that reflect the current competitive landscape.

## Solution Overview
To solve the problem, GTM Competitive Intelligence & Sales Analysis uses GitHub Actions to schedule a Python-based changelog collector and detect the new updates (in this case, Folk). It automatically compares latest snapshot with the previously collected snapshot, and finds out which product updates are new. Then, it passes on to Gemini to assess the potential impact of detected changes on Attio's differentiation, then generates a report and battlecard including confidence, evidence gaps, and recommendations.

## Technical Architecture
1. GitHub Actions - Orchestrates daily scheduled pipeline and supports manual execution.
2. Python Collector - Uses Requests and BeautifulSoup to extract product update titles from Folk's changelog.
3. Snapshot Comparison - Compare latest snapshot with historical snapshot to detect new changes.
4. Gemini Analyzer - If new updates are detected, use Gemini to analyze its impact, illustrate evidence gaps, provide recommendations, and generate report.
5. JSON Battlecard - Produces a structured JSON Battlecard containing potential impact, confidence, evidence gaps, recommended actions, and evidence status.

## How to Run

### Prerequisites
- Python: Python 3.12+ to run collector and analyzer
- Git: to clone the project from Github
- Python Dependencies: Required packages listed in requirements.txt.
- Gemini API Key: to access Gemini to execute AI Analysis

### Local Setup

#### 1. Clone the Repository
```bash
git clone https://github.com/hansonz1/gtm-competitor-intelligence.git
cd gtm-competitor-intelligence
```
#### 2. Install Dependencies
```bash
python -m pip install -r requirements.txt
```
#### 3. Configure Gemini API Key
This project uses Google Gemini for AI-powered competitive analysis. A Gemini API key is required to run the AI Analyzer. 
```bash
export GEMINI_API_KEY="YOUR_API_KEY"
```
!!! Important: Never commit your API key to GitHub or expose it in public repositories.!!!
#### 4. Run the Collector
```bash
python collector.py
```
The first run creates a baseline snapshot. Subsequent runs compare newly collected updates against historical data.
#### 5. Run the AI Analyzer
```bash
python ai_analyzer.py
```
If no new competitor updates are detected, the analyzer skips the AI analysis to avoid unnecessary use of token.

## Testing & Validation
1. No-Change Test:
The system was tested with real Folk changelog and successfully skipped unnecessary Gemini API calls.

2. Positive Path Test:
A synthetic competitor update was used to test the Gemini Analyzer, and the system successfully generated a structured JSON Battlecard.

3. Test Limitation:
The synthetic update is hypothetical and does not represent a verified product announcement.

## Limitations & Future Improvements
### Limitation 1: 
#### The project currently uses Attio as a case study and monitors only one competitor, Folk.
   
**Future Improvement**: Expand monitoring to multiple competitors and consolidate all their updates into a unified competitive intelligence report for better marketing strategy purpose.
### Limitation 2: 
#### Although requires AI to give every analysis a evidence-based reason, it does not ensure every conclusion has been verified.
   
**Future Improvement**: Introduce source-backed claim verification and human review before accepting AI-generated recommendations.
### Limitation 3: 
#### The example of Attio is given, and the project cannot change according to different industry or companies.
    
**Future Improvement**: Add company and industry specific onboarding that generates a draft ICP and positioning baseline for human verification before competitive analysis.