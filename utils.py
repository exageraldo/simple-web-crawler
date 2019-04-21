from urllib.parse import urlsplit


def remove_fragment(link):
    parts = urlsplit(link)
    if parts.fragment:
        link = f'{parts.scheme}://{parts.netloc}{parts.path}'
    return link


def get_base_url(url):
    parts = urlsplit(url)
    return f'{parts.scheme}://{parts.netloc}'