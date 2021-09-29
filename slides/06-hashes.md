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

# Criptografía
<!-- _class: first-slide -->

**Tema 6: Funciones de Hash y Blockchains**

Juan Vera del Campo - <juan.vera@campusviu.es>


# Como decíamos ayer...

- **Confidencialidad**: AES/ChaCha20 + D-H
* **Integridad**: ¿?
* **Autenticidad**: ¿?
* **No repudio**: ¿?
* Para los demás necesitamos conocer hashes, MAC y más sobre criptografía asimétrica

![bg right w:90%](https://i.imgur.com/Cq78TET.png?1)

# Hoy hablamos de...
<!-- _class: cool-list -->

1. [Funciones de hash](#4)
1. [Blockchain](#30)
1. [Resumen y referencias](#45)

# Funciones de hash
<!-- _class: lead -->

## Función digest, hash o resumen

Recibe los tres nombres, aunque cuando se usan en criptografía se prefiere "hash"

Función que resume una cadena de longitud arbitraria $m$, a un valor $r$ de tamaño fijo $l$

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

<!--
Los bits de paridad o los CRC se utilizan mucho con protocolos que esperan errores: RS232, lectura de CDs, la parte de paridad de un RAID... Un código de detección/corrección de errores se puede entender también como un "resumen" del mensaje: si el resumen no coincide con lo recibido, entonces sabemos ue ha habido un error.

Pero estas funciones, en general, no sirven en criptografía: imagina que un atacante puede cambiar un mensaje y también su resumen. Entonces, ¡no nos sirve de nada validar que el resumen sea correcto!
-->

## Funciones de hash criptográficas

Funciones hash criptográficas (CHF) son aquellas que:

- Comprimen la entrada a una salida de menor longitud y son fáciles de calcular. Es decir, son **funciones resumen**
- Cumplen **propiedades adicionales**. Muy por encima:
    - Dado un resumen, no es posible calcular el mensaje original
    - No es factible encontrar dos mensajes con el mismo resumen

Dado un mensaje $m$ con un resumen $r=h(m)$, para encontrar un mensaje $m'$ con el mismo resumen que $m$, es decir, $r=h(m)=h(m')$, la manera más eficiente tiene que ser probar mensajes uno a uno: fuerza bruta

> https://en.wikipedia.org/wiki/Cryptographic_hash_function

## ¿Mensajes con el mismo resumen?
<!-- _class: with-success -->

Obvio: no puede existir una aplicación inyectiva entre un conjunto de $m$ elementos y otro de $n$ elementos si $m>n$

Mensajes diferentes tendrán el mismo resumen: esto se llama "colisión"

![bg right:50% w:100%](https://upload.wikimedia.org/wikipedia/commons/5/5c/TooManyPigeons.jpg)


> [Principio del palomar](https://es.wikipedia.org/wiki/Principio_del_palomar)

<!--
El principio del palomar dice que si tienes 9 agujeros y 10 palomas, es necesario que dos palomas compartan agujero. Puede parecer una obviedad, pero a veces se nos pasan las obviedades:

Si los mensaje de 1.000.000 de caracteres se resumen en 256 caracteres... ¡por fuerza varios mensajes tendrán el mismo resumen!
-->

---
<!-- _class: with-success -->

Por ejemplo:

Si queremos resumir fotografías de 1MB en resúmenes de 256 bits (tamaño típico)

$$
\left.
\begin{aligned}
    \|r\| & = 256\text{b} \Rightarrow |r| = 2^{256}\text{resúmenes} \\
    \|m\| & \approx 10^6\text{B} \Rightarrow |m| = 2^{2^{23}}\text{fotografías}
\end{aligned}
\right\} \frac{|m|}{|r|} = \frac{2^{2^{23}}}{2^{256}} = 2^{2^{23}-256} \approx 2^{8·10^6} \approx 10^{26·10^6}
$$

Es decir, hay un número $10^{26·10^6}$, que en la práctica es "casi infinito", de fotografías de 1MB que se resumen en el mismo número de 256 bits

A pesar de eso, queremos que no sea nada fácil (computacionalmente hablando) encontrar cualquiera de esas "casi infinitas" fotografías: la única forma debe de ser probar las fotografías una a una

## Requisitos de una función de hash criptográfica

- Que sea rápida de calcular
- Resistencia a la preimagen: dado un hash, no se puede calcular la imagen más que probando una a una
- Resistencia a la colisión: dado el hash de un mensaje, no se puede encontrar otro con el mismo hash más que por fuerza bruta
- Sensibilidad: un cambio mínimo en el mensaje produce un hash totalmente diferente

> https://en.wikipedia.org/wiki/Cryptographic_hash_function#Properties

## ¿Cuántos hashes podemos calcular por segundo?

Los hashes se usan mucho en minería bitcoin, así que podemos utilizar sus tablas para conocer velocidades:

- ARM1176JZ(F)-S (Raspberry): 0.2 MH/s
- NVidia GTX1080: 222MH/s
- Bitmain AntMiner D3: 19,3 GH/s
- Avalon 6: 3.5 TH/s

![bg right:50%](https://images-na.ssl-images-amazon.com/images/I/610vUTCY-qL._AC_SL1000_.jpg)

> Más ejemplos: https://miningchamp.com/
> En la imagen, un Avalon 6, bloque especializado en calcular hashes

## Ejemplos de valores de hash

![center w:25em](https://upload.wikimedia.org/wikipedia/commons/2/2b/Cryptographic_Hash_Function.svg)

<!--
Ejemplos de valores de hash:

- el primero "resume" un texto "Fox" en otro más largo: la función de hash siempre tiene la misma longitud, incluso si el texto es corto: SHA-256 siempre dará un resumen de 256 bits sea como sea el texto de entrada.
- Los demás son variaciones del mismo texto de entrada. Fíjate: pequeñas variaciones dan un hash diferente a simple vista

¿Qué tenemos que cambiar en "The red fox jumps over the blue dog" para que tenga el mismo hash? Es decir, para que el hash no detecte el cambio. Ya que el texto es mayor de 256 bits, sabemos seguro que habrá otro texto que tendrá el mismo resumen. Pero lo único que podemos hacer es probar cambios uno y otro hasta tener suerte!
-->

## Paradoja del cumpleaños

En realidad hay un ataque a la resistencia a la colisión que deriva de la paradoja del cumpleaños:

*si tenemos un grupo de 23 personas, la probabilidad de tener un par con la misma fecha de cumpleaños es del 50%*

Sólo hace falta que el grupo llegue a 70 personas para que la probabilidad sea del 99%

![bg right:40%](images/pexels-nappy-3063910.jpg)

> Foto: [nappy](https://www.pexels.com/photo/group-of-people-standing-on-metal-stairs-3063910/), free to use

---
<!-- _class: with-success -->

Si tenemos un hash de tamaño $\|r\|$ la probabilidad de colisión será muy alta a medida que nos acercamos a las $\sqrt{\|r\|}$ operaciones

Para $\|r\|=256$ bits esto son unas $\sqrt{2^{256}} = 2^\frac{256}{2} = 2^{128}$ operaciones

Esto implica que para un hash hacen falta resúmenes el doble de largos de lo que hacía falta para las claves simétricas para obtener el mismo nivel de seguridad

La *security strength* de una función de hash de longitud $b$ bits es $b/2$

## Ejemplos de funciones de hash


- MD5: utilizado mucho tiempo. [Totalmente roto desde 2008](https://www.win.tue.nl/hashclash/rogue-ca/): no hay que usarlo.
- SHA-1: 160 bits. [En la actualidad se considera roto](https://empresas.blogthinkbig.com/nuevo-ataque-sha-1-explicacion/)
- SHA-2: longitudes de 256 b y 512 b. Son conocidos como **SHA-256 y SHA-512**.
- SHA-3: longitudes entre 224 b a 512 b

Los hashes recomendados en la actualidad son el SHA-2 (cualquier de las dos variantes) y el SHA-3

Fíjate: longitudes aproximadamente el doble que las longitudes de claves que las claves de AES (128 b, 192 b, 256 b) para una seguridad equivalente

---
<!-- _class: with-warning -->

Ejemplos de valores de hash MD5, SHA256 y SHA512 de esta presentación:

```
> ms5sum 06-hashes.md
c99fe5e1ec0f637d77dddb32b1679c21  06-hashes.md

> sha256sum 06-hashes.md
06efc998ac8ad6867b4f1a9ee94d903503c0c52e6f1184a9561000eb303844ec  06-hashes.md

> sha512sum 06-hashes.md 
64b378a66da3714e723ac8469525ac7b460d7ad7ff348b9453d177907a14fd4a
445a11c07206b7df599bcf3ec70475a6e89b4bbfe605c928c36494ff1a31311d  06-hashes.md
```

Si calculas los valores de hash del archivo, verás que no coinciden. Eso es porque no se puede calcular el hash de un archivo, meter el hash en el propio archivo, volver a calcular el hash ¡y que dé lo mismo! Recuerda: cualquier cambio (como por ejemplo meter el hash) cambia totalmente el hash

## ¿SHA-2 ó SHA-3?

La familia SHA-2 está **diseñada** por la NSA, la familia SHA-3 fue **escogida** por el NIST después de organizar una competición para definir el siguiente hash a utilizar

El SHA-3 se ha desarrollado teniendo en cuenta la eficiencia y como backup en caso de encontrar vulnerabilidades en el SHA-2 (diseños totalmente diferentes)

El SHA-2 hasta ahora ha sido sometido a un trabajo de análisis muy superior al SHA-3 y  no se han encontrado ninguna vulnerabilidad

## Construcción

Formas de construir una función de hash:

- A partir de un cifrado de bloque en un modo realimentado: el hash es el último bloque. Posible, pero lento.
- [Merkle–Damgård](https://en.wikipedia.org/wiki/Merkle%E2%80%93Damg%C3%A5rd_construction): es el ejemplo mostrado en la figura. MD5, SHA-1, SHA-2... usan este método
- [SHA-3](https://en.wikipedia.org/wiki/SHA-3): utiliza función Keccak

![center w:20em](https://upload.wikimedia.org/wikipedia/commons/f/f0/FastWidePipeHashFunction.png)

## Ataque: rainbow table

[Tablas de consulta](https://es.wikipedia.org/wiki/Tabla_arco%C3%ADris) que ofrecen un compromiso para obtener claves en texto simple a partir del resultado de una función de hash.

Son bases de datos:

$$hash \rightarrow mensaje$$

![bg right:50% w:100%](https://upload.wikimedia.org/wikipedia/commons/5/53/Dr._Oechslin_Rainbow_Table_Crypto_2003_Illustration.png)

> https://project-rainbowcrack.com/table.htm

---

Ejemplo:

```sh
$ echo -n sesame | sha256sum
d0c04f4b1951e4aeaaec8223ed2039e542f3aae805a6fa7f6d794e5afff5d272  -
$ echo -n hello | sha256sum
2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824  -
$ echo -n hola | sha256sum
b221d9dbb083a7f33428d7c2a3c3198ae925614d70210e28716ccaa7cd4ddb79  -
$ echo -n jñkjhafdiu232332 | sha256sum
b12ee96400fa19e7909a48f1727d3c81f6af71178209b58b612b5d2e75bf2d13  -
```

https://crackstation.net/

![center w:40em](images/crackstation.png)

---
<!-- _class: extra-slide -->

En este curso no hacemos criptoanálisis, es decir, no rompemos cosas. Si estáis interesados, se puede intentar romper hashes:

- Simplemente buscándolos en google
- Usando alguna *rainbow table*
- Usando diccionarios de "contraseñas probables"
- Herramientas como [John the Ripper](https://www.openwall.com/john/) o [CrackHash](https://pypi.org/project/crackhash/) aprovechan estas técnicas

## Usos: Merkle Hash tree

Permite firmar bases de datos, discos... de forma eficiente

![center w:25em](images/Hash_Tree.svg)

## Usos: almacenamiento de contraseñas

El sistema operativo no debe guardar las contraseñas de los usuarios: si alguien consigue entrar, ¡obtiene la contraseña del usuario!

Podemos guardar simplemente su hash: $hash(contraseña)$

Pero esto tiene un problema: muchos usuarios usan palabras, nombres, etc. limitados. Las palabras, nombres conocidos són del orden de ≈100.000

Un atacante realizar un "diccionario" con el hash de todas las palabras, nombres, etc. (ataque de diccionario y rainbow table)

## Contramedida a ataques de diccionario / rainbowtables

Añadir un valor aleatorio o salt y lo guardamos:

$$salt\|hash(salt\|contraseña)$$

Esto fuerza al atacante a calcular el diccionario para cada contraseña

Pero sigue siendo factible realizar $\approx 100.000$ operaciones para encontrar una contraseña

Contramedida adicional: realizar iteraciones implementar un hash "costoso":

$$hash(hash(hash(...hash(salt\|contraseña))))$$

(Recuerda [bcrypt del tema 3](#03-simetrica.html))

## Usos: Integridad de mensajes

Se puede usar un hash para asegurar la integridad de un mensaje: [HMAC](https://en.wikipedia.org/wiki/HMAC)

$$
HMAC(k, m) = hash(E_k(m))
$$

Es decir, el código para validar que un mensaje no ha sido modificado por un atacante:

- Las dos partes escogen una clave de verificación (suele ser diferente a la clave de cifrado)
- El mensaje por un lado se cifra con la clave de cifrado
- El mensaje por otro lado se cifra con la clave de verificación, y se calcula su hash

Un atacante tendría que romper el cifrado y el HMAC para modificar un mensaje: **si hacer solo una de esas dos cosas es lleva siglos, las dos a la vez llevaría siglos de siglos**

## Usos: Firma digital

Podemos proteger la **integridad, no-repudio y autenticidad de un mensaje** mediante una combinación de hash y cifrado asimétrico: cifrnado **el hash de un mensaje** con nuestra clave privada, aseguramos que ese mensaje lo hemos enviado nosotros y cualquier puede comprobarlo

![center w:15em](https://upload.wikimedia.org/wikipedia/commons/7/78/Private_key_signing.svg)

---

![](https://wizardforcel.gitbooks.io/practical-cryptography-for-developers-book/content/assets/signature-sign-verify.png)

> https://wizardforcel.gitbooks.io/practical-cryptography-for-developers-book/content/digital-signatures.html

## Usos: cadena de custodia

Cuando se investiga un crimen... ¿cómo se protegen las evidencias digitales contra modificaciones?

Inicio de cadena de custodia publicando sus hashes

![center w:20em](https://www.ealde.es/wp-content/uploads/2021/02/analisis-forense-digital-ealde.jpg)

## Usos: ...

Ya veis que los hashes tienen muchos usos en criptografía

Vamos a ver con un poco más de detalle su uso en las monedas digitales: Blockchain y BitCoin

![bg right:40%](https://www.ledgerinsights.com/wp-content/uploads/2019/10/digital-currency-dollar.2-810x476.jpg)

# Blockchain
<!-- _class: lead -->

## Bitcoin

![center w:15em](https://upload.wikimedia.org/wikipedia/commons/c/c5/Bitcoin_logo.svg)

- Inventado en 2008 por Satoshi Nakamoto (¡no se sabe quién es!)
- Sistema descentralizado de pagos digitales
- Utiliza firma digital y *proof-of-work* mediante hashes

> [Bitcoin: A Peer-to-Peer Electronic Cash System](https://bitcoin.org/bitcoin.pdf), Satoshi Nakamoto 2008


<!--
El paper original de "Satoshi Nakamoto" es sencillo de entender al menos en su primera parte, y se recomienda su lectura
-->


---

![center](https://steemitimages.com/DQmbuB6M8nfThcsUeWWJwpNrzHDDXMJQAmXL7aLtxEshrJA/blockchain%20transitionnew.jpeg)

> https://www.investopedia.com/news/how-bitcoin-works/

## Transacciones

![w:25em center](images/bc-transactions.png)

<!--
Esto es una transacción bitcoin: "X le da a Y Z bitcoins". Y el mensaje va firmado por Y.

Además, las transacciones se encadenan unas con otras: una transacción contiene también el hash de las transacción anterior. Para modificar una transacción... ¡habría que modificar todas las transacciones anteriores, y sus firmas!
-->

## Proof of work: Hashcash

Hashcash fue propuesto por Adam Back en 1997 para reducir el spam.

- Problema a resolver: queremos que un ordenador solo pueda enviar un correo electrónico por minuto.
- Solución: obligémosle a calcular 10.000.000 de hashes antes de que pueda enviar un correo.

> [Hashcash- A Denial ofServiceCounter-Measure](http://hashcash.org/papers/hashcash.pdf), Adam Back 2002


---

1. Crea una cadena con la dirección de correo destino
1. Añade la fecha de envío
1. Busca un número tal que el hash de todo esto empiece por 8 ceros

La única manera de que pueda hacer eso es "entreteniéndose" probando números uno después de otro

La idea es ajustar "el número de ceros iniciales" para que sepamos que tarde más o menos un minuto en encontrar el número

![bg w:100% right:40%](https://www.coinkolik.com/wp-content/uploads/2021/03/Proof-of-work-no-purple-line-730x410.jpg)

> http://ronny-roehrig.com/criptoavances/que-es-el-algoritmo-proof-of-work-pow-como-funciona/

---

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

## Minería

Se adaptó el X-Hashcash. Un bloque es así:

```
HASH DEL BLOQUE ANTERIOR
TRANSACCION 1: ALICE LE PAGA A BOB
TRANSACCIÓN 2: BOB LE PAGA A CHARLIE
...
1 BITCOIN PARA MÍ
COUNTER
```

Y minar es encontrar un COUNTER tal que el hash de ese bloque empiece por el-número-de-ceros que toque

SHA2-256(bloque)=000000000000000000000000000000000000000000000000000000000000000000000001... y 185 bits más

El primero que encuentre ese COUNTER, se lleva un bitcoin

---

https://btc.com/

![](images/btccom.png)

El número de ceros necesario se ajusta para que  más o menos cada 15 minutos alguien encuentre ese COUNTER: la dificultad es ajustable

---

![](images/btccom3.png)

---

Pincha en cualquiera de los bloques y verás las transacciones

![w:25em center](images/btccom2.png)

## Consenso distribuido

![bg right:50% w:100%](https://miro.medium.com/max/600/0*FCWGyPmN-wBK4wBe.jpeg)

Bitcoin funciona por consenso distribuidos: todos se tienen que poner de acuerdo en quién ha sido el primero en encontrar el COUNTER

Pero estamos hablando de dinero... un tema en el que pocas veces hay consenso y sí mucha competitividad

¿Qué pasa si algún nodo es egoísta y no reconoce que otro ha encontrado antes el hash?

> https://kasunindrasiri.medium.com/understanding-raft-distributed-consensus-242ec1d2f521

---

- Bit coin: red P2P de nodos
- Cada nodo está constantemente tratando de encontrar el COUNTER del bloque que provoque que el hash se inicie con un número determinado de ceros.
- Cuando lo consigue: lo anuncia a todos los nodos que conocen.
- Los demás nodos lo comprueban y reconocen y empiezan un nuevo bloque.

![bg right:50%](https://miro.medium.com/max/539/0*0qwTOWUxevWKigsv)

---
- A veces es imposible llegar a un consenso: [The Byzantine General Problem](https://es.wikipedia.org/wiki/Tolerancia_a_faltas_bizantinas)
- En Bitcoin se resuelve:
    - Creando una moneda nueva
    - Cuando los nodos en la cadena más pequeña "claudican" y desisten
- El protocolo funciona siempre que al menos la mitad de los nodos cooperen

![bg right:50% w:200%](https://academy.horizen.io/assets/post_files/technology/expert/2.4.1-distributed-consensus/longest_chain_D.jpg)

> https://academy.binance.com/en/articles/what-is-a-51-percent-attack

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
    - HMAC (integridad)
    - ...

## Referencias

- [Hashing Algorithms and Security - Computerphile](https://www.youtube.com/watch?v=b4b8ktEV4Bg)
- [But how does bitcoin actually work?](https://www.youtube.com/watch?v=bBC-nXj3Ng4)
- [Bitcoin: A Peer-to-Peer Electronic Cash System](https://bitcoin.org/bitcoin.pdf), Satoshi Nakamoto 2008
- [Hashcash - A Denial of Service Counter-Measure](http://hashcash.org/papers/hashcash.pdf), Adam Back 2002
- [The State of Hashing Algorithms — The Why, The How, and The Future](https://medium.com/@rauljordan/the-state-of-hashing-algorithms-the-why-the-how-and-the-future-b21d5c0440de)

---

<!-- _class: center -->

Continúa en: [Integridad](07-integridad.html)
