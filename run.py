from crawler import crawler
from loguru import logger
from mongo import save_links
import os
from datetime import datetime
from collections import deque
from utils import url_categorizer


def run_crawler(url, allows_foreign_urls=False):
    deque_urls = deque([url])
    broken_urls = []
    all_links = {}
    while deque_urls:
        url = deque_urls.popleft()
        if url in broken_urls:
            continue
        crawled_data = crawler(url)
        if allows_foreign_urls:
            deque_urls += deque(crawled_data['foreign_urls'])
            broken_urls += crawled_data['broken_urls']
        all_links[crawled_data['base_url']] = crawled_data
        save_links(
            crawled_data['base_url'],
            {   
                'base_url': crawled_data['base_url'],
                'processed_urls': url_categorizer(
                    crawled_data['processed_urls']
                ),
                'foreign_urls': crawled_data['foreign_urls'],
                'updated_at': datetime.now()
            }
        )
    return all_links



if __name__ == "__main__":
    def _str2bool(var):
        if var.lower() in ['true', 'yes', '1']:
            return true
        return False

    url = os.getenv('ROOT_URL')
    allows_foreign_urls = _str2bool(
        os.getenv('ALLOWS_FOREIGN_URLS', '')
    )
    if url:
        run_crawler(url, allows_foreign_urls)
    else:
        logger.warning('NO ROOT_URL DEFINED')