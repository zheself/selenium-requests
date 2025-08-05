# data_get.py
import pandas as pd

def parse_and_save_data(json_list, output_file='data.xlsx'):
    """
    解析多个页面的 JSON 数据并保存为 Excel
    :param json_list: 包含多个 JSON 响应的列表，每个是 {'total': int, 'rows': [...]}
    :param output_file: 输出文件名
    """
    all_data = []

    for i, data in enumerate(json_list, start=1):
        if not data or 'rows' not in data:
            print(f"⚠️  第 {i} 页数据格式错误或为空")
            continue

        rows = data['rows']
        print(f"📄 第 {i} 页解析 {len(rows)} 条项目")

        for item in rows:
            row_data = [
                item.get('ID', ''),
                item.get('Status', ''),
                item.get('Code', ''),                    # 项目编号
                item.get('ProjectName', ''),            # 项目名称
                item.get('TradeName', ''),              # 赛道类型
                item.get('ZoneName', ''),               # 行业板块（专题赛名称）
                item.get('Contract', ''),               # 联系人
                item.get('ContractPhoneNum', ''),       # 联系电话
                item.get('ZoneEndDate', ''),            # 截止日期
            ]
            all_data.append(row_data)

    # 创建 DataFrame
    df = pd.DataFrame(all_data, columns=[
        'ID', '状态', '项目编号', '项目名称',
        '赛道类型', '行业板块', '联系人', '联系电话', '截止日期'
    ])

    # 保存到 Excel
    df.to_excel(output_file, index=False)
    print(f"✅ 所有数据已保存到 {output_file}")