from pywinauto import application, win32defines
from pywinauto.win32functions import SetForegroundWindow, ShowWindow

# Select random app from the pull of apps
def displayBDO():
    # Init App object
    app = application.Application().connect(title_re=".*%s.*" % 'BLACK DESERT')
    w = app.top_window()

    #bring window into foreground
    if w.HasStyle(win32defines.WS_MINIMIZE): # if minimized
        ShowWindow(w.wrapper_object(), 9) # restore window state
    else:
        SetForegroundWindow(w.wrapper_object()) #bring to front