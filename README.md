# lys0.1.2 bot 

[![Discord](https://img.shields.io/discord/123456789012345678?color=7289da&label=Discord&logo=discord&logoColor=white)](https://discord.gg/NhSyY4aqdZ)
[![Python](https://img.shields.io/badge/Python-3.10%2B-blue)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Este repositorio contiene el código fuente de un bot para Discord, desarrollado con Python y `discord.py`. El bot se encuentra en desarrollo.

## Tabla de Contenidos

- [Características](#características)
- [Requisitos](#requisitos)
- [Instalación](#instalación)
- [Configuración](#configuración)
- [Ejecución](#ejecución)
- [Estructura del Proyecto](#estructura-del-proyecto)
- [Contribuir](#contribuciones)
- [Configuración de logs](#configuración-de-logs)
- [Releases](#releases)
- [Créditos](#créditos)
- [Soporte](#soporte)

## Características

- **Comando `!ping`**: Verifica la latencia del bot.
- **Comando `!ayuda`**: Muestra los comandos disponibles.
- **Comando `!poll`**: Crea una encuesta con múltiples opciones.
- **Comando `!ochoball`**: Realiza una pregunta a la bola 8 mágica y obtén una respuesta aleatoria.
- Presencia para que el bot aparezca jugando algo en Discord.

## Requisitos

- Python 3.10 o superior.
- `discord.py` versión 2.0 o superior.

## Instalación

### Clonar el repositorio

```bash
git clone https://github.com/tu_usuario/lys.git
cd lys
```

## Configuración

### Crear y activar entorno virtual

Bash (por ejemplo: GIT terminal):
```bash
python -m venv venv
source venv/bin/activate
```
Windows:
```bash
venv\Scripts\activate
```

### Instalar dependencias

```bash
pip install -r requirements.txt
```

### Variables de entorno

Crea un archivo `.env` en la raíz del proyecto y añade tu token de Discord:

```.env
DC_TOKEN=tu_token
```

### Ejecución

Para iniciar el bot, utiliza el siguiente comando:

```bash
python main.py
```

### Estructura del proyecto

```bash
/lys
    /bot/cogs
        __init__.py
        admin.py
        fun.py
        interaction_commands.py
    /bot/core
        __pycache__
        bot.py
        config.py
    /venv
    bot.log
    CHANGELOG.md
    LICENSE
    log_config.py
    main.py
    README.md
    requirements.txt
    .env
    .gitignore
```

## Contribuciones

Agradezco a todas las contribuciones. Para contribuir, sigue estos pasos:

- Haz un fork al repositorio
- Crea una nueva rama `git checkout -b feature/nombre_de_la_rama`.
- Realiza cambios que veas oportunos y haz commit `git commit -am 'Describe aquí brevemente los cambios'`.
- Haz push a la rama `git push origin feature/nombre_de_la_raam`.
- Abre un Pull Request.

## Configuración de logs

Se ha implementado un sistema de logs para registrar eventos importantes del bot. Esto mejora la visibilidad y permite una depuración más efectiva. Revisar el archivo `bot/log_config.py` y los registros en `bot.log` para monitorear el comportamiento del bot y diagnosticar problemas.

## Releases

### Versión 0.2.0 (Próximo Release)

- **Nuevas Características Planificadas:**
  - Implementación de configuración avanzada de logging para mejoras en la gestión de errores y seguimiento de actividad.
  - Mejoras en la gestión de errores y seguimiento de actividad mediante configuración avanzada de logging.
  - Implementación de nuevos comandos para interacción más rica con los usuarios.
  - Integración con APIs externas para funcionalidades extendidas.
  - Mejoras en la seguridad y privacidad de datos de los usuarios.

### Versión 0.1.2 (Actual - Update 16/07/2024)
- **Nuevos Comandos:**

| Comando         | Descripción                                                                                         | Uso                                                 | Ejemplo                                              |
|-----------------|-----------------------------------------------------------------------------------------------------|------------------------------------------------------|------------------------------------------------------|
| `!ayuda`        | Muestra los comandos disponibles o información específica sobre un comando.                         | `!ayuda`                                   | `!ayuda`                                        |
| `!poll`         | Crea una encuesta con múltiples opciones.                                                           | `!poll ¿Tu pregunta? \| opción1 \| opción2 \| ...`   | `!poll ¿Cuál es tu película favorita? \| Avengers \| Harry Potter \| Star Wars` |
| `!ochoball`     | Realiza una pregunta a la bola 8 mágica y obtén una respuesta aleatoria.                             | `!ochoball <tu pregunta>`                            | `!ochoball ¿Debería salir hoy?`                      |
- **Características Iniciales:**
  - Funcionalidad básica del bot con comandos básicos.
  - Presencia para que el bot aparezca jugando algo en Discord.

Este repositorio está en desarrollo activo y continúa mejorando. Consulta el archivo [CHANGELOG.md](CHANGELOG.md) para obtener detalles completos sobre cada release y cambios específicos.

## Créditos

- **Álex** - Desarrollador Principal - [LexDevM](https://github.com/LexDevM)

## Soporte

Este proyecto es mantenido y desarrollado activamente. Para obtener soporte o realizar preguntas, únete al [servidor de Discord](https://discord.gg/NhSyY4aqdZ).
