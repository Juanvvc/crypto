---
marp: true
title: Criptografía - Principios Básicos
author: Juan Vera
keywords: criptografía,principios
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
</style>

# Criptografía: conceptos básicos
<!-- _class: first-slide -->

Juan Vera del Campo

<juan.vera@campusviu.es>

# Hoy hablamos de...
<!-- _class: cool-list -->

1. [Servicios criptográficos: objetivos](#3)
1. [Estrategias de los sistemas seguros: seguridad por oscuridad, principios de Kerckhoffs y máxima de Shannon](#9)
1. [Primitivas criptográficas: hash, cifrado simétrico, cifrado asimétrico](#21)
1. [Protocolos criptográficos: composición de primitivas](#28)
1. [Conclusiones: resumen y referencias](#34)

Ejercicios: <https://github.com/Juanvvc/crypto/tree/master/ejercicios/01>


<!--
El glosario es un resumen de las trasparencias de este tema, y un recordatorio de las matermáticas que usaremos
-->

# Servicios criptográficos
<!--
_class: lead
header: 'Servicios criptográficos'
-->

¿Qué queremos proteger?

---

![bg left:40% w:100%](https://pics.filmaffinity.com/the_imitation_game-824166913-large.jpg)

Años 40: Alemania controla Europa y amenaza al resto del mundo

Sus comunicaciones radio están protegidas con "la cifra indescifrable"

¿Por qué pensaban que era indescifrable?

¿Cómo se descifró?

¿Qué hemos aprendido desde entonces?

## ¿Qué es la criptografía?

Protección de la comunicaciones a través de **medios desprotegidos** entre un emisor y uno o varios destinatarios

![bg right:40% w:100%](images/pexels-cottonbro-7319077.jpg)

...y eso es mucho más que mantener un mensaje secreto...

> Fondo: [(c) cottonbro](https://www.pexels.com/photo/clear-glass-bowl-on-white-table-cloth-7319077/). Free to use

<!--
Tradicionalmente hemos entendido la criptogafía como las técnicas para mantener un mensaje confidencial y que solo pueda leerlo la persona para la que está destinado.

Pero hay mucho más detrás: ¿cómo nos aseguramos que realmente solo el receptor puede leer un mensaje? ¿Es posible demostrar matemáticamente que solo el receptor puede leerlo? ¿ Y cómo se asegura el receptor que el emisor es realmente quien dice ser?
-->

## ¿Qué queremos proteger?

Recurso|Ejemplo
--|--
**El contenido de un mensaje**|¿Cuánto dinero se está transfiriendo?
**Las veces que se envía un mensaje**|¿Ha sido una transferencia o dos? Un atacante no puede repetir una transferencia, aunque no sepa de cuánto es
**Los participantes**|¿Seguro que el ordenante es Paco Pérez? ¿Seguro que está hablando con su banco?
**El no repudio**|Paco Pérez no podrá decir que no ordenó la transferencia

<!--
Solo el primer punto trata de mantener un mensaje secreto. Además vamos a querer saber con quién estamos hablando, entre otros servicios.

¡Si estamos hablando con un malo, da igual que el mensaje esté perfectamente cifrado!
 -->

## ¿Contra quién nos queremos proteger?

Atacante|Ejemplo
--|--
**Ladrón**|Persona con pocos recursos, ataques oportunistas
**Competidor**|Profesionalización, interés
**ATP - estado**|Recursos enormes, dedicación

La seguridad tiene costes:

- Coste de las tecnologías
- Complejidad en los procesos

Decidir, evaluar y asumir el riesgo de ataques contra los que no nos podemos proteger

<!--
¿Contra quién queremos proteger la información?

- Una persona que quiere consumir un servicio sin pagar
- Una persona que quiere invadir nuestra privacidad
- Un competidor que quiere acceso a nuestros documentos secretos
- Una grupo financiado por un estado nación
-->



## Servicios de seguridad

[New Directions in Cryptography](https://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.37.9720) (Whitfield Diffie y Martin Hellman, 1976) exploraba qué se necesitaba para que dos empresas pudiesen firmar un contrato mercantil:


- **Confidencialidad**: solo el legítimo destinatario debe poder ser capaz de leer el contenido del contrato o cualquier información asociada.
- **Integridad**: el destinatario debe ser capaz de verificar que el contenido del contrato no ha sido modificado por el camino... ni en el futuro
- **Autenticidad**: el destinatario debe ser capaz de verificar que el emisor es realmente el autor del contrato
- **No repudio**: nadie puede decir que ese no es el contrato que ha firmado
- **Otros**: autorización, acuerdo de claves, partición de secretos, PRNG...

> [New Directions in Cryptography](https://www.cs.utexas.edu/~shmat/courses/cs395t_fall06/dh.pdf), Whitfield Diffie y Martin Hellman en 1976. Hablaremos de esto en el [tema 5](05-asimetrica.html)
> Estándar: [NIST Special Publication 800-57 Part 1, Section 3](https://doi.org/10.6028/NIST.SP.800-57pt1r5)


<!--

El objetivo más evidente de un sistema criptográfico es alcanzar confidencialidad: no queremos que nadie pueda leer nuestras comunicaciones aparte de la persona a la que están destinadas

Pero un sistema que solo ofrezca confidencialidad no es seguro casi nunca. Por ejemplo, si estamos hablando con un adversario en vez de nuestro banco, da igual que nadie más pueda leer nuestras comunicaciones. Tenemos que estar seguros de que al otro lado está realmente el banco: autenticidad

En ocasiones, un adversario puede modificar un mensaje a pesar de que no sepa qué es lo que hay en él. O puede que lo realmente importante para un banco es asegurar que uno de sus clientes ordenó una trasferencia desde sus cuentas y no hacia sus cuentas.

Los objetivos de un sistema criptográfico son los servicios de seguridad que ofrece

El NIST es la agencia de estandarización de EEUU, y entre las cosas que estandariza también está la seguridad del gobierno de EEUU. Sus estándares son sencillos de leer e incluyen un glosario que viene muy bien para introducirse en la criptografía.

-->

## El problema que queremos resolver

Firma digital de un contrato entre dos empresas

- **Confidencialidad**: el contrato tiene que ser secreto para cualquier otra parte
- **Autenticación**: las empresas tienen que estar seguras de que están hablando con quien creen
- **Integridad**: ninguna de las dos empresas puede cambiar unilaterlamente el contrato
- **No repudio**: ninguna de las empresas podrá decir que no lo ha firmado

# Estrategias de los sistemas seguros
<!-- _class: lead -->

*The thing is secure if its outputs look like random junk*

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



<!--
Este es el modelo sobre el que trabajaremos: dos personas "Alice y Bob" comunicándose por un canal inseguro porque puede haber un adversario "Maloy" en medio.

Alice y Bob no tienen otra forma de comunicación: no pueden confirmar una operación bancaria enviada por correo electrónico usando una clave enviada al teléfono, por ejemplo. En criptografía asumiremos que no existen estas vías alternativas de comunicación, aunque en la realidad sí existen y los utilizamos en la vida real para mejorar aún más la seguridad del sistema.
-->

## Grados de seguridad
<!-- _class: with-warning -->

- **Seguridad incondicional**: un atacante no puede descifrar el mensaje aunque tenga infinito dinero o infinito poder computacional.
- **Seguridad computacional**: un atacante podría teóricamente descifrar el mensaje, pero no es razonable que lo haga porque lleva demasiado tiempo, dinero o recursos. Por ejemplo, millones de años o más memoria de la que cabe en el universo.

Aunque la seguridad perfecta puede parecer lo mejor, veremos que no es práctica: nos conformaremos con la seguridad computacional

> Hablaremos de esto en el [tema 3](03-simetrica.html)

<!--

Tenemos que **poder** **proteger** los mensajes.

Veremos que existen protocolos que ofrecen seguridad incondicional, pero su utilización es tan pesada que no es práctica, y actualmente se prefiere la seguridad computacional
-->

## Seguridad computacional
<!-- _class: with-info -->

La criptografía actual se basa en la seguridad computacional: una comunicación será **probablemente** segura durante las próximas **décadas**. 

- Solo con cierta probabilidad matemática
- Solo durante un tiempo determinado

Para poder diseñar un sistema seguro moderno empezamos con la pregunta: ¿con qué probabilidad queremos que ningún atacante pueda leer el mensaje durante la próxima década?

> Hablaremos de esto en el [tema 4](04-complejidad.html)


## Seguridad por oscuridad
<!-- _class: with-warning -->

**Falacia**: "Nadie sabe cómo es nuestro sistema, y por tanto es seguro"

- Mantener el secreto del código fuente del software.
- Mantener el secreto de algoritmos y protocolos utilizados, o utilizar un protocolo ad-hoc o inventado.
- Adopción de políticas de no revelación pública de la información sobre vulnerabilidades.
- Confiar en configuraciones no estándar (por ejemplo, poner el servidor en el puerto 3181)

Confiar solo en "la oscuridad" para ofrecer seguridad no es buena idea.

<!--
La seguridad por oscuridad es pensar que un sistema secreto es más seguro que un sistema conocido. En realidad, es muy difícil mantener un sistema en secreto. Además, la criptografía está llena de "trampas" y razonamientos no evidentes. Es muy difícil que unas pocas personas puedan diseñar un sistema realmente seguro y además mantenerlo en secreto. Eso es lo que se llama "seguridad por oscuridad", y fiar la seguridad a la oscuridad no es buena idea, como nos ha enseñado la experiencia.

Un sistema no es inseguro por ser oscuro. Es simplemente oscuro. Basar tu seguridad en la oscuridad lo consideramos una mala idea porque los hackers pueden saber más que tú. No hay ningún error lógico en querer basar tu seguridad en la oscuridad. Simplemente, la experiencia nos dice que no es buena idea, y que los sistemas cuya seguridad se basa en la oscuridad caen antes.

PERO que un sistema sea seguro de por sí, utilizando protocolos realmente seguros y buenas prácticas criptográficas, Y ADEMÁS lo ocultamos al mundo, es sin duda una buena idea que no perjudica. Tendrás a los adversarios entretenidos para intentar entender tu sistema, y cuando lo consigan verán que es un indescifrable AES-512.

No bases tu seguridad en la oscuridad, pero añadir un poco de oscuridad siempre ayuda.
-->

---

![center](https://res.cloudinary.com/practicaldev/image/fetch/s--NDXZXYxb--/c_imagga_scale,f_auto,fl_progressive,h_420,q_auto,w_1000/https://www.explainhownow.com/assets/images/security_through_obscurity_cover.png)

> https://www.robohara.com/?p=1439
> <https://dev.to/ctrlshifti/what-security-through-obscurity-is-and-why-it-s-evil-47d5>


<!--
![bg right:75%](images/security-through-obscurity-is-everywhere.jpg)
-->

## Principios de diseño
<!-- _class: center -->

Si la seguridad por oscuridad no es recomendable...

...¿qué principios de diseño tenemos que seguir?

## Principios de Kerckhoffs
<!-- _class: smallerfont -->

<https://en.wikipedia.org/wiki/Kerckhoffs%27s_principle>

![bg left:33%](images/Auguste_Kerckhoffs.jpg)

1. **Si el sistema no es teóricamente irrompible, al menos debe serlo en la práctica.**
1. **La efectividad del sistema no debe depender de que su diseño permanezca en secreto.**
1. ~~*La clave debe ser fácilmente memorizable de manera que no haya que recurrir a notas escritas*~~
1. *Los criptogramas deberán dar resultados alfanuméricos*
1. ~~*El sistema debe ser operable por una única persona*~~
1. **El sistema debe ser fácil de utilizar.**

<!-- Kerckhoffs enunció sus principios en 1883.

Los principios 1, 2 y 6 guiarán todo el desarrollo de la criptografía actual

1. Confidencialidad computacional (capítulo 3)
2. No basarse en seguridad por oscuridad
3. Requisito de complejidad (capítulo 4)

Pero atención: la criptografía actual

- En cuanto a clave, tienen que ser específicamente aleatorias y por tanto no
  fácilmente memorizables.
- Los resultados son binarios, y por tanto no son alfanuméricos en general. Aún
  así y aunque no sea estrictamente necesario, la criptografía tiene como
  "costumbre" guardar claves codificadas en Base64, es decir, usando solo
  caracteres imprimibles. El principio 4 se sigue cumpliento parcialmente, aunque
  no sea estrictamente necesaria.
- El sistema completo suele necesitar de varias personas para operar, y en
  particular una "tercera parte de confianza"

Kerckhoffs definió sus principios para un contexto en que una persona solitaria
pudiese utilizar el criptosistema fácilmente y escribir el resultado. Ahora
tenemos la ayuda de ordenadores y esos principios no son ni necesarios, ni
recomendables.

Eso nos lleva a que: la seguridad a veces es cuestión de opinión. "Buenas
prácticas". "Recomendaciones". Por ejemplo, el NIST solo emite recomendaciones.
Pero son recomendaciones muy informadas.

-->

## Máxima de Shannon
<!-- _class: with-success -->

![bg left:33%](images/220px-ClaudeShannon_MFO3807.jpg)

*El atacante conoce el sistema*

**Claude Elwood Shannon (1906-2001)**

Diseña el sistema asumiendo que el atacante sabe qué hacer para cifrar o descifrar, pero no conoce la clave

> [Communication Theory of Secrecy Systems](http://netlab.cs.ucla.edu/wiki/files/shannon1949.pdf), Claude E. Shannon, Bell System Technical Journal, vol.28-4, page 656--715, Oct. 1949.
> Hablaremos más de Shanon en el [tema 3](03-simetrica.html)

<!-- Shanon es un gran matemático del siglo XX, que creó la teoría de la información. Le debemos la teoría detrás de la criptografía, los archivos comprimidos, la codificación digital...

Su máxima se contrapone a la "seguridad por oscuridad". Es decir, la seguridad de un sistema secreto solo será segura mientras el sistema sea secreto. ¿Y si deja de serlo? ¿Y si pensamos que es seguro, pero no lo es?

El paper enlazado es una estupenda introducción a los conceptos fundamentales de la criptografía y se recomienda mucho su lectura
-->

## Gestión de claves

![bg left:30% h:100%](https://securityledger.com/wp-content/uploads/2021/07/Lea_Kissner.jpeg)

*La criptografía es una herramienta para convertir un montón de problemas diferentes en un problema de gestión de claves*

Lea Kissner, antigua ingeniera principal de seguridad de Google

- **Contraseña**: palabra que utilizamos para entrar en un sistema. "Sesamo"
- **Clave criptográfica**: conjunto de números que dan seguridad a un sistema: "82198329382371291821201"

<!--
Si la clave es lo único que tiene que ser secreto, tenemos que protegerla a toda costa.

En este curso no estudiaremos cómo proteger las claves, pero tened en cuenta que, al ser la pieza central de la seguridad de un sistema, es necesario que los usuarios de criptografía dispongan de algún modo de gestión segura de claves criptogrtáficas

Una contraseña no es lo mismo que una clave criptográfica. Las contraseñas suelen ser mucho más inseguras que una clave (a veces no son aleatorias o están pensadas para que las pueda recordar un humano) A veces las contraseñas serán el primer paso para entrar en un sistema seguro, pero **no son buenas claves criptográficas**

En muchas ocasiones un sistema se romperá no por que la criptopgrafía sea débil, sino porque incluye un paso de control con contraseña que es habitualmente la parte más débil de un protocolo.
-->

# Primitivas criptográficas
<!--
_class: lead
header: 'Primitivas criptográficos'
-->

---

La criptografía actual se basa en **composición** de técnicas primitivas:

- Composición de **operaciones matemáticas** que crean "**puertas criptográficas**" (*cryptographic gates*).
- Composición de puertas que crean **algoritmos**.
- Composición de algoritmos que crean **protocolos de seguridad**.

La composición es compleja y todo debe funcionar como un reloj.

<!--
- **Sin clave**: el emisor usa sólo el mensaje $m$ como argumento de la función criptográfica. Ejemplo: hash.

- **Clave simétrica**: misma clave $k$ para cifrar y descifrar un mensaje $m$. Emisor y receptor deben tener la misma clave. Ejemplo: AES, ChaCha...

- **Clave asimétrica**: claves diferentes para cifrar (pública) y descifrar (privada) un mensaje $m$. El emisor debe conoce la clave pública del receptor. Ejemplo: RSA
-->

---

![](images/cta2296-fig-0002-m.jpg)

## Primitivas: hash

Calcula un resumen sobre un mensaje. Para validar el resumen, se vuelve a calcular y se compara

```sh
> cat test.mp3| sha256sum 
71a3644f14bdd5d2ebf56aaca440ad3c2b76b13f6a0708a9918e6b8bfabaeff3  -
```

> Hablaremos del hash en el [tema 6](06-hashes.html)

## Primitivas: clave simétrica
<!-- _class: with-warning -->


- El algoritmo de cifrado y el de descrifrado pueden ser el mismo
- **Una sola clave** para cifrar y descifrar

```
> openssl aes-256-cbc -a -salt -in test.mp3 -out test.aes -pass pass:1234

> openssl aes-256-cbc -d -a -salt -in test.aes -out test2.mp3 -pass pass:1234
```

> Hablaremos del cifrado simétrico en el [tema 3](06-simetrico.html)


**AVISO**: pasar el password como argumento no es buena práctica. Solo se presenta aquí como ejemplo

## Primitivas: clave asimétrica

- Un algoritmo para cifrar y otro para descifrar
- **Una clave para cifrar y otra para descrifrar**
- La clave de cifrado suele ser conocida por todos, por eso se llama también "pareja de clave pública y privada".

```sh
# Generar par de claves
> openssl genrsa -aes256 -out private.key 2048
> openssl rsa -in private.key -pubout -out public.key
> cat public.key

> openssl rsautl -encrypt -pubin -inkey public.key -in test.mp3 -out test.rsa  
RSA operation error
4345576940:error:04FFF06E:rsa routines:CRYPTO_internal:data too large for key size
```

> Hablaremos del cifrado asimétrico en el [tema 5](05-asimetrico.html)


<!--
Aquí vemos un error provocado porque estamos usando la primitiva defectuosa. Las primitivas deben utilizarse en los contextos en que fueron diseñadas, y apoyarse entre ellas.
-->

## Servicios de seguridad a primitivas

Objetivo|Primitiva
--|--
**confidencialidad**|cifrado simétrico, cifrado asimétrico
**integridad**|hash, firma simétrica, firma asimétrica
**autenticidad**|firma simétrica, firma asimétrica
**no repudio**|firma asimétrica
**compartir**|clave simétrica, acuerdo de clave

<!--
Ya hemos visto unas pocas primitivas. ¿Qué servicios de seguridad ofrece cada una?

Lo normal será que no queramos que el sistema ofrezca un solo servicio sino varios de ellos. Es decir, juntar primitivas criptográficas.

La unión de primitivas criptográficas crea un protocolo criptográfico
-->

# Prococolos criptográficos
<!--
_class: lead 
header: 'Protocolos criptográficos'
-->

*If A is a secure thingamajig, then B is a secure doohickey*

## Protocolo de seguridad

La secuenciación de mensajes y la composición de primitivas se materializa en un "protocolo"

El protocolo (el lenguaje) se define a partir de:

- Formatos/estructuras de los mensajes o "sintaxis" (funciones/algoritmos, secuenciación)
- "Máquina de estados" (que tipos de mensajes son posibles después de otros)
- Especificación del significado de mensajes y/o estado, "semántica"

El protocolo es un eslabón de la cadena de seguridad, tan importante como pueden ser las primitivas

## Seguridad del protocolo de seguridad.

La fortaleza (o debilidad) de la criptografía depende de todos los eslabones de la cadena:

- **algoritmos** (diseño, criptoanálisis)
- **algoritmos** (dimensionado, longitud de claves, security strength)
- **protocolos** (estructura, secuenciación)
- **implementación** (condiciones de uso, abuso de buffers, abuso de la máquina de estados)
- **gestión** (PKI, gestión de certificados...)

## Composición de algoritmos

Habitualmente no usamos una única primitiva/función criptográfica:

- **objetivos múltiples**: me interesa confidencialidad, integridad y autenticidad simultáneamente para la transmisión del mensaje $m$
- **eficiencia**: los algoritmos simétricos son varios órdenes de magnitud más rápidos que los asimétricos
- **robustez**: muchas primitivas (individuales) no devuelven error en caso de que algo vaya mal (una firma asimétrica simplemente devuelve un mensaje firmado distinto)
- **secuencias de mensajes**: nos interesa proteger secuencias de mensajes $\{m_1,m_2, ..., m_n\}$ o diálogos $\{m_{a_1},m_{b_1},m_{a_2},m_{b_2}, ...\}$ para que no llegen mensajes repetidos o desordenados.

<!--
# Ejemplo de composición: cifrado eficiente

```sh
# Generar par de claves
> openssl genrsa -aes256 -out private.key 2048
> openssl rsa -in private.key -pubout -out public.key
> cat public.key

# Generar clave simétrica y cifrar con ella
> openssl rand -hex 64 -out key.bin
> openssl aes-256-cbc -a -salt -in test.mp3 -out test.aes-rsa -pass file:./key.bin

# Cifrar clave simétrica con clave pública
> openssl rsautl -encrypt -inkey public.key -pubin -in key.bin -out key.bin.enc

# Descrifrar clave simétrica con clave privada
> openssl rsautl -decrypt -inkey private.key -in key.bin.enc -out key.bin

# Descifrar archivo con clave simétrica
> openssl aes-256-cbc -d -a -salt -in test.aes -out test2.mp3 -pass file:./key.bin

```

<!--
Aquí vemos la manera correcta de usar la primitiva que dio error en el caso anterior:

- Ciframos la información de gran tamaño con una clave simétrica
- Usamos la primitiva de cifrado asimétrico para cifrar la clave simétrica, y solo ella
- Enviamos a la otra parte el archivo cifrado y el cifrado de la clave simétrica
- La otra parte primero descifra la clave simétrica y después con ella descifra el mensaje.
- ->

## Ejemplo de composición: secuencias

La sesión protege de que los mensajes (integridad de sesión):

- no se pierdan
- no se dupliquen
- no se desordenen

Las primitivas criptográficas anteriores no cumplen con estos objetivos (e.g. un atacante borrando un mensaje no tiene contramedida); puede considerarse la sesión como una primitiva criptográfica adicional

---

Se puede solucionar con:

- añadiendo un identificador de secuencia ${1||m_1,2||m_2,...}$
- añadiendo el hash del mensaje anterior {${1,2||hash(m_1),3||hash(m_2),...}$

<!--
Es decir, los mensajes son eslabones de una cadena, cada mensaje tiene el hash del eslabón anterior.

Casi, casi, hemos definido una blockchain como bitcoin
- ->

-->

## Objetivos: "otros"

- **Autorización**: ¿está el interlocutor autorizado a acceder a estos datos?
- **Acuerdo de claves**: permite que un grupo de actores generen una clave sin que nadie externo al grupo la conozca
- **Partición de secretos**: permite repartir un secreto entre un grupo de actores, exigiendo un mínimo de actores para recomponerlas
- **Esteganografía**: queremos ocultar que dos personas están hablando
- **Anonimato**: el emisor quiere ocultar su identidad
- etcétera

<!--
Nos centraremos en los servicios de confidencialidad, integridad y autenticación. Además, podemos conseguir no-repudio como consecuencia de juntar autenticidad e integridad.

También veremos, aunque a más alto nivel, los servicios de acuerdo de claves, PRNG, partición de secretos... porque están relacionados con los primeros

Otros servicios como la autorización, aunque sin duda son importantes para que un sistema sea seguro, quedan fuera de este curso por limitación de tiempo.
-->

---

[![w:33em center](images/rely-attack.png)](https://www.youtube.com/watch?v=uxzm_6SYBFo)

> https://www.youtube.com/watch?v=uxzm_6SYBFo

<!--
Aquí tenemos un ejemplo de un protocolo de comunicaciones donde el objetivo no es la confidencialidad.

Estos son unos ladrones robando un coche, que se abre cuando la llave está cerca. La persona de la derecha está utilizando una antena enorme para "hacer relay" de la comunicaciones entre la llave (que se supone dentro de la casa, cerca de la pared) y el coche.

Aquí el protocolo no tiene que proteger la confidencialidad del mensaje: todos sabemos que la llave envía "ABRETE". Fíjate que el protocolo tampoco está protegido con contraseñas, ni con una firma digital.

Lo que se necesita en esta caso es detectar cuándo el atacante está accediendo a los mensajes y ampliando su radio de acción diseñado

¿Se te ocurre alguna manera de proteger contra esta situación?
-->

# Conclusiones
<!--
_class: lead
header: ''
-->

---

- Diseña el sistema pensando que el atacante lo conoce.
- Servicios básicos de seguridad: **confidencialidad**, **integridad**, **autenticación**, **no repudio**.
- Técnicas para ofrecer estos servicios: criptografía simétrica, criptografía asimétrica, intercambio de claves, firma digital, funciones de hash, protocolos (composisión de técnicas)
- La seguridad del sistema depende de que todos los engranajes encajen totalmente: algoritmos escogidos, sus parámetros de configuración, los protocolos utilizados...

## Referencias

- Primer capítulo de "[*The Joy of Cryptography*](https://joyofcryptography.com/)" de Mike Rosulek, 2021
- [Recommendation for Key Management: Part 1 – General](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-57pt1r5.pdf), NIST SP 800-57 Part 1, Revision 5, mayo 2020. Capítulos 2 (glosario) y 3 (servicios), aunque el resto serán de utilidad en el resto del curso
- Introducción del paper [Communication Theory of Secrecy Systems](http://netlab.cs.ucla.edu/wiki/files/shannon1949.pdf), Claude E. Shannon, Bell System Technical Journal, vol.28-4, page 656--715, Oct. 1949.

---
<!-- _class: center -->

Continúa en: [Criptografía clásica](02-historia.html)

Es muy recomendable tener a mano el [glosario](A1-glosario.html) para recordar los conceptos fundamentales
