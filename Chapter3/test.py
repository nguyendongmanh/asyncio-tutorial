import time
import asyncio


def test():
    print("Test function")
    for i in range(100000000):
        pass


async def main():
    print(f"{time.ctime()}: This is main function")
    loop = asyncio.get_running_loop()
    loop.run_in_executor(None, test)
    await asyncio.sleep(1.0)
    print(f"{time.ctime()} Goodbye!")


async def task1():
    print(f"{time.ctime()} Task 1")
    await asyncio.sleep(1.0)
    print(f"{time.ctime()} Goodbye Task 1!")


loop = asyncio.get_event_loop()
task = loop.create_task(main())
task1 = loop.create_task(task1())
loop.run_until_complete(task)
loop.run_until_complete(task1)

pending = asyncio.all_tasks(loop=loop)
for t in pending:
    task.cancel()

group = asyncio.gather(*pending, return_exceptions=True)
loop.run_until_complete(group)

loop.close()
