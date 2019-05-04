# Simple Python Web Crawler

This code is based in a [Ahad Sheriff's article](https://medium.freecodecamp.org/how-to-build-a-url-crawler-to-map-a-website-using-python-6a287be1da11). He used [BeautifulSoup](https://pypi.org/project/beautifulsoup4/) and [requests](http://docs.python-requests.org/en/master/) but I decided to use [requests_html](https://github.com/kennethreitz/requests-html) instead ([mongodb]() to save the data and [loguru](https://github.com/Delgan/loguru) to prettify the outputs).

The idea is very simple:
1.  Visit a web page
2.  Scrape all unique URL’s found on the webpage and add them to a queue
3.  Recursively process URL’s one by one until we exhaust the queue
4.  Save the results in a database

Before execute the docker-compose, change the `ROOT_URL` variable (at line 22):
```yml
- ROOT_URL=https://url.com/
```

And after, it's only run normally:
```
docker-compose up --build
```
**Warning**: currently, this program should be used exclusively to crawl local URLs, foreign URLs will take a **VERY** long time. If you want to change this setting, change `ALLOWS_FOREIGN_URLS` to `true`.