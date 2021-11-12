---
marp: true
title: Criptografía - Glosario
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

# Criptografía
<!-- _class: first-slide -->

**Anexo: Glosario**

Juan Vera del Campo

<juan.vera@campusviu.es>


## Fuentes de información
<!-- _class: center -->

- [NIST Special Publication 800-57 Part 1, Section 3](https://doi.org/10.6028/NIST.SP.800-57pt1r5), NIST SP 800-57. El NIST es la agencia de estandarización de EEUU, y entre las cosas que estandariza también están las definiciones de seguridad. Sus estándares son sencillos de leer y empiezan un glosario que viene muy bien para introducirse en la criptografía
- [Algorithms, key size and parameters report](https://www.enisa.europa.eu/publications/algorithms-key-size-and-parameters-report-2014/), ENISA, 2014. ENISA es el equivalente al NIST para Europa. Su documento de referencia es válido para definiciones y descripciones generales

## Generales

- [*Alice*, *Bob*, *Charlie*, *Eve* y *Mallory*](https://en.wikipedia.org/wiki/Alice_and_Bob): al describir protocolos, se suelen utilizar estos nombres para los participantes. Fijate: A, B, C, E y M.
    - Alice, Bob y Charlie son participantes legítimos
    - Eve es un atacante pasivo, solo escucha
    - Malloy es atacante activo, modifica mensajes

## Servicios de seguridad principales

- **Confidencialidad**: solo el legítimo destinatario debe poder ser capaz de leer el contenido del mensaje original o de sacar cualquier información estadística.
- **Integridad**: el destinatario debe ser capaz de verificar que el contenido del mensaje original no ha sido modificado
- **Autenticidad**: el destinatario debe ser capaz de verificar que el emisor es realmente el autor del mensaje
- **No repudio**: el emisor no debe ser capaz de negar que es el autor del mensaje

## Servicios de seguridad secundarios

- **Autorización**: ¿está el interlocutor autorizado a acceder a estos datos?
- **Acuerdo de claves**: permite que un grupo de actores generen un número (pseudo) aleatorio sin que nadie externo al grupo pueda conocerlo
- **Partición de secretos**: permite repartir un secreto entre un grupo de actores, exigiendo un mínimo de actores para recomponerlas
- **PRNG** (Pseudo Random Number Generation): permite generar una secuencia aparentemente aleatoria para cualquiera que no conozca la semilla

## Modelo de sistema criptográfico
<!-- _class: two-columns with-header -->

![center w:25em](https://www.tutorialspoint.com/cryptography/images/cryptosystem.jpg)

- Mensaje o texto en claro: $m$
- Cifrado: $c = e(k_1, m)$
- Descifrado: $m' = d(k_2, m)$
- Objetivo: $m=m'$

## Primitivas criptográficas

- **Sin clave**: el emisor usa sólo el mensaje $m$ como argumento de la función criptográfica. Ejemplo: hash. No hay clave.
- **Clave simétrica**: misma clave $k=k_1=k_2$ para cifrar y descifrar un mensaje $m$. Emisor y receptor deben tener la misma clave. Ejemplo: AES, ChaCha...
- **Clave asimétrica**: claves diferentes para cifrar $k_1$ y descifrar $k_2$ un mensaje $m$. Si el emisor solo conoce $k_1$. puede cifrar pero no descifrar. Ejemplo: RSA

---

![](images/cta2296-fig-0002-m.jpg)

## Servicios de seguridad a primitivas

Objetivo|Primitiva
--|--
**confidencialidad**|cifrado simétrico, cifrado asimétrico
**integridad**|hash, firma simétrica, firma asimétrica
**autenticidad**|firma simétrica, firma asimétrica
**no repudio**|firma asimétrica
**compartir**|clave simétrica, acuerdo de clave

## Acrónimos

- [D-H](04-complejidad.html): Protocolo de acuerdo de claves Diffie-Hellman 
- [DLP](04-complejidad.html): Problema del logaritmo discreto
- [HSM](A2-rng.html): Hardware Secure Module
- [PRNG](03-simetrica.html): Pseudo Random Number Generator
- [RNG](A2-rng.html): Random Number Generator

