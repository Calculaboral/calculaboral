#!/usr/bin/env python3
"""Valida el sitio de Calculadora Lista. Uso: python3 .claude/skills/nueva-guia/validar.py (desde la raíz del repo)."""
import glob, json, os, re, sys
import xml.dom.minidom

NOINDEX_OK = {"404.html", "legal/afiliados.html", "legal/aviso-legal.html", "legal/privacidad.html"}
SIN_CANONICA_OK = NOINDEX_OK | {"googlec177279e72e35813.html"}
errores, avisos = [], []

def err(f, m): errores.append(f"{f}: {m}")
def warn(f, m): avisos.append(f"{f}: {m}")

archivos = sorted(glob.glob("*.html") + glob.glob("*/*.html"))
for f in archivos:
    t = open(f, encoding="utf-8").read()
    for tag in ("div", "section", "details", "ul", "table", "main"):
        a = len(re.findall(rf"<{tag}[\s>]", t)); b = len(re.findall(rf"</{tag}>", t))
        if a != b: err(f, f"<{tag}> abiertas {a} y cerradas {b}")
    for j in re.findall(r'<script type="application/ld\+json">(.*?)</script>', t, re.S):
        try: json.loads(j)
        except Exception as e: err(f, f"JSON-LD no válido: {e}")
    if f == "googlec177279e72e35813.html": continue
    titulo = re.search(r"<title>(.*?)</title>", t, re.S)
    desc = re.search(r'<meta name="description" content="([^"]*)"', t)
    if not titulo: err(f, "falta <title>")
    elif len(titulo.group(1)) > 65: warn(f, f"título largo ({len(titulo.group(1))} caracteres)")
    if not desc: err(f, "falta meta description")
    elif len(desc.group(1)) > 160: warn(f, f"descripción larga ({len(desc.group(1))} caracteres)")
    tiene_noindex = "noindex" in t
    if f in NOINDEX_OK and not tiene_noindex: err(f, "debería llevar noindex")
    if f not in NOINDEX_OK and tiene_noindex: err(f, "lleva noindex y no debería")
    if f not in SIN_CANONICA_OK:
        m = re.search(r'<link rel="canonical" href="([^"]*)"', t)
        if not m: err(f, "falta canonical")
        else:
            esperada = "https://calculadoralista.es/" + ("" if f == "index.html" else f)
            if m.group(1) != esperada: err(f, f"canonical {m.group(1)} distinto de {esperada}")
    if f.startswith("guias/"):
        for marca in ('class="fuentes"', 'class="relacionado"', 'class="disclaimer"', "pagead2"):
            if marca not in t: err(f, f"falta {marca}")
        n_det = len(re.findall(r"<details", t))
        n_q = 0
        for j in re.findall(r'<script type="application/ld\+json">(.*?)</script>', t, re.S):
            try: n_q = len(json.loads(j).get("mainEntity", []))
            except Exception: pass
        if n_det != n_q: err(f, f"FAQ visibles ({n_det}) y en JSON-LD ({n_q}) no coinciden")

sm = open("sitemap.xml", encoding="utf-8").read()
try: xml.dom.minidom.parseString(sm)
except Exception as e: err("sitemap.xml", f"XML no válido: {e}")
urls = re.findall(r"<loc>https://calculadoralista\.es/([^<]*)</loc>", sm)
for u in urls:
    ruta = u or "index.html"
    if not os.path.exists(ruta): err("sitemap.xml", f"apunta a {ruta}, que no existe")
for f in archivos:
    if f in SIN_CANONICA_OK: continue
    if f"/{'' if f == 'index.html' else f}" not in sm and not (f == "index.html"): err("sitemap.xml", f"falta {f}")

print(f"{len(archivos)} archivos HTML revisados, {len(urls)} URLs en el sitemap")
for a in avisos: print("AVISO", a)
for e in errores: print("ERROR", e)
print("OK" if not errores else f"{len(errores)} errores")
sys.exit(1 if errores else 0)
