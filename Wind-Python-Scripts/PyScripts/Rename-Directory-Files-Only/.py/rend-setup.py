import os
import sys
import winreg

def add_context_menu_entry():
    key = winreg.HKEY_CLASSES_ROOT
    subkey = "AllFilesystemObjects\\shell\\Rename Dir Script"
    command = os.path.abspath("rend.exe")
    with winreg.CreateKey(key, subkey) as key_handle:
        winreg.SetValueEx(key_handle, "", 0, winreg.REG_SZ, "Rename Dir Script")
        with winreg.CreateKey(key_handle, "command") as command_key_handle:
            winreg.SetValue(command_key_handle, "", winreg.REG_SZ, f'"{command}" "%1"')

if __name__ == "__main__":
    add_context_menu_entry()
