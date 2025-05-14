# 🛫 Qualiflight: TAF Weather Data Parser

A Python script to extract and parse meteorological forecast data from **TAF (Terminal Aerodrome Forecast)** messages. The script processes key weather elements such as written timestamp, wind conditions, and forecast duration, providing structured data useful for pilots and aviation professionals.

---

## 🚀 Features

- Extracts **written timestamp** of the TAF message
- Extracts **wind information** (direction and power)
- Extracts **forecast start and end dates**
- Converts extracted date/time information into **Unix timestamps**
- Stores the parsed data in a **structured dictionary format**

---

## 🖥️ Prerequisites

- Python **3.x+**

---

## 📦 Installation

1. Clone this repository or download the project files.
2. Install required Python packages using:

```bash
pip install -r requirements.txt
```
Or manually install:
```bash
pip install datetime
```

## ▶️ How to Run 

```bash
python qualiflight.py
```


It will:

    Parse the provided TAF message

    Extract weather data (written timestamp, wind info, forecast dates)

    Print the structured data as a dictionary
## ⚠️ Notes

1.The script assumes that the TAF message follows the standard format. Errors may occur if the format is different.

2.The extracted timestamps are based on the current year and month.

## 📁 Project Structure

qualiflight/
├── qualiflight.py        # Main script for extracting TAF data
├── consts.py             # Constants used for parsing the TAF message
├── requirements.txt      # Python dependencies
└── README.md             # Project documentation

## 🧪 Testing Ideas (Not Included) 
Although this project doesn't include testing, here are ideas for expanding it:

   1. Verify if the extracted timestamps are correct based on the input TAF string

   2. Ensure wind data (direction and power) is parsed correctly

   3. Use pytest to test each parsing function with different TAF message inputs.

## Author 👩‍💻

Developed with ❤️ for fun, learning, and aviation data parsing.

## 🏷 Tags 

#python #taf #weatherparser #aviation #automation #data
