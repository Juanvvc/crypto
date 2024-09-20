# Introducción a la criptografía

Presentación en
[juanvvc.github.io/crypto/](https://juanvvc.github.io/crypto/index.html),
pero puedes acceder directamente a cada capítulo seleccionando los enlaces en
el apartado "Contenido".

## Contenido

1. [Introducción](https://juanvvc.github.io/crypto/index.html)
1. [Principios básicos](https://juanvvc.github.io/crypto/01-conceptos.html)
    - Anexo: [Glosario](https://juanvvc.github.io/crypto/A1-glosario.html) 
1. [Criptografía clásica](https://juanvvc.github.io/crypto/02-historia.html)
1. [Cifrado simétrico o de clave secreta: ChaCha y AES](https://juanvvc.github.io/crypto/03-simetrica.html)
    - Anexo: [RNG y HSM](https://juanvvc.github.io/crypto/A2-rng.html)
1. Cifrado asimétrico o de clave pública
    - [Teoría de la complejidad y Diffie-Hellman](https://juanvvc.github.io/crypto/04-complejidad.html)
    - [RSA y Curvas elípticas](https://juanvvc.github.io/crypto/05-asimetrica.html)
1. [Funciones de hash](https://juanvvc.github.io/crypto/06-hashes.html)
	- Anexo: [Blockchain](https://juanvvc.github.io/crypto/A3-blockchain.html)
1. [*Public Key Infrastructure*](https://juanvvc.github.io/crypto/07-pki.html)
	- Anexo: [Firma digital](https://juanvvc.github.io/crypto/A4-firmadigital.html)
    - Anexo: [TLS en detalle](https://juanvvc.github.io/crypto/A2-protocolos.html)
1. [Autenticación](https://juanvvc.github.io/crypto/11-autenticacion.html)
    
1. [Comunicationes anónimas](https://juanvvc.github.io/crypto/12-anonimato.html)
1. Criptografía ofensiva:
    - [Business Email Compromise](https://juanvvc.github.io/crypto/08-ransomware.html)
    - [Ransomware](https://juanvvc.github.io/crypto/08-ransomware.html)
1. [Esteganografía](https://juanvvc.github.io/crypto/09-esteganografia.html)
1. [Criptografía Post-cuántica](https://juanvvc.github.io/crypto/10-postcuantica.html)

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

Copyright © 2020-2024 [Juan Vera del Campo](https://github.com/juanvvc)

Basado en curso Copyright © 2016-2017 [Jordi Íñigo Griera](https://github.com/jig/crypto)


