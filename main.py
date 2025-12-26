from core.cli import CLI
from core.logger import Logger
from core.scanner import Fuzzer

def main():
    # 1. Parsear argumentos
    args = CLI.parse_arguments()

    # 2. Configurar Logger
    Logger.setup_logging()

    # 3. Iniciar Fuzzer
    fuzzer = Fuzzer(args)
    fuzzer.start()

if __name__ == "__main__":
    main()
