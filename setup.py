import setuptools

setuptools.setup(
    name="rpipress-downloader",
    version="0.0.2",
    scripts=[
        "scripts/rpipress-downloader",
    ],
    install_requires=['beautifulsoup4', 'lxml', 'progressbar2', 'requests', 'wheel'],
)
