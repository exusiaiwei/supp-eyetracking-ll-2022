import pandas as pd
import os


def process_414_data():
    """从414文件夹的xlsx文件中提取数据，这是最完整的数据源"""

    # 读取414文件夹中的主要xlsx文件
    main_file = "experiment_data/414/注视情况.xlsx"
    output_path = "cleaned_data_from_414"
    os.makedirs(output_path, exist_ok=True)

    print(f"正在读取主文件: {main_file}")
    main_df = pd.read_excel(main_file)
    print(f"主文件大小: {main_df.shape}")
    print(f"主文件列名: {list(main_df.columns)}")

    # 参与者ID映射
    id_map = {
        'h1': 'S01', 'hxq': 'S02', 'ljj': 'S03', 'lsx': 'S04',
        'lx': 'S05', 'myw1': 'S06', 'wzc': 'S07', 'zxj': 'S08', 'zy': 'S09'
    }

    # 获取所有参与者
    participants = main_df['RECORDING_SESSION_LABEL'].unique()
    print(f"参与者列表: {sorted(participants)}")

    # 为每个参与者创建单独的CSV文件
    for old_id in participants:
        if old_id in id_map:
            new_id = id_map[old_id]

            # 提取该参与者的数据
            participant_df = main_df[main_df['RECORDING_SESSION_LABEL'] == old_id].copy()

            # 更新参与者ID
            participant_df.loc[:, 'RECORDING_SESSION_LABEL'] = new_id

            # 保存为CSV文件
            output_filename = f"{new_id}_414.csv"
            output_filepath = os.path.join(output_path, output_filename)
            participant_df.to_csv(output_filepath, index=False, encoding='utf-8')

            print(f"已保存: {output_filename} ({len(participant_df)} 行数据)")

    print(f"\n所有数据已保存到 {output_path} 文件夹")

    # 创建汇总信息
    print("\n=== 数据汇总 ===")
    summary_df = main_df['RECORDING_SESSION_LABEL'].value_counts().sort_index()
    for old_id, count in summary_df.items():
        if old_id in id_map:
            new_id = id_map[old_id]
            print(f"{new_id} ({old_id}): {count} 行数据")


if __name__ == "__main__":
    process_414_data()