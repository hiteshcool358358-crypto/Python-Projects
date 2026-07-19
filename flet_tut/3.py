import flet as ft

def main(page: ft.Page):
    page.window.width = 350
    page.window.height = 600
    page.title = "Text Field Widget"
    page.window.always_on_top = True
    page.theme_mode = "light"
    # page.theme_mode = "system"
    # page.theme_mode = "dark"

    page.add(
        # some ft.TextField() attributes here:
        ft.TextField(
            color=ft.Colors.RED,
            border=ft.InputBorder.OUTLINE,
            # border=ft.InputBorder.NONE,
            # border=ft.InputBorder.UNDERLINE,
            border_color=ft.Colors.RED,
            border_width=2.5,
            border_radius=20,
            content_padding=10,
            capitalization=ft.TextCapitalization.NONE,
            # capitalization=ft.TextCapitalization.SENTENCES,
            # capitalization=ft.TextCapitalization.CHARACTERS,
            # capitalization=ft.TextCapitalization.WORDS,
            disabled=False,
            # value="email@gmail.com"
            hint_text="Enter your email here"
        )
    )

ft.app(target=main)