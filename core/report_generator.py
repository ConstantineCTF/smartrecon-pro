from jinja2 import Environment, FileSystemLoader
import weasyprint
import os
from typing import Dict
from datetime import datetime

class ReportGenerator:
    def __init__(self, results: Dict, output_dir: str, domain: str):
        self.results = results
        self.output_dir = output_dir
        self.domain = domain
        self.env = Environment(loader=FileSystemLoader(os.path.join(os.path.dirname(__file__), "../reports/templates")))
        os.makedirs(output_dir, exist_ok=True)

    def generate_pdf(self):
        template = self.env.get_template("report.html.j2")
        html_content = template.render(
            domain=self.domain,
            timestamp=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            critical_findings=sorted(self.results["vulns"], key=lambda x: x["risk_score"], reverse=True)[:3],
            subdomains=self.results["subdomains"],
            assets=self.results["assets"],
            leaks=self.results["leaks"]
        )
        output_path = os.path.join(self.output_dir, f"{self.domain}_report.pdf")
        weasyprint.HTML(string=html_content).write_pdf(output_path)

    def generate_markdown(self):
        template = self.env.get_template("report.md.j2")
        md_content = template.render(
            domain=self.domain,
            timestamp=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            critical_findings=sorted(self.results["vulns"], key=lambda x: x["risk_score"], reverse=True)[:3],
            subdomains=self.results["subdomains"],
            assets=self.results["assets"],
            leaks=self.results["leaks"]
        )
        output_path = os.path.join(self.output_dir, f"{self.domain}_report.md")
        with open(output_path, "w") as f:
            f.write(md_content)