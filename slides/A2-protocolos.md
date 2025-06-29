---
marp: true
title: Criptografía - Protocolo TLS
author: Juan Vera
keywords: criptografía,protocolos,tls
paginate: true
footer: '[Inicio](index.html)'
headingDivider: 2
theme: marp-viu
transition: fade
---

<style>
    /* You can add custom style here. VSCode supports this.
    Other editor might need these custom code in
    the YAML header: section: | */
	/* section header { display: none; } */
	/* section footer { display: none; } */
</style>

# Protocolo TLS
<!-- _class: first-slide -->

Juan Vera del Campo - <juan.vera@professor.universidadviu.com>

# Transport Layer Security
<!-- _class: lead -->

## Transport Layer Security

Seguridad de la capa de transporte (en inglés: *Transport Layer Security* o TLS) y su antecesor Secure Sockets Layer (*Secure Socket Layer*) son protocolos criptográficos que proporcionan:
- **Autenticación** mediante certificados. Es decir: criptografía asimétrica.
- Gestión de claves. Es decir: protocolo Diffie-Hellman
- **Confidencialidad** de las comunicaciones. Es decir: criptografía simétrica

![bg right:30% w:80%](images/pki/tls-versiones.png)


>  [The Transport Layer Security (TLS) Protocol Version 1.3, RFC8446 2018](https://tools.ietf.org/html/rfc8446)

<!--
El antecesar de TLS es SSL, que era igual en la práctica pero con colecciones de cifrado y gestión ligeramente diferente. Aunque el protocolo que usamos es TLS, aún es común referirnos a este protocolo como TLS.
-->

---
<!-- _class: with-warning -->

**TLS es el protocolo utilizado en cualquier conexión a Internet**

![w:35em](images/pki/tls-candado.png)

- La "s" de "https" es para pedir que se use TLS
- El "candado" de los navegadores indica que se está usando TLS
- Si pulsas en el escudo verás las propiedades de esta conexión TLS

En la web actual, deberemos desconfiar de cualquier página o servicio que no tenga candado. Es decir, que no use TLS

---

![](https://hpbn.co/assets/diagrams/9873c7441be06e0b53a006aac442696c.svg)

> https://hpbn.co/transport-layer-security-tls/

<!--
TLS se pone entre TCP y HTTP, como una capa adicional: ni TCP ni HTTP "saben" que está ahí.

Es decir, las peticiones son peticiones HTTP estándar, que viajan sobre TCP estándar. Pero entre medias estas peticiones crean una sesión inicial y se cifran.
-->

## Propiedades de seguridad

Funcionalmente equivalente a un socket TCP aportándole:

- Autenticidad: Clave pública
    - autenticación mutua: cliente y servidor tienen certificado
    - autenticación de servidor: solo el servidor tiene un certificado
- integridad: HMAC/MAC
- confidencialidad:
    - acuerdo de claves
    - cifrado simétrico

<!--
A veces no da tiempo a ver qué es MAC/HMAC en este curso: es un hash cifrado con una clave simétrica que asegura que un mensaje no ha cambiado durante la transmisión. La idea es similar a una firma digital: cifrado (con clave simétrica) del hash del mensaje. Pero las implicaciones tanto legales como operativas son diferentes: no garantiza autenticidad pero es mucho más rápido.
-->

## Fases de establecimiento de una sesión TLS

1. **Autenticación** mútua (raro) o solo de servidor (habitual) mediante intercambio de certificados
1. **Acuerdo** de los parámetros de seguridad y protocolos que se usarán en la comunicación
1. **Establecimiento de clave compartida** con criptografía asimétrica. Opciones:
    - Diffie-Hellman
    - Encapsulación de clave (RSA, DSA)
1. **Cifrado simétrico** de la comunicación AES/ChaCha con la clave establecida

Veremos estos pasos uno a uno

## Fases en TLSv2 y TLSv3

![center](images/pki/tlsv2v3.png)

> https://www.a10networks.com/glossary/key-differences-between-tls-1-2-and-tls-1-3/
> https://www.cloudflare.com/learning/ssl/why-use-tls-1.3/

## (1) Autenticación

TLS tiene dos modos para garantizar la autenticación de las partes:

- **Autenticación mútua**: cliente y servidor tienen certificado. El cliente sabe que está hablando con su banco, y el banco que está hablando con su cliente.
- **Autenticación de servidor**: solo el servidor tiene un certificado. El cliente sabe que está hablando con el banco, pero **el banco no sabe nada del cliente**

Utilizar TLS solo con autenticación de servidor es lo más habitual en Internet

## Autenticación: gestión de la identidad

- **Servidor**: certificdo y clave privada
- **Cliente**:
    - sin autenticación de cliente: anónimo, usuario y contraseña, etc.
    - con autenticación de cliente: fichero PKCS #12, o accediendo a un HSM en forma de SmartCard o de token USB vía librería PKCS #11

![bg left:50%](images/auth/identities.png)

---

Lo más habitual en Internet es utilizar TLS con solo autenticación de servidor

**Las páginas web tienen que autenticar al visitante**

- Usuario y contraseñas
- Sistemas Cl@ve, firma electrónica en momentos puntuales, 2FA...

Más información en el [la sesión de autenticación](11-autenticacion.html)



## (2) Acuerdos de los parámetros de la conexión

Los clientes cuando se conectan acuerdan utilizar la versión más moderna que soporten ambos extremos:

- SSL 3.0: obsoleto
- TLS 1.0/1.1: fin de vida en 2020
- TLS 1.2: versión recomendada
- TLS 1.3: publicada en 2018; fuerza a utilizar DHE/ECDHE para acuerdo de claves

<!--
Poder escoger los parámetros de conexión es un arma de doble filo: el pasado, algunos atacantes forzaban a los clientes a utilizar versiones antiguas y débiles de los protocolos

Los servidores pueden exigir a sus clientes utilizar solo versiones actualizadas de todos los protocolos
-->

---

![center w:20em](https://upload.wikimedia.org/wikipedia/commons/d/d3/Full_TLS_1.2_Handshake.svg)

> Fuente: wikipedia
> Detalles de los datos intercambiados, byte a byte: https://tls12.xargs.org/

## Cipher Suites

Prococolos que describen las conexión:

Se identifican (aprox) con la cadena `KEA_SIGN_WITH_CIPHER_HASH`

Componente|Contenido
--|--
KEA|Algoritmo de acuerdo de claves
SIGN|Algoritmo de firma
CIPHER|Algoritmo de cifrado simétrico
HASH|Algoritmo de hash



## Algoritmos en TLS v1.3

los siguientes cipher-suites son de obligada implementación (*MUST*):

- `{DHE|ECDHE}_ECDSA_WITH_AES_128_GCM_SHA256`
- `{DHE|ECDHE}_RSA_WITH_AES_128_GCM_SHA256`

y se recomienda la implementación de estos (*SHOULD*):

- `{DHE|ECDHE}_ECDSA_WITH_AES_256_GCM_SHA384`
- `{DHE|ECDHE}_ECDSA_WITH_CHACHA20_POLY1305_SHA256`
- `{DHE|ECDHE}_RSA_WITH_AES_256_GCM_SHA384`
- `{DHE|ECDHE}_RSA_WITH_CHACHA20_POLY1305_SHA256`

---

- claves de sesión establecidas por acuerdo de claves (PFS)
- DH-2048, ECDH-256, X25519: longitudes mínimas para acuerdo de claves
- RSA-2048, ECDSA-256, EdDSA25519: longitudes mínimas para firma
- desaparecen DSA, SHA-1, SHA-224, 3DES


---

![center w:30em](images/pki/tls-example1.png)


## (3) Cifrado: establecimiento de la clave de cifrado

Una vez que hemos establecido la identidad de la otra parte, acordamos qué clave AES vamos a utilizar. Opciones:

1. [Elliptic Curve Diffie-Hellman](https://en.wikipedia.org/wiki/Elliptic-curve_Diffie%E2%80%93Hellman), como hemos visto en temas anteriores
1. [Protocolo de encapsulación de clave](https://en.wikipedia.org/wiki/Key_encapsulation_mechanism):
    - "Escojo la clave de cifrado y la envío a la otra parte cifrada con su clave pública"

![bg right:50% w:90%](images/asimetrica/keyencapsulation.png)

<!--
Imagen: https://blog.cloudflare.com/content/images/2022/10/image3.png
-->

## Inicialización (caso general, PFS)

Usando Diffie-Hellman sobre Curvas Elípticas (ECDH) genera el *MasterSecret*, del que se derivan 4 claves y 2 vectores de inicialización (IV):

- clave de cifrado de cliente a servidor (y viceversa)
- IV, para el cifrado de cliente a servidor (y viceversa)
- clave HMAC de cliente a servidor (y viceversa)

Notas:

- PFS: Perfect Forward Secrecy
- Ephemeral ECDH: se ejecuta ECDH cada pocos minutos para cambiar la clave periódicamente

<!--

Seguridad "a futuro": Perfect Forward Secrecy

Un ataque que revele una clave privada implica que se debe cambiar la clave privada

pero si no se usa _DHE_ ó _ECDHE_ el revelado de la clave privada permite el descifrado de tráfico pasado

-->


## Inicialización (caso sin PFS)

Si no se usa ECDH, el cliente debe enviar el MasterSecret al servidor cifrándolo con la clave del servidor:

MasterSecret: PBKservidor(MasterSecretcliente)

En este caso (no-PFS) una revelación de la clave privada del servidor en cualquier momento, permite descifrar el tráfico futuro y también el tráfico pasado

## Ejemplo

```
$ curl -v https://www.google.com -o salida

* Connected to www.google.com (142.250.200.100) port 443 (#0)
* ALPN, offering h2
* ALPN, offering http/1.1
* successfully set certificate verify locations:
*  CAfile: /etc/ssl/certs/ca-certificates.crt
*  CApath: /etc/ssl/certs
} [5 bytes data]
* TLSv1.3 (OUT), TLS handshake, Client hello (1):
} [512 bytes data]
* TLSv1.3 (IN), TLS handshake, Server hello (2):
{ [122 bytes data]
* TLSv1.3 (IN), TLS handshake, Encrypted Extensions (8):
{ [15 bytes data]
* TLSv1.3 (IN), TLS handshake, Certificate (11):
{ [3813 bytes data]
* TLSv1.3 (IN), TLS handshake, CERT verify (15):
{ [80 bytes data]
* TLSv1.3 (IN), TLS handshake, Finished (20):
{ [52 bytes data]
* TLSv1.3 (OUT), TLS change cipher, Change cipher spec (1):
} [1 bytes data]
* TLSv1.3 (OUT), TLS handshake, Finished (20):
} [52 bytes data]
* SSL connection using TLSv1.3 / TLS_AES_256_GCM_SHA384
* ALPN, server accepted to use h2
* Server certificate:
*  subject: CN=www.google.com
*  start date: May 19 08:43:37 2025 GMT
*  expire date: Aug 11 08:43:36 2025 GMT
*  subjectAltName: host "www.google.com" matched cert's "www.google.com"
*  issuer: C=US; O=Google Trust Services; CN=WR2
*  SSL certificate verify ok.
* Using HTTP2, server supports multi-use
```

## Transporte

los datos se fragmentan en bloques de hasta 16 kB

cada bloque está protegido por algoritmos simétricos acordados durante la inicialización y las claves y IV's derivados de la MasterKey...

y por un número de secuencia


# Seguridad

- Algoritmos: TLS hasta la versión v1.2 permite configurar algoritmos (cipher suites) que actualmente son obsoletos
- Protocolo: versiones antiguas, mecanismos de renegociación (para bajar a versiones antiguas)…
- Implementaciones: limitación de parámetros, uso de PRNG de baja calidad
- Condiciones de uso: gestión del servidor (o el cliente)


## Seguridad: Algoritmos

TLS hasta la versión v1.2 permite configurar algoritmos obsoletos (v1.3 lo impide pero su publicación es muy reciente como para que todos los componentes lo hayan adoptado)

TLS hasta la versión v1.2 renegocia el mejor protocolo entre cliente y servidor. Un cliente "antiguo" puede forzar a usar o bien un cipher suite obsoleto o bien no dejarlo conectar

## Seguridad: Algoritmos (TLS v1.3)

En la versión v1.3 se han eliminado cualquier algoritmo que resulte en un cipher-suite inseguro, facilitando la configuración segura de los servidores

Eliminados NULL, ANON, sin acuerdo de claves, con acuerdo de claves no efímero, SHA-1, 3DES, DSS (DSA)

Se debe vigilar que RSA y DHE sean de 2048 bit o más, y que ECDSA y ECDH usen P-256, P-384, P-521, Curve25519 ó Curve448


## Seguridad: condiciones de uso

- Las claves privadas está protegidas directamente por el S.O.
- Los certificados deben recrearse frecuentemente:
    - Automatización del proceso
- Let's Encrypt para proteger nuestras webs

## Let's encrypt

[![center](images/pki/letsencrypt.png)](https://letsencrypt.org/)

Hasta 2014, los certificados de las webs tenía que comprarse a VeriSign o similares.

En 2014, la EFF democratizó la seguridad en Internet: todos los servidores públicos deben poder usar HTTPS sin tener que pagar a nadie

"Desventajas":

- Solo válido para páginas web públicas, no es válido ni para certificados de personas, ni para sistemas de la intranet que no sean públicos
- hay que renovarlos cada 3 meses, aunque el proceso puede automatizarse: <https://certbot.eff.org/instructions>

---

Paso 1 y 2:

- Le envías a Let's Encrypt la clave pública de un dominio
- Let's encrypt te pide que pongas un *nonce* en un lugar determinado por ellos de tu web, y que lo firmes que la clave privada del dominio

![center](images/pki/letsencrypt-nonce.png)

> https://letsencrypt.org/how-it-works/


---

Paso 3:

- Let's Encrypt visita la página que espera encontrar. Si el *nonce* y la firma son correcta, emite el certificado para esa web

![center](images/pki/letsencrypt-challenge.png)

> https://letsencrypt.org/how-it-works/

# Prácticas
<!-- _class: lead -->

## Creación de una CA

![center](https://upload.wikimedia.org/wikipedia/commons/d/d1/Chain_of_trust.svg)

> https://es.wikipedia.org/wiki/Cadena_de_confianza

<!--
La clave privada de una TTP es muy delicada: se protege en grandes edificios con una enorme seguridad física, en PCs desconectados de Internet y dentro de cajas fuertes.

Por eso los certificados de usuarios no suelen estar firmados por una TTP final (llamada "Root CA") sino por otras terceras partes intermedias con capacidad para firmas certificados de usuarios. El certificados de estos intermediarios sí que está firmado por la Autoridad raíz
-->


## Creación de CA

Simplificado de https://jamielinux.com/docs/openssl-certificate-authority/create-the-root-pair.html

```bash
mkdir -p private
mkdir -p certs
# Genera clave privada para la CA
openssl genrsa -aes256 -out private/ca.key.pem 4096
# Genera certificado público para la CA
openssl req -key private/ca.key.pem -new -x509 -days 7300 -sha256 -out certs/ca.cert.pem
# Muestra el certificado por pantalla
openssl x509 -noout -text -in certs/ca.cert.pem
```

## Creación de nuevo certificado de usuario

Esto lo ejecuta cualquier en su casa:

```bash
# Genera par de claves para www.example.com
openssl genrsa -out private/www.example.com.key.pem 2048
# Genera par de claves para www.example.com, protegido por contraseña
# openssl genrsa -aes256 -out private/www.example.com.key.pem 2048

# Genera petición de firmado. Esta es la petición que le enviamos a la CA
openssl req -key private/www.example.com.key.pem -new -sha256 -out csr/www.example.com.csr.pem
```

- Guardamos: `private/www.example.com.key.pem` Este arhchivo incluye nuestras claves pública y privada
- Enviamos a CA: `csr/www.example.com.csr.pem` Este archivo incluye nuestra clave pública

---

Una CA obtiene el archivo `csr`, comprueba nuestra identidad de alguna manera (presencial, DNI, DNS...) y ejecuta:

```bash
# La CA firma la petición y devuelve el certificado
openssl x509 -signkey private/ca.key.pem -in csr/www.example.com.csr.pem -req -days 365 -out certs/www.example.com.cert.pem
openssl x509 -noout -text -in certs/www.example.com.cert.pem
```

- Guardamos: `certs/www.example.com.cert.pem` Este archivo incluye nuestra clave pública y es lo que podemos darle a cualquier persona

# Conclusiones
<!-- _class: lead -->

## Resumen

- TLS es el protocolo "que lo combina todo": confidencialidad, autenticación, acuerdo de claves, integridad...
- Se basa en que existe un sistema de PKI funcional en Internet
- La seguridad de Internet está basada en la confianza que tenemos en la distribución de certificados, es decir, en la distribución de claves públicas de los servidores

## Referencias

- [Transport Layer Security, TLS 1.2 and 1.3 (Explained by Example)](https://www.youtube.com/watch?v=AlE5X1NlHgg)
- [SSL/TLS handshake Protocol](https://www.youtube.com/watch?v=sEkw8ZcxtFk)
- [What is TLS (Transport Layer Security)?](https://www.cloudflare.com/learning/ssl/transport-layer-security-tls/)
- [Seguridad en el protocolo SSL-TLS. Ataques criptoanaliticos modernos](https://github.com/mindcrypt/libros/blob/master/Book_Seguridad_en_el_protocolo_SSL_TLS_Ataques_criptoanaliticos_modernos.%20Dr%20Alfonso%20Munoz%20mindcrypt%20-%2019102023.pdf)  Dr. Alfonso Muñoz, 2023
- [A modern overview of SSL/TLS - TLS 1.2](https://www.paolotagliaferri.com/an-overview-of-ssl-tls-secure-sockets-layer-transport-layer-security-tls-1-2/). Hay una segunda parte en la que se habla de TLS 1.3

# ¡Gracias!
<!-- _class: last-slide -->