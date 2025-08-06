from nicegui import ui

@ui.page('/')
def index():
    ui.markdown('# ✨ AuraCraft AI Test')
    ui.markdown('If you see this, NiceGUI is working!')
    ui.button('Test Button', on_click=lambda: ui.notify('Button works!'))

if __name__ in {"__main__", "__mp_main__"}:
    ui.run(port=8081, show=True)
