---
marp: true
title: Criptografía - Funciones de Hash y Blockchains
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

# Criptografía y Teoría de Códigos
<!-- _class: first-slide -->

**Tema 5: Funciones de Hash y Blockchains**

Juan Vera del Campo

juan.vera@campusviu.es

# Como decíamos ayer...

- **Confidencialidad**: AES/ChaCha20 + D-H
* **Integridad**: ¿?
* **Autenticidad**: ¿?
* **No repudio**: ¿?
* Para los demás necesitamos conocer hashes, MAC y más sobre criptografía asimétrica

![bg right w:90%](https://i.imgur.com/Cq78TET.png?1)

# Hoy hablamos de...

- [Funciones de hash](#4)
- [Blockchain](#27)
- [Conclusiones](#35): resumen y referencias

# Funciones de hash
<!-- _class: lead -->

## Función de resumen

Resume una cadena de longitud arbitraria $m$, a un valor $r$ de tamaño fijo $l$

$$
\begin{aligned}
r &= h(m)\\
\|r\| &= min(\|m\| , l)
\end{aligned}
$$

Ejemplos:

- "Resumir" un mensaje de 12 bytes en 32 bytes
- Resumir una imagen de 532KB en 32 bytes
- Resumir un vídeo de 4GB en 32 bytes

## Ejemplos

- Bit de paridad un mensaje: número de "1" en el mensaje
- CRC
- Checksum

Todos estos son resúmenes, pero no son de utilidad en criptografía

![bg right:30% w:100%](https://www.gatevidyalay.com/wp-content/uploads/2018/10/Parity-Check-Parity-Bit.png)


> https://es.wikipedia.org/wiki/Verificaci%C3%B3n_de_redundancia_c%C3%ADclica

## Colisiones
<!-- _class: with-success -->

No puede existir una aplicación inyectiva entre un conjunto de $m$ elementos y otro de $n$ elementos si $m>n$

Mensajes diferentes tendrán el mismo resumen

![bg right:50% w:100%](https://upload.wikimedia.org/wikipedia/commons/5/5c/TooManyPigeons.jpg)


> [Principio del palomar](https://es.wikipedia.org/wiki/Principio_del_palomar)

---

Por ejemplo:

Si queremos resumir fotografías de 1MB en resúmenes de 256 bits (tamaño típico)

$$
\left.
\begin{aligned}
    \|r\| & = 256\text{b} \Rightarrow |r| = 2^{256}\text{b} \\
    \|m\| & \approx 10^6\text{B} \Rightarrow |m| = 2^{2^{23}}\text{b}
\end{aligned}
\right\} \frac{|m|}{|r|} = \frac{2^{2^{23}}}{2^{256}} = 2^{2^{23}-256} \approx 2^{8·10^6} \approx 10^{26·10^6}
$$

Es decir, hay un número "casi infinito" de fotografías de 1MB que se resumen en el mismo número de 256 bits

Queremos que no sea nada fácil (computacionalmente hablando) encontrar cualquiera de esas "casi infinitas" fotografías

## Funciones de hash criptográficas

Aunque cada resumen $r$ es compartido por una gran cantidad de mensajes (colisiones) una función de hash segura hace que sea infactible encontrar dichas duplicidades

Dado un mensaje $m$ con un resumen $r=h(m)$ encontrar un mensaje con el mismo resumen $m$ la manera más eficiente tiene que ser generar mensajes hasta encontrar otro con el mismo resumen $r$

e.g. si el resumen es de $\|r\|=256$, entonces deberemos realizar $2^{256}$ operaciones de hash hasta encontrar una igual

## Requisitos

- Que sea rápido de calcular
- Resistencia a la preimagen: dado un hash, no se puede calcular la imagen
- Resistencia a la colisión: dado el hash de un mensaje, no se puede encontrar otro con el miso hahs
- Sensibilidad: un cambio mínimo en el mensaje produce un hash diferente

---

![center w:25em](https://upload.wikimedia.org/wikipedia/commons/2/2b/Cryptographic_Hash_Function.svg)

## Paradoja del cumpleaños

Hay un ataque mejor que el anterior de fuerza bruta, que deriva de la paradoja del cumpleaños:

*si tenemos un grupo de 23 personas, la probabilidad de tener un par con la misma fecha de cumpleaños es del 50%*

Sólo hace falta que el grupo llegue a 70 personas para que la probabilidad sea del 99%

![bg right:40%](images/pexels-nappy-3063910.jpg)

> Foto: [nappy](https://www.pexels.com/photo/group-of-people-standing-on-metal-stairs-3063910/), free to use

---
<!-- _class: with-success -->

Si tenemos un hash de tamaño $\|r\|$ la probabilidad de colisión será muy alta a medida que nos acercamos a las $\sqrt{\|r\|}$ operaciones

Para $\|r\|=256$ bits esto son unas $\sqrt{2^{256}} = 2^\frac{256}{2} = 2^{128}$ operaciones

Esto implica que para un hash hacen falta resúmenes el doble de largos de lo que hacía falta para las claves para obtener el mismo nivel de seguridad

La *security strength* de una función de hash de longitud $b$ bits es $b/2$

## Ejemplos


- MD5: utilizado mucho tiempo. [Totalmente roto desde 2008](https://www.win.tue.nl/hashclash/rogue-ca/): no hay que usarlo.
- SHA-1: 160 bits. [En la actualidad se considera roto](https://empresas.blogthinkbig.com/nuevo-ataque-sha-1-explicacion/)
- SHA-2: longitudes de 256 b y 512 b. Son conocidos como **SHA-256 y SHA-512**.
- SHA-3: longitudes entre 224 b a 512 b

Los hashes recomendados en la actualidad son el SHA-2 (cualquier de las dos variantes) y el SHA-3

Fíjate: ongitudes aproximadamente el doble que las longitudes de claves que las claves de AES (128 b, 192 b, 256 b) para una seguridad equivalente

---

```
> ms5sum 06-hashes.md
c99fe5e1ec0f637d77dddb32b1679c21  06-hashes.md

> sha256sum 06-hashes.md
06efc998ac8ad6867b4f1a9ee94d903503c0c52e6f1184a9561000eb303844ec  06-hashes.md

> sha512sum 06-hashes.md 
64b378a66da3714e723ac8469525ac7b460d7ad7ff348b9453d177907a14fd4a
445a11c07206b7df599bcf3ec70475a6e89b4bbfe605c928c36494ff1a31311d  06-hashes.md
```

## ¿SHA-2 ó SHA-3?

los primeros están diseñados por la NSA, y los segundos escogidos por el NIST después de organizar una competición para definir el siguiente hash a utilizar

el SHA-3 se ha desarrollado teniendo en cuenta la eficiencia y como backup en caso de encontrar vulnerabilidades en el SHA-2 (diseños totalmente diferentes)

el SHA-2 hasta ahora ha sido sometido a un trabajo de análisis muy superior al SHA-3

## Construcción

Formas de construir una función de hash:

- A partir de un cifrado de bloque en un modo realimentado: el hash es el último bloque. Posible, pero lento.
- [Merkle–Damgård](https://en.wikipedia.org/wiki/Merkle%E2%80%93Damg%C3%A5rd_construction): es el ejemplo mostrado en la figura. MD5, SHA-1, SHA-2... usan este método
- [SHA-3](https://en.wikipedia.org/wiki/SHA-3): utiliza función Keccak

![center w:20em](https://upload.wikimedia.org/wikipedia/commons/f/f0/FastWidePipeHashFunction.png)

## Ataque: rainbow table

[Tablas de consulta](https://es.wikipedia.org/wiki/Tabla_arco%C3%ADris) que ofrecen un compromiso para obtener claves en texto simple a partir del resultado de una función de hash.

$$hash \rightarrow mensaje$$

![bg right:50% w:100%](https://upload.wikimedia.org/wikipedia/commons/5/53/Dr._Oechslin_Rainbow_Table_Crypto_2003_Illustration.png)

## Seguridad en conjuntos de mensajes

Hace falta vigilar que la seguridad con la que protegemos los mensajes individuales, debe extrapolarse a secuencias de mensajes (la sesión)

Si no hacemos nada más que lo comentado hasta ahora, seríamos vulnerables a ataques:

- de réplica (replay attacks)
- de reordenado
- de eliminado

## Sesiones

Por ejemplo, añadiendo un identificador de secuencia

$$\{1\|\text{more}\|m_1, 2\|\text{more}\|m_2, \dots, n\|\text{last}\|m_n\}$$

Cada mensaje debe ir protegido por hash, HMAC o firma, cifrado, etc.

## Protocolos: Merkle Hash tree

Permite firmar bases de datos, discos, de forma eficiente

![center w:25em](images/Hash_Tree.svg)

## Prococolos: almacenamiento de contraseñas

El sistema operativo no debe guardar las contraseñas de los usuarios, no hace falta.

Podemos guardar simplemente su hash: hash(contraseña)

Pero esto tiene un problema: muchos usuarios usan palabras, nombres, etc. limitados. Las palabras, nombres conocidos són del orden de ≈100.000

Un atacante realizar un "diccionario" con el hash de todas las palabras, nombres, etc. (ataque de diccionario)

## Contramedida ataques de diccionario

Añadir un valor aleatorio o salt y lo guardamos:

$$salt\|hash(salt\|contraseña)$$

Esto fuerza al atacante a calcular el diccionario para cada contraseña

Pero sigue siendo factible realizar $\approx 100.000$ operaciones para encontrar una contraseña

Contramedida adicional: realizar iteraciones implementar un hash "costoso":

$$hash(hash(hash(...hash(salt\|contraseña))))$$

(Recuerda [bcrypt del tema 3](#03-simetrica.html))

## PRNG basado en hash

también (como con cifradores de bloque) se puede generar una función PRNG basada en hash:

- Hash DRBG
- HMAC DRBG

## Firma digital

Podemos proteger la **integridad, no-repudio y autenticidad de un mensaje** mediante una combinación de hash y cifrado asimétrico

![center w:15em](https://upload.wikimedia.org/wikipedia/commons/7/78/Private_key_signing.svg)

Recordad (tema 5): [PKCS#1](https://en.wikipedia.org/wiki/PKCS_1) incluye recomendaciones para hacer esto con seguridad.

## Cadena de custodia

Cuando se investiga un crimen... ¿cómo se protegen las evidencias digitales contra modificaciones?

Inicio de cadena de custodia publicando sus hashes

![center w:20em](https://www.ealde.es/wp-content/uploads/2021/02/analisis-forense-digital-ealde.jpg)

# Blockchain
<!-- _class: lead -->

## Bitcoin


- Inventado en 2008 por Satoshi Nakamoto (¡no se sabe quién es!)
- Sistema descentralizado de pagos digitales
- Utiliza firma digital, hashes y proof-of-work

![center w:15em](https://upload.wikimedia.org/wikipedia/commons/c/c5/Bitcoin_logo.svg)

> [Bitcoin: A Peer-to-Peer Electronic Cash System](https://bitcoin.org/bitcoin.pdf), Satoshi Nakamoto 2008

---

![center](https://steemitimages.com/DQmbuB6M8nfThcsUeWWJwpNrzHDDXMJQAmXL7aLtxEshrJA/blockchain%20transitionnew.jpeg)

> https://www.investopedia.com/news/how-bitcoin-works/

## Transacciones

![w:25em center](images/bc-transactions.png)

## Minería

Desafío (aka "minería"): resumen "escogiendo" un hash "costoso"

SHA2-256(bloque)=000000000000000000000000000000000000000000000000000000000000000000000001… y 185 bits más

Para poder escoger el hash, se debe añadir una secuencia de bits adecuada a la estructura a firmar (el bloque de transacciones de los últimos minutos):

$$hash(prefijo\ adecuado\|bloque)$$

Nota: este hash (la "minería") se realiza sobre el libro de transacciones de bitcoin (ledger)
(el titular del dinero se conoce porque se asocia la transacción con criptografía asimétrica)

## Consenso distribuido

- Red P2P de nodos
- Cosntantemente tratando de encontrar un prefijo al bloque que dé que su hash se inicie con un número determinado de ceros.
- Cuando lo consigue: lo anuncian a todos los nodos que conocen.
- Los demás nodos lo comprueban y reconocen, y empiezan un nuevo bloque.
- A veces es imposible llegar a un consenso: [The Byzantine General Problem](https://es.wikipedia.org/wiki/Tolerancia_a_faltas_bizantinas). En Bitcoin se resuelve:
    - O bien separando la red
    - O bien cuando los nodos en la cadena más pequeña "claudican" y desisten
- El protocolo funciona siempre que al menos la mitad de los nodos cooperen


## Proof of work: Hashcash
<!-- _class: smaller-font -->

Hashcash fue propuesto por Adam Back en 1997 para reducir el spam: el el correo incluía una PoW o no se admitía. En la actualidad se utiliza en varios sustemas de pago electrónico como PoW:

```
X-Hashcash: 1:52:380119:calvin@comics.net:::9B760005E92F0DAE
```

- versión
- bits: número de bits iniciales del hash
- date: fecha
- resource: Descripción del recurso: correo electrónico, transacción...
- counter: La PoW: lo que añadido al resto del mensaje da un hash con un número determinado de ceros

```
echo -n 1:52:380119:calvin@comics.net:::9B760005E92F0DAE | sha1sum  
0000000000000756af69e2ffbdb930261873cd71  -
```

> [Hashcash- A Denial ofServiceCounter-Measure](http://hashcash.org/papers/hashcash.pdf), Adam Back 2002

## Usos adicionales

El "ledger" BlockChain (y otros como NameCoin, Ethereum...) se está usando también como notaría:

En el libro de transacciones, a parte de transacciones, se pueden inscribir datos que quedan públicos (el ledger es público) para posterior consulta

# Conclusiones
<!-- _class: lead -->

## Resumen

- Las funciones de hash reducen un mensaje de cualquier tamaño (pocos bits o gigas de información) en un conjunto de pocos bytes
- SHA-2 (SHA-256 ó SHA-512) es el más usado. Debe evitarse MD5 o SHA-1
- Usos:
    - Firma digital: cifrado con clave asimétrica del hash de un mensaje, para probar autoría e integridad
    - Bitcoin
    - Cadena de custodia
    - ...

## Referencias

- [Hashing Algorithms and Security - Computerphile](https://www.youtube.com/watch?v=b4b8ktEV4Bg)
- [But how does bitcoin actually work?](https://www.youtube.com/watch?v=bBC-nXj3Ng4)
- [Bitcoin: A Peer-to-Peer Electronic Cash System](https://bitcoin.org/bitcoin.pdf), Satoshi Nakamoto 2008
- [Hashcash- A Denial ofServiceCounter-Measure](http://hashcash.org/papers/hashcash.pdf), Adam Back 2002

## Ejercicios

1. Calcula el valor de hash de un archivo de texto con el texto `hola mundo` en tu ordenador
    - Powershell: `Get-FileHash`
    - Linux/OSX: `sha256sum`
1. Cambia el texto a `Hola mundo` (¡mayúsculas!) y compara el hash: ¿cuántos bytes han cambiado?
1. Cambia el nombre del archico y compara el hash: ¿cuántos bytes han cambiado?
1. Calcula el hash SHA-256 y SHA-512 de un archivo de unos 500MB en tu ordenador (por ejemplo, película) ¿Cuánto tiempo lleva?