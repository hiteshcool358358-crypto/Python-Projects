import flet as ft

def main(page: ft.Page):
    page.window.width = 350
    page.window.height = 600
    page.title = "Text Function"
    page.window.always_on_top = True

    page.add(
        # some ft.Text() attributes
        ft.Text("Hi, I am Text", size=19),
        ft.Text("bgcolour property", size=19, bgcolor="red"),
        ft.Text("opacity property", opacity=0.1),
        ft.Text("visible property", visible=False),
        ft.Text("weight", weight=ft.FontWeight.BOLD),
        ft.Text("selectable", selectable=True),
        ft.Text("scale", scale=5),
        ft.Text("tooltip", tooltip="Hello bruh this is a tooltip"),
        ft.Text("max_line. Using this attribute or function we can set the max no. of lines in which this text will appear", max_lines=2),
        
        ft.Text("font_family", font_family="comicsansm")
    )

ft.app(target=main)