#!/usr/bin/env python3
"""Inserisce, in fondo a ogni unità pubblicata di una classe, i due bottoni
di navigazione: unità precedente e unità successiva (quest'ultima sostituita
dal link all'indice della classe, per l'ultima unità)."""
import json, os, re, sys

RAD = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def cartelle_ordinate(percorso):
    base = os.path.join(RAD, percorso, 'argomenti')
    return sorted(d for d in os.listdir(base) if os.path.isdir(os.path.join(base, d)))

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
    cartelle = cartelle_ordinate(percorso)
    dati = dati_classe(percorso)
    titoli = titoli_per_numero(dati)
    modificati = 0
    for i, cart in enumerate(cartelle):
        fp = os.path.join(RAD, percorso, 'argomenti', cart, 'index.html')
        html = open(fp, encoding='utf-8').read()
        n = int(cart.split('-', 1)[0])

        bottoni = []
        if i > 0:
            cart_prec = cartelle[i - 1]
            bottoni.append(bottone('precedente', '&larr; Precedente', titoli.get(n - 1, ''),
                                    '../%s/index.html' % cart_prec))
        if i + 1 < len(cartelle):
            cart_succ = cartelle[i + 1]
            bottoni.append(bottone('successiva', 'Successiva &rarr;', titoli.get(n + 1, ''),
                                    '../%s/index.html' % cart_succ))
        else:
            bottoni.append(bottone('successiva', 'Indice &rarr;', dati['classe'],
                                    '../../index.html'))
        nav = '<nav class="nav-unita">%s</nav>\n' % ''.join(bottoni)

        # rimuovo un'eventuale versione precedente (vecchio link singolo, o nav-unita già inserita)
        html, _ = re.subn(r'<nav class="prossima">.*?</nav>\n', '', html)
        html, _ = re.subn(r'<nav class="nav-unita">.*?</nav>\n', '', html)

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
