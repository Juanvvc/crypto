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

---
<!-- _class: cool-list -->

1. [Definiciones Generales](#3)
1. [Matemáticas](#12)

## Definiciones generales
<!-- _class: lead -->

## Definiciones básicas

- $m$ **texto en claro**: mensaje que queremos proteger
- $c$ **mensaje cifrado**: mensaje protegido
- $e()$ y $d()$ **algoritmos de cifrado y descifrado**: convierten un texto en claro en un mensaje cifrado o al revés
- $k_1$ y $k_2$: **clave criptográfica de cifrado o descifrado**: parte secreta de los algoritmos de cifrado y descifrado

<!--
No confundas clave criptográfica y contraseña.

Contraseña: texto que un humano recuerda para entrar en algún sitio, abrir una clave criptográfica... Las contraseñas no suelen tener la suficiente seguridad para un protocolo criptográfico.

En ocasiones podremos crear (también se dice "derivar") una clave criptográfica a partir de una contraseña, aunque no siempre es buena idea porque los humanos son muy malos para escoger contraseñas.
-->

## Modelo de sistema criptográfico
<!-- _class: two-columns with-header -->

![center w:25em](https://www.tutorialspoint.com/cryptography/images/cryptosystem.jpg)

- Mensaje o texto en claro: $m$
- Cifrado: $c = e(k_1, m)$
- Descifrado: $m' = d(k_2, m)$
- Objetivo: $m=m'$

## Los amigos de Alice

![bg right w:35em](https://www.explainxkcd.com/wiki/images/8/8d/alice_and_bob.png)

Por tradición, cuando se describen protocolos criptográficos:

- Alice y Bob son dos personas que quieren intercambiar información
- Charlie será otro participante legítimo, cuando lo necesitemos
- Eve es un atacante pasivo, solo escucha
- Malloy es atacante activo, modifica mensajes

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

# Matemáticas
<!-- _class: lead -->

## Logaritmos y exponenciaciones

$$
\begin{aligned}
(x^a)(x^b) &= x^{a+b} \\
(x^a)^b &= x^{ab} \\
\log_x (ab) &= \log_x a + \log_x b \\
a \log_x b &= \log_x (b^a) \\
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

<!-- La aritmética modular produce ciclos: 012301230123

Si hacemos loquesea módulo N, el resultado estará entre 0 y N-1. Es decir, hay N posible resultados

Usaremos constantemente la aritmética modular en sistemas de cifrado asimétrico (tema 4 y siguientes)

-->


## XOR

Operación XOR de dos cadenas binarias: $a \otimes b=c$

El bit de la posición $x$ de $c$, $c_x$ tiene: (1) $a_x$ si el bit $b_x$ es 0; (2) el bit cambiado de $a_x$ si $b_x$ es 1.

También se puede entender como que $c$ es la suma binaria de $a$ y $b$, sin acarreo.

$$
\begin{aligned}
...1010...\otimes...1100...&=...0110... \\
...1010...\otimes...0101...&=...1111... \\
...1010...\otimes...0000...&=...1010... \\
...1010...\otimes...1111...&=...0101...
\end{aligned}
$$

---

Propiedades de XOR. Fíjate:

- $a \otimes 0000...0000 = a$. XOR con todos 0, es el mismo mensaje
- $a \otimes 1111...1111 = NOT\ a$. XOR con todos 1, cambia todos los bits
- $a \otimes b = b \otimes a$. XOR es conmutativo.
- $a \otimes (b \otimes c) = (a \otimes b) \otimes c$. XOR es asociativo.

XOR es una operación muy común en criptografía que usaremos en el tema 3, y la base de muchos algoritmos criptográficos: el mensaje cifrado es muchas veces el mensaje en claro $\otimes$ algo, como por ejemplo una clave.

<!--
Pero solo XOR no es suficiente para un algoritmo: si la clave es 0000, ¡el texto cifrado será el texto en claro! Eso es lo que nos permitió romper el sistema de los Cuentacuentos en la primera sesión
-->
