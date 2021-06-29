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

**Tema 8: Firma digital y Public Key Infrastructure**

Juan Vera del Campo

juan.vera@campusviu.es

## Hoy hablamos de...

- [Cifrado híbrido](#3)
- [Firma digital](#12)
- [Certificados electrónicos](#20)
- [Conclusiones y resumen](#27)

## Recordatorio

![center w:25em](https://docs.huihoo.com/globus/gt4-tutorial/images/security_concepts_asymmetric.png)

<!-- Recordatorio de cómo funciona el cifrado asimétrico:

- Todo el mundo tiene dos claves:
    - una privada, que solo conoce la persona
    - una pública, que se asume que cualquier persona puede conocer
- A partir de la pública no se puede sacar la privada
- Loq ue cifras con una lo puedes cifrar con la otra
- Envío con confidencialidad: cifra la información con la clave pública de la otra persona
    - Solo la otra persona puede descifrarla, porque solo ella tiene la clave privada
- Pero también funciona al revés: una persona  puede cifrar un mensaje con su clave privada y lanzarlo al mundo
    - Cualquier persona pueda descifrar el mensaje, ya que solo se necesita la clave pública de quien cifró. Es decir, este esquema NO OFRECE CONFIDENCIALIDAD
    - PERO: dado que el mensaje podemos descifrarlo con una clave pública específica, sabemos que solo la persona que tenga la clave privada podría haber enviado ese mensaje: estamos acercándonos a la **autenticidad**: probar quién ha enviado un mensaje
-->

# Criptografía híbrida
<!-- _class: lead -->

(Fue ejercicio del [tema 5](05-asimetrica.html))

## Definición

* La criptografía simétrica permite cifrar **muy rápidamente**
* Los hashes permiten calcular resúmenes **muy rápidamente**
* La criptografía asimétrica permite cifrar cosas sin tener que intercambiar una clave privada... **pero es lenta**
* [Criptografía híbrida](https://es.wikipedia.org/wiki/Criptograf%C3%ADa_h%C3%ADbrida)
    - **Cifrado híbrido**: enviamos clave simétrica cifrado con clave pública
    - **Firma digital**: ciframos hash con clave privada

## Cifrado híbrido: proceso

* Los algoritmos como [RSA](05-asimetrica.html) solo cifran **números enteros** de una longitud igual a la clave. Por ejemplo, 4096 bits.
* Podría enviarse solo mensajes de 4096 bits, pero eso no es razonable (ni rápido)
* Solución:
    - Alice se inventa una clave simétrica totalmente aleatoria
    - Alice cifra la clave simétrica usando la clave pública de Bob
    - Bob descifra usando su clave privada
    - Alice y Bob pueden usar la clave simétrica para hablar entre ellos
* Diffie-Hellman del [tema 5](05-asimetrica.html) es una variación de este protocolo: acuerdo de clave simétrica
* Veremos esto con más detalle con [TLS](09-protocolos.html)


## Integridad: firma digital

Podemos proteger la **integridad, no-repudio y autenticidad de un mensaje** mediante una combinación de hash y cifrado asimétrico

- Alice tiene un documento que quiere firmar
- Alice tiene también una clave pública y otra privada
- Bob conoce la clave pública de Alice

## Firma digital: proceso


* Los algoritmos como RSA solo cifran **números enteros** de una longitud igual a la clave. Por ejemplo, 4096 bits.
* Alice podría dividir el documento en bloques de 4096B, pero eso no es eficiente
* Solución: **hash cifrado con la clave privada**
    - Alice calcula el hash de su documento de 10MB. El hash tiene 512 bytes
    - Alice cifra el hash con su clave privada
    - Cualquiera persona (eso incluye a Bob) puede conocer la clave pública de Alice y descifrar el hash
    - Si se encuentra un documento con un hash firmado por una clave pública, cualquier persona puede verificar que el autor del documento es el poseedor de la clave privada.

> https://cryptobook.nakov.com/digital-signatures/rsa-signatures

---

![center w:30em](https://docs.huihoo.com/globus/gt4-tutorial/images/security_concepts_digitalsig.png)

## Ejemplo: Debian firma sus imágenes

- Ejemplo: https://danilodellaquila.com/en/blog/how-to-verify-authenticity-of-downloaded-debian-iso-images
- Archivos: https://cdimage.debian.org/debian-cd/10.9.0-live/amd64/iso-hybrid/

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

# Firma digital
<!-- _class: lead -->

(desde un punto de vista legal)

## Desde un punto de vista legal...

- Firma: artículo 3.11
    - Persona física
    - Autenticación, no repudio, integridad
    - Misma función que firma manuscrita
- Sello: artículo 3.26
    - Persona jurídica
    - Autenticación e integridad


> [Reglamento (UE) 910/2014 del Parlamento Europeo y del Consejo, de 23 de julio de 2014 relativo a la identificación electrónica y los servicios de confianza para las transacciones electrónicas en el mercado interior](https://www.boe.es/doue/2014/257/L00073-00114.pdf)

## Propiedades de firmas y sellos

- Vinculadas de forma única creador
- Permite la identificación del creador: **autenticación**
- Solo controlada por el creador
- Permite probar que el creador ha tenido acceso al documento: sabe qué está firmando
- Permite detección de alteraciones en el documento: **integridad**
- Necesita la utilización de un dispositivo informático

![bg right:30% w:100%](https://sellosdecauchonline.es/wp-content/uploads/2018/01/pro_256.jpg)

## Firma cualificada

Firma electrónica aceptada por la administración

¡No tiene por qué ser la mejor!

Caso DNI-e en España: mínima implantación por problemas de usabilidad

Se exige personarse presencialmente en una agencia de certificación

![bg left:40% w:80%](https://cdn.computerhoy.com/sites/navi.axelspringer.es/public/styles/1200/public/media/image/2014/08/55497-como-activar-certificados-tu-dni.jpg)

## Usos

La administración solo admite firmas/sellos electrónicos cualificados

En Europa, asimilables a firma manuscrita o sello de entidad

ojo: firmas no cualificadas **podrían tener también efectos jurídicos**

## Un poco de historia: ROCA

The ROCA factorization attack could potentially allow a remote attacker to reverse-calculate a private encryption key just by having a target’s public key

Algunas tarjetas utilizaban una implementación no segura

Se tuvieron que retirar todas y [no aceptar firma electrónica durante ese periodo](https://elpais.com/politica/2017/11/09/actualidad/1510217634_470836.html)

![bg right:50% w:100%](https://crocs.fi.muni.cz/_media/public/papers/roca_impact.png?w=400&tok=973b60)

> https://crocs.fi.muni.cz/public/papers/rsa_ccs17

---

Del anuncio de la vulnerabilidad (https://crocs.fi.muni.cz/public/papers/rsa_ccs17): 

The time complexity and cost for the selected key lengths (Intel E5-2650 v3@3GHz Q2/2014):

- 512 bit RSA keys - 2 CPU hours (the cost of $0.06);
- 1024 bit RSA keys – 97 CPU days (the cost of $40-$80);
- 2048 bit RSA keys – 140.8 CPU years, (the cost of $20,000 - $40,000).

## Delegación de firma

- Sellos “por poderes”: una persona firma en nombre de una empresa
- Sistema “Cl@ve”: la administración firma por nosotros

## Certificados electrónicos

- Declaración electrónica que vincula los datos de validación de un sello con una persona jurídica y confirma el nombre de esa persona
- Declaración que permite autenticar un sitio web y vincula el sitio web con la persona física o jurídica a quien se ha expedido el certificado
- La norma exige que se gestione el ciclo de vida de un certificado. Revocaciones, cambios de estado...

# Certificados electrónicos
<!-- _class: lead -->

(desde un punto de vista técnico)

<!-- ¿Cómo implementamos técnicamente todo lo que acabamos de describir? -->

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

## El problema de la confianza

¿Cómo conseguimos la clave pública de los demás?

- sistema central de distribución: lista de PBKs compartida: idea original de Diffie y Hellman el 1976
- manualmente: nos guardamos una lista de PBKs propia: SSH
- certificados
    - PGP: gestión descentralizada (Web of trust)
    - PKI/X.509: gestión centralizada

---

Para el resto de la sesión usaremos las transparencias de cursos pasados, aún no adaptadas al curso actual:

https://jig.github.io/crypto/es/pki.html#/

# Conclusiones
<!-- _class: lead -->

## Referencias

- Ejemplos de bases de datos de certificados:
    - [OpenPGPkeyserver](http://keys.gnupg.net/)
    - [debian.org Developers LDAP Search](https://db.debian.org/)
- [IZENPE sustituirá los certificados electrónicos afectados por "ROCA", la amenaza mundial a los chips de algunas tarjetas de identificación](https://www.euskadi.eus/gobierno-vasco/-/noticia/2017/izenpe-sustituira-los-certificados-electronicos-afectados-por-roca-la-amenaza-mundial-a-los-chips-de-algunas-tarjetas-de-identificacion/)
- [Diferencias entre firma digital, electronica, digitalizada y certificado digital. Autónomos y Pymes](https://www.youtube.com/watch?v=-_SARWc3ots)

---
<!-- _class: center -->

Anexo recomendable: [Criptografía ofensiva](A3-ofensiva.html)

Continúa en: [Protocolos](09-protocolos.html)
