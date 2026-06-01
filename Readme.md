# YC 26 Batch Analyzer 🚀

A Python-based data analysis project that fetches YC 2026 startup data, analyzes trends, and visualizes insights.

## Libraries Used

- requests
- pandas
- matplotlib
- json
- python-dotenv

## Features

- Fetches startup data from YC's Algolia API
- Filters and structures company information
- Analyzes startup trends and distributions
- Generates visual reports automatically

## Sample Metrics

- Total startups analyzed
- Team size distribution
- Most popular industries
- Most common startup tags
- Top office locations
- AI vs Non-AI startup ratio


## Generated Insights

### Team Size Distribution
![Team Sizes](./Team%20Sizes.png)

### Top Industries
![Top Industries](./Top%20industries.png)

### Top Startup Tags
![Top Startup Tags](./Top%20startup%20tags.png)

### Office Locations
![Office Locations](./Office%20Locations.png)

### AI vs Non-AI Startups
![AI vs Non-AI](./AI%20vs%20Non-AI.png)

## Project Structure

```text
YC-26-BATCH-ANALYZER/
│
├── main.py
├── .env
├── companies.json
├── reqCompaniesData.json
├── Team Sizes.png
├── Top industries.png
├── Top startup tags.png
├── Office Locations.png
├── AI vs Non-AI.png
└── README.md
```

## Run Locally

```bash
pip install requests pandas matplotlib python-dotenv
python main.py
```
---

Built for learning:
**Requests → APIs → JSON → Pandas → Data Analysis → Matplotlib**