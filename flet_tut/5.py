import flet as ft

def main(page: ft.Page):
    page.window.width = 350
    page.window.height = 600
    page.window.always_on_top = True
    page.title = "Text Field Widget P-3"
    page.theme_mode = "light"

    page.add(
        # all leftover attributes
        ft.TextField(
            border_radius=20,
            border_color=ft.Colors.BLACK,
            label="Enter url here",
            text_align=ft.TextAlign.START,
            # text_align=ft.TextAlign.CENTER.
            # text_align=ft.TextAlign.END,
            # text_align=ft.TextAlign.JUSTIFY,
            # text_align=ft.TextAlign.LEFT,
            # text_align=ft.TextAlign.RIGHT,
            filled=True,
            # bgcolor=ft.Colors.BLACK,
            prefix="https://",
            suffix=".com",
            prefix_icon=ft.Icons.SEARCH,
            error=None,
            # error="This is a error just for demo",
            focus_color=ft.Colors.RED,
            focused_border_color=ft.Colors.BLUE,
            max_length=10,
            selection_color=ft.Colors.BLACK,
            shift_enter=True,
            width=1000         
        ),
        ft.TextField(
            border_radius=20,
            border_color=ft.Colors.BLACK,
            label="Enter gmail address here",
            suffix="@gmail.com",
            suffix_icon=ft.Icons.MAIL,
            multiline=True,
            read_only=True,
        ),
        ft.TextField(
            border_radius=20,
            border_color=ft.Colors.BLACK,
            label="Enter your password here",
            icon=ft.Icons.PASSWORD,
            password=True,
            can_reveal_password=True
        )
    )

ft.app(target=main)