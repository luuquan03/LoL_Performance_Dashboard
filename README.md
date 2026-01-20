# League of Legends Performance Analytics Dashboard 🎮📊

## Overview
This project focuses on analyzing personal match history data from **League of Legends** using the **Riot Games API**. The goal is to track performance metrics, identify trends in combat efficiency, and optimize gameplay strategies through data visualization in **Power BI**.

## Key Questions Answered
- What is my overall win rate and KDA performance across recent matches?
- How does my Gold Per Minute (GPM) fluctuate, and what is its correlation with winning?
- Which "First Item" builds (Kraken, BORK, Yun Tal) yield the highest win rates?
- How does my combat efficiency (Damage/Min) relate to my KDA in different match scenarios?

## Tools Used
- **Power BI:** For creating interactive dashboards and performing data modeling (DAX).
- **Riot Games API:** Sourced match history and player statistics.
- **Python (Optional):** For data extraction and handling nested JSON structures from the API.
- **Excel/CSV:** Used as a middle-layer for data cleaning.

## Dashboard Highlights
- **Win Rate & KDA Tracker:** Provides a high-level summary of performance (Current Win Rate: 65%).
- **GPM Analysis:** Visualizes gold accumulation efficiency over time.
- **Build Path Optimization:** A pie chart comparing the selection rate and win probability of different item builds.
- **Performance Scatter Plot:** Analyzes the relationship between Damage Per Minute (DPM) and Total KDA.

## Insights Derived
- **Build Efficiency:** Found that the "Kraken" build has a 53% selection rate with an 86% win rate, significantly outperforming other starts.
- **Combat Consistency:** Identified a positive correlation between maintaining a DPM above 800 and securing a match grade of 'S'.
