from crawler import run_crawler
from loguru import logger
import os


if __name__ == "__main__":
    url = os.getenv('ROOT_URL')
    allows_foreign_urls = os.getenv('ALLOWS_FOREIGN_URLS', False)
    if url:
        run_crawler(url, allows_foreign_urls)
    else:
        logger.warning('NO ROOT_URL DEFINED')