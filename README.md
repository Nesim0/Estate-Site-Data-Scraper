# Estate Data Scraper

## Description
The purpose of this project is to extract data for properties for sale from a real estate website and save it in JSON format. Additionally, the collected data can be converted into Excel and CSV formats. Due to the volume of data, this scraper is designed to work on a single page. To scrape multiple pages, we can create a for loop that appends the count value to the URL to retrieve data from other pages. The loop can continue until it returns to the starting page: https://www.emlakjet.com/satilik-konut/.

### Loop URL
Url to use in the loop: `https://www.emlakjet.com/satilik-konut/{count}/`

## Features
- Extracts property data from a specified estate website.
- Saves data in JSON format.
- Converts JSON data into Excel and CSV formats.

## Notes
The URLs and data in this project are arbitrary and used solely for demonstration purposes. The content collected from EmlakJet is not intended for any specific use, and the data has no meaningful value. This project is designed to serve as a placeholder for learning and testing web scraping techniques