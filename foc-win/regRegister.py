from _winreg import *
from PySide import QtCore

DEBUG_MSGBOX = False

def log(txt):
    if DEBUG_MSGBOX:
        from PySide.QtGui import QMessageBox
        msgBox = QMessageBox()
        msgBox.setText(txt)
        msgBox.exec_()
    else:
        print txt

def handler_path(exe_path):
    return (exe_path +  ' "%1"')

def icon_path(exe_path):
    return (exe_path + ',0')

def get_classes_key():
    return OpenKey(HKEY_CURRENT_USER, "Software\\Classes")

def get_protocol_key(prot):
    return CreateKey(get_classes_key(), prot)

def register_progID(exe_path, progID):
    # Create registry entry to associate file extension with application in C++
    # http://stackoverflow.com/q/1387769
    log("registering progID")
    pk = CreateKey(get_classes_key(), progID)
    with CreateKey(pk, "shell\\open\\command") as k:
        log("setting shell\\open\\command to " + handler_path(exe_path))
        SetValue(k, None,  REG_SZ, handler_path(exe_path))
    with CreateKey(pk, "DefaultIcon") as k:
        log("setting DefaultIcon key value to " + icon_path(exe_path))
        SetValue(k, None,  REG_SZ, icon_path(exe_path))

def associate_extension(progID, exe_path, ext):
    if ext[0] != '.':
        log('dot missing in extension "' + ext + '", fixed to ' + '.' + ext)
        ext = '.' + ext
    try:
        k = OpenKey(get_classes_key(), progID)
    except WindowsError:
        log("progID " +  progID + " was not found in registry, creating it")
        register_progID(exe_path, progID)
    with CreateKey(get_classes_key(), ext) as k:
        log("setting " + ext + " class to " + progID)
        SetValue(k, None, REG_SZ, progID)

def associate_protocol(exe_path, prot):
    # Registering an Application to a URL Protocol
    # http://msdn.microsoft.com/en-us/library/aa767914(v=vs.85).aspx
    SetValue(get_protocol_key(prot), None, REG_SZ, 'URL: Magnet Protocol')
    SetValueEx(get_protocol_key(prot), 'URL Protocol', None, REG_SZ, '')
    with CreateKey(get_protocol_key(prot), "shell\\open\\command") as k:
        log("setting shell\\open\\command to " + handler_path(exe_path))
        SetValue(k, None,  REG_SZ, handler_path(exe_path))
    with CreateKey(get_protocol_key(prot), "shell\\open\\ddeexec") as k:
        log("setting shell\\open\\ddeexec to nothing")
        SetValue(k, None,  REG_SZ, "")
    with CreateKey(get_protocol_key(prot), "DefaultIcon") as k:
        log("setting DefaultIcon key value to " + icon_path(exe_path))
        SetValue(k, None,  REG_SZ, icon_path(exe_path))
