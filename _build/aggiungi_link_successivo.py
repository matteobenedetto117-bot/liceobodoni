#!/usr/bin/env python3
"""Inserisce, in fondo a ogni unità pubblicata di una classe, un link alla
unità successiva (o all'indice della classe, per l'ultima unità)."""
import json, os, re, sys

RAD = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def cartelle_ordinate(percorso):
    base = os.path.join(RAD, percorso, 'argomenti')
    return sorted(d for d in os.listdir(base) if os.path.isdir(os.path.join(base, d)))

def titoli_per_numero(percorso):
    dati = json.load(open(os.path.join(RAD, '_dati', percorso + '.json'), encoding='utf-8'))
    out = {}
    for area in dati['aree']:
        for u in area['unita']:
            out[u['n']] = u['titolo']
    return out

def inserisci(percorso):
    cartelle = cartelle_ordinate(percorso)
    titoli = titoli_per_numero(percorso)
    modificati = 0
    for i, cart in enumerate(cartelle):
        fp = os.path.join(RAD, percorso, 'argomenti', cart, 'index.html')
        html = open(fp, encoding='utf-8').read()
        if 'class="prossima"' in html:
            continue  # già presente, non duplicare
        n = int(cart.split('-', 1)[0])
        if i + 1 < len(cartelle):
            prossima_cart = cartelle[i + 1]
            titolo_prossima = titoli.get(n + 1, '')
            nav = ('<nav class="prossima"><a href="../%s/index.html">Unità successiva: %s &rarr;</a></nav>\n'
                   % (prossima_cart, titolo_prossima))
        else:
            nav = '<nav class="prossima"><a href="../../index.html">Torna all\'indice degli argomenti &rarr;</a></nav>\n'
        nuovo_html, n_sost = re.subn(r'<footer>', nav + '<footer>', html, count=1)
        if n_sost != 1:
            print("ATTENZIONE: nessun <footer> trovato in", fp)
            continue
        open(fp, 'w', encoding='utf-8').write(nuovo_html)
        modificati += 1
    print("%s: %d file modificati su %d" % (percorso, modificati, len(cartelle)))

if __name__ == '__main__':
    for percorso in sys.argv[1:]:
        inserisci(percorso)
