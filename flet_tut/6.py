import flet as ft


def inputFocus(e:ft.ControlEvent):
    print("I am focused")

def inputBlur(e:ft.ControlEvent):
    print("I am blurred")

def inputChanged(e:ft.ControlEvent):
    text_field:ft.TextField = e.control
    a=text_field.value
    print(a)
    
def main(page:ft.Page):
    page.window.width=350
    page.window.height=600
    page.window.always_on_top=True
    page.theme_mode="light"
    page.title="ft.TextField() attributes - P4"

    page.add(
        ft.TextField(
            on_focus=inputFocus,
            on_blur=inputBlur,
            on_change=inputChanged,
            on_submit=inputChanged
        )
    )

ft.app(main)