import urllib.parse
import webbrowser

import requests
import rich

from . import defaults


class TexDocCLI:
    base: str

    def __init__(self, base: str = defaults.TEXDOC_BASE_URL) -> None:
        self.base: str = base

    def version(self) -> None:
        url: str = urllib.parse.urljoin(base=self.base, url=f"/version")
        res: dict = requests.get(url=url).json()
        max_width: int = max([len(key) for key in res.keys()])
        for key, value in res.items():
            rich.print(f"[green bold]{key:>{max_width}}", ":", value)

    def texdoc(self, name: str) -> None:
        url: str = urllib.parse.urljoin(base=self.base, url=f"/texdoc/{name}")
        res: list[dict] = requests.get(url=url).json()
        for i, entry in enumerate(res):
            path: str = entry["path"]
            description: str = entry["description"]
            link: str = urllib.parse.urljoin(base=self.base, url=f"/serve/{name}/{i}")
            rich.print("-", "[green bold]path        :", f"[link={link}]{path}[/link]")
            rich.print(" ", "[green bold]description :", description)

    def pkg(self, name: str) -> None:
        url: str = urllib.parse.urljoin(base=self.base, url=f"/pkg/{name}")
        webbrowser.open(url=url)
