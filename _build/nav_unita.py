#!/usr/bin/env python3
"""Inserisce, in fondo a ogni unità pubblicata di una classe, i due bottoni
di navigazione: unità precedente e unità successiva. Sulla prima unità il
bottone precedente diventa un link all'indice della classe; sull'ultima
diventa il bottone successiva."""
import json, os, re, sys

RAD = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def cartella_unita(u):
    # come in genera.py: "cartella" permette di cambiare titolo o numero senza cambiare l'indirizzo
    import unicodedata
    if u.get('cartella'):
        return u['cartella']
    t = unicodedata.normalize('NFKD', u['titolo']).encode('ascii', 'ignore').decode()
    t = re.sub(r'-+', '-', re.sub(r'[^a-zA-Z0-9]+', '-', t).strip('-').lower())[:60]
    return "%02d-%s" % (u['n'], t)

def unita_pubblicate(percorso, dati):
    """(numero, cartella, titolo) delle unità presenti su disco, nell'ordine di _dati."""
    base = os.path.join(RAD, percorso, 'argomenti')
    out = []
    for area in dati['aree']:
        for u in area['unita']:
            c = cartella_unita(u)
            if os.path.isdir(os.path.join(base, c)):
                out.append((u['n'], c, u['titolo']))
    return out

def dati_classe(percorso):
    return json.load(open(os.path.join(RAD, '_dati', percorso + '.json'), encoding='utf-8'))

def titoli_per_numero(dati):
    out = {}
    for area in dati['aree']:
        for u in area['unita']:
            out[u['n']] = u['titolo']
    return out

def bottone(classe, direzione, titolo, href):
    return ('<a class="%s" href="%s"><span class="dir">%s</span><span class="tit">%s</span></a>'
            % (classe, href, direzione, titolo))

def inserisci(percorso):
    dati = dati_classe(percorso)
    unita = unita_pubblicate(percorso, dati)
    modificati = 0
    for i, (n, cart, _) in enumerate(unita):
        fp = os.path.join(RAD, percorso, 'argomenti', cart, 'index.html')
        html = open(fp, encoding='utf-8').read()

        bottoni = []
        if i > 0:
            bottoni.append(bottone('precedente', '&larr; Precedente', unita[i - 1][2],
                                    '../%s/index.html' % unita[i - 1][1]))
        else:
            bottoni.append(bottone('precedente', '&larr; Indice', dati['classe'],
                                    '../../index.html'))
        if i + 1 < len(unita):
            bottoni.append(bottone('successiva', 'Successiva &rarr;', unita[i + 1][2],
                                    '../%s/index.html' % unita[i + 1][1]))
        else:
            bottoni.append(bottone('successiva', 'Indice &rarr;', dati['classe'],
                                    '../../index.html'))
        nav = '<nav class="nav-unita">%s</nav>\n' % ''.join(bottoni)

        # sostituisco la barra esistente al suo posto; altrimenti prima di <footer>
        # o, in mancanza, prima dell'ultimo </div>
        html, _ = re.subn(r'<nav class="prossima">.*?</nav>\n', '', html)
        nuovo_html, n_sost = re.subn(r'<nav class="nav-unita">.*?</nav>\n?', lambda m: nav, html, count=1)
        if n_sost != 1:
            nuovo_html, n_sost = re.subn(r'<footer>', lambda m: nav + '<footer>', html, count=1)
        if n_sost != 1:
            k = html.rfind('</div>')
            if k < 0:
                print("ATTENZIONE: nessun punto di inserimento in", fp)
                continue
            nuovo_html = html[:k] + nav + html[k:]
        if nuovo_html == html:
            continue
        open(fp, 'w', encoding='utf-8').write(nuovo_html)
        modificati += 1
    print("%s: %d file modificati su %d" % (percorso, modificati, len(unita)))

if __name__ == '__main__':
    for percorso in sys.argv[1:]:
        inserisci(percorso)
