# Vid Game Best Sellers Spider README 🎮
## Project Overview
This project is a web scraping spider built using Scrapy, a Python framework for building web scrapers. The spider is designed to extract data from the Amazon.co.za Best Seller section for video games.

## Project Structure
vid_game_best_sellers_spider.py: The main spider file containing the Scrapy Spider class.

## Configuration 🤖
allowed_domains: The spider is configured to scrape data from tinyurl.com.
start_urls: The spider starts scraping from the URL https://tinyurl.com/4swm2a8b, which redirects to the Amazon.co.za Best Seller section for video games.

## To-Do List 👾
13/06/2024: Modify the spider to suit the project's crawling needs.

## Running the Spider 🕷️
To run the spider, navigate to the project directory and execute the following command:
```
Open In Editor
Edit
Copy code
scrapy crawl vid-game-best-sellers
Note: This spider is currently in development and does not extract any data. The parse method is empty and needs to be implemented to extract the desired data.
```

## Contributing
If you'd like to contribute to this project, please fork the repository and submit a pull request with your changes.

## NB: The README is subject to change as the solution comes together.
