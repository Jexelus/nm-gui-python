import flet as ft


def main(page: ft.Page):
    page.title = "nm-gui-python"
    page.window_center()
    page.window_width = 600
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER


ft.app(target=main)
