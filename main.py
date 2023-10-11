import requests
import aiohttp
import asyncio
import httpx
import time


url = "https://pokeapi.co/api/v2/pokemon/{}/"


async def main():
    st = time.time()
    responses = [http_get(url.format(num)) for num in range(1, 20)]
    et = time.time()
    print("---------")
    print(f"synchronous requests ran in {et-st}")

    st = time.time()
    responses = await asyncio.gather(
            *[asyncify(http_get, url.format(num)) for num in range(1, 20)])
    et = time.time()
    print("---------")
    print(f"async requests ran in {et-st}")

    st = time.time()
    async with aiohttp.ClientSession() as session:
        tasks = [aio_get(session, url.format(num)) for num in range(1, 20)]
        responses = await asyncio.gather(*tasks)
    et = time.time()
    print("---------")
    print(f"aiohttp get ran in {et-st}")

    st = time.time()
    async with httpx.AsyncClient() as client:
        tasks = [httpx_get(client, url.format(num)) for num in range(1, 20)]
        responses = await asyncio.gather(*tasks)
    et = time.time()
    print("---------")
    print(f"httpx get ran in {et-st}")


def http_get(url: str):
    return requests.get(url).json()


async def asyncify(fn, *args, **kwargs):
    return await asyncio.to_thread(fn, *args, **kwargs)


async def aio_get(session, url: str):
    async with session.get(url) as response:
        return await response.json()


async def httpx_get(client, url: str):
    response = await client.get(url)
    return response.json()


if __name__ == "__main__":
    asyncio.run(main())
