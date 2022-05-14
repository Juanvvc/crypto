---
marp: true
title: Criptografía - Esteganografía
author: Juan Vera
keywords: criptografía,esteganografía,watermarking
paginate: true
footer: '[Inicio](index.html)'
headingDivider: 2
theme: marp-incide
transition: fade
---

<style>
    /* You can add custom style here. VSCode supports this.
    Other editor might need these custom code in
    the YAML header: section: | */
	/* section header { display: none; } */
	/* section footer { display: none; } */
</style>

# Esteganografía
<!-- _class: first-slide -->

Juan Vera del Campo

<juan.vera@campusviu.es>

## Hoy hablamos de...
<!-- _class: cool-list -->

1. [Esteganografía](#3)
1. [Ejemplos](#9)
1. [Ataques y detección](#22)
1. [Resumen y referencias](#27)

# Esteganografía
<!-- _class: lead -->

## Esteganografía

![left:40% bg](https://mymodernmet.com/wp/wp-content/uploads/archive/s24fY-fNlvsNkyhLvLM4_gecko.jpg)]

*Ocultación de información dentro de otra información más comúnn, un documento que no sea secreto, o un documento que no levante sospechas*

## Usos

- Confidencialidad: enviar información en un canal oculto
- Plausible deniability: ¡no estoy haciendo nada malo!
- Copyright: marcar un texto como de mi propiedad
- DLP / DRM: detectar quién ha distribuido un documento
- Atacantes: ¡llevar el malware sin que sea detectado!

<!--
DLP: Data Leak Protection
DRM: Digital Right Management
-->

## Técnicas de ocultación de información

![center w:30em](images/5325040.fig.001.png)

> ["A Comparative Analysis of Information Hiding Techniques for Copyright Protection of Text Documents"](https://www.hindawi.com/journals/scn/2018/5325040/),Milad Taleby Ahvanooey,1 Qianmu Li, Hiuk Jae Shim, and Yanyan Huang. Security and Communication Networks / 2018

## Proceso

![](images/5325040.fig.002.png)

<!--
¿Es posible detectarlo?

Después de cambios en la imagen, ¿podemos seguir pasando el mensaje?

Si la imagen se imprime, ¿el mensaje oculto se mantiene?
-->

## Propiedades

(Deseables o no)

- Que no pueda ser detectado
- Que no pueda quitarse con facilidad
- Que pueda ser verificable: criptografía
- Coste computacional para poner / quitar

# Ejemplos
<!-- _class: lead -->

Watermarking y fingerprinting

## Imágenes

![bg left:30%](https://static.bhphotovideo.com/explora/sites/default/files/proof.jpg)

- Pixeles "muertos"
- Bit menos significativo: en pixeles o en sus transformadas
- Paleta de color
- Campos EXIF
- ...

<https://www.mobilefish.com/services/steganography/steganography.php>

---

![](https://blog.fastforwardlabs.com/images/2017/06/stego_images.jpg)

<!--
¿Se mantiene la marca después de convertir la imagen?
-->

---

![](https://i.blogs.es/e7a33c/look2/1366_2000.jpg)

> [Look Scanned](https://lookscanned.io/)

---

![](https://ychef.files.bbci.co.uk/1600x900/p05568yh.webp)

> https://www.bbc.com/future/article/20170607-why-printers-add-secret-tracking-dots

---

![](https://ychef.files.bbci.co.uk/1600x900/p05568js.png)

## Textos

![bg left:30%](images/stego-julio.png)

- A la vista
- Resiste impresiones y algunas manipulaciones
- Linguístico: cambiar palabras, frases...
- Estructural: espacios, marcas, tipos de letra...

# Shaadow.io

[![w:20em center](images/stego-shadowio.png)](https://www.shaadow.io/)

> https://www.elladodelmal.com/2022/04/como-poner-una-marca-oculta-shaadow-los.html

<!--
Los de shadow.io dicen que pueden mantener la marca incluso después de imprimir el texto a papel
-->

---

![center](images/stego-text1.png)

---

![center](images/stego-text2.png)


## DNS tunneling

![](https://help.zscaler.com/downloads/zia/documentation-knowledgebase/creating-and-managing-policies/firewall/firewall-policies-resources/about-dns-application-groups/dns%20tunneling%20diagram.png)

> https://help.zscaler.com/zia/about-dns-tunnel-detection

## Esconder malware en archivos

![center w:20em](https://blog.reversinglabs.com/hubfs/Blog/malware-in-images/malware_in_images_03.jpg)

> https://blog.reversinglabs.com/blog/malware-in-images

---

![center](images/estego-bezzos.png)

> https://ia802801.us.archive.org/6/items/ftireportintojeffbezosphonehack/FTI-Report-into-Jeff-Bezos-Phone-Hack_text.pdf

# Ataques y detección
<!-- _class: lead -->

## Ataques

- Activos: el atacante quiere quitar la marca
- Pasivos: el atacante quiere detectar la marca
- Colisiones: el atacante usa dos documentos marcados para obtener uno sin marca
- Simulación: el atacante genera un documento con una marca falsa


## Estimación de la marca

![w:40em center](images/stego-image17.gif)

> https://ai.googleblog.com/2017/08/making-visible-watermarks-more-effective.html

## Entropía

![bg left w:100%](https://i.stack.imgur.com/uZH9F.png)

- Medida de la aleatoriedad de un archivo
- Texto normal: 0.6 bits por bit
- Texto cifrado: 1 bit por bit
- Si encuentras más entropía de la esperada ¡cifrado!
- Aplicable a muchos canales de comunicación: DNS, chat, imágenes, email...
- No aplicable a canales que ya tengan entropía máxima por estar comprimidos: vídeo, imágenes...

---

![center w:20em](images/estego-entropy1.png)

<!-- Ejemplo del archivo cifrado del primer ejericio. Fíjate: al principio y al final no tiene entropía, y esas son las partes "que estaban a cero" -->


# Referencias
<!-- _class: lead -->

## Referencias

- [IMAGE WATERMARKING USING DISCRETE COSINE TRANSFORM [DCT] AND GENETIC ALGORITHM](https://www.researchgate.net/publication/317605329_IMAGE_WATERMARKING_USING_DISCRETE_COSINE_TRANSFORM_DCT_AND_GENETIC_ALGORITHM_GA_MAHIMA_SINGH), MAHIMA SINGH June 2017. INTERNATIONAL JOURNAL OF INNOVATION IN ENGINEERING RESEARCH & MANAGEMENT ISSN :2348-4918
- ["A Comparative Analysis of Information Hiding Techniques for Copyright Protection of Text Documents"](https://www.hindawi.com/journals/scn/2018/5325040/),Milad Taleby Ahvanooey,1 Qianmu Li, Hiuk Jae Shim, and Yanyan Huang. Security and Communication Networks / 2018

---
<!-- _class: last-slide -->

¡Esto ha sido todo!

Juan Vera
<juan.vera@campusviu.es>