import requests
import json

def query_power(bui_id, bui_name, floor_id, floor_name, room_name, room_id ="1111"):
    # 根据 bui_id 判断校区
    if bui_id.startswith("xl"):
        url = "http://172.27.2.95:8899/query/Default.aspx"  # 仙林校区
    else:
        url = "http://114.212.254.14:8899/query/Default.aspx"  # 鼓楼校区
    data = {
        "submitDirectEventConfig": f'{{"config":{{"extraParams":{{"rid":"{room_id}"}}}}}}',
        "__VIEWSTATEGENERATOR": "E32D4683",
        "hid_bui_id": bui_id,
        "hid_bui_name": bui_name,
        "hid_floor_id": floor_id,
        "hid_floor_name": floor_name,
        "hid_r_id": room_id,
        "hid_room_name": room_name,
        "__EVENTTARGET": "ctl04",
        "__EVENTARGUMENT": "-|public|RoomQuery"
    }
    headers = {
        "X-Requested-With": "XMLHttpRequest",
        "X-Ext-Net": "delta=true",
        "Origin": "http://114.212.254.14:8899",
        "Referer": "http://114.212.254.14:8899/query/Default.aspx",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36 Edg/140.0.0.0",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Accept": "*/*",
        "Accept-Language": "zh,zh-CN;q=0.9",
        "Accept-Encoding": "gzip, deflate",
        "Connection": "keep-alive"
    }
    resp = requests.post(url, data=data, headers=headers)
        # 直接用字符串分割和json解析，确保能获取remain字段
    try:
        result_prefix = 'result:"'
        start = resp.text.find(result_prefix)
        if start != -1:
            start += len(result_prefix)
            end = resp.text.find('"}', start)
            result_str = resp.text[start:end]
            result_str = result_str.encode().decode('unicode_escape')
            info = json.loads(result_str)
        else:
            print("未找到剩余电量信息")
    except Exception as e:
        print("解析失败：", e)
    return info["remain"]

remain_power = query_power("gl11", "11舍", "002", "第2层", "204房间")