# JobBoardsCrawler

## About
A web crawler that scrapes through various Job Boards Online, based on user preference. Developed using Python and Scrapy Library

## Web Crawler using Python and Scrapy Library

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

## Library(s) Used in this Project:
 - Scrapy: 
An open source and collaborative framework for extracting the data you need from websites.
   

## Developer Getting Started Guide:

1. Create and Activate a Python Virtual Environment for the project 

```buildoutcfg
> virtualenv .
> Scripts\activate
```

2. Upgrade PIP (Optional Step) 

```buildoutcfg
> python.exe -m pip install --upgrade pip
```

3. Install Scrapy Library

```buildoutcfg
> pip install scrapy
```

4. Create a src folder and a Spider Script
```buildoutcf
> mkdir src
```
``` SpiderScript.py
import scrapy

class BlogSpider(scrapy.Spider):
    name = 'blogspider'
    start_urls = ['https://www.zyte.com/blog/']

    def parse(self, response):
        for title in response.css('.oxy-post-title'):
            yield {'title': title.css('::text').get()}

        for next_page in response.css('a.next'):
            yield response.follow(next_page, self.parse)
```

5. Run the Spider Script

```buildoutcfg
> scrapy runspider SpiderScript.py
```

6. Debug Configuration for Scrapy with PyCharm

-   Create a Python Configuration in PyCharm 
-   Set Script FilePath to ```<ProjectDir>\Lib\site-packages\scrapy\cmdline.py```
-   Set Parameters to ```runspider $FileName$```
-   Set Python Interpreter to point to Project's Virtual Env Python.exe
-   Set Working Directory to ```<ProjecDirt>\src```
-   Check ```Run With Python Console``` under ```Execution```

![image](https://user-images.githubusercontent.com/42498389/125747364-c5c2a1b5-d24b-4bfe-b2a9-311a6c3d7a94.png)

