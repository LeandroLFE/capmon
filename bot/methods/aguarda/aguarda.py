from asyncio import sleep

async def aguarda(self, waittime):
    await sleep(waittime)
    return True