import asyncio
import time
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from tests.test_do import prtsc_main_page_do

async def tick():
    await prtsc_main_page_do()

scheduler = AsyncIOScheduler()
scheduler.add_job(tick, 'interval', minutes=15)
scheduler.start()


try:
    asyncio.get_event_loop().run_forever()
except (KeyboardInterrupt, SystemExit):
    print('exit')

