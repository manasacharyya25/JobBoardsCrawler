# Web Crawler using Python and Scrapy Library

## About

Web crawlers programmatically scans through a collection of web pages, and extracts information according to specified rules.

The basic workflow of a general web crawler is as follows:

1. Get the initial URL. The initial URL is an entry point for the web crawler, which links to the web page that needs to be crawled;

2. While crawling the web page, we need to fetch the HTML content of the page, then parse it to get the URLs of all the pages linked to this page.

3. Put these URLs into a queue;

4. Loop through the queue, read the URLs from the queue one by one, for each URL, crawl the corresponding web page, then repeat the above crawling process;

5. Check whether the stop condition is met. If the stop condition is not set, the crawler will keep crawling until it cannot get a new URL.

## Why use a Scraping Library

Python by default has enough modules to perform the task of web scraping as specified in the workflow above. But using a Scrapnig Library takes care
of lot of non-functional requirements like :

- Allow Concurrent Crawling of more than one web page at a time
- Transform Crawled Data into different formats for eg. CSV, XML, JSON etc.
- Dealing with Sites that require specific access patterns.
