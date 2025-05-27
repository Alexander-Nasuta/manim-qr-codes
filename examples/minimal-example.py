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
