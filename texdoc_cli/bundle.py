import os

import PyInstaller.__main__


def run():
    PyInstaller.__main__.run(
        [
            os.path.join(__package__, "__main__.py"),
            "--onefile",
            "--name",
            "texdoc-cli",
            "--collect-all",
            "texdoc_cli",
        ]
    )
