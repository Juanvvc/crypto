---
marp: true
title: Criptografía - Autenticación
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

**Tema 7: Autenticación de usuarios**

Juan Vera del Campo

juan.vera@campusviu.es

# Como decíamos ayer...

[New Directions in Cryptography](https://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.37.9720) (Whitfield Diffie y Martin Hellman, 1976) exploraba qué se necesitaba para que dos empresas pudiesen firmar un contrato mercantil:

1. **Confidencialidad**, sin tener una clave secreta común
1. **Autenticación** de la identidad (llamada "autencidad de usuario" en el paper original)
1. **Integridad** del contrato (llamada "autenticidad del mensaje")
1. **No repudio** del contrato por ninguna de las partes

Es la lista que conocemos como "los servicios básicos de seguridad" (tema 1)

## Hoy hablamos de...

Integridad y primer paso hacia autenticación

- [Autenticación](#5)
- [Challenge / Response](#18)
- [Usuario y contraseña](#23)
- [Tokens](#35)
- [Conclusiones](#44): resumen y referencias

## TLS y la autenticación
<!-- _class: extra-slide -->

En el [Tema 9](09-protocolos.html) se ve cómo TLS puede ofrecer autenticación

- Autenticación de servidor: el servidor envía su clave pública al cliente, que lo acepta por PKI, como se ve en el [Tema 8](08-pki.html). El servidor ahora autentica al cliente con algún mecanismo que no se explica en el tema 9
- Autenticación doble: servidor y cliente intercambian claves públicas, que se aceptan por PKI, como se ve en el [Tema 8](08-pki.html)

En ambos casos, con tener la clave pública de la otra persona no es suficiente: tenemos que **probar** que la otra persona tiene también la privada.

En este tema veremos los detalles técnicos de estos métodos de autenticación

# Autenticación
<!-- _class: lead -->

## ¿Qué es la autenticación?

**En Internet, nadie es quien dice ser**

- Man in the middle
- Impersonation

La autenticación: proceso de confirmar que alguien es quien dice ser

![bg right:40%](https://www.totalentertainment.biz/wp-content/gallery/impersonators/elvis.jpg)


> https://es.wikipedia.org/wiki/Autenticaci%C3%B3n
> Foto: https://www.totalentertainment.biz/rentals/entertainment/impersonators.html

## Identidades

Para poder tener autenticación es necesaria la existencia de identidades

- Personas: su identidad física
- Webs: que el servidor de una URL sea el que tiene que ser

![bg left:60%](https://technofaq.org/wp-content/uploads/2015/06/idtheft830-1024x659.jpg.webp)

## Factores de la autenticación

**Algo que sabemos** (*knowledge*): contraseña, PIN...

**Algo que tenemos** (*ownership*): smartcards, Google Authentication...

**Algo que somos** (*inference*): huellas digitales, voz, cara...

El servidor podría también comprobar que nos estamos conectando desde el lugar y a las horas habituales

> https://searchsecurity.techtarget.com/feature/5-common-authentication-factors-to-know

![bg right:50% w:100%](https://cdn.ttgtmedia.com/rms/onlineimages/security-multifactor_authentication.png)

## Autenticación tradicional

Tradicionalmente solo se ha utilizado el *algo que sabemos*: la contraseña

Este sistema está poco seguro, pero fácil de usar

![bg right w:80%](https://upload.wikimedia.org/wikipedia/commons/f/f1/Mediawiki_1.25_sign_in_form.png)

## Two factor authentication: 2FA

Usa al menos dos de los factores anteriores

![center](https://4.bp.blogspot.com/-JSXGwbHpQCQ/W1FIvIjGNLI/AAAAAAAAIJM/E1oNm8OE-vIJsEc-VzYbuNK5a6YLwPyvwCLcBGAs/s1600/Two%2BFactor%2BAuthentication.jpg)

Fíjate: si desbloqueamos el móvil con biometría, ya estamos usando los tres factores

## "Passwordless" authentication

No usa el factor *algo que sabemos*

![center w:25em](https://doubleoctopus.com/wp-content/uploads/2020/04/img_5e8b02587d9e4.png)

---

En muchas webs nos podemos autenticar con nuestro usuario de Google, Facebook o Microsoft

[Microsoft](https://www.microsoft.com/en-us/security/business/identity-access-management/passwordless-authentication) y [Google](https://androidcommunity.com/google-planning-on-a-more-secure-no-password-future-20210506/) proponen que nos autentiquemos en sus sistemas solo con nuestro móvil: en el futuro próximo, ¡puede que no usemos contraseñas!

![center w:25em](https://img-prod-cms-rt-microsoft-com.akamaized.net/cms/api/am/imageFileData/RE4MHhB?ver=3b34&q=0&m=6&h=771&w=1619&b=%23FFFFFFFF&u=t&l=f&f=jpg&o=t&aim=true)

## Vulnerabilidades de *algo que sabemos*

- Ataques de diccionario "offline"
- Muchos usuarios utilizan contraseñas del "top 100": https://en.wikipedia.org/wiki/List_of_the_most_common_passwords
- Muchos usuarios **reutilizan** contraseñas en varios lugares
- A veces es posible "adivinar contraseñas", si tienen una estructura
- A veces, el administrador de sistemas no cambia la contraseña por defecto

## Vulnerabilidades de *algo que tenemos/somos*

- Que nos roben el móvil, o que esté intervenido por un atacante
- [Que la biometría no sea una ciencia exacta](https://www.ncsc.gov.uk/collection/biometrics/how-biometrics-are-attacked)

![center](https://www.idrnd.ai/wp-content/uploads/2021/05/Liveness-Presentation-Attacks-e1619997533456.jpg.webp)

> https://www.idrnd.ai/can-biometric-data-be-stolen/

## Vulnerabilidades generales

- Si hay un equipo secuestrado y le enviamos credenciales, la hemos perdido en ese equipo y en todos los que usen la misma contraseña: redes windows, pass the hash...
- Un atacante puede repetir exactamente lo que hemos hecho: replay attack
- Un atacante puede obligarnos a hacer algo (sin que nos demos cuenta) aprovechando nuestas credenciales

## *Lateral movement*

Piensa en una red Windows: si un atacante controla un equipo y se pone a escuchar las contraseñas que los trabajadores usan en ese equipo en concreto... ¡podría aprovechar estas contraseñas en otros equipos!

Esto no es tan raro: es la etapa *lateral movement* en cualquier ataque cibernético

![bg right w:100%](https://i0.wp.com/ciberseguridadenlinea.com/wp-content/uploads/2020/06/lateralmovement.jpg?resize=768%2C563&ssl=1)

## Vamos a ver tres soluciones

- Desafío-respuestas
- Contraseñas / biometría
- Tokens

# Desafío - Respuesta
<!-- _class: lead -->


## Desafío-Respuesta (*Challenge-Response*)

Los sistemas de CAPTCHA son un sistemas básico de autenticación por desafío - respuesta: eres una persona

pueden ser un primer filtro de entrada a tus sistemas para evitar ataques automáticos

> https://en.wikipedia.org/wiki/CAPTCHA

![bg right:50% w:60%](https://upload.wikimedia.org/wikipedia/en/8/80/Images_Recaptcha.png)

## Desafío-Respuesta (*Challenge-Response*) usando criptografía asimétrica

Aprovechamos criptografía asimétrica: si tenemos la clave pública de una persona, podemos desafiarle:

- **Alice**: Bob, ¿eres capaz de firmar *8u2348j48749082904* con tu clave privada?
- **Bob**: $RSA_{sk_{Bob}}(8u2348j48749082904) = yuh137321h1238$
- **Alice**: si $RSA_{pk_{Bob}}(yuh137321h1238) = 8u2348j48749082904$, sabe que está hablando con Bob

> https://es.wikipedia.org/wiki/Protocolos_desaf%C3%ADo-respuesta

<!--
Aunque los CAPTCHA son ejemplos sencillos de desafío-respuesta, vamos a centrarnos en protocolos criptográficos

Como parte de otros protocolos, se suele implementar un sistemas challenge-response para probar que alguien tiene la clave privada que se corresponde con una clave pública

Fíjate:

- Cuando hablamos con alguien, nos envía su certificado con su clave pública. Con los mecanismos del tema 8 sabemos que esa es, sin ninguna duda, la clave pública de Bob
- ¿Pero realmente estamos hablando con Bob? En realidad solo estamos hablando con alguien que TIENE la clave pública de Bob, igual que nosotros la tenemos ahora.
- Aunque sepamos que esa es sin duda la clave pública de Bob, aún es necesario asegurarse de que estamos hablando realmente con Bob. Le desafiamos a que firme algo con la clave privada que dice tener.
-->

## Proceso
<!-- _class: two-columns smaller-font -->

[![w:20em](https://mermaid.ink/img/eyJjb2RlIjoic2VxdWVuY2VEaWFncmFtXG4gICAgQWxpY2UtPj4rQm9iOiBIRUxMT1xuICAgIEJvYi0-Pi1BbGljZTogQ2xhdmUgcMO6YmxpY2EgQm9iXG4gICAgQWxpY2UtPj5BbGljZTogQ29tcHJ1ZWJhIHF1ZSBsYSBjbGF2ZSBww7pibGljYSBlcyBPS1xuICAgIEFsaWNlLT4-K0JvYjogQ2hhbGxlbmdlPVwiODMyN2g0aDN5XCJcbiAgICBCb2ItPj4tQWxpY2U6IFJTQSg4MzI3aDRoM3kpXG4gICAgQWxpY2UtPj5BbGljZTogQ29tcHJ1ZWJhIHF1ZSBlbCBkZXNjaWZyYWRvIGVzIE9LXG4gICAgTm90ZSBvdmVyIEFsaWNlLEJvYjogRGlmZmllLUhlbGxtYW4gcGFyYSBhY29yZGFyIGNsYXZlIEFFU1xuICAgIE5vdGUgb3ZlciBBbGljZSxCb2I6IENvbXVuaWNhY2nDs24gY2lmcmFkYSBjb24gQUVTIiwibWVybWFpZCI6eyJ0aGVtZSI6ImRlZmF1bHQifSwidXBkYXRlRWRpdG9yIjpmYWxzZSwiYXV0b1N5bmMiOnRydWUsInVwZGF0ZURpYWdyYW0iOmZhbHNlfQ)](https://mermaid-js.github.io/mermaid-live-editor/edit/##eyJjb2RlIjoic2VxdWVuY2VEaWFncmFtXG4gICAgQWxpY2UtPj4rQm9iOiBIRUxMT1xuICAgIEJvYi0-Pi1BbGljZTogQ2xhdmUgcMO6YmxpY2EgQm9iXG4gICAgQWxpY2UtPj5BbGljZTogQ29tcHJ1ZWJhIHF1ZSBsYSBjbGF2ZSBww7pibGljYSBlcyBPS1xuICAgIEFsaWNlLT4-K0JvYjogQ2hhbGxlbmdlPVwiODMyN2g0aDN5XCJcbiAgICBCb2ItPj4tQWxpY2U6IFJTQSg4MzI3aDRoM3kpXG4gICAgQWxpY2UtPj5BbGljZTogQ29tcHJ1ZWJhIHF1ZSBlbCBkZWNpZnJhZG8gZXMgT0tcbiAgICBOb3RlIG92ZXIgQWxpY2UsQm9iOiBEaWZmaWUtSGVsbG1hbiBwYXJhIGFjb3JkYXIgY2xhdmUgQUVTXG4gICAgTm90ZSBvdmVyIEFsaWNlLEJvYjogQ29tdW5pY2FjacOzbiBjaWZyYWRhIGNvbiBBRVMiLCJtZXJtYWlkIjoie1xuICBcInRoZW1lXCI6IFwiZGVmYXVsdFwiXG59IiwidXBkYXRlRWRpdG9yIjpmYWxzZSwiYXV0b1N5bmMiOnRydWUsInVwZGF0ZURpYWdyYW0iOmZhbHNlfQ)

- Alice tiene que enviar una challenge diferente cada vez, que no sea predecible por un atacante
- Alice necesita algún mecanismo adicional para comprobar que esa clave pública está asociada a Bob ([tema 8](08-pki.html))
- Fíjate: este esquema es una firma electrónica:
    - Firma electrónica: $challenge=hash(documento)$
    - Pero en firma electrónica normalmente no hará falta que Alice haga un dasafío, Bob ya envía su firma junto con el documento original antes de que le desafíen

## TLS y la autenticación
<!-- _class: extra-slide -->

En TLS se aprovecha la fase D-H para hacer un challenge-response y probar que el servidor tiene la clave privada del certificado que ha enviado, en lo que se conoce como [Diffie-Hellman autenticado](https://datatracker.ietf.org/doc/html/rfc5246#appendix-F.1.1.3)

# Autenticación por contraseña
<!-- _class: lead -->

(en esta sección: "contraseña" es algo guardado una BBDD: una clave, una huella digital...)

## Solución 1: contraseña en claro en la BBDD
<!-- _class: two-columns -->

[![](https://mermaid.ink/img/eyJjb2RlIjoic2VxdWVuY2VEaWFncmFtXG4gICAgQWxpY2UtPj4rQm9iOiBVc3VhcmlvIC8gUGFzc3dvcmRcbiAgICBCb2ItPj4rQkJERDogVXN1YXJpbyAvIFBhc3N3b3JkXG4gICAgQkJERC0-Pi1Cb2I6IE9LXG4gICAgQm9iLT4-LUFsaWNlOiBPS1xuICAgICAgICAgICAgIiwibWVybWFpZCI6eyJ0aGVtZSI6ImRlZmF1bHQifSwidXBkYXRlRWRpdG9yIjpmYWxzZSwiYXV0b1N5bmMiOnRydWUsInVwZGF0ZURpYWdyYW0iOmZhbHNlfQ)](https://mermaid-js.github.io/mermaid-live-editor/edit/##eyJjb2RlIjoic2VxdWVuY2VEaWFncmFtXG4gICAgQWxpY2UtPj4rQm9iOiBVc3VhcmlvIC8gUGFzc3dvcmRcbiAgICBCb2ItPj4rQkJERDogVXN1YXJpbyAvIFBhc3N3b3JkXG4gICAgQkJERC0-Pi1Cb2I6IE9LXG4gICAgQm9iLS0-Pi1BbGljZTogT0tcbiAgICAgICAgICAgICIsIm1lcm1haWQiOiJ7XG4gIFwidGhlbWVcIjogXCJkZWZhdWx0XCJcbn0iLCJ1cGRhdGVFZGl0b3IiOmZhbHNlLCJhdXRvU3luYyI6dHJ1ZSwidXBkYXRlRGlhZ3JhbSI6ZmFsc2V9)

- En la base de datos se guarda el usuario y contraseña
- Si roban la base de datos... ¡roban las contraseñas!
    - Los usuarios suelen reutilizar contraseñas
    - El administrator de la BBDD conoce nuestra contraseña

<!--
La BBDD podría cifrar las contraseñas, pero eso es una solución parcial: si alguien es capaz de robar la base de datos, es muy posible que también sea capaz de robar la contraseña de cifrado.

Aún así, guardar las contraseñas cifradas es sin duda mejor que guardarla en claro. Simplemente, hay soluciones mejores que no requieren una contraseña de cifrado, como veremos a continuación

Que el adminitrador de la BBDD conozca la contraseña es un problema: ¿realmente podemos confiar en él? No sería la primera vez que el ladrón está dentro de casa, y que sea el administrador de sistemas
-->

## Solución 2: hash de la contraseña
<!-- _class: two-columns -->


[![](https://mermaid.ink/img/eyJjb2RlIjoic2VxdWVuY2VEaWFncmFtXG4gICAgQWxpY2UtPj4rQm9iOiBVc3VhcmlvIC8gUGFzc3dvcmRcbiAgICBCb2ItPj4rQkJERDogVXN1YXJpbywgaGFzaChQYXNzd29yZClcbiAgICBCQkRELT4-LUJvYjogT0tcbiAgICBCb2ItPj4tQWxpY2U6IE9LXG4gICAgICAgICAgICAiLCJtZXJtYWlkIjp7InRoZW1lIjoiZGVmYXVsdCJ9LCJ1cGRhdGVFZGl0b3IiOmZhbHNlLCJhdXRvU3luYyI6dHJ1ZSwidXBkYXRlRGlhZ3JhbSI6ZmFsc2V9)](https://mermaid-js.github.io/mermaid-live-editor/edit/##eyJjb2RlIjoic2VxdWVuY2VEaWFncmFtXG4gICAgQWxpY2UtPj4rQm9iOiBVc3VhcmlvIC8gUGFzc3dvcmRcbiAgICBCb2ItPj4rQkJERDogVXN1YXJpbyBcbiAgICBCQkRELT4-LUJvYjogXCJTYWx0XCIgZGVsIHVzdWFyaW9cbiAgICBCb2ItPj4rQkJERDogVXN1YXJpbywgaGFzaChQYXNzd29yZClcbiAgICBCQkRELT4-LUJvYjogT0tcbiAgICBCb2ItPj4tQWxpY2U6IE9LXG4gICAgICAgICAgICAiLCJtZXJtYWlkIjoie1xuICBcInRoZW1lXCI6IFwiZGVmYXVsdFwiXG59IiwidXBkYXRlRWRpdG9yIjpmYWxzZSwiYXV0b1N5bmMiOnRydWUsInVwZGF0ZURpYWdyYW0iOmZhbHNlfQ)

- Ventaja: la BBDD no guarda las contraseñas sino sus hashes. Si alguien roba la BBDD, tiene que romper los hashes
- Existen hashes especializados en huellas biométricas


<!--
Nota: Alice podría enviar o bien su contraseña, o bien su hash. Es normal que Alice envíe a Bob (una página web) la contraseña, pero Bob calcula inmediatamente el hash: Alice se fía de Bob, pero Bob no se fía de la base de datos
-->

## Análisis de seguridad

- En realidad, queremos un hash criptográfico pero **no un hash rápido**:
    - Bob solo hará la operación una vez, no pasa nada si es costosa
    - Un atacante tiene que hacer fuerza bruta: **interesa que cada intento lleve mucho tiempo**
- Se suele implementar como una serie de hashes. Ejemplo: "calculamos el hash de la contraseña 1024 veces". así obligaríamos a un atacante a hacer un número descomunal de operaciones para cada prueba.
- Problemas:
    - si varios usuarios tienen la misma contraseña... la BBDD lo sabe
    - si se usan contraseñas sencillas... se pueden romper con *rainbow tables* o tablas precalculadas de contraseñas

## Solución 3: hash de contraseña + salt
<!-- _class: two-columns -->

[![](https://mermaid.ink/img/eyJjb2RlIjoic2VxdWVuY2VEaWFncmFtXG4gICAgQWxpY2UtPj4rQm9iOiBVc3VhcmlvIC8gUGFzc3dvcmRcbiAgICBCb2ItPj4rQkJERDogVXN1YXJpb1xuICAgIEJCREQtPj4tQm9iOiBcIlNhbHRcIiBkZWwgdXN1YXJpb1xuICAgIEJvYi0-PitCQkREOiBVc3VhcmlvLCBoYXNoKFNhbHQ6UGFzc3dvcmQpXG4gICAgQkJERC0-Pi1Cb2I6IE9LXG4gICAgQm9iLT4-LUFsaWNlOiBPSyIsIm1lcm1haWQiOnsidGhlbWUiOiJkZWZhdWx0In0sInVwZGF0ZUVkaXRvciI6ZmFsc2UsImF1dG9TeW5jIjp0cnVlLCJ1cGRhdGVEaWFncmFtIjpmYWxzZX0)](https://mermaid-js.github.io/mermaid-live-editor/edit/##eyJjb2RlIjoic2VxdWVuY2VEaWFncmFtXG4gICAgQWxpY2UtPj4rQm9iOiBVc3VhcmlvIC8gUGFzc3dvcmRcbiAgICBCb2ItPj4rQkJERDogVXN1YXJpb1xuICAgIEJCREQtPj4tQm9iOiBcIlNhbHRcIiBkZWwgdXN1YXJpb1xuICAgIEJvYi0-PitCQkREOiBVc3VhcmlvLCBoYXNoKFNhbHQ6UGFzc3dvcmQpXG4gICAgQkJERC0-Pi1Cb2I6IE9LXG4gICAgQm9iLT4-LUFsaWNlOiBPSyIsIm1lcm1haWQiOiJ7XG4gIFwidGhlbWVcIjogXCJkZWZhdWx0XCJcbn0iLCJ1cGRhdGVFZGl0b3IiOnRydWUsImF1dG9TeW5jIjp0cnVlLCJ1cGRhdGVEaWFncmFtIjpmYWxzZX0)

- El "salt" es algo parecido al "nonce": se puede guardar en claro en la BBDD
- El salt tiene que ser un valor **totalmente aleatorio y diferente para cada usuario**
- Ya no es posible tener tablas precomputadas
- Esta es la solución tomada en la actualidad

## Análisis de seguridad

- La BBDD guarda $hash(SALT:PASSWORD)$
    - No es vulenrable a tablas precalculadas de contraseñas
    - Si dos usuarios tienen la misma contraseña, con gran probabilidad tendrán salt diferente así que la BBDD no sabe que las contraseñas son iguales
    - La BBDD no conoce la contraseña original, solo el hash
- La salt tiene que ser aleatoria
- Es el mecanismo usado en Linux, Windows... y en la mayor parte de las webs
- Guardar una contraseña en una BBDD es un error, hay que guardar solo $hash(SALT:PASSWORD)$

Nota: a veces, como en bcrypt, no se hace un hash sino un cifrado simétrico irreversible

## Protocolo Bcrypt

[Bcrypt (1999)](https://www.usenix.org/legacy/events/usenix99/provos/provos_html/node1.html), de Niels Provos y David Mazieres, es un sistema para proteger contraseñas en bases de datos.

- Basado en el cifrado por bloques de [Blowfish (1994)](https://www.schneier.com/academic/archives/1994/09/description_of_a_new.html) de Bruce Schneier (en la foto)
- Se aprovecha de que Blowfish es muy lento durante la fase de expansión de claves

![bg right:40%](https://upload.wikimedia.org/wikipedia/commons/f/fc/Bruce_Schneier_at_CoPS2013-IMG_9174.jpg)

<!--
En la fotografía no está el creador de bcrypt sino el creador de Blowfish: Bruce Schneier

El blog y los libros de Bruce Schneier son un imprescidible para estar en el mundo de la criptografía y la seguridad operacional. Es un divulgador nada técnico y accesible a personas con cualquier conocimiento.

https://www.schneier.com/
-->

## Cifrado como "hash", nonce como "salt"

![center w:35em](https://upload.wikimedia.org/wikipedia/commons/3/32/Bcrypt.png)

Esto es lo que guarda la BBDD para cada usuario

## Algoritmo

- Entrada:
	- `password`
	- `cost`, 10 ó 12 es usual son valores usuales
	- `salt`, que se se escoge automáticamente. La *salt* es otro nombre para el *nonce*
- Derivación de clave, que es el proceso lento de Blowfish, se hace $2^{cost}$ veces.
- Cifra con la clave derivada la cadena estándar *OrpheanBeholderScryDoubt* 64 veces.

---

![center w:32em](https://i.stack.imgur.com/Z63W8.png)

## Ejemplos
<!-- _class: smaller-font -->

PWD|Bcrypt
--|--
abracadabra|`$2a$12$sWfsiB42yT.LvoyCqAHURujcDUTmEHVUjQHqTP4kL1Zs1p.j4G6Lu`
sesamo|`$2a$12$kWTGyiUbTha.bKpGXyz8ieRIYMAVNaO7gvrZMZ86DKZNgpiJzh49u`
sesamo|`$2a$12$LQbVUSGksM2vCoZiBhmKCerSTe/Uq7BWVgbxFAe8eY/9y3y1P8dzS`

```python
from Crypto.Protocol.KDF import bcrypt, bcrypt_check

password = 'sesamo'

hpwd = bcrypt(password, 12)
# $2a$12$kWTGyiUbTha.bKpGXyz8ieRIYMAVNaO7gvrZMZ86DKZNgpiJzh49u

bcrypt_check(password, hpwd)
# True
```

<!--
Fijaos que ejecutar bcrypt sobre la misma contraseña "sesamo", da resultados diferentes. De esta forma se puede guardar las contraseñas repetidas sin que ndie pueda saber que son repetidas
-->

## Problema

Imagina una petición con HTTP (ó HTTPS)

```http
GET / HTTP/1.1
Host: www.vuelasim.com
Authorization: Basic YWxpY2U6c2VzYW1l
...
```

La cabecera *Authentication* incluye el usuario y contraseña (o su hash) codificado en Base64.

```bash
$ echo 'YWxpY2U6c2VzYW1l' | base64 -d
alice:sesame% 
```

Para evitar enviar siempre la contrasela (o su hash): sesiones por tokens


# Sesiones por tokens
<!-- _class: lead -->

## Autenticación por token

1. El usuario envía un usuario y contraseña
2. Si es correcto (ver sección anterior), el usuario recibe un token
3. Para el resto de peticiones el usuario envía **solo** el token
4. En cada petición, el servidor verifica que el token es correcto
    - el token **podría** está firmado digitalmente, o cifrado con una clave que solo conoce el servidor
    - el token **podría** ser un número aleatorio guardado la base de datos
    - (opcional, pero muy recomendable) con cada nueva petición, el token se renueva

> https://sherryhsu.medium.com/session-vs-token-based-authentication-11a6c5ac45e4


## Proceso
<!-- _class: two-columns smaller-font -->

[![](https://mermaid.ink/img/eyJjb2RlIjoic2VxdWVuY2VEaWFncmFtXG4gICAgQWxpY2UtPj4rQm9iOiBVc3VhcmlvIC8gUGFzc3dvcmRcbiAgICBCb2ItPj4rQkJERDogVXN1YXJpb1xuICAgIEJCREQtPj4tQm9iOiBcIlNhbHRcIiBkZWwgdXN1YXJpb1xuICAgIEJvYi0-PitCQkREOiBVc3VhcmlvLCBoYXNoKFNhbHQ6UGFzc3dvcmQpXG4gICAgQkJERC0-Pi1Cb2I6IE9LXG4gICAgQm9iLT4-LUFsaWNlOiB0b2tlbiA9IENpZnJhZG8odXN1YXJpbywxIGhvcmEpXG4gICAgQWxpY2UtPj4rQm9iOiBwZXRpY2nDs24sIHRva2VuXG4gICAgQm9iLT4-Qm9iOiB0b2tlbiBPSz9cbiAgICBCb2ItPj4tQWxpY2U6IHJlc3B1ZXN0YVxuIiwibWVybWFpZCI6eyJ0aGVtZSI6ImRlZmF1bHQifSwidXBkYXRlRWRpdG9yIjpmYWxzZSwiYXV0b1N5bmMiOnRydWUsInVwZGF0ZURpYWdyYW0iOmZhbHNlfQ)](https://mermaid-js.github.io/mermaid-live-editor/edit/##eyJjb2RlIjoic2VxdWVuY2VEaWFncmFtXG4gICAgQWxpY2UtPj4rQm9iOiBVc3VhcmlvIC8gUGFzc3dvcmRcbiAgICBCb2ItPj4rQkJERDogVXN1YXJpb1xuICAgIEJCREQtPj4tQm9iOiBcIlNhbHRcIiBkZWwgdXN1YXJpb1xuICAgIEJvYi0-PitCQkREOiBVc3VhcmlvLCBoYXNoKFNhbHQ6UGFzc3dvcmQpXG4gICAgQkJERC0-Pi1Cb2I6IE9LXG4gICAgQm9iLT4-LUFsaWNlOiB0b2tlbiA9IENpZnJhZG8odXN1YXJpbywxIGhvcmEpXG4gICAgQWxpY2UtPj4rQm9iOiBwZXRpY2nDs24sIHRva2VuXG4gICAgQm9iLT4-Qm9iOiB0b2tlbiBPSz9cbiAgICBCb2ItPj4tQWxpY2U6IHJlc3B1ZXN0YVxuIiwibWVybWFpZCI6eyJ0aGVtZSI6ImRlZmF1bHQifSwidXBkYXRlRWRpdG9yIjpmYWxzZSwiYXV0b1N5bmMiOnRydWUsInVwZGF0ZURpYWdyYW0iOmZhbHNlfQ)

- Hay una verificación inicial de usuario
- El token es $E_ {K_{Bob}}(Alice, caducidad)$. Es decir: cifrado con una clave que solo Bob conoce del nombre de Alice y una caducidad
- Una vez obtenido el token, Alice lo incluye siempre en las siguientes peticiones: mientras no caduque el token, no tiene que volver a enviar usuario / contraseña
- Cuando Bob recibe una nueva petición, comprueba el token:
    - que puede descifrarlo
    - que no ha caducado

<!--
En esta transparencia se muestra el caso de que el usuario utilice nombre/contraseña para autenticarse, pero funciona exactamente igual si usa un servicio no-password como el de Google:

1. El usuario entre en la web manolita.com, que utiliza Google como autenticación
2. Google confirma la identifidad de usuario en el móvil y avisa a manolita.com
3. manolita.com envía al usuario un token de autenticación
-->

## Tipos de token

1. $E_ {K_{Bob}}(Alice, caducidad)$: cifrado de la identidad de Alice y una caducidad
1. Un número completamente aleatorio generado para cada usuario y guardado en la base de datos
    - En este caso, cada nueva petición puede exigir un nuevo token: en la respuesta se incluye el token a utilizar en la siguiente petición

## Análisis de seguridad

- Si un atacante consigue el token de seguridad, solo será válido hasta que caduque
- Un atacante podría obligarnos a enviar un token válido a una página web:
    - [Cross site scripting](https://owasp.org/www-community/attacks/xss/)
    - [Cross-site request forgery](https://blog.cobalt.io/a-pentesters-guide-to-cross-site-request-forgery-csrf-57adedbad4be)

Para solucionarlo: usa tokens con caducidad tan corta como sea posible. Idealmente: tokens de un solo uso. Cada respuesta incluye el token que hay que usar en la petición siguiente

## Servidores de autenticación
<!-- _class: two-columns -->

[![](https://mermaid.ink/img/eyJjb2RlIjoic2VxdWVuY2VEaWFncmFtXG4gICAgQWxpY2UtPj4rQXV0aHNlcnZlcjogVXN1YXJpbyAvIFBhc3N3b3JkXG4gICAgQXV0aHNlcnZlci0-Pi1BbGljZTogdG9rZW4gPSBDaWZyYWRvKHVzdWFyaW8sMSBob3JhKVxuICAgIEFsaWNlLT4-K0JvYjogcGV0aWNpw7NuLCB0b2tlblxuICAgIEJvYi0-PkJvYjogdG9rZW4gT0s_XG4gICAgQm9iLT4-LUFsaWNlOiByZXNwdWVzdGFcbiIsIm1lcm1haWQiOnsidGhlbWUiOiJkZWZhdWx0In0sInVwZGF0ZUVkaXRvciI6ZmFsc2UsImF1dG9TeW5jIjp0cnVlLCJ1cGRhdGVEaWFncmFtIjpmYWxzZX0)](https://mermaid-js.github.io/mermaid-live-editor/edit/##eyJjb2RlIjoic2VxdWVuY2VEaWFncmFtXG4gICAgQWxpY2UtPj4rQXV0aHNlcnZlcjogVXN1YXJpbyAvIFBhc3N3b3JkXG4gICAgQXV0aHNlcnZlci0-Pi1BbGljZTogdG9rZW4gPSBDaWZyYWRvKHVzdWFyaW8sMSBob3JhKVxuICAgIEFsaWNlLT4-K0JvYjogcGV0aWNpw7NuLCB0b2tlblxuICAgIEJvYi0-PkJvYjogdG9rZW4gT0s_XG4gICAgQm9iLT4-LUFsaWNlOiByZXNwdWVzdGFcbiIsIm1lcm1haWQiOnsidGhlbWUiOiJkZWZhdWx0In0sInVwZGF0ZUVkaXRvciI6ZmFsc2UsImF1dG9TeW5jIjp0cnVlLCJ1cGRhdGVEaWFncmFtIjpmYWxzZX0)

- El uso de tokens nos permite tener servidores especializados en la autenticación, que son independientes del servicio
- El servicio final no necesita conocer usuario y contraseña, solo validar que el token viene desde el servidor de autenticación.
    - Verificación: el token está firmado con la clave privada del servidor de autenticación

## oAuth
<!-- _class: smaller-font -->

Gracias a oAuth, un usuario puede delegar el acceso a terceros a su cuenta de Google, Facebook, Twitter... sin necesidad de compartir contraseña

1. El usuario accede a un se∫rvicio de terceros (aplicación, página web...) que necesita acceder al Twitter, fotos de Google... del usuario
2. Twitter, Google confirma con el usuario que garantiza el acceso
3. Twitter, Google envían a la aplicación de terceros un **token** que la aplicación puede usar para acceder al contenido protegido

![bg right:40% w:100%](https://docs.axway.com/bundle/APIGateway_762_OAuthUserGuide_allOS_en_HTML5/page/Content/Resources/Images/docbook/images/oauth/APIgw_Oauth_ex_client_workfl.png)

> https://docs.axway.com/bundle/APIGateway_762_OAuthUserGuide_allOS_en_HTML5/page/Content/OAuthGuideTopics/oauth_intro.htm
> https://aaronparecki.com/oauth-2-simplified/

## Kerberos

- Desarrollado en el MIT en los 80
- Separa:
    - el servidor del autenticación
    - servidor de tokens
    - servicios finales
- Redes Windows corporativas: el *Authserver* es el *Domain Controller*


![right:50% w:100% bg](https://upload.wikimedia.org/wikipedia/commons/6/68/Kerberos_protocol.svg)

> Fuente: https://es.wikipedia.org/wiki/Kerberos
> [The Kerberos Version 5 (RFC4121, 2005)](https://datatracker.ietf.org/doc/html/rfc4121)

<!--
Kerberos se utiliza, por ejemplo, en redes Windows corporaivas: un usuario de dominio se autentica en el DC y obtiene un token que luego puede utilizar en cualquier ordenador de la empresa

CUIDADO: en los ciberataques actuales, los atacantes buscan por todos los medios hacerse con estos tokens
-->

## Ataques

Se han descrito ataques contra TODOS estos sistemas

- [Pass the hash](https://en.wikipedia.org/wiki/Pass_the_hash)
- [Reflection attack](https://en.wikipedia.org/wiki/Reflection_attack)
- ...

El problema de la autenticación segura aún está a medio resolver en entornos complejos


![bg right:60% w:100%](https://blogvaronis2.wpengine.com/wp-content/uploads/2018/12/what-can-mimikatz-do@2x-1-960x669.png)

# Conclusiones
<!-- _class: lead -->

## Resumen

- La autenticación es el servicio para probar que realmente estamos hablando con otra persona
- Si tenemos su clave pública, podemos desafiarle a que firme algo con su clave privada
- Si usamos usuario y contraseña, la base de datos no puede guardar esa información en claro
    - hash + salt
    - bcrypt
- Lo ideal es que solo tengamos que "probar nuestra identidad" una vez, y el resto de peticiones funcionamos con tokens

## Referencias

- [WebAuthn 101 - Demystifying WebAuthn](https://i.blackhat.com/USA-19/Thursday/us-19-Brand-WebAuthn-101-Demystifying-WebAuthn.pdf). Christiaan Brand, Google. Blackhat 2019
- [Kerberos Authentication Explained | A deep dive](https://www.youtube.com/watch?v=5N242XcKAsM)
- [What is OAuth really all about - OAuth tutorial - Java Brains](https://www.youtube.com/watch?v=t4-416mg6iU)

---
<!-- _class: center -->

Continúa en: [Public Key Infrastructure](08-pki.html)

