### Simple "OOB Read/SSRF" via Path"-Scanner

Quick and dirty, based on a finding some days ago which allowed access to the internal network of a known company. 
It basically sends a request to a host while replacing the path with a burp collaborator payload. Then you just have to
watch if something pops up in the client. This tool __only__ handles the path injection point, nothing else!

#### Examples

That command grabs all urls and sends GET requests with 5 threads:
```
python3 simple-oob-scanner.py -b 31337.burpcollaborator.net -u example/url_list.txt
```

That one just uses 25 threads, a higher request timeout and POST instead of GET:

```
python3 simple-oob-scanner.py -b 31337.burpcollaborator.net -u example/url_list.txt -t 25 -to 10 -m POST
```

Using the commands above, the tool create hostbased burl urls, like:
- test-domain1.com.31337.burpcollaborator.net
- test-domain2.com.31337.burpcollaborator.net
- test-domain3.com.31337.burpcollaborator.net

That way you can see easily which domain/host is vulnerable within your burp collaborator client.

__BUT:__

There are cases were only 31337.burpcollaborator.net will result in a http request to burp or you want to use you own 
server/domain. In that case there is the following option (-wbe):

```
python3 simple-oob-scanner.py -b my-server.com -wbe -u example/url_list.txt -t 25 -to 10 -m POST
```

#### How it looks

Here you can see the tool in action. 

![Request](https://i.imgur.com/P7IEAuV.png)

The response is visible withing burp:

![Burp](https://i.imgur.com/g5JlDi4.png)

#### simple-oob-scanner -h
```
usage: simple-oob-scanner.py [-h] -b BURPURL [-wbe] -u URLLIST
                             [-t MAX_THREADS] [-to TIMEOUT]
                             [-m {GET,get,POST,post,HEAD,headPUT,put,OPTIONS,options,DELETE,delete}]

optional arguments:
  -h, --help            show this help message and exit
  -b BURPURL, --burp-url BURPURL
                        burpurl
  -wbe, --without-burp-extension
                        Do not prepend hostname before burpurl
  -u URLLIST, --urllist URLLIST
                        Path to url list
  -t MAX_THREADS, --threads MAX_THREADS
                        Max. threads, default: 5
  -to TIMEOUT, --timeout TIMEOUT
                        Timeout in seconds for each request, default: 3
  -m {GET,get,POST,post,HEAD,headPUT,put,OPTIONS,options,DELETE,delete}, --method {GET,get,POST,post,HEAD,headPUT,put,OPTIONS,options,DELETE,delete}
```