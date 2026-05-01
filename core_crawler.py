import asyncio
import aiohttp

# Targets to surpass standard Sherlock lists
TARGET_SITES = {
    "GitHub": "https://github.com{}",
    "Twitter": "https://twitter.com{}",
    "Instagram": "https://instagram.com{}/",
}

async def check_user(session, name, platform, url):
    async with session.get(url.format(name)) as response:
        if response.status == 200:
            print(f"[+] FOUND on {platform}: {url.format(name)}")
            return platform
        return None

async def main(username):
    async with aiohttp.ClientSession() as session:
        tasks = [check_user(session, username, p, u) for p, u in TARGET_SITES.items()]
        await asyncio.gather(*tasks)

if __name__ == "__main__":
    import sys
    target = sys.argv[1] if len(sys.argv) > 1 else "theosintvault"
    asyncio.run(main(target))
