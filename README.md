# lys0.1.0 bot 

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
- [Licencia](#licencia)
- [Créditos](#créditos)
- [Soporte](#soporte)

## Características

- **Comando `!ping`**: Verifica la latencia del bot.

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

Linux (SHELL terminal):
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
    /bot/core
        __pycache__
        bot.py
        config.py
    /venv
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

### Versión 0.1.2 (Próximo Release)

- **Nuevas Características Planificadas:**
  - Implementación de configuración avanzada de logging para mejoras en la gestión de errores y seguimiento de actividad.
  - Mejoras en la gestión de errores y seguimiento de actividad mediante configuración avanzada de logging.
  - Implementación de nuevos comandos para interacción más rica con los usuarios.
  - Integración con APIs externas para funcionalidades extendidas.
  - Mejoras en la seguridad y privacidad de datos de los usuarios.

### Versión 0.1.1 (Actual)

- **Características Iniciales:**
  - Funcionalidad básica del bot con comandos básicos.

Este repositorio está en desarrollo activo y continúa mejorando. Consulta el archivo [CHANGELOG.md](CHANGELOG.md) para obtener detalles completos sobre cada release y cambios específicos.


## Licencia

MIT License

Copyright (c) 2024 LexDevM

Se concede permiso, de forma gratuita, a cualquier persona que obtenga una copia
de este software y los archivos de documentación asociados (el "Software"), para tratar
en el Software sin restricciones, incluidos, entre otros, los derechos
para usar, copiar, modificar, fusionar, publicar, distribuir, sublicenciar y/o vender
copias del Software, y para permitir a las personas a quienes se les
proporciona el Software que lo hagan, sujeto a las siguientes condiciones:

El aviso de derechos de autor anterior y este aviso de permiso se incluirán en todos
las copias o partes sustanciales del Software.

EL SOFTWARE SE PROPORCIONA "TAL CUAL", SIN GARANTÍA DE NINGÚN TIPO, EXPRESA O
IMPLÍCITA, INCLUIDAS, PERO NO LIMITADAS A LAS GARANTÍAS DE COMERCIABILIDAD,
IDONEIDAD PARA UN PROPÓSITO PARTICULAR Y NO INFRACCIÓN. EN NINGÚN CASO LOS
AUTORES O LOS TITULARES DE LOS DERECHOS DE AUTOR SERÁN RESPONSABLES DE NINGUNA RECLAMACIÓN, DAÑO O
OTRA RESPONSABILIDAD, YA SEA EN UNA ACCIÓN DE CONTRATO, AGRAVIO O DE OTRO MODO,
QUE SURJA DE, FUERA O EN CONEXIÓN CON EL SOFTWARE O EL USO U OTROS TRATOS
EN EL SOFTWARE.

## Créditos

- **Álex** - Desarrollador Principal - [LexDevM](https://github.com/LexDevM)

## Soporte

Este proyecto es mantenido y desarrollado activamente. Para obtener soporte o realizar preguntas, únete al [servidor de Discord](https://discord.gg/NhSyY4aqdZ).
