import flet as ft

def main(page: ft.Page):
    page.title = "Dropdown Example"
    page.padding = 20

    def dropdown_selected(e):
        t.value = f"Selected item: {dd.value}"
        page.update()

    t = ft.Text()

    dd = ft.Dropdown(
        label="Select a Language",
        hint_text="Choose one...",
        width=300,
        border_radius=30,
        on_select=dropdown_selected,
        options=[
            ft.dropdown.Option("Java"),
            ft.dropdown.Option("Python"),
            ft.dropdown.Option("QBasic"),
            ft.dropdown.Option("Spanish"),
        ],
    )

    page.add(dd, t)

ft.app(target=main)