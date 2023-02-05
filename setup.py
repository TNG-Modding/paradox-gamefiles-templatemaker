from setuptools import setup, find_packages

setup(
    name = "intemplator",
    version = "0.0.0",
    author = "Oliver Barnum",
    author_email = "oliverbarnum32@gmail.com",
    description = "Create templates populated by json",
    url = "",
    packages=find_packages(),
    install_requires=["asyncio", "aiofile", "click", "markdown2", "WeasyPrint", "ensure", "svgutils", "wand", "mpmath", "tabulate", "aiohttp"],
    entry_points = {
        "console_scripts": [
            "intemplator=intemplator:cli"
        ]
    },
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)