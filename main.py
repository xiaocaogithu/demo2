# 这是一个示例 Python 脚本。

# 按 Shift+F10 执行或将其替换为您的代码。
# 按 双击 Shift 在所有地方搜索类、文件、工具窗口、操作和设置。
import aiohttp
import asyncio

headers = {
    'Host': 'www.microchipdirect.com',
    'Connection': 'keep-alive',
    'sec-ch-ua': '',
    'Accept': 'application/json, text/plain, */*',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
    'sec-ch-ua-platform': '',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cookie': 'BuyMicrochipCatalog=BuyMicrochip_CN; CurrentLanguage=cn;'

}

async def print_hi():
    # url = f'https://www.microchipdirect.com/api/Product/ProductInfo?CPN={part_num}&start=0&rows=15&t=1688023798746'
    txt=open('微芯料号.txt',encoding='utf-8').readlines()
    for i in txt:
        url = f'https://www.microchipdirect.com/api/Product/ProductInfo?CPN={i[:-2]}&start=0&rows=15&t=1688023798746'
        return url

async def get_data():
    txt = open('微芯料号.txt', encoding='utf-8').readlines()
    print(len(txt))
    for i in txt:
        url = f'https://www.microchipdirect.com/api/Product/ProductInfo?CPN={i[:-2]}&start=0&rows=15&t=1688023798746'
        async with aiohttp.ClientSession() as seeion:
            async with await seeion.get(url,headers=headers) as resp:
                print("kaishi")
                page =  resp.text()
        print('爬取完成-》', url)
    return page

def parse(task):
    page=task.result()
    print(len(page))

async def main():
    tasks = []
    # c = await
    # for i in range(10):
    task = asyncio.create_task(get_data())
    # task1 = asyncio.create_task(print_hi())
    task.add_done_callback(parse)
    tasks.append(task)

    await asyncio.wait(tasks)

# 按间距中的绿色按钮以运行脚本。
if __name__ == '__main__':
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(main())
    loop.close()