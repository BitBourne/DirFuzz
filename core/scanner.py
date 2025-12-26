import time
import requests
import logging
from colorama import Fore
from yaspin import yaspin

class Fuzzer:
    def __init__(self, config):
        self.url = config.url
        self.diccionario_path = config.diccionario
        self.timeout = config.timeout
        self.status_list = config.status
        self.delay = config.delay
        self.silent = config.silent
        self.wordlist = []

    def load_wordlist(self):
        try:
            with open(self.diccionario_path, "r", encoding="utf-8", errors="ignore") as file:
                self.wordlist = file.read().splitlines()
            return True
        except FileNotFoundError:
            print(f"{Fore.RED}[!] Diccionario no encontrado: {self.diccionario_path}")
            return False

    def start(self):
        if not self.load_wordlist():
            return

        logging.info(f"Iniciando fuzzing en {self.url} | delay={self.delay}s")
        print(f"{Fore.YELLOW}\nIniciando Escaneo...")

        try:
            with yaspin(text="Iniciando...", color="cyan") as sp:
                total = len(self.wordlist)

                for i, linea in enumerate(self.wordlist, start=1):
                    ruta = linea.strip()
                    url_completa = self.url + ruta
                    sp.text = f"Proceso {i}/{total} - {ruta}"

                    self._scan_url(url_completa, sp)

                    # Control de velocidad
                    if self.delay > 0:
                        time.sleep(self.delay)

                logging.info("Escaneo Finalizado.")
                sp.ok("Escaneado")
                
        except KeyboardInterrupt:
            logging.info("Stop Scan (Ctrl + C)")
            print(f"{Fore.RED}\n[!] Stop Scan (Ctrl + C)")
        finally:
            print(f"{Fore.YELLOW}\nEscaneo Finalizado.")

    def _scan_url(self, url, spinner):
        try:
            response = requests.get(url, timeout=self.timeout)
        except requests.RequestException as e:
            logging.warning(f"Error en {url}: {e}")
            return

        if response.status_code in self.status_list:
            mensaje = f"{url} ------ status {response.status_code}"

            if response.status_code == 200:
                logging.info(f"[FOUND] {mensaje}")
                if not self.silent:
                    spinner.write(f"{Fore.GREEN}[+] {mensaje}")

            elif response.status_code == 404 and not self.silent:
                logging.warning(f"[NOT FOUND] {mensaje}")
                spinner.write(f"{Fore.RED}[-] {mensaje}")
