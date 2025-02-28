import asyncio
#import logging

from pyrubicon.objc.eventloop import EventLoopPolicy

__all__ = [
  'loop',
]
#logging.basicConfig(level=logging.DEBUG)
asyncio.set_event_loop_policy(EventLoopPolicy())
#loop = asyncio.get_event_loop()
loop = asyncio.new_event_loop()
#loop.set_debug(True)

