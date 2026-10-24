---
name: nueva-guia
description: Crear una guía nueva en Calculadora Lista a partir de una existente, con FAQ, JSON-LD, fuentes oficiales, tarjeta en la home y entrada en el sitemap. Usar cuando se pida añadir una guía.
disable-model-invocation: true
---

# Nueva guía de Calculadora Lista

Argumento: el tema de la guía (por ejemplo "modelo 130 PDF").

## Pasos
1. **Investigar con fuentes oficiales.** Busca y lee BOE, SEPE, AEAT o Seguridad Social. Anota cada cifra con su fuente. No escribas nada que no hayas podido comprobar; si algo no se confirma, dilo con cautela o déjalo fuera.
2. **Elegir una guía existente como plantilla** (por ejemplo `guias/modelo-130-pagos-fraccionados-irpf-autonomos.html`) y copiarla a `guias/<slug>.html`. El slug va en minúsculas, sin tildes y con guiones.
3. **Reescribir el contenido** respetando la estructura: h1, introducción, 6-9 secciones h2, al menos una tabla en `.table-scroll` si hay cifras, ejemplo resuelto si procede, `.cta` hacia la calculadora más relacionada, `.faq` con 3-5 preguntas, `.fuentes` con enlaces oficiales comprobados, `.relacionado` y `.disclaimer`. Extensión objetivo: 1.400-1.900 palabras.
4. **Cabecera SEO:** `<title>` de hasta unos 60 caracteres, descripción de hasta 160, `canonical` y `og:url` absolutos con la URL nueva, y `og:title` / `twitter:title` / descripciones iguales.
5. **JSON-LD `FAQPage`** con las mismas preguntas y respuestas que las `<details>` visibles.
6. **Home:** añadir la tarjeta en `index.html` junto a las demás guías (copiar el markup de una tarjeta existente, con su icono).
7. **Sitemap:** añadir la URL a `sitemap.xml` con `lastmod` de hoy y prioridad 0.8. Enlazar la guía nueva desde 2-3 guías o calculadoras relacionadas.
8. **Validar:** `python3 .claude/skills/nueva-guia/validar.py`. Debe terminar en OK.
9. **Publicar:** commit con un mensaje claro en español y `git push origin main`. Recuerda al usuario pedir la indexación en Search Console con la URL nueva.

## No hacer
- No inventar cifras, normas ni enlaces.
- No copiar texto de otras webs.
- No olvidar el aviso legal (`.disclaimer`) ni las fuentes.
