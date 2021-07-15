import scrapy


class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    start_urls = [
        'https://weworkremotely.com/',
    ]

    def parse(self, response):
        # for job in response.css('li.feature'):
        #     yield {
        #         'Company': job.css('span.company::text').get(),
        #         'Job Title': job.css('span.title::text').get(),
        #         'Location': job.css('span.region::text').get(),
        #     }
        # for job_section in response.css('section.jobs'):
        #     yield {
        #         'Section': job_section.xpath('article/h2/a/text()').get(),
        #         'View All': job_section.css('li.view-all a::attr("href")').get(),
        #     }

        for job_section in response.css('section.jobs'):
            section = job_section.xpath('article/h2/a/text()').get()

            if section == "Full-Stack Programming Jobs":
                for job in job_section.css('li.feature'):
                    location = job.css('span.region::text').get()

                    if location == "Anywhere (100% Remote) Only":
                        yield {
                            'Company': job.css('span.company::text').get(),
                            'Job Title': job.css('span.title::text').get(),
                        }

            next_page = job_section.css('li.view-all a::attr("href")').get()
            if next_page is not None:
                yield response.follow(next_page, self.parse)
