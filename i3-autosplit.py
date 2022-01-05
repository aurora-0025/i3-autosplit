from i3ipc import Connection, Event

i3 = Connection()
# Dynamically change the split direction on window focus
def on_window(i3, e):
    focused_window = e.container
    full=bool(focused_window.fullscreen_mode)
    if(not full):
        if(focused_window.rect.width>focused_window.rect.height):
            # set split to horizontal
            i3.command('split horizontal')
        else:
            # set split to vertical           
            i3.command('split vertical')

def on_mode_change(i3, e):
    print(e.current.layout)

# Subscribe to events
i3.on(Event.WINDOW, on_window)
i3.main()


