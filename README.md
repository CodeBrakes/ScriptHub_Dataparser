# Exercise - Data Parsing / Scripting
Suppose that we have a web server log file, with the following space-delimited contents:
Access Date, Access Time, Requestor IP, HTTP Method, Requested Route, HTTP Status code, Number of bytes returned to the requestor, Duration of the request - in microseconds

Given the following log file contents:
2017-01-01 12:00:00 192.168.1.1 GET /route1 200 12345 100000
2017-01-01 12:00:01 10.1.1.2 GET /route1 200 12345 200000
2017-01-01 12:00:01 192.168.1.2 GET /route11 404 0 123400
2017-01-01 12:00:02 192.168.1.3 POST /route2 200 5000 900000
2017-01-01 12:00:03 192.168.1.4 POST /route3 200 7000 1200000
2017-01-01 12:00:04 192.168.1.1 GET /route1 200 12345 125000

Question 1: Using your preferred scripting language and/or shell command(s), parse the above log file and
print to stdout, a newline delimited list of ‘Requestor IP -> Duration of the request’.
The output should look as follows:
192.168.1.1 -> 100000
10.1.1.2 -> 200000
192.168.1.2 -> 123400
192.168.1.3 -> 900000
192.168.1.4 -> 1200000
192.168.1.1 -> 125000

Question2: Using your preferred scripting language and/or shell command(s), parse the above log file and
print to stdout, a summary of the distinct routes requested, with the count of the number of times
that each route has been requested. The output should be sorted in order of descending
number of requests.
The output should look as follows:
/route1,3
/route2,1
/route3,1
/route11,1
