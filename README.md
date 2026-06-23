# Process Automation Pipeline: RPA Challenge (Exercise 1)

Modular Python solution for processing and validating a simulated inbox. Designed and structured within a 24-hour window using an object-oriented approach.

> 💡 **Note:** Real automation technical test.

---

## 🛠️ Tech Stack

* **Language:** Python 3.10+
* **Configuration:** Native `json`.
* **Logs:** Standard `logging` for technical auditing.
* **Lifecycle:** Context Managers (`__enter__` / `__exit__`) for clean execution flows.

---

## ⚙️ Architecture and Components

The project divides responsibilities into independent modules:

1. **`Config` (`read_config_file.py`):** Dynamically defines project base paths and input/output names in a cross-platform manner.
2. **`Emails` (`read_dummy_mails.py`):** Main class acting as a Context Manager. It cleans up previous directories at startup, ensures process teardown upon exit, and captures error states.
3. **`Log` (`create_log_file.py`):** Configures event tracing by mapping severity levels (`INFO`, `DEBUG`, `CRITICAL`) into a physical file.
4. **`JsonManipulation` (`read_json_file.py`):** Handles opening, reading, and filtering structured parameters in JSON format.

---

## 📁 Repository Structure

```text
├── config/
│   └── read_config_file.py     # Workspace initialization
├── json_activities/
│   └── read_json_file.py       # JSON data reader
├── log_activities/
│   └── create_log_file.py      # Log system instantiator
├── mail_activites/
│   └── read_dummy_mails.py     # Bot Orchestrator (Context Manager)
├── main.py                     # Main entry point script
├── config.json                 # Process parameters file
└── README.md                   # Technical documentation

=========================================================================================================================

# Pipeline de Automatización de Procesos: Desafío RPA (Ejercicio 1)

Solución modular en Python para el procesamiento y validación de una bandeja de entrada simulada. Diseñado y estructurado en un periodo de 24 horas bajo un enfoque orientado a objetos.

> 💡 **Nota:** Prueba técnica de automatización real.

---

## 🛠️ Stack Tecnológico

* **Lenguaje:** Python 3.10+
* **Configuración:** `json` nativo.
* **Logs:** `logging` estándar para auditoría técnica.
* **Ciclo de Vida:** Controladores de contexto (`__enter__` / `__exit__`) para flujos de ejecución limpios.

---

## ⚙️ Arquitectura y Componentes

El proyecto divide responsabilidades en módulos independientes:

1. **`Config` (`read_config_file.py`):** Define dinámicamente las rutas base del proyecto y los nombres de las entradas/salidas de forma multiplataforma.
2. **`Emails` (`read_dummy_mails.py`):** Clase principal que actúa como Context Manager. Limpia directorios previos en el inicio, asegura el desmontaje del proceso al salir y captura estados de error.
3. **`Log` (`create_log_file.py`):** Configura el rastreo de eventos mapeando niveles de severidad (`INFO`, `DEBUG`, `CRITICAL`) hacia un archivo físico.
4. **`JsonManipulation` (`read_json_file.py`):** Encargado de la lectura, apertura y filtrado de parámetros estructurados en formato JSON.

---

## 📁 Estructura del Repositorio

```text
├── config/
│   └── read_config_file.py     # Inicialización del entorno de trabajo
├── json_activities/
│   └── read_json_file.py       # Lector de datos JSON
├── log_activities/
│   └── create_log_file.py      # Instanciador del sistema de logs
├── mail_activites/
│   └── read_dummy_mails.py     # Orquestador del Bot (Context Manager)
├── main.py                     # Script de entrada principal
├── config.json                 # Archivo de parámetros del proceso
└── README.md                   # Documentación técnica
