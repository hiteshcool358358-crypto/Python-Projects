import flet as ft

def main(page: ft.Page):
    page.window.width = 350
    page.window.height = 600
    page.title = "Text Function"
    page.window.always_on_top = True

    page.add(
        ft.Text("Hi, I am Text", size=19),
        ft.Text("bgcolour property", size=19, bgcolor="red"),
        ft.Text("opacity property", opacity=0.1),
        ft.Text("visible property", visible=False),
        ft.Text("visible property", visible=False)
    )

ft.app(target=main)