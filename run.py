import time
import re

import requests

url = 'https://johnshall.github.io/Shadowrocket-ADBlock-Rules-Forever/sr_top500_banlist.conf'
res = requests.get(url)
while res.status_code != 200:
    res = requests.get(url)
    time.sleep(20)
text = res.text
match = re.search(r'\[Rule\](.*?)\[URL Rewrite\]', text, re.DOTALL)
if match:
    result = match.group(1).strip().replace(',PROXY', '').replace('FINAL,direct', '')
    with open("ban.list", "w", encoding="utf-8") as file:
        file.write(result)
    print("内容已写入文件 ban.list")
else:
    print("未找到匹配的内容")
