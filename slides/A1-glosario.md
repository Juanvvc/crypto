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

Juan Vera del Campo - <juan.vera@campusviu.es>

---
<!-- _class: cool-list -->

1. [Definiciones Generales](#3)
1. [Matemáticas](#11)

## Definiciones generales
<!-- _class: lead -->

## Los amigos de Alice

![bg right w:35em](https://www.explainxkcd.com/wiki/images/8/8d/alice_and_bob.png)

Por tradición, cuando se describen protocolos criptográficos:

- Alice y Bob son dos personas que quieren intercambiar información
- Charlie será otro participante legítimo, cuando lo necesitemos
- Eve (solo escucha) y Malloy (puede enviar mensajes) son atacantes

 Fijate: A, B, C, E y M

> Alice y Bob: https://www.explainxkcd.com/wiki/index.php/177:_Alice_and_Bob


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

## Primitivas criptográficas

- **Sin clave**: el emisor usa sólo el mensaje $m$ como argumento de la función criptográfica. Ejemplo: hash.
- **Clave simétrica**: misma clave $k$ para cifrar y descifrar un mensaje $m$. Emisor y receptor deben tener la misma clave. Ejemplo: AES, ChaCha...
- **Clave asimétrica**: claves diferentes para cifrar (pública) y descifrar (privada) un mensaje $m$. El emisor debe conoce la clave pública del receptor. Ejemplo: RSA

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

# Matemáticas
<!-- _class: lead -->

## Logaritmos y exponenciaciones

$$
\begin{aligned}
(x^a)(x^b) &= x{a+b} \\
(x^a)^b &= x^{ab} \\
\log_x (ab) &= \log_x a + \log_x b \\
a \log_x b &= \log_x (ba) \\
\end{aligned}
$$

## Aritmética modular

$$a \mod b = m$$

Significa: $a$ divivido entre $b$ da lo que sea y de resto $m$. **Lo único que interesa en la aritmética modular es el resto de la división**.

Ejemplos:

$$
\begin{aligned}
9 \mod 3 &= 0 \\
10 \mod 3 &= 1 \\
11 \mod 3 &= 2 \\
12 \mod 3 &= 0 \\
13 \mod 3 &= 1
\end{aligned}
$$

## XOR

Operación XOR de dos cadenas binarias: $a \otimes b=c$ El bit de la posición $x$ de $c$ tiene (1) el mismo bit que $a$ si el bit en $b$ es 0 (2) el bit cambiado de $a$ si el bit en $b$ es 1.

$$
\begin{aligned}
...1010...\otimes...1100...&=...0110... \\
...1010...\otimes...0101...&=...1111... \\
...1010...\otimes...0000...&=...1010... \\
...1010...\otimes...1111...&=...0101...
\end{aligned}
$$

<!-- Fíjate:

- XOR con todos 0, es el mismo mensaje
- XOR con todos 1, cambia todos los bits
- XOR es conmutativo, por eso da igual cuál interpretes como a o como b

XOR es una operación muy común en criptografía que usaremos en el tema 3, y la base de muchos algoritmos criptográficos.

Pero solo XOR no es suficiente para un algoritmo: si la clave es 0000, ¡el texto cifrado será el texto en claro! Eso es lo que nos permitió romper el sistema de los Cuentacuentos en la primera sesión

-->