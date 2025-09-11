import flet as ft
import datetime 


def main(page: ft.Page):
    page.title = "Моё первое приложение!"
    page.theme_mode = ft.ThemeMode.DARK


    greeting_text = ft.Text(value="Hello world!")

    greeting_history = []
    history_text = ft.Text('История приветствий:')

    def on_button_click(e):
        name = name_input.value.strip()
        #print(name)
        time_name = datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S") 

        if name:
            greeting_text.value = f"Hello {name}!"
            #print(greeting_text)
            name_input.value = ''

            greeting_history.append(f"{time_name} {name}")
            history_text.value = "История приветствий:\n " + "\n".join(greeting_history)

        else:
            greeting_text.value = "Пожалуйста, введите имя"

        page.update()

    

    def clear_history(e):
        greeting_history.clear()
        history_text.value = "История приветствий"
        page.update()

    def theme(_):
        if page.theme_mode == ft.ThemeMode.LIGHT:
            page.theme_mode = ft.ThemeMode.DARK

        else:
            page.theme_mode = ft.ThemeMode.LIGHT
        page.update()

    def toggle_history(e):
        if history_text.value:  # если текст истории есть
            history_text.value = ""
            toggle_history_button.text = "Показать историю"
        else:
            history_text.value = "История приветствий:\n " + "\n".join(greeting_history)
            toggle_history_button.text = "Скрыть историю"
        page.update()






    name_input = ft.TextField(label="Введите имя: ", on_submit=on_button_click)
    name_button = ft.ElevatedButton(text="SEND", on_click=on_button_click)
    clear_history_button = ft.IconButton(icon=ft.Icons.DELETE, on_click=clear_history)
    theme_button = ft.IconButton(icon=ft.Icons.BRIGHTNESS_6, on_click=theme, tooltip="Сменит тему")
    toggle_history_button = ft.ElevatedButton(text="Скрыть историю", on_click=toggle_history)



    page.add(greeting_text, name_input, name_button, clear_history_button,theme_button, toggle_history_button, history_text)


ft.app(target=main)    


