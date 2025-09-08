import flet as ft

def main(page: ft.Page):
    page.title = "Моё первое приложение!"
    page.theme_mode = ft.ThemeMode.DARK


    greeting_text = ft.Text(value="Hello world!")

    greeting_history = []
    history_text = ft.Text('История приветствий:')

    def on_button_click(e):
        name = name_input.value.strip()
        #print(name)

        if name:
            greeting_text.value = f"Hello {name}!"
            #print(greeting_text)
            name_input.value = ''

            greeting_history.append(f"{name}")
            history_text.value = "История приветствий:\n " + "\n".join(greeting_history)

        else:
            greeting_text.value = "Пожалуйста, введите имя"

        page.update()

    name_input = ft.TextField(label="Введите имя: ", on_submit=on_button_click)
    name_button = ft.ElevatedButton(text="SEND", on_click=on_button_click)


    page.add(greeting_text, name_input, name_button, history_text)


ft.app(target=main)    


