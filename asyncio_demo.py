import asyncio

async def task(name):
    print(f"Task {name} started")
    await asyncio.sleep(2)
    print(f"Task {name} finished")

async def main():
    await asyncio.gather(
        task(1),
        task(2),
        task(3)
    )

asyncio.run(main())