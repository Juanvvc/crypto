# Introducción a la criptografía

Transparencias en
[juanvvc.github.io/crypto/](https://juanvvc.github.io/crypto/index.html),
pero puedes acceder directamente a cada capítulo seleccionando los enlaces en
el apartado "Contenido".

## Contenido

- [Introducción](https://juanvvc.github.io/crypto/index.html)
- [Principios básicos](https://juanvvc.github.io/crypto/01-conceptos.html)
    - Anexo: [Glosario](https://juanvvc.github.io/crypto/A1-glosario.html) 
- [Criptografía clásica](https://juanvvc.github.io/crypto/02-historia.html)
- [Cifrado simétrico o de clave secreta: ChaCha y AES](https://juanvvc.github.io/crypto/03-simetrica.html)
    - Anexo: [RND y HSM](https://juanvvc.github.io/crypto/A2-rnd.html) 
- [Teoría de la complejidad y Diffie-Hellman](https://juanvvc.github.io/crypto/04-complejidad.html)
- [Cifrado asimétrico o de clave pública: RSA](https://juanvvc.github.io/crypto/05-asimetrica.html)
- [Funciones de hash y *blockchain*](https://juanvvc.github.io/crypto/06-hashes.html)
- [TLS y *Public Key Infrastructure*](https://juanvvc.github.io/crypto/07-pki.html)
- [Ransomware](https://juanvvc.github.io/crypto/08-ransomware.html)
- [Esteganografía](https://juanvvc.github.io/crypto/09-esteganografia.html)

Recuerda: puedes "imprimir a PDF" para obtener las translarencias en PDF

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

```
$ git clone git@github.com:juanvvc/crypto.git
```

De esta manera tienes una copia local que siempre puedes mantener al día con:

```
$ git pull
```

Puedes crear las transparencias con:
 
```
# Si no tienes marp instalado, ejecuta esto solo una vez
npm install -g @marp-team/marp-cli

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

Copyright © 2020-2022 [Juan Vera del Campo](https://github.com/juanvvc)

Basado en transparencias Copyright © 2016-2017 [Jordi Íñigo Griera](https://github.com/jig/crypto)


