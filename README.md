# DirFuzz

**DirFuzz** es una herramienta de *fuzzing* ligera y modular diseñada para descubrir directorios y archivos ocultos en aplicaciones web mediante ataques de diccionario.

## Características

- **Modular**: Arquitectura separada en lógica de escaneo, CLI y logging.
- **Rápido**: Control de velocidad y timeouts configurables.
- **Visual**: Interfaz de consola con colores y spinner de progreso.
- **Flexible**: Permite definir códigos de estado a monitorear (ej. 200, 404, 301).

## Estructura del Proyecto

El proyecto ha sido refactorizado para seguir una arquitectura modular:

```text
DirFuzz/
├── main.py            # Punto de entrada de la aplicación
├── core/              # Lógica principal
│   ├── cli.py         # Manejo de argumentos de línea de comandos
│   ├── logger.py      # Configuración de logs y salida por consola
│   └── scanner.py     # Lógica del fuzzer (clase Fuzzer)
├── diccionario.txt    # Archivo de ejemplo con rutas a probar
├── fuzzing_log.log    # Log generado automáticamente
└── requirements.txt   # Dependencias del proyecto
```

## Requisitos

- Python 3.8+
- Librerías listadas en `requirements.txt`

## Instalación

1. Clona el repositorio o descarga los archivos.
2. Instala las dependencias:

```bash
pip install -r requirements.txt
```

## Uso

Para ejecutar la herramienta, utiliza `main.py` seguido de la URL objetivo y el archivo de diccionario.

### Comandos Básicos

```bash
# Uso estándar
python main.py https://example.com/ diccionario.txt
```

### Opciones Avanzadas

| Argumento | Descripción |
| :--- | :--- |
| `-t`, `--timeout` | Timeout de las peticiones en segundos (defecto: 10). |
| `-s`, `--status` | Lista de códigos de estado HTTP a reportar (defecto: 200 404). |
| `--delay` | Tiempo de espera entre peticiones en segundos (útil para evitar bloqueos). |
| `--silent` | Modo silencioso, reduce la salida en consola. |

### Ejemplos

**Escaneo lento (0.5s de delay) para evitar rate-limits:**
```bash
python main.py https://example.com/ diccionario.txt --delay 0.5
```

**Buscar solo redirecciones (301) y éxitos (200), en modo silencioso:**
```bash
python main.py https://example.com/ diccionario.txt --status 200 301 --silent
```

## Logs

La herramienta genera automáticamente un archivo `Fuzzing_log.log` (o el nombre configurado) con el detalle de la ejecución, incluyendo timestamps y resultados encontrados.

## Contribuir

Si deseas agregar nuevas funcionalidades:
1. La lógica de argumentos está en `core/cli.py`.
2. La configuración de visualización en `core/logger.py`.
3. El motor de peticiones en `core/scanner.py`.
