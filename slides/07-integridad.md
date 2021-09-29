---
marp: true
title: Criptografía - Integridad
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

**Tema 7: Integridad**

Juan Vera del Campo - <juan.vera@campusviu.es>


## Hoy hablamos de...
<!-- _class: cool-list -->

1. [Integridad](#3)
1. [HMAC](#12)
1. [MAC](#20)
1. [Resumen y referencias](#27)


# Integridad
<!-- _class: lead -->

## Definición

Capacidad de **detectar** si un mensaje ha sido modificado desde su transmisión hasta su recepción.

La modificación se refiere tanto a una modificación **explícita por un atacante** como a una modificación debido a un error (por ejemplo de transmisión). 

> https://es.wikipedia.org/wiki/Integridad_del_mensaje

![bg right:40%](https://upload.wikimedia.org/wikipedia/commons/1/12/Darwin_Hybrid_Tulip_Mutation_2014-05-01.jpg)


## Cifrado autenticado: tipos

- **Encrypt-then-MAC** (EtM): primero cifra, luego calcula MAC 
- **Encrypt-and-MAC** (E&M): cifra y calcula MAC a la vez
- **MAC-then-Encrypt** (MtE): primero calcula MAC, luego cifra

> https://en.wikipedia.org/wiki/Authenticated_encryption

## Encrypt-then-MAC (EtM)
<!-- _class: two-columns -->

![center](https://upload.wikimedia.org/wikipedia/commons/b/b9/Authenticated_Encryption_EtM.png)

- Usado en IPSec
- Necesita dos claves: una para cifrar y otra para el MAC

## Encrypt-and-MAC (E&M)
<!-- _class: two-columns -->

![center](https://upload.wikimedia.org/wikipedia/commons/a/a5/Authenticated_Encryption_EaM.png)

- Usado en SSH
- Puede reutilizar clave para cifrar y calcular MAC

## MAC-then-Encrypt (MtE)
<!-- _class: two-columns -->

![MAC-then-Encrypt](https://upload.wikimedia.org/wikipedia/commons/a/ac/Authenticated_Encryption_MtE.png)

- Usado en TLS
- Permite algún ataques de padding: [Padding Oracle, pentesterlab](https://book.hacktricks.xyz/crypto/padding-oracle-priv)

---
<!-- _class: center -->

Continúa en: [Firma digital y PKI](08-pki.html)
