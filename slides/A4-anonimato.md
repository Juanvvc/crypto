---
marp: true
title: Criptografía - Anonimato
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

**Tema 11: Servicio de anonimato**

Juan Vera del Campo

juan.vera@campusviu.es

# Como decíamos ayer...

Servicios de seguridad:

- Los clásicos: confidencialidad, autenticidad, integridad, no repudio
- Auxiliares: acuerdos de clave, anonimato...

En este tema veremos cómo usar la criptografía para ofrecer el servicio de anonimato. Así aprendemos un nuevo servicio, afianzamos conceptos que ya sabemos, conoceremos nuevos protocolos y exploramos qué capacidades tienen los adversarios

# Hoy hablamos de...

- [Comunicaciones anónimas](#4)
- [Enrutamiento onion](#16)
- [Servicios onion](#27)
- [Referencias y ejercicios](#37)

# Comunicaciones anónimas
<!-- _class: lead -->

---

![center](https://www.htl.london/images/top-tips-to-combat-voip-eavesdropping.jpg)

Los servicios clásicos de seguridad (*confidencialidad*) aseguran que nadie que escuche pasivamente una comunicación sabe qué estamos diciendo. También evitan ataques activos man-in-the-middle (*integridad*, *autenticación*). Todo esto lo ofrece TLS ([tema 9](09-protocolos.html))

**Pero no evitan que se sepa quién habla con quién**: el cifrado se aplica en la capa de aplicación, no estamos cifrando los paquetes de red que incluyen IP origen e IP destino

**Servicio de anonimato**: impide que un atacante sepa quién está hablando con quién

## Recordatorio: un paquete IP
<!-- _class: extra-slide -->

![center w:20em](https://upload.wikimedia.org/wikipedia/commons/7/71/IPv4_Packet_-en.svg)

- Un paquete IP incluye obligatoriamente las direcciones IP reales de origen y destino
- Todos los routers en el camino tienen que conocer estas direcciones para poder enrutar un mensaje
- Todos los routers en el camino saben quién habla con quién

## Estructura de Internet

Los usuarios nos conectamos a un servidor ISP... ¿y después qué?

Los ISPs se conectan entre ellos en puntos neutros nacionales (IXP, *Internet Exchange Point*)

Los IXP se conectan entre ellos con cables submarinos (entre otros)

Los servidores normalmente están "en la nube"

![bg w:100% right:40%](https://upload.wikimedia.org/wikipedia/commons/3/36/Internet_Connectivity_Distribution_%26_Core.svg)

> Puntos neutros: https://es.wikipedia.org/wiki/Punto_neutro
> Ejemplo: Espanix http://www.espanix.net/es/traffic.html

---

![w:30em center](images/submarines-cables.png)

Muchos de estos cables submarinos son propiedad de Google

> https://www.submarinecablemap.com/#/

---

![center](https://1.cms.s81c.com/sites/default/files/2019-12-30/LS003.jpg)

Gran parte de la cloud pertenece a Amazon

## ¿Quién sabe a dónde te conectas?
<!-- _class: with-warning -->

- Tu ISP lo sabe
- Tu gobierno, en el punto neutro, sabe todo lo que tenga que salir de tu ISP
- Google, en el cable submarino, sabe todo lo que salga del país
- El gobierno de destino, en su puntro neutro, sabe quién se está conectando
- Amazon, propietaria de la cloud en el servidor destino sabe quién se conecta
- El servidor destino sabe quién se conecta y qué se está diciendo

Todos estos actores tienen la posibilidad de saber con quién te conectas, pero... ¿lo están haciendo realmente? [Great Chinese Firewall](https://en.wikipedia.org/wiki/Great_Firewall), [ECHELON](https://en.wikipedia.org/wiki/ECHELON), [Data Retention Directive](https://en.wikipedia.org/wiki/Data_Retention_Directive)...

> https://euobserver.com/opinion/146376
> https://www.eff.org/nsa-spying
> https://ssd.eff.org/en

# Anonimato en Internet, ¿sí o no?
<!-- _class: extra-slide smallest-font -->

A favor del anonimato:

- Querer intimidad NO equivale a tener algo que ocultar
- Nada que ocultar... mientras estés 100% de acuerdo con la visión y las políticas de tu gobierno
- Esta gente está buscando delincuentes. Podrías ser la persona más inocente del mundo, pero si alguien programado para ver patrones de delincuencia analiza tus datos, no va a encontrarte a ti: va a encontrar a un delincuente. *Edward Snowden*
- Si no tenemos nada que ocultar, ¿por qué estamos bajo vigilancia? La privacidad debería ser un derecho a menos que se haga algo que levante sospechas legítimas
- La intimidad no es para esconderse; la intimidad es para protegerse
- Si se prohíben las comunicaciones anónimas... los malos seguirán usándolas igualmente como usan armas prohibidas

En contra del anonimato:

- Controlar quién se conecta con quién permite a nuestros gobiernos detectar terroristas o pederastas
- Las tecnologías de comunicaciones anónimas **realmente ayudan** a los terroristas y pederastas
- La identificación de las personas puede rebajar el ciberacoso en Internet
- La identificación de las personas impide que los niños accedan a contenido inadecuado

> https://www.es.amnesty.org/en-que-estamos/blog/historia/articulo/siete-razones-por-las-que-no-tengo-nada-que-ocultar-es-la-respuesta-equivocada-a-la-vigilancia-mas/
> https://www.bbc.com/future/article/20170529-the-reasons-you-can-never-be-anonymous-again
> https://www.pewresearch.org/internet/2017/03/29/the-future-of-free-speech-trolls-anonymity-and-fake-news-online/

<!--
No es el objetivo de este curso no es evangelizar sobre la conveniencia del anonimato en Internet. Ahí tienes algunos argumentos a favor y en contra y enlaces con discusiones y propuestas

Vamos de describir unas tecnologías que pueden usarse para objetivos terriblemente perversos pero también para proteger la libertad de las personas y para saber cómo trabajan los ciberdelincuentes. El uso que les des es responsabilidad tuya
-->

# ¿Quién es el adversario?
<!-- _class: extra-slide -->

- No quiero que el gobierno conozca mis ideas políticas
- No quiero que mis compañeros de trabajo conozcan mi orientación sexual
- No quiero que el jefe sepa que estoy buscando trabajo
- No quiero que Google sepa que fumo
- No quiero que mis clientes encuentren fotos de la fiesta de anoche
- No quiero que la policía sepa qué he hecho
- No quiero que X sepa que soy yo quien le acosa


## Solución 1: servidores anónimos y adversarios
<!-- _class: with-success -->

[ProtonMail](https://protonmail.com/) es un servicio de correo anónimo: nunca le dirá a las autoridades quién envió un correo. **PERO** alguien controlando las comunicaciones sabe quién estaba conectado a ProtonMail a la hora de envío de un correo.

ProtonMail puede ser perfectamente válido para tus seguridad: es necesario "identificar a tú adversario" para decidir el mejor método de protección.

- ¿El adversario es tu pareja? Es suficiente el modo seguro del navegador
- ¿Es tu empresa? VPN, la empresa tendrá acceso al firewall y sabe que te has conectado a Protonmail
- ¿Es el sistema judicial? ProtonMail no enviará registros a ningún juez
- ¿Es un gobierno? Tor, porque pueden controlar comunicaciones nacionales

<!--
Ojo: decidir la potencia que tiene tu adversario sirve para todos los sistemas de seguridad que hemos visto.
-->

## Solución 2: CROWDS y k-anonimato

1. Organízate con amigos para crear una red de $k=6$ personas (tú y 5 más). $p=\frac{k-1}{k}=\frac{5}{6}$
1. Si quieres descargar algo, con probabilidad $p$ le pides el favor a un amigo, y con probabilidad $1-p$ lo haces tú.
1. El amigo hace lo mismo: con probabilidad $p$ le pasa el favor a otro (¡puedes ser tú!), y con probabilidad $1-p$ lo hace él.
1. Así hasta que alguien hace la petición.
1. El servidor no sabe quién de las $k$ personas ha hecho la petición: **k-anonimato**.

![bg w:100% right:35%](images/crowds.png)

> Michael Reiter and Aviel Rubin (June 1998). "[Crowds: Anonymity for Web Transactions](https://web.archive.org/web/20051212103028/http://avirubin.com/crowds.pdf)" (PDF). ACM Transactions on Information and System Security.

<!--
OJO: esto funciona si confiamos en todos los amigos. Ellos colaborarán porque les conviene, pero hay que estar seguros de que ninguno de ellos es realmente "un topo". En este caso, el k-anonimato se reduce

CROWDS fue un sistema teórico, nunca se ha implementado como tal. Pero esta idea de k-anonimato se aprovecha en muchos otros sistemas. Además, el sistema de CROWDS es óptimo: no se puede tener más anonimato que el ofrecido por CROWDS.

Problema principal de CROWDS: no es posible predecir cuánto tiempo tardará un mensaje en salir de la red. ¡Un mensaje puede estar rebotando dentro de CROWDS para siempre!
-->

## Solución 3: Mix Networks y VPN
<!-- _class: with-warning -->

![center](https://upload.wikimedia.org/wikipedia/commons/a/aa/Chaum_Mix.svg)

1. Contrata los servicios de alguien que hace las peticiones por ti: [Mix Network](https://en.wikipedia.org/wiki/Mix_network). Por ejemplo: una VPN
1. La VPN hace las peticiones en nombre de sus $k$ clientes. Para evitar timing attacks, las mezcla entre ellas
1. Ningún observador externo puede correlar peticiones que entran en el Mix y las que salen (¡siempre que haya suficientes entradas!)

Problema: ¿seguro que la VPN no está logueando qué hacemos?

# Enrutamiento onion
<!-- _class: lead -->

## Solución completa: Tor

![center](https://upload.wikimedia.org/wikipedia/commons/1/15/Tor-logo-2011-flat.svg)

Tor (sigla de *The Onion Router* - El Enrutador Cebolla) es un proyecto con el objetivo de crear una red de comunicaciones de baja latencia y superpuesta sobre internet, en la que el encaminamiento de los mensajes intercambiados entre los usuarios no revela su identidad (dirección IP) y que mantiene la integridad y el secreto de la información que viaja por ella, y que además sea muy sencillo de utilizar.

- Navegador: Tor browser: https://www.torproject.org/download/
- *Daemon* de enrutamiento: para línea de comandos
- Tor Relays, ejecutados por voluntarios en Internet

## Usos
<!-- _class: with-warning -->

- Navegación anónima: "Web normal"
    - Para el usuario: anónimo
    - Para el servidor: nada especial, el servidor no tiene por qué saber que el usuario es anónimo (pero ojo: algunos servidores detectan y expulsan a los usuarios que vienen de Tor)
- Navegación .onion: "Dark web"
    - Para el usuario: anónimo
    - Para el servidor: anónimo
- Si eres un investigador analizando malware, no querrás que los malos te identifiquen: ¡utiliza navegación anónima!

![bg right:30%](https://www.silicon.es/wp-content/uploads/2013/10/Fuente-Shutterstock_Autor-Tomas-Urbelionis_anonimato-anonimo.jpg)



<!--
Aparte de las razones que hemos visto para utilizar navegación anónima, hay una más: si eres "de los buenos", a veces querrás visitar las webs "de los malos". Y casi nunca querrás avisar de que estás investigándoles.

- Descarga del malware que están usando, sin avisarles de qué país vienes y por tanto sin avisarles de que los has descubierto: si un malo sabe que los has descubierto, puede explotar "la bomba" ransomware inmediatamente. Durante una investigación conviene que los malos no sepan quién eres.
- Visita a sus páginas web, a ver si realmente tienen información de tus clientes
- ...
-->

## Surface, deep and dark web
<!-- _class: extra-slide -->

- **Surface web**: la web visible por Google
- **Deep web**: no visible por Google o similares. Parte privada de foros, correos electrónicos, intranets de empresa, bases de datos...
- **Dark web**: solo accesible con navegadores especiales y conociendo el enlace .onion

![bg right:50% w:100%](https://upload.wikimedia.org/wikipedia/commons/1/1f/Deepweb_graphical_representation.svg)


<!--
Deep y dark web a veces se confunden. Esta es una propuesta de definiciones muy utilizada en la literatura para distinguie la web normal que no puedes encontrar en Google, porque es privada, de la web que no puede ser accedida con normalidad.
-->

## Navegación normal

- Si usamos HTTPS, nadie sabe qué transmitimos
- Pero hay muchos actores que saben que estoy hablando con un servidor
- Y el servidor lo sabe todo

![right:60% bg w:100%](https://www.eff.org/files/tor-https-1.png)

> https://www.eff.org/pages/tor-and-https

<!--
Como hemos estado viendo en todas estas sesiones, HTTPS ofrece confidecialidad, autenticidad e integridad: nadie sabe qué noticia estoy leyendo de elpais.com

- Excepto elpais.com, que sabe qué IP tengo y qué leo, y lo puede compartir con cualquiera
- Mi ISP también sabe que estoy conectándome a elpais.com
- Y los IXP, servidores de cloud, ISP destino... tienen que saber que yo estoy conectándome con elpais.com para poder enrutar mis mensajes. Auque no sepan qué página descargo, todo ellos saben que alguna página será. Incluso pueden sospechar cuál es midiendo tamaño de la conexión, tiempos de lectura...
-->

## Navegación anónima

- El servidor no sabe qué IP ha realizado la petición
- Nuestro ISP sabe que estamos usando Tor
- Los actores saben que alguien está usando Tor

![right:60% bg w:100%](https://www.eff.org/files/tor-https-2.png)

> https://www.eff.org/pages/tor-and-https

<!--
- Si usamos comunicaciones anónimas como Tor, todo el mundo verás que hay alguien en Tor intentando conectarse a algún sitio. Pero ningún actor conoce todos los datos: la IP del cliente y la IP del servidor.
- OJO: si utilizamos un usuario y contraseña... elpais.com sabe quiénes somos aunque no sepa en qué IP estamos, y se lo puede contar a cualquiera
-->

## Navegación anónima: proceso

<!-- _class: two-columns smaller-font -->

1. Alice **conoce** una lista de enrutadores Tor
1. Alice **crea** una cadena (circuito) de enrutadores: 1, 2, 3
1. Alice envía a $1$ el mensaje: $E_{pk1}(2|E_{pk2}(3|E_{pk3}(Bob|MSG)))$
1. $1$ descifra el mensaje, y se encuentra que es un mensaje cifrado para $2$. Lo reenvía
1. $2$ descifra el mensaje, y se encuentra que es un mensaje cifrado para $3$. Lo reenvía
1. $3$ descifra el mensaje, y se encuentra que es un mensaje para $Bob$. Lo reenvía

![center w:30em](https://www.wordfence.com/wp-content/uploads/2015/12/HowTorWorks_1340px.png)

> https://www.wordfence.com/learn/the-tor-network-faq/

<!--
Este esquema se parece un poco a CROWDS, pero Alice puede controlar la longitud del circuito. Normalmente es 3 ó 4 saltos. Alice cambiará el circuido cada 10 minutos, aproximadamente. O más bien: el servicio de Tor de Alice cambiará el circuito automáticamente, sin que Alice tenga que hacer nada

Alice debería buscar relays en países bien diferenciados, y quizá aquellos entre los que no haya "buen intercambio de datos", es decir, entre diferentes "bloques mundiales"
-->

## Enrutamiento "cebolla", en detalle
<!-- _class: smallest-font -->

- Alice escoge un nodo $3$ para que reenvíe un mensaje a Bob, y lo cifra con la clave pública de $3$: $m_3=E_{pk3}(Bob|MSG)$
    - Solo $3$ puede descifrar $m_3$, ya que solo $3$ tiene su clave privada.
    - $3$ sabe que el mensaje es para Bob, y conoce el mensaje a menos que Alice use TLS para comunicarse con Bob, lo que es **obligatorio**.
    - Si Alice le enviase $m_3$ directamente a Bob, Bob sabría que el mensaje viene de Alice
- Para evitar que $3$ la identifique, Alice envía $m_3$ a $2$ diciendo que se lo reenvía a $3$: $m_2=E_{pk2}(3|m_3)=E_{pk2}(3|E_{pk3}(Bob|MSG))$
    - $2$ sabe que el mensaje viene de Alice, pero no sabe a dónde va: solo sabe que el siguiente paso es $3$
    - Nadie más que $2$ puede descifrar $m_2$
- Alice puede hacer esto varias veces para mejorar su anonimato: Alice envía un mensaje $m_1=E_{pk1}(2|m_2)$ a $1$ para que lo abra y se lo reenvíe a $2$, que lo abrirá y lo reenviará a $3$, que lo abrirá y lo reenviará a Bob.

![bg right:30%](https://upload.wikimedia.org/wikipedia/commons/8/8e/Nina_Rusa._Mu%C3%B1eca_Rusa.JPG)

> https://en.wikipedia.org/wiki/Onion_routing

<!--
Una explicación más detallada de la transparencia anterior: el enrutamiento onion es como un ogro, tiene capas. También es como las muñecas rusas, una dentro de otra.
-->

## Enrutamiento "cebolla", en dibujos

![center w:30em](https://geekytheory.com/wp-content/uploads/2013/10/onion-routingf-keys.png)

![center w:20em](https://upload.wikimedia.org/wikipedia/commons/e/e1/Onion_diagram.svg)

> https://es.wikipedia.org/wiki/Encaminamiento_cebolla

<!--
Esta es la transparencia anterior, pero con explicación gráfica del enrutamiento "cebolla"
-->

---

![center w:28em](https://geekytheory.com/wp-content/uploads/2013/10/onion-routing-4.png)

<!--
El sistema funciona también como una mix network: hay mucha gente usándolo a la vez, así que no es fácil correlar las entradas y las salidas de la red ni siquiera para un adversario muy poderoso que sea capaz de monitorizar varios nodos (gobiernos)

¿Qué pasaría si el sistema solo tuviese un usuario? ¡Un adversario que vea un mensaje en Tor sabría de quién es!
-->

## Navegación anónima
<!-- _class: smaller-font -->

Ejemplo: visitando google.com con el navegador Tor (navegador basado en Firefox)

Observa:

- El circuito de relays es de cuatro eslabones
- Google se piensa que estamos en Suiza porque el nodo de salida está en Suiza
- Curiosidad: ¡el nodo de entrada (Guard) cambia solo cada 2 o 3 meses!

![w:100% bg right](images/tor-google.png)

> [Tor Browser](https://www.torproject.org/)
> [Why is the first IP address in my relay circuit always the same?](https://support.torproject.org/tbb/tbb-2/)

# Servicios onion
<!-- _class: lead -->

## Servicios .onion

<!-- _class: two-columns -->

- A veces, los servidores **también** quieren permanecer anónimos: que nadie sepa dónde están ni qué IP tienen. De esta manera evitan que puedan cerrarse o atacarse
- En realidad el ejemplo de Breaking Bad ilustraría un mal uso de Tor: Gus controla el punto de encuentro, así que puede conocer a Walter sin que Walter lo reconozca (como pasó en la serie)
- Walter debería haber escogido él mismo el punto de encuentro, como en Tor

![center w:25em](images/onion-services.png)

<!--
Piensa en la temporada 2 de Breaking Bad, cuanto Walter quiere hablar con un traficante (que no sabe que es Gus):

- Walter utiliza a Saul para contactar con el traficante. En realidad Saul "conoce a alquien que conoce a alguien", pero no conoce directamente a Gus. Esto es un servicio de directorio, y "alquien que conoce a alquien" las personas que aceptan mensajes en nombre de Gus.
- Cuando le vuelve el mensaje a Walter, Gus y Walter quedan en un sitio "neutral": Los Pollos Hermanos. Este es el rendezvous
-->

---

![w:18em](https://2019.www.torproject.org/images/tor-onion-services-1.png) ![w:18em](https://2019.www.torproject.org/images/tor-onion-services-2.png)

Cuando un servidor quiere ofrecer un servicio, crea una dirección .onion (ejemplo: https://www.bbcnewsv2vjtpsuy.onion/) que se publica en un servicio de directorio y deja una lista de servidores que recibirán mensajes en su nombre

<!--
Las direcciones .onion tiene normalmente algunos caracteres al azar detrás de ellas. Eso es porque los servicios de directorio en realidad están distribuidos (tablas de hash distribuidas) y las direcciones .onion se comportan como un hash. Normalmente, creas una dirección .onion que empiece con un nombre identificable, como bbcnewsXXXXXXX, pero no siempre es así
-->

---

![w:18em](https://2019.www.torproject.org/images/tor-onion-services-3.png) ![w:18em](https://2019.www.torproject.org/images/tor-onion-services-4.png)

Cuando alguien quiere usar el servicio, tiene que conocer **de antemano** la dirección .onion

En el ejemplo, Alice escoge un lugar de encuentro (*rendezvous*) y envía un mensaje a Bob a través de alguno de los intermediarios

---

![w:18em](https://2019.www.torproject.org/images/tor-onion-services-5.png) ![w:18em](https://2019.www.torproject.org/images/tor-onion-services-6.png)

Bob y Alice se encuentran en el *rendezvous* y establecen una conexión Tor entre ellos


> https://2019.www.torproject.org/docs/onion-services.html.en

## ¿Pero quién mantiene los relays de Tor?

Los relays al final enrutaran mensajes que es muy posible que sean ilegales. ¿Quién querría hacer algo así?

- Gente que quiere apoyar el proyecto
- Gente que piensa que quiere apoyar el proyecto, pero venderá tu información ante cualquier problema
- Universidades haciendo investigación
- La policía intentando obtener información
- La NSA, o el equivalente europeo, ruso o chino
- Atacantes

No deberías fiarte de un nodo Tor. El sistema asume que los nodos Tor no son fiables. Si fuesen fiables, ¡serían suficientes circuitos de un solo relay!

## ¿Qué pasa si hay nodos Tor comprometidos?

Imagina un circuito con tres nodos Tor 1-2-3:

- Si un adversario controla los tres nodos, nadie que use ese circuito es anónimo
- Si un adversario controla el 1 y 3 (nodos de entrada y salida), puede intentar correlar entradas y salidas: puede (probabilidad) que descubra identidades
- Si un adversario controla un nodo, aprende datos estadísticos, pero es poco probable que aprenda identidades

En realidad se usan circuitos de 4, 5 o más relays. ¡Cuantos más uses, menos probable es que un solo adversario los controle todos!

---

![center w:25em](images/relays-tor.png)

La lista de nodos Tor es conocida aunque cambiante: es "fácil" para un servidor detectar si sus clientes están usando Tor

De hecho, si "un trabajador" intenta entrar en la VPN empresarial usando Tor... ¡muy probablemente es un atacante! Las VPN empresariales suelen detectar y bloquear las entradas desde Tor

> Ejemplo de lista de notos Tor: https://tormap.void.gr/

<!--
Ejemplos de relays Tor existentes cuando preparaba estas transparencias. La mayoría de relays Tor están en Europa, siempre ha sido así. Otros países tienen o bien poco interés de mantener nodos, o bien es peligroso hacerlo, o bien esos nodos pueden ser sospechosos de estar controlados por sus gobiernos.
-->

## Recomendaciones de uso
<!-- _class: two-columns-33 -->

¡Tor no te protege de todo! El servidor destino aún sabe qué datos estás enviando... y eso puede ser suficiente para identificarte.

![center w:22em](https://www.eff.org/files/tor-https-3.png)

> https://www.eff.org/pages/tor-and-https

<!--
De nada sirve que tus comunicaciones sean perfectamente anónimas con Tor si al final te logueas en Facebook y vas dejando comentarios en Internet con tu usuario
-->

---

1. No envíes información personal
    1. No uses Tor para conectarte a Facebook, Google, Twitter...: ¡te estás identificando!
    1. No uses Tor para búsquedas Google (o cosas similares): te perfilarán
1. Mantén Tor actualizado
1. Evita que te perfilen (*fingerprinting*). Tor está diseñado para que todos sus usuarios tengan el mismo perfil. ¡No hagas nada que cambie el perfil!
    1. No cambies tamaño de ventana, ni la maximices
    1. No instales plugins nuevos
    1. Borra cookies y otros datos

![bg right:30%](images/generic/photo-1484480974693-6ca0a78fb36b.webp)

> [The Web Never Forgets](https://www.esat.kuleuven.be/cosic/publications/article-2457.pdf) ACM SIGSAC Conference on Computer and Communications Security November 2014
> Photo: https://unsplash.com/photos/RLw-UC03Gwc

<!--
Hay muchos sistemas para perfilar: no hay mucha gente en el mundo que tenga una pantalla de  800x600, con un navegador con soporte de AVI345 y que use Linux Debian 9. Un navegador envía toda esta información al servidor nada más presentarse!

El navegador Tor intenta no enviar nada de esto, y utiliza un User-Agent cambiante. Pero eso no evita que la web pueda identificarte por los plugins que tengas instalados o el tamaño de tu ventana. ¡No cambies estas cosas!
-->

# Referencias y ejercicios
<!-- _class: lead -->

## Referencias

- Proyecto Tor, incluido su navegador: https://www.torproject.org/
- Tor y el Onion Routing, de tejedoresdelweb: http://tejedoresdelweb.com/w/TOR
- How Tor works?, by Hussein Nasser: https://www.youtube.com/watch?v=gIkzx7-s2RU
- Is Tor Trustworthy and Safe? https://restoreprivacy.com/tor/

## Ejercicio 1

Instala [el navegador Tor](https://www.torproject.org/download/) y visita estos sitios de la web normal, tanto con Tor browser como con tu browser habitual. Compara el tiempo que tardan en cargar con el tiempo que carga en cargar la web normal de estos sitios. Comprueba el circuito de nodos usado con cada sitio ¿ves una web diferente (idioma, por ejemplo) que cuando lo visitas desde tu navegador normal? 

- Google
- Youtube, y abre un vídeo cualquiera
- https://whatismyipaddress.com/ ¿Qué IP tienes en Tor y qué IP en tu navegador habitual?
- https://www.whatismybrowser.com/detect/am-i-using-tor ¿Te detecta que estás en Tor?

## Ejercicio 2
<!-- _class: with-warning smaller-font -->

Instala el navegador Tor y visita estos sitios en .onion. Compara el tiempo que tardan en cargar con el tiempo que carga en cargar la web normal de estos sitios

- BBC, web de noticias internacionales prohibida en algunos países: https://www.bbcnewsv2vjtpsuy.onion/
- ProPublica, web de noticias internacionales prohibida en algunos países: https://p53lf57qovyuvwsc6xnrppyply3vtqm7l6pcobkmyqsiofyeznfu5uqd.onion/
- ProtonMail, también en Tor: https://protonirockerxow.onion
- Wasabi: para comprar bitcoins anonimamamente (**comprar bitcoins no es una recomendación ni un ejercicio. Simplemente visita la web, sin comprar nada**): http://wasabiukrxmkdgve5kynjztuovbg43uxcbcxn6y2okcrsg7gb6jdmbad.onion/

Estos sitios son probablemente seguros, pero hay sitios .onion **terriblemente desagradables, inmorales o delictivos**. Ten **mucho cuidado** con seguir un enlace .onion que no sepas qué es. En mi opinión, el navegador Tor no debería estar al alcance de los niños