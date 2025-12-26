import argparse

class CLI:
    @staticmethod
    def parse_arguments():
        parser = argparse.ArgumentParser(
            prog="fuzzer",
            description="Herramienta de fuzzing para descubrir directorios y archivos ocultos en aplicaciones.",
            epilog="""
Ejemplos de uso:
  python main.py https://example.com/ diccionario.txt
  python main.py --delay 0.5 https://example.com/ diccionario.txt 
  python main.py --status 200 301 --silent https://example.com/ diccionario.txt 

Notas:
  - La URL debe terminar con /
  - El diccionario debe ser un archivo local
""",
            formatter_class=argparse.RawTextHelpFormatter
        )

        parser.add_argument("url", help="URL base objetivo (ej: https://example.com/)")
        parser.add_argument("diccionario", help="Ruta al diccionario local")

        parser.add_argument(
            "-t", "--timeout",
            type=int,
            default=10,
            help="Timeout de las peticiones HTTP (default: 10)"
        )

        parser.add_argument(
            "-s", "--status",
            nargs="+",
            type=int,
            default=[200, 404],
            help="Códigos HTTP a mostrar (default: 200 404)"
        )

        parser.add_argument(
            "--delay",
            type=float,
            default=0.0,
            help="Tiempo de espera entre requests en segundos (ej: 0.5)"
        )

        parser.add_argument(
            "--silent",
            action="store_true",
            help="Modo silencioso (solo resultados relevantes)"
        )

        return parser.parse_args()
