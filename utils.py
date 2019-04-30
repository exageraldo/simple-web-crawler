from urllib.parse import urlsplit


def remove_fragment(url):
    parts = urlsplit(url)
    if parts.fragment:
        url = f'{parts.scheme}://{parts.netloc}{parts.path}'
    return url


def get_base_url(url):
    parts = urlsplit(url)
    return f'{parts.scheme}://{parts.netloc}'


def get_url_group(url):
    parts = urlsplit(url)
    path_list = parts.path.split('/')
    path_list = [path for path in path_list if path]
    if len(path_list) > 1:
        return path_list[0]
    return 'root'


def url_categorizer(url_list):
    dict_result = dict()
    for url in url_list:
        group = get_url_group(url)
        if group in dict_result:
            dict_result[group].append(url)
        else:
            dict_result[group] = [url]
    return dict_result


def base_categorizer(url_list):
    dict_result = dict()
    for url in url_list:
        base = urlsplit(url).netloc
        if base in dict_result:
            dict_result[base].append(url)
        else:
            dict_result[base] = [url]
    return dict_result
