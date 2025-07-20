<div align="center">
  <h1>眼动实验程序与数据</h1>
  <p>
    <a href="README.md">English</a> |
    <b>简体中文</b>
  </p>

  <!-- 徽章 -->
  <p>
    <img src="https://img.shields.io/badge/readme%20样式-标准-brightgreen.svg" alt="readme 样式">
    <img src="https://img.shields.io/github/stars/exusiaiwei/supp-eyetracking-ll-2022" alt="星标数">
    <img src="https://img.shields.io/github/forks/exusiaiwei/supp-eyetracking-ll-2022" alt="分支数">
    <img src="https://img.shields.io/github/license/exusiaiwei/supp-eyetracking-ll-2022" alt="许可证">
    <img src="https://img.shields.io/github/last-commit/exusiaiwei/supp-eyetracking-ll-2022" alt="最后提交">
  </p>
</div>

本项目包含了我使用Eyelink眼动仪的实验程序和数据。

## 📋 目录

- [🌟 背景](#-背景)
- [📊 数据说明](#-数据说明)
- [💻 安装](#-安装)
- [📖 使用说明](#-使用说明)
- [🔗 相关仓库](#-相关仓库)
- [👤 维护者](#-维护者)
- [📄 许可证](#-许可证)

## 🌟 背景

本项目是我在学习和研究眼动追踪技术过程中积累的程序和数据。

- 眼动仪设备：Eyelink 1000+
- 实验编写软件：SR Research Experiment Builder 2.3.1
- 数据分析软件：SR Research Data Viewer

设备来自武汉大学语言学习与认知科学实验室。

## 📊 数据说明

### 处理后的数据文件
`experiment_data_processed/` 文件夹包含经过处理的眼动追踪数据，以CSV格式存储，数据来源于 `experiment_data/414/注视情况.xlsx` 中的综合数据集。

**数据文件：**
- `S01.csv` - S09.csv：个体参与者数据文件
- 每个文件包含一个参与者的完整眼动追踪数据
- 总计：9个参与者，9,766个数据点

**数据列：**
- `RECORDING_SESSION_LABEL`：参与者ID (S01-S09)
- `TRIAL_INDEX`：试验编号
- `CURRENT_FIX_INTEREST_AREA_LABEL`：兴趣区标签
- `CURRENT_FIX_START`：注视开始时间 (毫秒)
- `CURRENT_FIX_END`：注视结束时间 (毫秒)
- `CURRENT_FIX_INTEREST_AREA_DWELL_TIME`：兴趣区停留时间 (毫秒)

**参与者信息：**
| 文件 | 数据点数 | 说明 |
|------|----------|------|
| S01.csv | 1,149 | 完整数据 |
| S02.csv | 992 | 完整数据 |
| S03.csv | 1,146 | 完整数据 |
| S04.csv | 1,089 | 完整数据 |
| S05.csv | 884 | 完整数据 |
| S06.csv | 1,231 | 完整数据 |
| S07.csv | 1,079 | 完整数据 |
| S08.csv | 998 | 完整数据 |
| S09.csv | 1,198 | 完整数据 |

### 数据处理
数据使用 `process_414_data.py` 脚本进行处理，该脚本：
1. 从 `experiment_data/414/` 中的综合Excel文件提取数据
2. 按参与者分离数据
3. 标准化参与者ID以保护隐私
4. 导出单独的CSV文件，便于分享和分析

## 💻 安装

本项目包含实验程序和数据，需要安装SR Research Experiment Builder和Data Viewer软件才能查看。

## 📖 使用说明

本仓库包括以下内容：

1. **Experiment Builder**：使用SR Research Experiment Builder 2.3.1软件创建的两个实验设计文件及其部署程序。
2. **Experiment Data**：实验的原始归档数据。
3. **Processed Data**：经过处理的CSV文件，可直接用于分析（详见数据说明）。
4. **Interest Area**：实验材料的兴趣区文件。
5. **Library**：实验材料。
6. **Code**：实验数据及相关数据处理代码。

## 🔗 相关仓库

目前暂无。

## 👤 维护者

[@exusiaiwei](https://github.com/exusiaiwei)

## 📄 许可证

[MIT](LICENSE) © exusiaiwei

<div align="center">
  <p>
    <a href="#-眼动实验程序与数据">返回顶部</a>
  </p>
</div>