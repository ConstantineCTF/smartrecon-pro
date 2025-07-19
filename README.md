SmartRecon Pro
SmartRecon Pro is an enterprise-grade reconnaissance tool built by ConstantineCTF for pentesters and bug bounty hunters. It delivers actionable security insights with zero manual effort, featuring AI-driven risk scoring, stealth mode, and professional reports. Perfect for eJPT, OSCP, and bug bounty workflows, it includes specialized detection for vulnerable apps like DVWA.
Features

Adaptive Scanning: Dynamically adjusts to target size (startups to Fortune 500) and defenses (WAFs, rate limits).
Risk Intelligence: Prioritizes high-value targets, detects CVEs, and monitors credential leaks.
Stealth Mode: Evades detection with proxy rotation and randomized timing.
DVWA Detection: Identifies Damn Vulnerable Web Application instances for training and testing.
Reports: Generates board-ready PDFs and hacker-friendly Markdown with curl-ready PoCs.
Cross-Platform: Runs on Linux, macOS, Windows, and Docker.

Installation
Clone the repository and install dependencies:
git clone https://github.com/ConstantineCTF/smartrecon-pro.git
cd smartrecon-pro
python -m venv venv
source venv/bin/activate  # On Windows: source venv/Scripts/activate
pip install -r requirements.txt

Note: On Windows, weasyprint may require GTK3. Install it from tschoonj/gtk3-windows and add to PATH.
Usage
Run SmartRecon Pro with main.py. The tool supports multiple plugins and options for flexible scanning.
Basic Command
python main.py <target_url> [options]


<target_url>: The target to scan (e.g., http://127.0.0.1/DVWA, https://example.com).
[options]: Customize the scan with plugins, stealth mode, report formats, and more.

Command-Line Options
SmartRecon Pro supports the following options for main.py:



Option
Description
Example



--plugins <name|all>
Specify plugins to run: vuln (vulnerability scan), subdomain (subdomain enumeration), cloud (cloud asset discovery), leak (credential leak check), or all for all plugins.
--plugins vuln or --plugins all


--stealth
Enable stealth mode with proxy rotation and randomized request timing to evade detection.
--stealth


--offline
Skip network-based checks, using cached or local data (useful for testing or restricted environments).
--offline


--report <format>
Generate a report in specified format: pdf (board-ready PDF), markdown (hacker-friendly Markdown), or both.
--report pdf


--output <file>
Save report to a specific file (e.g., report.pdf or report.md). Default: report_<timestamp>.<format>.
--output scan1.pdf


--threads <number>
Set number of concurrent threads (1-50, default: 10). Higher values increase speed but may trigger rate limits.
--threads 20


--timeout <seconds>
Set request timeout in seconds (default: 10). Increase for slow networks.
--timeout 15


--proxy <url>
Use a specific proxy for requests (e.g., http://proxy:8080). Overrides stealth mode proxies.
--proxy http://127.0.0.1:8080


--verbose
Enable verbose logging for detailed output (useful for debugging).
--verbose


--version
Display the tool’s version and exit.
--version


Scanning with SmartRecon Pro
SmartRecon Pro is designed for reconnaissance and vulnerability scanning. Follow these steps to scan a target:

Activate Virtual Environment:
cd smartrecon-pro
source venv/bin/activate  # On Windows: source venv/Scripts/activate


Run a Scan:

Full Scan (All Plugins):
python main.py http://127.0.0.1/DVWA --plugins all


Scans with all plugins (vuln, subdomain, cloud, leak).
Example output:2025-07-19 23:32:00 - INFO - Validating input: http://127.0.0.1/DVWA
2025-07-19 23:32:00 - INFO - Validated: domain=127.0.0.1, path=/DVWA
2025-07-19 23:32:00 - INFO - Starting scan for http://127.0.0.1/DVWA (stealth=False)
2025-07-19 23:32:01 - INFO - Skipping subdomain scan for IP address
2025-07-19 23:32:01 - INFO - Starting vuln scan on http://127.0.0.1/DVWA ascent: 0
2025-07-19 23:32:01 - INFO - Vuln scan completed: {'vulns': [{'vuln': 'DVWA detected', 'url': 'http://127.0.0.1/DVWA', 'cvss_score': 7.5, 'public_poc': False}]}
...




Vulnerability Scan Only:
python main.py http://example.com --plugins vuln


Runs only the vuln plugin (e.g., checks for CVEs, DVWA).


Stealth Scan:
python main.py https://example.com --plugins all --stealth


Uses proxy rotation and randomized timing.


Generate PDF Report:
python main.py http://127.0.0.1/DVWA --plugins all --report pdf --output dvwa_report.pdf


