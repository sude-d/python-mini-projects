# 📚 Web Book Scraper

A Python-based web scraping tool designed to extract book information from online bookstores.

## 🚀 Project Overview
This project uses **BeautifulSoup** and **Requests** to navigate through a bookstore website and collect:
* Book Titles
* Prices
* Availability Status

## 🛠️ Technical Stack
* **Python 3.13**
* **BeautifulSoup4:** For parsing HTML content.
* **Requests:** For handling HTTP requests.

## 💡 Challenges Overcome
* Managed **User-Agent** headers to bypass basic bot detection.
* Handled **NoneType** errors by implementing safe data extraction logic.
* Navigated through different HTML tags (`div`, `p`, `article`) to find the correct data points.

---
*Next Step: Migrating to Selenium for dynamic content scraping!*