import threading
import asyncio


async def hello():
    print('hello world!(%s'%threading.currentThread())
    print('start...%s'%threading.currentThread())
    await asyncio.sleep(10)
    print('Done...%s'%threading.currentThread())
    print('Hello again%s'%threading.currentThread())
# 启动消息循环
loop=asyncio.get_event_loop()
#定义任务
tasks=[hello(),hello()]
#asyncio使用wait等待task执行完毕
loop.run_until_complete(asyncio.wait(tasks))
#关闭消息循环
loop.close()