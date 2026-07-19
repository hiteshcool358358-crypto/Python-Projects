import flet as ft

def main(page: ft.Page):
    page.window.width = 350
    page.window.height = 600
    page.window.always_on_top = True
    page.title = "Text Field Widget P-2"
    page.theme_mode = "light"

    page.add(
        # some more ft.TextField() attributes
        ft.TextField(
            border_width=1,
            border_color=ft.Colors.BLACK,
            border_radius=20,
            # text_size=20 
            autofocus=True,
            counter=29,
            cursor_color=ft.Colors.GREEN,
            cursor_width=3,
            cursor_radius=20,
            helper="max no. of words reached",
            label="Enter email id."
        )  
    )

ft.app(target=main)