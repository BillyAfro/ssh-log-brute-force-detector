🛡️ ssh-log-brute-force-detector

📌 Lightweight Python tool for detecting SSH brute-force attacks by analyzing authentication logs (auth.log).
It identifies repeated failed login attempts from the same IP within a defined time window and flags suspicious activity.

🧠 How it works?

The tool parses SSH authentication logs line by line and extracts:

IP addresses
Failed login attempts
Timestamps of events

It then groups attempts by IP and checks whether the number of failed logins exceeds a defined threshold within a given time window.

If the threshold is exceeded, the IP is flagged as a potential brute-force source.

🚀 Usage

Run the script on an SSH authentication log file:

python detector.py

Make sure the script is configured to point to your log file (e.g. auth.log) inside the code.

⚙️ Features
- Detects SSH brute-force attempts from authentication logs
- Groups failed login attempts by IP address
- Time-window based detection logic
- Flags suspicious IPs exceeding threshold
- Lightweight Python implementation

⚙️ Installation

git clone https://github.com/BillyAfro/ssh-log-brute-force-detector.git
cd ssh-log-brute-force-detector

🧪 Example log

```
Failed password for root from 111.111.1.11  
Failed password for admin from 112.111.1.11  
Failed password for user from 113.111.1.11
```

📊 Example output

```
IP: 111.111.1.11 - Attempts: 8  
IP: 112.111.1.11 - Attempts: 6
```
