from setuptools import setup, find_packages

setup(
    name="smartrecon-pro",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        "aiohttp>=3.8.0",
        "aiodns>=3.0.0",
        "weasyprint>=57.0",
        "jinja2>=3.1.0",
        "pyyaml>=6.0",
        "scikit-learn>=1.2.0",
    ],
    entry_points={
        "console_scripts": [
            "smartrecon=smartrecon_pro.main:main",
        ],
    },
)