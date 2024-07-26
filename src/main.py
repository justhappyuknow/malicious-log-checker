import os
from log_checker import check_logs
from report_generator import generate_report

def main():
    # Define the actual path to your system log files
    log_files = [
        'D:\Projects\malicious_log_checker\logs\log1.log',  # Replace with your actual path
        'D:\Projects\malicious_log_checker\logs\log2.log',  # Replace with your actual path
        # Add more paths as needed
    ]
    
    # Check logs for malicious content
    malicious_entries = check_logs(log_files)
    
    # Generate a report
    report_path = 'reports/report.txt'
    generate_report(malicious_entries, report_path)
    print(f'Report generated at {report_path}')

if __name__ == "__main__":
    main()
