# Python-Email-Keylogger

![Python 3.x](https://img.shields.io/badge/Python-3.x-blue.svg)
![Offensive Security](https://img.shields.io/badge/Category-Offensive_Security-red.svg)
![Post-Exploitation](https://img.shields.io/badge/Attack-Post--Exploitation-orange.svg)
![OS: Cross-platform](https://img.shields.io/badge/OS-Cross--platform-informational.svg) ![License](https://img.shields.io/badge/License-MIT-green.svg) ---

### 📄 Descripción General del Proyecto

Este repositorio presenta un **Keylogger básico desarrollado en Python3**, diseñado con fines puramente **educativos y demostrativos**. Su función principal es capturar las pulsaciones de teclas en un sistema comprometido y exfiltrar (`enviar`) estos registros a una dirección de correo electrónico predefinida a intervalos regulares.

El objetivo de este proyecto es **demostrar de forma clara y concisa** cómo funcionan los keyloggers a nivel de software, las librerías de Python involucradas en la intercepción de eventos de teclado y cómo se puede implementar un mecanismo de reporte para exfiltrar datos. Es una herramienta fundamental para comprender las tácticas de persistencia y recolección de información en un escenario de post-explotación.

### 💡 ¿Cómo Funciona un Keylogger?

Imagina que cada tecla que presionas en tu teclado es un susurro al sistema operativo. Un keylogger es como un "oído" sigiloso que intercepta esos susurros antes de que lleguen a su destino final.

1.  **Intercepción de Eventos:** En lugar de que el sistema operativo procese directamente las pulsaciones, el keylogger se "engancha" al flujo de eventos del teclado. Cada vez que una tecla es presionada (o liberada), el keylogger recibe una notificación.
2.  **Registro (`Logging`):** El keylogger no solo escucha, sino que toma nota. Guarda todas las pulsaciones de teclas en una cadena de texto (un "log"). Esto incluye letras, números, símbolos y también teclas especiales como `ENTER`, `SPACE`, `SHIFT`, etc.
3.  **Exfiltración (`Reporting`):** De nada sirve registrar las teclas si no se pueden obtener. Nuestro keylogger tiene un mecanismo para "sacar" esos logs del sistema comprometido. En este caso, utiliza el correo electrónico como canal de exfiltración, enviando los logs a una dirección de correo del atacante a intervalos regulares. Esto permite al atacante obtener la información remotamente.
4.  **Persistencia (Concepto Opcional/Futuro):** Un keylogger en un entorno real buscaría también persistencia, es decir, asegurarse de que se inicie automáticamente cada vez que el sistema se reinicie. Este script es básico y no implementa persistencia directamente, lo cual es importante para su uso ético en laboratorio.

### ✨ Características y Funcionalidades de este Keylogger

* **Captura de Pulsaciones de Tecla:** Registra tanto caracteres normales como teclas especiales (Espacio, Enter, Shift, Ctrl, Alt, Backspace).
* **Reporte por Correo Electrónico:** Envía los logs de las pulsaciones de teclas a una dirección de correo predefinida.
* **Reporte Temporizado:** Utiliza hilos (`threading.Timer`) para enviar los informes de forma periódica, sin bloquear el proceso principal.
* **Mensaje de Inicio:** Envía un primer correo para indicar que el keylogger se ha activado.
* **Manejo de Cierre:** Permite detener el keylogger limpiamente con `Ctrl+C`.

### 🚀 Tecnologías y Herramientas Utilizadas

* **Lenguaje de Programación:** Python 3.x
* **Librerías Python:**
    * `pynput`: Fundamental para la captura de eventos de teclado en diferentes sistemas operativos.
    * `threading`: Para ejecutar el reporte de logs en un hilo separado (Timer), sin interrumpir la captura de teclas.
    * `smtplib`: Para el envío de correos electrónicos a través del protocolo SMTP.
    * `email.mime.text.MIMEText`: Para construir el formato del mensaje de correo electrónico.
    * `os`, `sys`, `signal`: Para operaciones del sistema, manejo de la salida y señales.

### 🛠️ Pre-requisitos y Configuración

1.  **Máquina Objetivo:**
    * Un sistema con Python 3.x instalado (Windows, Linux, macOS son compatibles con `pynput`).
    * **Permisos:** Puede requerir permisos especiales dependiendo del sistema operativo (ej., en Linux, quizás permisos para escuchar eventos de teclado a bajo nivel; en macOS, acceso a grabaciones de pantalla en la configuración de privacidad).
2.  **Máquina Atacante (para recibir emails):**
    * No requiere una máquina separada para esto, ya que el reporte es por email.
3.  **Correo Electrónico para Envío:**
    * Necesitarás una cuenta de Gmail (o similar) configurada para permitir el envío de correos desde aplicaciones externas (generando una **contraseña de aplicación**).
    * **CRÍTICO: No uses la contraseña principal de tu cuenta de correo.**
        * **Para Gmail:** Debes activar la verificación en dos pasos y luego generar una "contraseña de aplicación" desde la configuración de seguridad de tu cuenta de Google. Esta contraseña generada es la que debes colocar en el código Python, NO tu contraseña habitual.

#### **Instalación de Librerías Python:**

```bash
pip3 install pynput
# La librería 'requests' no se usa en este script, pero la menciono por si acaso de otros proyectos
# pip3 install requests

by [Zm0kSec]
