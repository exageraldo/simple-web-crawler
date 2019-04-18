# Simple Python Web Crawler

This code is based in a [Ahad Sheriff's article](https://medium.freecodecamp.org/how-to-build-a-url-crawler-to-map-a-website-using-python-6a287be1da11). He used [BeautifulSoup](https://pypi.org/project/beautifulsoup4/) and [requests](http://docs.python-requests.org/en/master/) but I decided to use [requests_html](https://github.com/kennethreitz/requests-html) instead (and [loguru]() to prettify the outputs).

The idea is very simple:
1.  Visit a web page
2.  Scrape all unique URL’s found on the webpage and add them to a queue
3.  Recursively process URL’s one by one until we exhaust the queue
4.  Print results

**Warning:** The way the program currently works crawling only local URL's, foreign URL's will take a **VERY** long time.

Before execute the script, change the `url` variable (at line 7):
```python
url = "https://url.com/"
```

And after, it's only run normally:
```
python main.py
```
