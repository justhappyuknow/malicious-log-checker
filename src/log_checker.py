# src/log_checker.py

def check_logs(log_files):
    malicious_entries = []
    malicious_pattern = "Malicious pattern detected"  # Adjust pattern as needed
    
    for file_path in log_files:
        try:
            with open(file_path, 'r') as file:
                lines = file.readlines()
                
                for line in lines:
                    if malicious_pattern in line:
                        malicious_entries.append((file_path, line.strip()))
        except Exception as e:
            print(f"Error reading {file_path}: {e}")
    
    return malicious_entries
