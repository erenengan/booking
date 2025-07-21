# Hotel Price Analysis from Booking.com

This project collects, analyzes, and models hotel price data scraped from [Booking.com](https://www.booking.com). It aims to explore how factors such as location, customer rating, and amenities influence hotel prices in a major city. The ultimate goal is to build a predictive model that estimates hotel prices based on these features.

---

## Project Overview

- **Data Source**: Booking.com listings, scraped using Selenium
- **Objective**: Understand pricing factors and build a regression model to predict hotel prices
- **Technologies**: Python, Pandas, Seaborn, Scikit-learn, Selenium

---

## Motivation

Online hotel prices can vary significantly even within the same city. By analyzing structured data on hotel listings, we seek to answer:
- What features are most correlated with higher prices?
- Can we accurately predict hotel prices based on a few key variables?

---

## Project Structure

```bash
.
├── booking_sel.py               # Web scraping script (Selenium)
├── hotels.csv                   # Cleaned dataset of hotel listings
├── hotel_price_analysis.ipynb   # Main notebook: EDA, modeling, visualizations
├── requirements.txt             # Python dependencies
└── README.md                    # Project overview and documentation
