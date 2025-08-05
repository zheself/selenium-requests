# main.py
from login import login_and_get_cookies  # 确保这里导入的是正确的函数
from qingqiu import fetch_page_data
from data_get import parse_and_save_data


def main():
    # 1. 登录获取 cookies
    cookies = login_and_get_cookies()  # 直接接收 cookies 列表
    if not cookies:
        print("登录失败")
        return

    user_id = 2403  # 根据你请求中看到是 2403
    limit = 10
    all_pages_data = []

    # 2. 获取第一页，获取 total
    first_page = fetch_page_data(cookies, user_id=user_id, offset=1, limit=limit)
    if not first_page:
        print("无法获取第一页数据")
        return

    all_pages_data.append(first_page)
    total = first_page['total']
    total_pages = (total + limit - 1) // limit  # 向上取整

    # 3. 获取后续页
    for page in range(2, total_pages + 1):
        data = fetch_page_data(cookies, user_id=user_id, offset=page, limit=limit)
        if data:
            all_pages_data.append(data)

    # 4. 解析并保存
    parse_and_save_data(all_pages_data, '5G_BloomingCup_Projects.xlsx')


if __name__ == '__main__':
    main()