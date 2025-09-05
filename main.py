import flet as ft

def main(page: ft.Page):
    page.title = "Моё первое приложение!"
    page.theme_mode = ft.ThemeMode.DARK

    greeting_text = ft.Text(value="Hello world!")
    name_input = ft.TextField(label="Введите имя: ")

    def on_button_click(e):
        name = name_input.value.strip()
        print(name)

        greeting_text.value = f"Hello {name}"
        print(greeting_text)

        page.update()

    name_button = ft.ElevatedButton(text="SEND", on_click=on_button_click)


    page.add(greeting_text, name_input, name_button)


ft.app(target=main)    

