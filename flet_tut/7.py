import flet as ft

def main(page:ft.Page):
    page.window.height=600
    page.window.width=350
    page.window.resizable=False
    page.window.always_on_top=True
    page.theme_mode="light"

    page.add(
        ft.TextField(
            label="Email",
            icon=ft.Icons.MAIL,
            suffix="@gmail.com"
            ),
        ft.TextField(
            label="Password",
            password=True,
            can_reveal_password=True,
            icon=ft.Icons.PASSWORD
        ),
        ft.TextButton("Login")
    )

ft.app(main)