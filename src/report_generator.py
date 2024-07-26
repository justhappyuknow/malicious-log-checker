# src/report_generator.py

def generate_report(malicious_entries, report_path):
    with open(report_path, 'w') as report_file:
        if not malicious_entries:
            report_file.write("No malicious entries found.\n")
        else:
            report_file.write("Malicious Entries Report:\n")
            for file_path, line in malicious_entries:
                report_file.write(f"File: {file_path}\n")
                report_file.write(f"Malicious Entry: {line}\n")
                report_file.write("\n")
