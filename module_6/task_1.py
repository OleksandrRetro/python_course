import json
from threading import Thread
from time import perf_counter

import requests
from requests.exceptions import MissingSchema
from requests.exceptions import ConnectionError

from module_6.url_model import UrlModel, UrlModelEncoder
from utils.file_utils import FileUtils


class VerifyURLs:
    """
    Validate URLs form file [/resources/module_6/links.txt]
    Use [threading] and [requests] libraries.
    Save result in file [/resources/module_6/result.json]
    """

    def check_url(self, urls: list) -> None:
        result: list = list()
        for url in urls:
            try:
                response: requests = requests.get(url)
                if response.status_code == 200:
                    result.append(UrlModel(url, True, response.status_code))
                else:
                    result.append(UrlModel(url, False, response.status_code))
            except (ConnectionError, MissingSchema) as _:
                result.append(UrlModel(url, False, None))
        FileUtils.write_json_file_str("module_6/result.json", json.dumps(result, cls=UrlModelEncoder))


if __name__ == '__main__':
    file_path: str = "module_6/links.txt"
    urls: list = FileUtils.read_file_to_list(file_path)

    start_time: float = perf_counter()

    # create and start 10 threads
    threads = []
    for n in range(1, 11):
        t = Thread(target=VerifyURLs().check_url, args=(urls,))
        threads.append(t)
        t.start()

    # wait for the threads to complete
    for t in threads:
        t.join()

    end_time: float = perf_counter()

    print(f'It took {end_time - start_time: 0.2f} second(s) to complete.')
