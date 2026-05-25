---
marp: true
title: Criptografía - Índice
paginate: true
footer: '[Inicio](index.html)'
headingDivider: 2
theme: marp-viu
---

<style>
    /* You can add custom style here. VSCode supports this.
    Other editor might need these custom code in
    the YAML header: section: | */
</style>

# Criptografía y autenticación
<!-- _class: first-slide -->

**Presentación**

Juan Vera del Campo - <juan.vera@professor.universidadviu.com>


## Temario
<!-- _class: cool-list smaller-font -->

1. [Cifrado](02-cifrado.html)
1. *Protocolos*
   - [PKI](../07-pki.html)
   - [TLS](../A2-protocolos.html)
1. [Firma digital](../A4-firmadigital.html)
1. [Sistemas de autenticación (2 sesiones)](../11-autenticacion.html)
1. [Anonimato](../12-anonimato.html)
1. [Business Email Compromise](../13-bec.html)

# Presentación
<!-- _class: lead -->

## Sobre mí

![bg left:45%](../images/juanvi.jpg)

Dr. Juan Vera (Juanvi)

<juan.vera@professor.universidadviu.com>

Intereses:

- DFIR: [*Digital Forensics and Incident Response*](https://en.wikipedia.org/wiki/Computer_security_incident_management)
- Miembro del Cyber Incident Response Team de [Valeo](https://es.wikipedia.org/wiki/Valeo)
- Cualquier cosa que vuele

## Objetivos

- Criptografía moderna
  - Para qué se usa y por qué es tan complicada
  - Firma digital
  - Sistemas de autenticación
- Que te convenzas de que la mejor estrategia para evitar errores de seguridad son los protocolos y algoritmos abiertos
- Descubrir otros usos de la criptografía: ransomware, bitcoin...

## Intrucciones de uso de las transparencias

- Acceso directo HTML: <http://juanvvc.github.io/crypto/crypto2>
    - Pulsa `p` para notas de presentación
    - Puedes "Imprimir a PDF" las presentaciones si usas Chrome o Edge, pero no en Firefox o Safari
- Código Markdown: <https://github.com/juanvvc/crypto>

Es muy recomendable seguir los enlaces que aparecen en la presentación

[![Licencia de Creative Commons](https://i.creativecommons.org/l/by/4.0/88x31.png)](http://creativecommons.org/licenses/by/4.0/)

![bg right:40% w:100%](../images/guia-transparencias.png)

<!-- 
Esto es un ejemplo de notas de profesor. Aquí habrá información adicional, aclaraciones, referencias o explicaciones más largas de los conceptos de la transparencia
-->

## Instrucciones de las actividades
<!-- _class: with-info -->

1. Después de las algunas sesiones se incluirán enlaces a Google Colab en la zona de Actividades de la asignatura
1. Los ejercicios son notebook de Google Colab. Comandos básicos:
    - INTRO: edita línea actual
    - SHIFT+INTRO: ejecuta línea actual
1. Las actividades deben resolverse individualmente
1. No es necesario saber programar: son preguntas de texto libre
1. Entregad en un documento separado en formato PDF que sólo incluya el texto de las preguntas y su respuesta

Las actividades incluyen información adicional que no está en las clases

## Evaluación

- Puntuación. Dos partes:
    - 50% examen
    - 50% actividades
- Es necesario superar con nota media de 5 **cada parte por separado**
- Actividades:
    - No es  necesario superar las actividades individuales, solo que **la media de todos las actividades sea superior a 5**
    - Las actividades no presentados se puntúan como 0
    - Se pueden presentar las actividades hasta el día del examen correspondiente
- En segunda convocatoria, se mantiene la nota de aquella parte que fue superada en primera convocatoria

## Bibliografía
<!-- _class: smaller-font -->

- Del profesor: <https://juanvvc.github.io/crypto/>
- "[*A Graduate Course in Applied Cryptography*](http://toc.cryptobook.us/)".  Dan Boneh   and   Victor Shoup. Con vídeos en:
    - <https://crypto.stanford.edu/~dabo/courses/OnlineCrypto/>
    - https://www.coursera.org/learn/crypto
    - https://www.coursera.org/learn/crypto2
    - https://www.coursera.org/learn/cryptography
- "[*The Joy of Cryptography*](https://joyofcryptography.com/)" de Mike Rosulek, 2021
- "[*A Course in Cryptography*](https://www.cs.cornell.edu/courses/cs4830/2010fa/lecnotes.pdf)" Rafael Pass & Abhi Shelat. Más ligero que el anterior.
- "[*Handbook of Applied Cryptography*](http://cacr.uwaterloo.ca/hac/)" Alfred J. Menezes. Un clásico para conceptos fundamentales.
- "A Course in Cryptography" Heiko Knospe.
- "Criptografía Ofensiva. Atacando y defendiendo organizaciones". Dr. Alfonso Muñoz.

# Conceptos básicos
<!-- _class: lead -->

## El problema que queremos resolver

Firma digital de un contrato entre dos empresas

- El contrato tiene que ser secreto para cualquiera que no participe en la comunicación
- Las empresas tienen que estar seguras de con quién están hablando
- Ninguna de las dos empresas puede cambiar unilateralmente el contrato
- Ninguna de las empresas debe poder decir que no firmó el contrato

![bg right:40%](../images/generic/binding-contract-948442_1280.jpg)

<!--
Fondo: https://pixabay.com/photos/binding-contract-contract-secure-948442/ Uso comercial libre
-->

## Servicios de seguridad

- **Confidencialidad**: solo el legítimo destinatario debe poder ser capaz de leer el contenido del contrato o cualquier información asociada.
- **Integridad**: el destinatario debe ser capaz de verificar que el contenido del contrato no ha sido modificado por el camino... ni en el futuro
- **Autenticidad**: el destinatario debe ser capaz de verificar que el emisor es realmente el autor del contrato
- **No repudio**: nadie puede decir que ese no es el contrato que ha firmado

## Protocolos criptográficos

La criptografía actual se basa en **composición** de técnicas primitivas:

- Composición de **operaciones matemáticas** que crean "**puertas criptográficas**" (*cryptographic gates*).
- Composición de puertas que crean **algoritmos**.
- Composición de algoritmos que crean **protocolos de seguridad**.

La composición es compleja y todo debe funcionar como un reloj.


## Gestión de claves

![bg left:33% h:100%](../images/conceptos/Lea_Kissner.jpeg)

*La criptografía es una herramienta para convertir un montón de problemas diferentes en un problema de gestión de claves*

Lea Kissner, antigua ingeniera principal de seguridad de Google

- **Contraseña**: palabra que utilizamos para entrar en un sistema. "Sesamo"
- **Clave criptográfica**: conjunto de números que dan seguridad a un sistema: "82198329382371291821201"

<!--
Si la clave es lo único que tiene que ser secreto, tenemos que protegerla a toda costa.

En este curso no estudiaremos cómo proteger las claves, pero tened en cuenta que, al ser la pieza central de la seguridad de un sistema, es necesario que los usuarios de criptografía dispongan de algún modo de gestión segura de claves criptogrtáficas

Una contraseña no es lo mismo que una clave criptográfica. Las contraseñas suelen ser mucho más inseguras que una clave (a veces no son aleatorias o están pensadas para que las pueda recordar un humano) A veces las contraseñas serán el primer paso para entrar en un sistema seguro, pero **no son buenas claves criptográficas**

En muchas ocasiones un sistema se romperá no por que la criptopgrafía sea débil, sino porque incluye un paso de control con contraseña que es habitualmente la parte más débil de un protocolo.
-->

# ¡Gracias!
<!-- _class: last-slide -->
