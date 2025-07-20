<div align="center">
  <h1>Eye-tracking Experiment Program and Data</h1>
  <p>
    <b>English</b> |
    <a href="README.zh-CN.md">简体中文</a>
  </p>

  <!-- Badges -->
  <p>
    <img src="https://img.shields.io/badge/readme%20style-standard-brightgreen.svg" alt="readme style">
    <img src="https://img.shields.io/github/stars/exusiaiwei/supp-eyetracking-ll-2022" alt="stars">
    <img src="https://img.shields.io/github/forks/exusiaiwei/supp-eyetracking-ll-2022" alt="forks">
    <img src="https://img.shields.io/github/license/exusiaiwei/supp-eyetracking-ll-2022" alt="license">
    <img src="https://img.shields.io/github/last-commit/exusiaiwei/supp-eyetracking-ll-2022" alt="last-commit">
  </p>
</div>

This project contains the experiment program and data from my usage of the Eyelink eye-tracking device.

## 📋 Table of Contents

- [🌟 Background](#-background)
- [📊 Data Description](#-data-description)
- [💻 Installation](#-installation)
- [📖 Usage Instructions](#-usage-instructions)
- [🔗 Related Repositories](#-related-repositories)
- [👤 Maintainer](#-maintainer)
- [📄 License](#-license)

## 🌟 Background

This project is an accumulation of programs and data from my study and research involving eye-tracking technology.

- Eye-tracking device: Eyelink 1000+
- Experiment authoring software: SR Research Experiment Builder 2.3.1
- Data analysis software: SR Research Data Viewer

The equipment is from the Language Learning and Cognitive Science Laboratory at Wuhan University.

## 📊 Data Description

### Processed Data Files
The `experiment_data_processed/` folder contains processed eye-tracking data in CSV format, extracted from the comprehensive dataset in `experiment_data/414/注视情况.xlsx`.

**Data Files:**
- `S01.csv` - S09.csv: Individual participant data files
- Each file contains complete eye-tracking data for one participant
- Total: 9 participants, 9,766 data points

**Data Columns:**
- `RECORDING_SESSION_LABEL`: Participant ID (S01-S09)
- `TRIAL_INDEX`: Trial number
- `CURRENT_FIX_INTEREST_AREA_LABEL`: Interest area label
- `CURRENT_FIX_START`: Fixation start time (ms)
- `CURRENT_FIX_END`: Fixation end time (ms)
- `CURRENT_FIX_INTEREST_AREA_DWELL_TIME`: Dwell time in interest area (ms)

**Participant Information:**
| File | Data Points | Description |
|------|-------------|-------------|
| S01.csv | 1,149 | Complete data |
| S02.csv | 992 | Complete data |
| S03.csv | 1,146 | Complete data |
| S04.csv | 1,089 | Complete data |
| S05.csv | 884 | Complete data |
| S06.csv | 1,231 | Complete data |
| S07.csv | 1,079 | Complete data |
| S08.csv | 998 | Complete data |
| S09.csv | 1,198 | Complete data |

### Data Processing
The data was processed using `process_414_data.py` script, which:
1. Extracts data from the comprehensive Excel file in `experiment_data/414/`
2. Separates data by participant
3. Standardizes participant IDs for privacy protection
4. Exports individual CSV files for easy sharing and analysis

## 💻 Installation

This project contains experiment programs and data that require the installation of SR Research Experiment Builder and Data Viewer software for viewing.

## 📖 Usage Instructions

This repository includes the following:

1. **Experiment Builder**: Two experiment design files created using SR Research Experiment Builder 2.3.1 software and their deployed programs.
2. **Experiment Data**: Archived raw data from the experiments.
3. **Processed Data**: Processed CSV files ready for analysis (see Data Description above).
4. **Interest Area**: Files for areas of interest in the experimental materials.
5. **Library**: Experimental materials.
6. **Code**: Experimental data and related code for data processing.

## 🔗 Related Repositories

None at the moment.

## 👤 Maintainer

[@exusiaiwei](https://github.com/exusiaiwei)

## 📄 License

[MIT](LICENSE) © exusiaiwei

<div align="center">
  <p>
    <a href="#-eye-tracking-experiment-program-and-data">Back to Top</a>
  </p>
</div>
