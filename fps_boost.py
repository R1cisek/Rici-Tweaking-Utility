import os
import tkinter as tk
from tkinter import messagebox

# Funkce pro optimalizaci FPS
def disable_unnecessary_services():
    os.system('powershell Set-Service "SysMain" -StartupType Disabled; Stop-Service "SysMain" -Force')
    os.system('powershell Set-Service "WSearch" -StartupType Disabled; Stop-Service "WSearch" -Force')
    messagebox.showinfo("FPS Boost", "Nepotřebné služby vypnuty!")

def optimize_cpu():
    os.system('powershell powercfg -attributes SUB_PROCESSOR 0cc5b647-c1df-4637-891a-dec35c318583 -ATTRIB_HIDE')
    messagebox.showinfo("FPS Boost", "Optimalizace CPU dokončena!")

def clean_ram():
    os.system('powershell Clear-MemoryCache')
    os.system('powershell Clear-DnsClientCache')
    messagebox.showinfo("FPS Boost", "RAM a DNS cache vyčištěny!")

def game_mode():
    os.system('powershell reg add "HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\GameBar" /v AllowAutoGameMode /t REG_DWORD /d 1 /f')
    messagebox.showinfo("FPS Boost", "Herní režim aktivován!")

def optimize_network():
    os.system('powershell netsh interface tcp set global autotuninglevel=normal')
    os.system('powershell netsh interface tcp set global ecncapability=disabled')
    messagebox.showinfo("FPS Boost", "Síťová latence optimalizována!")

def reset_settings():
    os.system('powershell Set-Service "SysMain" -StartupType Automatic; Start-Service "SysMain"')
    os.system('powershell Set-Service "WSearch" -StartupType Automatic; Start-Service "WSearch"')
    messagebox.showinfo("FPS Boost", "Vše obnoveno na výchozí hodnoty!")

# GUI aplikace
root = tk.Tk()
root.title("FPS Boost Utility")
root.geometry("400x400")
root.configure(bg="black")

# Nadpis
label = tk.Label(root, text="FPS BOOST UTILITY", font=("Arial", 16, "bold"), fg="lime", bg="black")
label.pack(pady=10)

# Tlačítka
btn1 = tk.Button(root, text="Vypnout služby", command=disable_unnecessary_services, width=25, bg="gray", fg="white")
btn1.pack(pady=5)

btn2 = tk.Button(root, text="Optimalizovat CPU", command=optimize_cpu, width=25, bg="gray", fg="white")
btn2.pack(pady=5)

btn3 = tk.Button(root, text="Vyčistit RAM", command=clean_ram, width=25, bg="gray", fg="white")
btn3.pack(pady=5)

btn4 = tk.Button(root, text="Herní režim", command=game_mode, width=25, bg="gray", fg="white")
btn4.pack(pady=5)

btn5 = tk.Button(root, text="Síťová optimalizace", command=optimize_network, width=25, bg="gray", fg="white")
btn5.pack(pady=5)

btn6 = tk.Button(root, text="Obnovit nastavení", command=reset_settings, width=25, bg="red", fg="white")
btn6.pack(pady=10)

# Spuštění aplikace
root.mainloop()
