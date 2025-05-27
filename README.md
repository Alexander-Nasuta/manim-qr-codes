## About this Project

This poject contains a Python Module that provides allows theming of [Manim](https://www.manim.community) projects with [QR Codes](https://en.wikipedia.org/wiki/QR_code).

## Installation

Install the package with pip:
```
   pip install manim-qr-codes
```


## Minimal Example

**NOTE: Please make sure you have manim installed and running on your machine**

Below is a minimal example of how to use the Module.

```python
import manim as m

from manim_qr_codes.qr import qr_code


class MyQrCodeScene(m.Scene):

    def construct(self):

        qr_code_without_icon = qr_code("https://fishshell.com")
        qr_code_with_icon = qr_code(
            payload="https://fishshell.com",
            icon='terminal',
            icon_size=6
        )

        qr_code_group = m.VGroup(
            qr_code_without_icon,
            qr_code_with_icon).arrange(m.RIGHT, buff=0.75)

        label = m.Text("https://fishshell.com")
        label.to_edge(m.UP, buff=0.75)

        self.add(qr_code_group, label)



if __name__ == '__main__':
    import os
    from pathlib import Path

    FLAGS = "-pqm -s"
    SCENE = "MyQrCodeScene"

    file_path = Path(__file__).resolve()
    os.system(f"manim {Path(__file__).resolve()} {SCENE} {FLAGS}")
```

This should yield a Scene that looks like so:

![Example Output Screenshot](https://raw.githubusercontent.com/Alexander-Nasuta/manim-qr-codes/master/resources/MyQrCodeScene_ManimCE_v0.19.0.png)


### Documentation

This project uses `sphinx` for generating the documentation.
It also uses a lot of sphinx extensions to make the documentation more readable and interactive.
For example the extension `myst-parser` is used to enable markdown support in the documentation (instead of the usual .rst-files).
It also uses the `sphinx-autobuild` extension to automatically rebuild the documentation when changes are made.
By running the following command, the documentation will be automatically built and served, when changes are made (make sure to run this command in the root directory of the project):

```shell
sphinx-autobuild ./docs/source/ ./docs/build/html/
```

If sphinx extensions were added the `requirements_dev.txt` file needs to be updated.
These are the requirements, that readthedocs uses to build the documentation.
The file can be updated using this command:

```shell
poetry export -f requirements.txt --output requirements.txt --with dev
```

This project features most of the extensions featured in this Tutorial: [Document Your Scientific Project With Markdown, Sphinx, and Read the Docs | PyData Global 2021](https://www.youtube.com/watch?v=qRSb299awB0).
