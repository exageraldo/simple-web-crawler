from requests_html import HTMLSession
from urllib.parse import urlsplit, urlparse
from collections import deque
from loguru import logger


def crawler(url):
    deque_urls = deque([url])
    processed_urls = set()
    broken_urls = set()
    foreign_urls = dict()

    while deque_urls:
        local_urls = set()
        session = HTMLSession()
        url = deque_urls.popleft()
        processed_urls.add(url)
        logger.info(f'Processing {url}')

        try:
            response = session.get(url)
        except Exception as e:
            logger.error(f'URL: {url} | Error: {e}')
            broken_urls.add(url)
            continue

        parts = urlsplit(url)
        base_url = f'{parts.scheme}://{parts.netloc}'
        links = response.html.absolute_links

        for link in links:
            if not (link in processed_urls) and not (link in deque_urls):
                if link.startswith(base_url):
                    local_urls.add(link)
                else:
                    foreign_splited = urlsplit(link)
                    foreign_base = f'{foreign_splited.scheme}://{foreign_splited.netloc}'
                    if foreign_base in foreign_urls:
                        foreign_urls[foreign_base].append(link)
                    else:
                        foreign_urls[foreign_base] = [link]

        logger.info(f'Local: {len(local_urls)}')
        logger.info(f'Foreign: {len(foreign_urls)}')

        deque_urls += deque(local_urls)

    result_data =  {
        'base_url': base_url,
        'processed_urls': list(processed_urls),
        'broken_urls': list(broken_urls),
        'foreign_urls': foreign_urls
    }
    logger.info(f'Processed: {len(result_data["processed_urls"])} ({len(result_data["broken_urls"])} broken)')
    return result_data
