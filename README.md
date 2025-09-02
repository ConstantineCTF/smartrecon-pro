# SmartRecon Pro

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Platform: Linux/macOS/Windows/Docker](https://img.shields.io/badge/platform-Linux%20|%20macOS%20|%20Windows%20|%20Docker-lightgrey.svg)](https://github.com/ConstantineCTF/smartrecon-pro)

SmartRecon Pro is an enterprise-grade reconnaissance tool designed by ConstantineCTF for pentesters and bug bounty hunters. It delivers actionable security insights with zero manual effort, leveraging AI-driven risk scoring, stealth mode, and professional reporting. Tailored for eJPT, OSCP, and bug bounty workflows, it includes specialized detection for vulnerable applications like DVWA.

## Table of Contents
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Command-Line Options](#command-line-options)
- [Scanning with SmartRecon Pro](#scanning-with-smartrecon-pro)
- [License](#license)

## Features
- **Adaptive Scanning**: Dynamically adjusts to target size (startups to Fortune 500) and defenses (WAFs, rate limits).
- **Risk Intelligence**: Prioritizes high-value targets, detects CVEs, and monitors credential leaks.
- **Stealth Mode**: Evades detection with proxy rotation and randomized request timing.
- **DVWA Detection**: Identifies Damn Vulnerable Web Application instances for training and testing.
- **Reports**: Generates board-ready PDFs and hacker-friendly Markdown with curl-ready PoCs.
- **Cross-Platform**: Runs on Linux, macOS, Windows, and Docker.

## Installation
1. Clone the repository and navigate to the project directory:
   ```bash
   git clone https://github.com/ConstantineCTF/smartrecon-pro.git
   cd smartrecon-pro
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

**Note for Windows Users**: The `weasyprint` library may require GTK3. Install it from [tschoonj/gtk3-windows](https://github.com/tschoonj/gtk3-windows) and add it to your system PATH.

## Usage
Run SmartRecon Pro using the `main.py` script. The tool supports multiple plugins and options for flexible scanning.

**Basic Command**:
```bash
python main.py <target_url> [options]
```

- `<target_url>`: The target to scan (e.g., `http://127.0.0.1/DVWA`, `https://example.com`).
- `[options]`: Customize the scan with plugins, stealth mode, report formats, and more.

## Command-Line Options
SmartRecon Pro supports the following command-line options for `main.py`:

| Option            | Description                                                                 | Example                          |
|-------------------|-----------------------------------------------------------------------------|----------------------------------|
| `--plugins <name\|all>` | Specify plugins to run: `vuln` (vulnerability scan), `subdomain` (subdomain enumeration), `cloud` (cloud asset discovery), `leak` (credential leak check), or `all`. | `--plugins vuln` or `--plugins all` |
| `--stealth`       | Enable stealth mode with proxy rotation and randomized request timing.       | `--stealth`                      |
| `--offline`       | Skip network-based checks, using cached or local data.                       | `--offline`                      |
| `--report`        | Generate a report in `pdf` (board-ready PDF), `markdown` (hacker-friendly Markdown), or `both`. | `--report pdf`                   |
| `--output`        | Save report to a specific file (e.g., `report.pdf` or `report.md`). Default: `report_<timestamp>`. | `--output scan1.pdf`             |
| `--threads`       | Set number of concurrent threads (1-50, default: 10).                        | `--threads 20`                   |
| `--timeout`       | Set request timeout in seconds (default: 10).                                | `--timeout 15`                   |
| `--proxy`         | Use a specific proxy for requests (e.g., `http://proxy:8080`). Overrides stealth mode proxies. | `--proxy http://127.0.0.1:8080`  |
| `--verbose`       | Enable verbose logging for detailed output.                                  | `--verbose`                      |
| `--version`       | Display the tool’s version and exit.                                         | `--version`                      |

## Scanning with SmartRecon Pro
SmartRecon Pro is designed for reconnaissance and vulnerability scanning. Follow these steps to scan a target:

1. **Activate the Virtual Environment**:
   ```bash
   cd smartrecon-pro
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. **Run a Scan**:
   - **Full Scan (All Plugins)**:
     ```bash
     python main.py http://127.0.0.1/DVWA --plugins all
     ```
     Runs all plugins (`vuln`, `subdomain`, `cloud`, `leak`). Example output:
     ```
     2025-07-19 23:32:00 - INFO - Validating input: http://127.0.0.1/DVWA
     2025-07-19 23:32:00 - INFO - Validated: domain=127.0.0.1, path=/DVWA
     2025-07-19 23:32:00 - INFO - Starting scan for http://127.0.0.1/DVWA (stealth=False)
     2025-07-19 23:32:01 - INFO - Skipping subdomain scan for IP address
     2025-07-19 23:32:01 - INFO - Starting vuln scan on http://127.0.0.1/DVWA
     2025-07-19 23:32:01 - INFO - Vuln scan completed: {'vulns': [{'vuln': 'DVWA detected', 'url': 'http://127.0.0.1/DVWA', 'cvss_score': 7.5, 'public_poc': False}]}
     ```

   - **Vulnerability Scan Only**:
     ```bash
     python main.py http://example.com --plugins vuln
     ```
     Runs only the `vuln` plugin (e.g., checks for CVEs, DVWA).

   - **Stealth Scan**:
     ```bash
     python main.py https://example.com --plugins all --stealth
     ```
     Uses proxy rotation and randomized timing for evasion.

   - **Generate PDF Report**:
     ```bash
     python main.py http://127.0.0.1/DVWA --plugins all --report pdf --output dvwa_report.pdf
     ```
     Generates a board-ready PDF report.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
