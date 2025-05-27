# Example Gallery

This gallery contains a collection of code snippets together with their corresponding output, illustrating different colors themes in Manim and example objects.
```{note}
Check out [manim-nerdfont-icons](https://manim-nerdfont-icons.readthedocs.io/en/latest/icon-gallery.html) for available icons.
```

```{eval-rst}
.. manim:: MyQrCodeScene
    :save_last_frame:
    
    
    import manim as m

    from manim_qr_codes.qr import qr_code
    
    
    class MyQrCodeScene(m.Scene):
    
        def construct(self):
    
            qr_code_without_icon = qr_code("https://fishshell.com")
            qr_code_with_icon = qr_code(
                payload="https://fishshell.com",
                icon='terminal#2',
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


```{eval-rst}
.. manim:: ExhaustiveQrCodeExampleScene


    import manim as m
    
    from manim_qr_codes.qr import qr_code
    
    
    class ExhaustiveQrCodeExampleScene(m.Scene):
    
        def construct(self):
    
            neovim_qr_code = qr_code("https://neovim.io/", icon='Neovim')
    
            self.play(
                m.FadeIn(neovim_qr_code)
            )
            self.wait(1)
    
            rust_qr_code = qr_code("https://www.rust-lang.org/", icon="language-rust", data_shape='circles')
    
            self.play(
                m.ReplacementTransform(neovim_qr_code, rust_qr_code),
            )
            self.wait(1)
    
            python_qr_code = qr_code("https://www.python.org/",
                                          icon="language-python",
                                          data_shape='circles',
                                          corner_color=m.BLUE,
                                          icon_color=m.YELLOW,
                                          icon_size=4,  # make the icon 5 qr code pixels wide
                                          )
    
            self.play(
                m.ReplacementTransform(rust_qr_code, python_qr_code),
            )
            self.wait(1)
    
            # obligatory javascript joke
            js_qr_code = qr_code(
                payload="https://www.javascript.com/",
                icon="poo",
                data_shape='circles',
                corner_color=m.RED_B,
                white_color=m.YELLOW,
                icon_color=m.GRAY,
            )
    
            self.play(
                m.ReplacementTransform(python_qr_code, js_qr_code),
            )
            self.wait(1)
    
    
            github_catppuccin_qr_code = qr_code(
                payload="https://github.com/catppuccin/catppuccin",
                icon='cat',
                icon_color=m.DARK_BLUE,
                data_shape='circles',
                white_color=m.BLUE,
                corner_color=m.TEAL,
            )
    
            self.play(
                m.ReplacementTransform(js_qr_code, github_catppuccin_qr_code),
            )
            self.wait(1)
    
    
    
    if __name__ == '__main__':
    
        import os
        from pathlib import Path
    
        FLAGS = "-pqm"
        SCENE = "ExhaustiveQrCodeExampleScene"
    
        file_path = Path(__file__).resolve()
        os.system(f"manim {Path(__file__).resolve()} {SCENE} {FLAGS}")
        
    
```


