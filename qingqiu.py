# qingqiu.py
import requests


def fetch_page_data(cookies_dict, user_id=2403, offset=1, limit=10):
    """
    请求项目列表 API
    :param cookies_dict: 已经是 {name: value} 格式的字典
    :param user_id: 用户 ID
    :param offset: 页码
    :param limit: 每页数量
    :return: JSON 数据
    """
    url = "https://5gbloomingcup.5gaia.org.cn/MemberCenter/GetProjectList"

    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Origin': 'https://5gbloomingcup.5gaia.org.cn',
        'Referer': 'https://5gbloomingcup.5gaia.org.cn/MemberCenter/ProjectList/',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest',
        'promise': 'promise',
        'Sec-Fetch-Mode': 'cors',
    }

    data = {
        'UserId': str(user_id),
        'offset': str(offset),
        'limit': str(limit)
    }

    try:
        # 直接使用 cookies_dict（已经是 name: value 格式）
        response = requests.post(url, headers=headers, data=data, cookies=cookies_dict)
        response.raise_for_status()
        json_data = response.json()
        print(f"✅ 第 {offset} 页请求成功，共 {json_data.get('total', 0)} 条数据")
        return json_data
    except Exception as e:
        print(f"❌ 请求第 {offset} 页失败: {e}")
        return None