# -*- coding: utf-8 -*-
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#
#  Author: Damian Schwyrz

import sys

if sys.version_info < (3, 0):
    sys.stdout.write("Sorry, requires Python 3.x\n")
    sys.exit(1)

from inc.worker import WorkerThread
from inc.arguments import getArguments
from inc.urllist import get_urls
from inc.testdata import create_test_data
import queue
import ssl
import time

ssl._create_default_https_context = ssl._create_unverified_context


def main():
    burp_url, wo_burp_extend, url_list, max_threads, method, timeout = getArguments()

    urls = get_urls(url_list)

    test_data = create_test_data(urls, method, burp_url, wo_burp_extend, timeout)

    print("\033[32m[ i ]\033[0m Starting with scan of {} targets using {}".format(len(test_data), method))

    if wo_burp_extend:

        print("\033[32m[ i ]\033[0m Callback url:   http://{}".format(burp_url))

    else:

        print("\033[32m[ i ]\033[0m Callback url:   http://{}.{}".format("%HOSTNAME%", burp_url))

    print("\033[32m[ i ]\033[0m Threads:        {}".format(max_threads))

    print("\033[32m[ i ]\033[0m HTTP Timeout:   {}".format(timeout))

    print("\033[32m[ i ]\033[0m HTTP Method:    {}".format(method))

    time.sleep(3)

    queue_all = queue.Queue()

    threads = []

    for i in range(0, max_threads):
        print("\033[32m[ i ]\033[0m Worker {} started...".format(i))
        worker = WorkerThread(queue_all, i)
        worker.setDaemon(True)
        worker.start()
        threads.append(worker)

    for data in test_data:
        queue_all.put(data)

    for item in threads:
        item.join()


if __name__ == "__main__":
    main()
