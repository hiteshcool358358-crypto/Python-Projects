import flet as ft

def myfunc(e):
    print("Hello i have been clicked")

def func(f):
    print("The cursor is hovering on me")

def longPress(g):
    print("I have been long-clicked")

def main(page:ft.Page):
    page.window.width=350
    page.window.height=600
    page.window.resizable=False
    page.window.always_on_top=True
    page.theme_mode="light"
    page.title="Button"

    page.add(
        ft.Button(
            "Hello",
            # disabled=True
            opacity=1,
            tooltip="This is an elevated button",
            icon=ft.Icons.MUSIC_NOTE,
            on_click=myfunc,
            on_hover=func,
            on_long_press=longPress
            )
    )

ft.run(main)