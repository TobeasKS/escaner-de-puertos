# 🛡️ Escáner de Puertos Táctico (Tactical Port Scanner)

Una herramienta de ciberseguridad desarrollada en Python enfocada en el reconocimiento ágil de redes y el diagnóstico de puertos abiertos. Diseñada con un enfoque de optimización y rendimiento mediante procesamiento concurrente.

## ✨ Características Principales

* **Procesamiento Multihilo (Multi-threading):** Implementación de `concurrent.futures` para realizar escaneos simultáneos (hasta 50 workers), reduciendo drásticamente la latencia y los tiempos de espera asociados a las operaciones de red.
* **Banner Grabbing Integrado:** Capacidad para extraer e identificar versiones de software y servicios en ejecución sobre los puertos abiertos tras establecer la conexión TCP.
* **Interfaz de Línea de Comandos (CLI):** Uso de `argparse` para parametrizar la ejecución (IP y rango de puertos) de forma dinámica sin necesidad de modificar el código fuente.
* **Librerías Nativas:** Construido íntegramente con librerías estándar de Python (`socket`, `argparse`, `concurrent.futures`), lo que garantiza su portabilidad y fácil ejecución en cualquier entorno sin dependencias de terceros.
* **Tolerancia a Fallos:** Manejo robusto de excepciones (timeouts y conexiones sin respuesta) mediante bloques `try/except` para asegurar que el proceso de escaneo sea estable y no se interrumpa ante errores de conexión.

## ⚙️ Requisitos previos

* **Python 3.x** instalado en el sistema (Windows, Linux o macOS).
* No requiere la instalación de módulos externos vía `pip`.

## 🚀 Modo de Uso

La herramienta se ejecuta desde la terminal o línea de comandos. Debes especificar la dirección IP objetivo y, opcionalmente, el límite máximo de puertos a escanear.

```bash
# Sintaxis básica
python port_scanner.py -i <IP_OBJETIVO> [-p <LIMITE_PUERTOS>]

# Ejemplo: Escanear los primeros 500 puertos de la IP 192.168.1.100
python port_scanner.py -i 192.168.1.100 -p 500