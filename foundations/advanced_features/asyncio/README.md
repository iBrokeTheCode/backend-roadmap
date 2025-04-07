# Asyncio

## Theory

**Coroutines:**

- Coroutines are special functions that can be paused and resumed. This allows for non-blocking execution, which is crucial for handling multiple tasks concurrently.
- In Python, coroutines are defined using the `async def` syntax.
- The `await` keyword is used to pause the execution of a coroutine until another coroutine or awaitable object completes.

**Event Loop:**

- The event loop is the heart of asyncio. It manages the execution of coroutines and schedules them for execution.
- It continuously monitors the status of coroutines and resumes them when they are ready to proceed.
- `asyncio.run(main())` creates an event loop, runs the main coroutine, and closes the loop.

**Async I/O:**

- Asyncio is particularly well-suited for I/O-bound operations, such as network requests and file I/O.
- Libraries like `aiohttp` provide asynchronous versions of common I/O operations.
- `async with` statement is very used with async libraries to manage resources.

**Concurrency vs. Parallelism:**

- Concurrency is about managing multiple tasks at the same time, but not necessarily executing them simultaneously.
- Parallelism is about executing multiple tasks simultaneously, typically on multiple CPU cores.
- Asyncio provides concurrency, but not parallelism by default. To achieve parallelism, you can combine asyncio with multiprocessing or multithreading, but this is a advanced topic, and not needed for now.

**Important functions:**

- `asyncio.create_task()`: Schedule the execution of a coroutine as a task.
- `asyncio.gather()`: Run multiple coroutines concurrently and wait for their completion.
- `asyncio.sleep()`: Pause the execution of a coroutine for a specified time.

## Example

```python
import asyncio
import aiohttp
import time

async def fetch_url(url):
    print(f"Fetching {url}")
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                response.raise_for_status() # Raise HTTPError for bad responses (4xx or 5xx)
                return await response.text()
    except aiohttp.ClientError as e:
        print(f"Error fetching {url}: {e}")
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

    urls = [
        "https://www.example.com",
        "https://www.google.com",
        "https://www.youtube.com",
        "https://www.github.com"
    ]

    tasks_fetch = [fetch_url(url) for url in urls]
    results = await asyncio.gather(*tasks_fetch)

    for url, result in zip(urls, results):
        if result:
            print(f"{url}: {result[:100]}...")

    image_urls = [
        ("https://www.easygifanimator.net/images/samples/video-to-gif-sample.gif", "image1.gif"),
        ("https://media.geeksforgeeks.org/wp-content/uploads/20230713171351/gfg-puzzle-44-compressed.gif", "image2.gif")
    ]

    tasks_download = [download_image(url, filename) for url, filename in image_urls]
    await asyncio.gather(*tasks_download)

    end_time = time.time()
    print(f"Total time: {end_time - start_time:.2f} seconds")

if __name__ == "__main__":
    asyncio.run(main())
```

## Exercises

1. Error Handling:

   - Modify the fetch_url function to handle different HTTP status codes (e.g., 404, 500) and network errors.
   - Add a timeout to the fetch_url function to prevent it from waiting indefinitely. [Solution](./exercises/_01.py)

2. Rate Limiting:

   - Implement a rate limiter to prevent making too many requests to a website in a short period of time.

   - Use asyncio.sleep() to control the rate of requests.

3. Progress Tracking:

   - Add progress tracking to the download_image function to display the download progress.
   - You can get the content length from the response headers.

4. Concurrent File Processing:

   - Create a async application that reads multiple files concurrently, process their content, and write the results to new files.

5. Web scraping:
   - Create a simple web scraping application that fetches data from multiple web pages concurrently.
