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

# Criptografía y teoría de códigos
<!-- _class: first-slide -->

**Presentación**

Juan Vera del Campo - <juan.vera@professor.universidadviu.com>


## Temario
<!-- _class: cool-list -->

1. [Conceptos básicos](01-conceptos.html)
1. [Criptografía clásica](02-historia.html)
1. [Criptografía de clave simétrica: AES y ChaCha](03-simetrica.html)
    - Anexo: [RNG y HSM](A2-rng.html)
1. [Teoría complejidad y acuerdo Diffie-Hellman](04-complejidad.html)
1. [Criptografía de clave pública: RSA](05-asimetrica.html)

---
<!-- _class: cool-list -->

<style scoped>
    ol { counter-reset: li 5; }
</style>

6. [Funciones de Hash](06-hashes.html)
    - Anexo: [Blockchain](A3-blockchain.html)
1. [TLS y Public Key Infrastructure](07-pki.html)
1. [Ransomware](08-ransomware.html)
1. [Esteganografía](09-esteganografia.html)
1. [Criptografía post-cuántica](10-postcuantica.html)

# Presentación
<!-- _class: lead -->

## Sobre mí

![bg left:45%](images/juanvi.jpg)

Dr. Juan Vera (Juanvi)

<juan.vera@professor.universidadviu.com>

Intereses:

- DFIR: [*Digital Forensics and Incident Response*](https://en.wikipedia.org/wiki/Computer_security_incident_management)
- Miembro del Cyber Incident Response Team de [Valeo](https://es.wikipedia.org/wiki/Valeo)
- Cualquier cosa que vuele

## Objetivos

- Introducción a la criptografía moderna, para qué se usa y por qué es tan complicada
  - Confidencialidad
  - Autenticación
  - Firma digital
- Que te convenzas de que la mejor estrategia para evitar errores de seguridad son los protocolos y algoritmos abiertos
- Descubrir otros usos de la criptografía: ransomware, bitcoin...

## Intrucciones de uso de las transparencias
<!-- _class: smallest-font -->

Versión más actualizada:

- Acceso directo HTML: <http://juanvvc.github.io/crypto>
    - Pulsa `p` para ver las notas de presentación
    - El enlace "Inicio" lleva a esta presentación con el índice global de contenidos
    - Puedes "Imprimir a PDF" usando Chrome para tener las transparencias en PDF
- Código Markdown: <https://github.com/juanvvc/crypto>

Durante el estudio personal es muy recomendable seguir los enlaces que aparecen en las transparencias para completar el tema.

[![Licencia de Creative Commons](https://i.creativecommons.org/l/by/4.0/88x31.png)](http://creativecommons.org/licenses/by/4.0/) Esta obra esta sujeta a una licencia de [Atribución 4.0 Internacional de Creative Commons](http://creativecommons.org/licenses/by/4.0/)

![bg right:40% w:100%](images/guia-transparencias.png)

<!-- 
Esto es un ejemplo de notas de profesor. Aquí habrá información adicional, aclaraciones, referencias o explicaciones más largas de los conceptos de la transparencia
-->

## Instrucciones de uso de las actividades
<!-- _class: with-warning smaller-font -->

Los ejercicios son notebook de Google Colab:

1. Después de los temas 2, 3 y 5 se incluirá el enlace a Google Colab en la zona de Actividades de la asignatura
1. Comandos básicos:
    - INTRO: edita línea actual
    - SHIFT+INTRO: ejecuta línea actual
1. Las actividades deben resolverse individualmente
1. Aunque haya código, no es necesario saber programar: son preguntas de texto libre

**Presenta las actividades como PDF: imprimir a PDF**

<!-- Las actividades refuerzan el contenido de las clases e incluyen información adicional -->

## Evaluación
<!-- _class: smaller-font -->

- Puntuación. Dos partes:
    - 50% examen
    - 50% actividades
- Es necesario superar con nota media de 5 **cada parte por separado**
- Son tres actividades en total, se recomienda realizarlas después de los temas 2, 3 y 5
    - No es  necesario superar las actividades individuales, solo que **la media de todos las actividades sea superior a 5**
    - Las actividades no presentados se puntúan como 0
    - Se pueden presentar las actividades hasta el día del examen correspondiente
- En segunda convocatoria, se mantiene la nota de aquella parte que fue superada en primera convocatoria

## Conocimientos recomendables

- Álgebra básica, probabilidad
- Conocimientos básicos de programación: ejemplos en Python
- Conocimientos básicos de redes: cómo funciona la WWW.

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

# ¡Gracias!
<!-- _class: last-slide -->
