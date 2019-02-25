#!/usr/bin/env python
# coding: utf8

import threading
import http.client

stopSet = True


class WorkerThread(threading.Thread):
    def __init__(self, queue, tid):
        threading.Thread.__init__(self)
        self.queue = queue
        self.tid = tid

    def run(self):
        global stopSet

        while stopSet:

            try:
                hostname, url, method, burp_url, timeout = self.queue.get(timeout=1)
            except Exception as e:
                stopSet = False
                break

            try:

                if "https" in url:
                    print("\033[32m[ i ]\033[0m [Process: {}] HTTPS-Request to {}".format(self.tid, hostname))
                    connection = http.client.HTTPSConnection(hostname, 443, timeout=timeout)
                else:
                    print("\033[32m[ i ]\033[0m [Process: {}] HTTP-Request to {}".format(self.tid, hostname))
                    connection = http.client.HTTPConnection(hostname, 80, timeout=timeout)

                connection.request(method, burp_url)
                response = connection.getresponse()
                connection.close()

                print("\033[32m[ R ]\033[0m [Process: {}] Request to {} [{}]".format(
                    self.tid, hostname, response.status
                ))

            except Exception as e:
                print("\033[31m[ x ]\033[0m [Process: {}] [Host: {}] Error: {}".format(self.tid, hostname, e))

            self.queue.task_done()
