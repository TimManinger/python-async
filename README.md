# python-async

This is a short program that times different ways of executing HTTP requests in
Python. It starts with synchronous requests, then async requests, aiohttp, and
httpx. For an api that is http/2 compatible, the multiplexing makes httpx the
fastest option.
