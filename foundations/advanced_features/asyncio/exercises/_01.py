"""
Error Handling:

- Modify the fetch_url function to handle different HTTP status codes (e.g., 404, 500) and network errors.
- Add a timeout to the fetch_url function to prevent it from waiting indefinitely.
"""

import asyncio
import aiohttp
import time


async def fetch_url(url):
    print(f"Fetching {url}")
    try:
        timeout = aiohttp.ClientTimeout(total=5)

        async with aiohttp.ClientSession(timeout=timeout) as session:
            async with session.get(url) as response:
                response.raise_for_status()  # Raise HTTPError for bad responses (4xx or 5xx)
                return await response.text()
    except aiohttp.ClientError as e:  # Catch HTTPErrors and Network errors
        print(f"Error fetching {url}: {e}")
        return None
    except asyncio.TimeoutError as e:
        print(f'Timeout occurred while fetching {url}')
        return None
    except Exception as e:
        print(f'An unexpected error occurred while fetching {url}: {e}')
        return None


async def download_image(url, filename):
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                response.raise_for_status()
                with open(filename, "wb") as f:
                    f.write(await response.read())
                print(f"Downloaded {filename}")
    except aiohttp.ClientError as e:
        print(f"Error downloading {url}: {e}")


async def main():
    start_time = time.time()

    # [ FETCHING PAGES TO GET HTML SOURCE CODE ]

    urls = [
        "https://www.google.com",
        "https://www.python.org",
    ]

    tasks_fetch = [fetch_url(url) for url in urls]
    results = await asyncio.gather(*tasks_fetch)

    for url, result in zip(urls, results):
        if result:
            print(f"{url}: {result[:100]}...")

    # [ FETCHING IMAGES TO DOWNLOAD ]

    image_urls = [
        ("https://www.easygifanimator.net/images/samples/video-to-gif-sample.gif", "image1.gif"),
        ("https://media.geeksforgeeks.org/wp-content/uploads/20230713171351/gfg-puzzle-44-compressed.gif", "image2.gif")
    ]

    tasks_download = [download_image(url, filename)
                      for url, filename in image_urls]
    await asyncio.gather(*tasks_download)

    end_time = time.time()
    print(f"Total time: {end_time - start_time:.2f} seconds")

if __name__ == "__main__":
    asyncio.run(main())
