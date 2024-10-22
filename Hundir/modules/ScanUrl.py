import argparse
import asyncio
import logging
import aiofiles
import aiohttp
import os

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")


class ScanUrl:
    def __init__(self, scan_url, scan_dict, scan_thread):
        self.scan_url = (
            f"{('http://' if '://' not in scan_url else '')}{scan_url.rstrip('/')}/"
        )
        self.load_dict(scan_dict)
        self.scan_output = os.path.join(
            "log",
            f"{self.scan_url.split('//')[1].rstrip('/').replace(':', '_')}.txt",
        )
        os.makedirs(os.path.dirname(self.scan_output), exist_ok=True)
        self.semaphore = asyncio.Semaphore(scan_thread)

    def load_dict(self, dict_list):
        try:
            with open(dict_list, "r") as f:
                self.data = [line.strip() for line in f.readlines()]
            if not self.data:
                raise ValueError("NO Dictionary")
        except FileNotFoundError:
            logging.error(f"Dictionary file {dict_list} not found.")
            raise

    async def write_output(self, result):
        async with aiofiles.open(self.scan_output, "a") as f:
            await f.write(result + "\n")

    async def scan(self, url):
        headers = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/603.3.8 (KHTML, like Gecko) Version/10.1.2 Safari/603.3.8",
            "Referer": "https://www.baidu.com",
            "Accept-Encoding": "gzip, deflate",
            "Connection": "keep-alive",
        }
        try:
            async with self.semaphore:
                async with aiohttp.ClientSession() as session:
                    async with session.get(url, headers=headers, timeout=10) as resp:
                        code = resp.status
                        if code in (200, 301, 403):
                            print(f"[ {code} ] {url}")
                            await self.write_output(f"[ {code} ] {url}")
        except Exception as e:
            logging.error(f"Error scanning {url}: {e}")

    async def run(self):
        tasks = []
        for path in self.data:
            url = f"{self.scan_url}{path}"
            task = asyncio.create_task(self.scan(url))
            tasks.append(task)
        await asyncio.gather(*tasks)

    def start(self):
        asyncio.run(self.run())
        print("* End of Scan *")


def argument_parser():
    parser = argparse.ArgumentParser(
        description="'Hundir' is a script for URL Path scanning"
    )
    parser.add_argument(
        "-u",
        dest="url",
        type=str,
        required=True,
        help="The website URL that needs to be scanned.",
    )
    parser.add_argument(
        "-d",
        dest="dict",
        type=str,
        default="./dict/url.txt",
        help="Path to the dictionary file for scanning.",
    )
    parser.add_argument(
        "-t",
        dest="thread",
        type=int,
        default=25,
        help="Number of coroutine running the program.",
    )
    return parser.parse_args()
