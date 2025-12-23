def generate_markdown(sector: str, analysis: dict):
    return f"""
# Trade Opportunity Analysis: {sector.capitalize()} Sector (India)

## Executive Summary
{analysis['summary']}

## Opportunities
- {analysis['opportunities'][0]}
- {analysis['opportunities'][1]}
- {analysis['opportunities'][2]}

## Risks
- {analysis['risks'][0]}
- {analysis['risks'][1]}

## Outlook
{analysis['outlook']}
"""
