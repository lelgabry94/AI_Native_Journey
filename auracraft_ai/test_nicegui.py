from nicegui import ui

@ui.page('/')
def index():
    ui.label('Hello NiceGUI!')
    ui.button('Click me!', on_click=lambda: ui.notify('Button clicked!'))

ui.run(port=8081)
