---
marp: true
title: Criptografía - PKI
paginate: true
footer: '[Inicio](index.html)'
headingDivider: 2
theme: marp-viu
---

<style>
    /* You can add custom style here. VSCode supports this.
    Other editor might need these custom code in
    the YAML header: section: | */
	/* section header { display: none; } */
	/* section footer { display: none; } */
</style>

# Criptografía
<!-- _class: first-slide -->

**Tema 8: Pulic Key Infrastructure**

Juan Vera del Campo

juan.vera@campusviu.es

# Criptografía híbrida
<!-- _class: lead -->

## Definición

- La criptografía simétrica permite cifrar muy rápidamente
- Los hashes permiten resumir comunicaciones muy rápidamente
- La criptografía asimétrica permite cifrar cosas sin tener que dar nuestra clave privada... pero es lenta
- Solución: [Criptografía híbrida](https://es.wikipedia.org/wiki/Criptograf%C3%ADa_h%C3%ADbrida)
    - Cifrado híbrido
    - Firma digital

## Cifrado híbrido: proceso

* Los algoritmos como RSA solo cifran **números enteros** de una longitud igual a la clave. Por ejemplo, 4096 bits.
* Podría enviarse solo mensajes de 4096 bits, pero eso no es razonable (ni rápido)
* Solución:
    - Alice se inventa una clave simétrica totalmente aleatoria
    - Alice cifra la clave simétrica usando la clave pública de Bob
    - Bob descifra usando su clave privada
    - Alice y Bob puede usar la clave simétrica para hablar entre ellos
* Diffie-Hellman es una variación de este protocolo: acuerdo de clave simétrica


## Integridad: firma digital

Podemos proteger la **integridad, no-repudio y autenticidad de un mensaje** mediante una combinación de hash y cifrado asimétrico

- Alice tiene un documento que quiere firmar
- Alice tiene también una clave pública y otra privada
- Bob conoce la clave pública de Alice

## Firma digital: proceso


* Los algoritmos como RSA solo cifran **números enteros** de una longitud igual a la clave. Por ejemplo, 4096 bits.
* Alice podría dividir el documento en bloques de 4096, pero eso no es eficiente
* Solución:
    - Alice calcula el hash de su documento de 10MB. El hash tiene 512 bytes
    - Alice cifra el hash con su clave privada
    - Cualquiera persona (eso incluye a Bob) puede conocer la clave pública de Alice y desifrar el hash
    - Si se encuentra un documento con un hash firmado por una clave pública.cualquier persona sabe que el autor del documento es el proseedor de la clave privada.

---

- Ejemplo: https://danilodellaquila.com/en/blog/how-to-verify-authenticity-of-downloaded-debian-iso-images
- Archivos: https://cdimage.debian.org/debian-cd/10.9.0-live/amd64/iso-hybrid/

![bg right w:90%](https://upload.wikimedia.org/wikipedia/commons/7/78/Private_key_signing.svg)

---

![](images/hash-debian.png)

---

(archivo anterior, *hasheado* y cifrado con clave privada de Debian)

```
-----BEGIN PGP SIGNATURE-----

iQIzBAABCAAdFiEE35ucSeqpKYQyWJ122ofoDWKUvpsFAmBfrDUACgkQ2ofoDWKU
vpsNrRAAh+bSjSbiIXcugkI9faItOdKnwM+JaqGFRrDVK68Qbc/Y5Nv4Z8KmhL/a
7nlzOrwA7dyEWFuwRiyLpoZOnlNLTXLWr8/7UJhJGt//2vJFpoHmBcXKnRFeZHfE
4XXhAq7XA/naPoTHfbuEAFVqZlnWhewBtsvwL3cn/FwyvsujCxEK9LtXl6L7ziK5
Am6LcIB6TJe3shMeUSRmvhF+d/dZ1LTYKwmm4SkCLsp0Z52dg8eRUpbq2uyQpkHM
TdtC0kE4a2u7GmDZD+VIggslfHS2tm3vE9RLfWcobjoF51bvowrPGFGm9tg+ANFt
We+sUDNv+cAUrTq9dfwoDBJueR4IRxAZoEKyl4V4mxtRsawG6w0Uzz66qrq7ROUn
isBz3sGBcNerI6uOUfP/U1mMmDMsjbaVSQCUsM9Pzpt8Y39vHgzMVwTGOkfzgUZJ
Qcf+cqyGDSpin2DjcPlUAKKtGdnnWDPVPskrgSTxzQmV8n+VgEiGRW1y46i5sh4t
dc4ETsKoz2H1JFVJY/t3kAthHCAkW/hhDX4mBM8ZPSdfNZiXNNOZGu673VwLI/bN
pN8+FgezKfD8iZHWZxHk++91Kj8sZVToVI3m8rL5nKvhEKLFNS7XDq2bmKKbtF0t
kKw8HI5Tzv55YG0P4oToeLpE6ajxxZVrCAGJvD6lMiyfftOYU2A=
=KWqY
-----END PGP SIGNATURE-----
```

# Autenticación
<!-- _class: lead -->

## Qué sabemos hacer

- Sabemos enviar mensajes con confidencialidad: criptografía simétrica
    - [Tema 3](03-simetrica.html): AES, ChaCha20
- Sabemos acordar una clave con alguien a quien no conocíamos:
    - [Tema 5](05-asimetrica.html): Diffie-Hellman
- Sabemos firmar mensajes: hash y después cifrado con criptografía asimétrica
    - [Tema 6](06-hashes.html): resumen de mensajes, hashes
    - [Tema 5](05-asimetrica.html): RSA

    
---
<!-- _class: center -->

Hemos cambiado el problema de

**compartir claves simétricas**

por el de

**compartir claves públicas (asimétricas)**

## Ataque man in the middle

![center w:28em](images/bec2.png)

<!--
Durante un ataque man in the middle, un atacante se pone en medio de las comunicaciones. Cada una de las partes establece una conexión segura con el atacante: nadie de fuera sabe qué es está diciendo, pero no estamos hablando con quien queremos hablar.

El atacante dejará pasar la mayoría de las comunicaciones, solo está interesado en participar una vez, cambiando la cuenta bancaria en la que se realiza un pago.

Fíjate: no hemos decrito ningún protocolo que nos proteja ante este tipo de ataque!

- No hemos dado autenticación: no sabemos con quién estamos hablando
- No hemos dado integridad: un atacante podría cambiar el mensaje sin que nos enteremos

(aún así, en los protocolos descritos, es muy poco probable que el atacante pueda cambiar el contenido de un mensaje por otro CON SENTIDO. Pero algunos protocolos son muy sensibles al cambio: hashes, repeticiones...)
-->

# El problema de la confianza

¿Cómo conseguimos la clave pública de los demás?

- sistema central de distribución: lista de PBKs compartida: idea original de Diffie y Hellman el 1976
- manualmente: nos guardamos una lista de PBKs propia: SSH
- certificados
    - PGP: gestión descentralizada (Web of trust)
    - PKI/X.509: gestión centralizada

---

https://jig.github.io/crypto/es/pki.html#/

## Referencias

- Ejemplos de bases de datos de certificados:
    - [OpenPGPkeyserver](http://keys.gnupg.net/)
    - [debian.org Developers LDAP Search](https://db.debian.org/)
- [IZENPE sustituirá los certificados electrónicos afectados por "ROCA", la amenaza mundial a los chips de algunas tarjetas de identificación](https://www.euskadi.eus/gobierno-vasco/-/noticia/2017/izenpe-sustituira-los-certificados-electronicos-afectados-por-roca-la-amenaza-mundial-a-los-chips-de-algunas-tarjetas-de-identificacion/)

---
<!-- _class: center -->

Continúa en: [Protocolos](09-protocolos.html)