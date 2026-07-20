import flet as ft

def main(page:ft.Page):
    page.window.width=350
    page.window.height=600
    page.window.resizable=False
    page.window.always_on_top=True
    page.theme_mode="light"
    page.title="Button"

    page.add(
        ft.TextButton("Text Button"),
        ft.OutlinedButton("Outlined Button"),
        ft.ElevatedButton(
            "Elevated Button"
            )
    )

ft.run(main)