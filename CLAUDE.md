# Calculadora Lista (calculadoralista.es)

Web estática en español con calculadoras y guías laborales y fiscales de España. HTML, CSS y JavaScript sin dependencias ni build. Se publica en GitHub Pages desde `main` (dominio propio, ver `CNAME`). Objetivo: ingresos extra con AdSense y afiliados, con información lo más exacta y fiable posible.

## Reglas que no se negocian
- La información legal y fiscal debe ser exacta y comprobable. Cada guía cita fuentes oficiales (BOE, SEPE, AEAT, Seguridad Social). Si una cifra no se puede confirmar en la fuente oficial, se redacta con cautela ("unos", "aprox.") y no se afirma como exacta.
- No inventar datos, enlaces ni normativa. Enlazar solo a páginas oficiales que se hayan comprobado.
- Todo el texto va en español de España, tono claro y directo.
- No se hace autopromoción en foros (Reddit, Rankia, etc.): ya bloquearon publicaciones por spam.

## Estructura
- `index.html`: portada con pestañas Calculadoras y Guías (`#calculadoras`, `#guias`).
- `calculadora-*.html`: 7 calculadoras (indemnización, finiquito, nómina neta, paro, cuota de autónomos, IRPF de autónomos, modelo 303).
- `guias/*.html`: guías (unas 1.450-1.970 palabras) y `guias/cifras-clave-2026.html`.
- `sobre-nosotros.html`, `contacto.html` (contacto: calculaboraloficial@gmail.com).
- `legal/`: aviso legal, privacidad y cookies, afiliados. Llevan `noindex` a propósito y no están en el sitemap.
- `404.html` (noindex), `robots.txt`, `sitemap.xml`, `ads.txt`, archivos de favicon, `googlec177279e72e35813.html` (verificación de Search Console, no tocar).
- CSS y JS van dentro de cada página (no hay archivos externos). Fuentes de Google con carga diferida.

## Plantilla de una guía
Cabecera con el badge €, migas de pan, `.doc` con h2, tablas dentro de `.table-scroll`, bloque `.cta`, `.faq` con `<details>`, `.fuentes`, `.relacionado` y `.disclaimer`. Más un JSON-LD `FAQPage` que debe coincidir con las preguntas visibles. Copia siempre una guía existente (por ejemplo `guias/modelo-130-pagos-fraccionados-irpf-autonomos.html`) en vez de escribirla de cero.

## SEO
- `<title>` de hasta unos 60 caracteres y meta description de hasta 160, sin sufijo de marca en las guías.
- `canonical` y `og:url` absolutos y apuntando a la propia página.
- Cada página nueva: tarjeta en `index.html`, entrada en `sitemap.xml` con `lastmod`, y enlaces desde guías relacionadas.
- Actualizar `lastmod` del sitemap cuando se cambie una página.

## Cifras verificadas de 2026
- SMI 2026: 1.221 €/mes en 14 pagas (RD 126/2026).
- Paro: 70 % de la base reguladora los primeros 180 días y 60 % desde el día 181; topes 560 / 749 / 1.225 / 1.400 / 1.575 € con IPREM de 600 € más un sexto (hoja del SEPE).
- Cotización de trabajadores 2026: Orden PJC/297/2026.
- Tarifa plana de autónomos: 80 € de cuota reducida. El total con MEI (unos 88,64 €) NO está confirmado oficialmente: escribirlo siempre como aproximado.
- Plazos del modelo 130: 1-20 de abril, julio y octubre; 1-30 de enero. Presentación en la sede electrónica de la AEAT.

## Antes de publicar
1. Ejecutar `python3 .claude/skills/nueva-guia/validar.py` desde la raíz. Debe terminar en OK.
2. Comprobar a mano las cifras nuevas contra la fuente oficial.
3. Commit y `git push origin main`. GitHub Pages tarda un par de minutos en publicar.

## Datos del proyecto
- Repositorio público: Calculaboral/calculaboral.
- AdSense: `ads.txt` con el editor `pub-5573612679839513`. No pedir la revisión de AdSense hasta que haya más páginas indexadas y algo de tráfico (hacia mediados o finales de noviembre de 2026).
- Analítica: Cloudflare Web Analytics y Search Console. Search Console tarda unos 2-3 días en mostrar datos.
- GitHub Pages no permite cabeceras HTTP propias (no hay CSP ni HSTS); el riesgo real es bajo porque no hay cookies ni formularios.
