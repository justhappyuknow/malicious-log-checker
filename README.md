# Malicious Log Checker

## Overview

The Malicious Log Checker is a Python tool designed to analyze real system log files for malicious behavior and generate a comprehensive report. This tool helps in identifying potentially harmful log entries by scanning system logs for predefined patterns indicative of malicious activities.

## Features

- **Analyze Real Logs**: Check real system log files for malicious patterns.
- **Generate Report**: Create a detailed report of detected malicious entries.

## Installation

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/dhawalbisht/malicious-log-checker.git
   cd malicious-log-checker
   pip install -r requirements.txt
   
# Export Application log
Get-EventLog -LogName Application | Export-Csv -Path "C:\path\to\log1.log" -NoTypeInformation

# Export System log
Get-EventLog -LogName System | Export-Csv -Path "C:\path\to\log2.log" -NoTypeInformation

```bash
python src/main.py