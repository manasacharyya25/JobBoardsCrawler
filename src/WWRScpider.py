import scrapy


class WWRSpider(scrapy.Spider):
    name = 'quotes'
    start_urls = [
        'https://weworkremotely.com/categories/remote-full-stack-programming-jobs',
        'https://weworkremotely.com/categories/remote-front-end-programming-jobs',
        'https://weworkremotely.com/categories/remote-back-end-programming-jobs'
    ]

    def parse_job(self, job):
        job_header = job.css('div.listing-header')
        job_posted = job_header.xpath('div/h3/time/text()').get()
        organisation_name = job_header.css('h2 a::text')[1].get()
        role_name = job_header.css('h1::text').get()

        job_desc = job.css('div.listing-container').get()

        # TODO: 1. Create Search Tag
        # TODO      2. Regex Search
        if job_desc and 'Java' in job_desc:
            yield {
                'Posted Date': job_posted,
                'Organisation': organisation_name,
                'Role': role_name,
                'Url': job.request.url
            }

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

        for job in response.css('li.feature'):
            location = job.css('span.region::text').get()

            if location == "Anywhere (100% Remote) Only":
                job_desc_page = job.xpath('a/@href').get()
                yield response.follow(job_desc_page, self.parse_job)

            # for job in response.css('li.feature'):
            #     location = job.css('span.region::text').get()
            #
            #     if location == "Anywhere (100% Remote) Only":
            #         yield {
            #             'Company': job.css('span.company::text').get(),
            #             'Job Title': job.css('span.title::text').get(),
            #         }

            # next_page = job_section.css('li.view-all a::attr("href")').get()
            # if next_page is not None:
            #     yield response.follow(next_page, self.parse)
