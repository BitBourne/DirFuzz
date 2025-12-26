import logging
from colorama import init

class Logger:
    @staticmethod
    def setup_logging(filename="Fuzzing_log.log"):
        # Inicializar colorama
        init(autoreset=True)

        # Configurar logging
        logging.basicConfig(
            filename=filename,
            level=logging.INFO,
            format="%(asctime)s - %(levelname)s - %(message)s"
        )
