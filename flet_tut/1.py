import flet as ft

def main(page: ft.Page):
    page.window.width = 350
    page.window.height = 600
    page.window.always_on_top = True
    page.title = "My First Flet App"

    page.add(
        ft.Text("Hello World")
    )

ft.app(target=main)