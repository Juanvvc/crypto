# Introducción a la criptografía

Este es un curso de introducción a la criptografía orientado a alumnos de grado en Ingeniería Informáctica y alumnos de postgrado de un máster de ciberseguridad.

Presentación en
[juanvvc.github.io/crypto/](https://juanvvc.github.io/crypto/index.html),
pero puedes acceder directamente a cada capítulo seleccionando los enlaces en
el apartado "Contenido".

## Un repositorio, dos asignaturas

Por motivos históricos, este curso está dividido en dos asignaturas diferentes: uno centrado en confidencialidad (más detalle) y otro en autenticación (más alto nivel). El curso de autenticación resume al principio algunas de las ideas del curso de confidencialidad. Cada curso sigue un subconjunto de los contenidos listados más abajo.

- [Índice de "Criptografía y Teoría de Códigos"](https://juanvvc.github.io/crypto/index.html)
- [Índice de "Criptogafía y Autenticación"](https://juanvvc.github.io/crypto/crypto2/index.html)

## Contenido completo

1. [Principios básicos](https://juanvvc.github.io/crypto/01-conceptos.html)
    - Anexo: [Glosario](https://juanvvc.github.io/crypto/A1-glosario.html) 
1. [Historia de la criptografía](https://juanvvc.github.io/crypto/02-historia.html)
1. [Cifrado simétrico o de clave secreta: ChaCha y AES](https://juanvvc.github.io/crypto/03-simetrica.html)
    - Anexo: [RNG y HSM](https://juanvvc.github.io/crypto/A2-rng.html)
1. [Teoría de la complejidad y Diffie-Hellman](https://juanvvc.github.io/crypto/04-complejidad.html)
1. [RSA y Curvas elípticas](https://juanvvc.github.io/crypto/05-asimetrica.html)
1. [Funciones de hash](https://juanvvc.github.io/crypto/06-hashes.html)
	- Anexo: [Blockchain](https://juanvvc.github.io/crypto/A3-blockchain.html)
1. [*Public Key Infrastructure*](https://juanvvc.github.io/crypto/07-pki.html)
	- Anexo: [Firma digital](https://juanvvc.github.io/crypto/A4-firmadigital.html)
    - Anexo: [TLS en detalle](https://juanvvc.github.io/crypto/A2-protocolos.html)
1. [Ransomware](https://juanvvc.github.io/crypto/08-ransomware.html)
1. [Esteganografía](https://juanvvc.github.io/crypto/09-esteganografia.html)
1. [Criptografía postcuántica](https://juanvvc.github.io/crypto/10-postcuantica.html)
1. [Autenticación](https://juanvvc.github.io/crypto/11-autenticacion.html)
1. [Comunicaciones anónimas](https://juanvvc.github.io/crypto/12-anonimato.html)
1. [Business Email Compromise](https://juanvvc.github.io/crypto/13-bec.html)
1. [Cifrado de disco](https://juanvvc.github.io/crypto/14-disk.html)

    
Puedes crear la versión PDF de las transparencias "imprimiendo a PDF" en Google Chrome.

## Descarga local

Aunque lo más recomendable es acceder a la versión en línea para ver siempre la
versión actualizada, si quieres puedes descargarte las transparencias para
visualizarlas fuera de línea. Simplemente aprieta el botón `Download ZIP` de
arriba.

O si tienes cuenta en GitHub puedes simplemente un `fork` (botón de arriba a la
derecha), aunque no las voy a borrar a medio plazo, con lo que si simplemente
marcas con una estrella tendrás un recordatorio en tu cuenta de donde residen
para cuando las necesites.

O también, puedes clonar el proyecto en tu disco duro local (necesitas un
cliente `git`):

```bash
$ git clone git@github.com:juanvvc/crypto.git
```

De esta manera tienes una copia local que siempre puedes mantener al día con:

```bash
$ git pull
```

Puedes crear las transparencias con:
 
```bash
# Si no tienes marp instalado, ejecuta esto solo una vez
npm install @marp-team/marp-cli

# Para crear las transparencias en el directorio build
make

# Alternativamente, para crear PDFs en el directorio build
make pdfs
```

# Notas de presentación

Puedes acceder a las notas de presentación, que probablemente contengan
información interesante y extendida, pulsando la tecla `P`

# Licencia

Esta obra esta sujeta a una licencia de [Attribution-ShareAlike 4.0
International (CC BY-SA 4.0) ](https://creativecommons.org/licenses/by-sa/4.0/)

[![Licencia de Creative
Commons](https://licensebuttons.net/l/by-sa/3.0/88x31.png)](https://creativecommons.org/licenses/by-sa/4.0/)

Copyright © 2020-2026 [Juan Vera del Campo](https://github.com/juanvvc)

Basado inicialmente en el curso Copyright © 2016-2019 [Jordi Íñigo Griera](https://github.com/jig/crypto), pero muy modificado a lo largo de los años


