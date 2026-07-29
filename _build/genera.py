#!/usr/bin/env python3
"""Rigenera l'hub delle classi e l'indice degli argomenti a partire da _dati/*.json.
Va rilanciato dopo ogni unità pubblicata, così l'avanzamento resta aggiornato."""
import json, os, re, unicodedata, datetime

RAD = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def slug(t):
    t = unicodedata.normalize('NFKD', t).encode('ascii', 'ignore').decode()
    t = re.sub(r'[^a-zA-Z0-9]+', '-', t).strip('-').lower()
    return re.sub(r'-+', '-', t)[:60]

def cartella_unita(u):
    return "%02d-%s" % (u['n'], slug(u['titolo']))

def esiste(u, percorso):
    return os.path.isfile(os.path.join(RAD, percorso, 'argomenti', cartella_unita(u), 'index.html'))

ANNI = ["Prima", "Seconda", "Terza", "Quarta", "Quinta"]
MATERIE = ["Matematica", "Fisica"]

def carica_tutti():
    """Ogni _dati/*.json descrive una classe: serve dei campi percorso, materia, anno."""
    out = {}
    cart = os.path.join(RAD, '_dati')
    for f in sorted(os.listdir(cart)) if os.path.isdir(cart) else []:
        if not f.endswith('.json'):
            continue
        d = json.load(open(os.path.join(cart, f), encoding='utf-8'))
        if 'percorso' in d and 'materia' in d and 'anno' in d:
            out[(d['materia'], d['anno'])] = d
    return out

def hub(classi):
    blocchi = []
    for materia in MATERIE:
        carte = []
        for anno in ANNI:
            d = classi.get((materia, anno))
            if d:
                tot = sum(len(a['unita']) for a in d['aree'])
                fatte = sum(1 for a in d['aree'] for u in a['unita'] if esiste(u, d['percorso']))
                carte.append(
                    '<a class="classe attiva" href="%s/index.html">'
                    '<div class="anno">%s classe</div>'
                    '<div class="nome">%s</div>'
                    '<span class="stato">%d di %d unità</span></a>'
                    % (d['percorso'], anno.lower(), materia, fatte, tot))
            else:
                carte.append(
                    '<div class="classe attesa">'
                    '<div class="anno">%s classe</div>'
                    '<div class="nome">%s</div>'
                    '<span class="stato">in preparazione</span></div>'
                    % (anno.lower(), materia))
        blocchi.append(
            '<section class="materia"><h2>%s</h2>\n<div class="griglia">\n%s\n</div></section>'
            % (materia, "\n".join(carte)))
    return """<!DOCTYPE html>
<html lang="it">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Materiali di matematica e fisica — Liceo Bodoni</title>
<link rel="stylesheet" href="assets/stile.css">
</head>
<body>
<div class="foglio">
<header class="testata">
  <p class="occhiello">Liceo scientifico Bodoni</p>
  <h1>Materiali di matematica e fisica</h1>
  <p class="sommario">Appunti riorganizzati, verificati e resi interattivi, raccolti per materia e per anno di corso.
  Ogni classe apre sul proprio indice degli argomenti; da lì si raggiungono le singole unità, con teoria,
  grafici manovrabili tramite cursori, esempi svolti e quesiti d'esame commentati.</p>
</header>
%s
<footer>
  <p>Ultimo aggiornamento: %s. Le sezioni contrassegnate come in preparazione verranno pubblicate man mano.</p>
</footer>
</div>
</body>
</html>
""" % ("\n".join(blocchi), datetime.date.today().strftime("%d/%m/%Y"))

def indice(dati):
    perc = dati['percorso']
    tot = sum(len(a['unita']) for a in dati['aree'])
    fatte = sum(1 for a in dati['aree'] for u in a['unita'] if esiste(u, perc))
    pct = round(100 * fatte / tot) if tot else 0
    sez = []
    for a in dati['aree']:
        righe = []
        for u in a['unita']:
            c = cartella_unita(u)
            pronto = esiste(u, perc)
            tit = ('<a href="argomenti/%s/index.html">%s</a>' % (c, u['titolo'])) if pronto else u['titolo']
            meta = ("pagine %s degli appunti" % u['pagine']) if u['pagine'] != '—' else "testo nuovo, non presente negli appunti"
            if not pronto:
                meta += " · in attesa di pubblicazione"
            righe.append(
                '<article class="unita">'
                '<div class="numero">%02d</div>'
                '<div><p class="titolo">%s</p><p class="testo">%s</p><p class="meta">%s</p></div>'
                '<span class="peso %s">%s</span>'
                '</article>' % (u['n'], tit, u['descrizione'], meta,
                                slug(u['peso']), u['peso']))
        etichetta = ' <span class="badge-nuovo">nuovo</span>' if a.get('nuovo') else ''
        sez.append('<h2>%s%s</h2>\n<p class="area-desc">%s</p>\n%s'
                   % (a['nome'], etichetta, a['descrizione'], "\n".join(righe)))
    return """<!DOCTYPE html>
<html lang="it">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>%s — indice degli argomenti</title>
<link rel="stylesheet" href="../assets/stile.css">
</head>
<body>
<div class="foglio">
<header class="testata">
  <nav class="briciole"><a href="../index.html">&larr; Tutte le classi</a></nav>
  <p class="occhiello">Indice degli argomenti</p>
  <h1>%s</h1>
  <p class="sommario">%s. Il percorso segue l'ordine degli appunti di classe: si parte dai limiti e si arriva
  agli integrali e alle equazioni differenziali, passando per i teoremi che ogni anno tornano fra i quesiti.
  L'indicazione a destra di ciascuna unità segnala quanto quell'argomento pesa nella prova, ed è la misura
  con cui è stato calibrato l'approfondimento.</p>
</header>
<div class="avanzamento">
  <strong>%d unità pubblicate su %d.</strong>
  <div class="barra"><span style="width:%d%%"></span></div>
</div>
%s
<footer>
  <p>Fonte: appunti manoscritti della classe, %s. Le equazioni differenziali sono state redatte ex novo.
  Ultimo aggiornamento: %s.</p>
</footer>
</div>
</body>
</html>
""" % (dati['classe'], dati['classe'], dati['sottotitolo'], fatte, tot, pct,
       "\n".join(sez), dati['fonte'], datetime.date.today().strftime("%d/%m/%Y"))

if __name__ == '__main__':
    classi = carica_tutti()
    open(os.path.join(RAD, 'index.html'), 'w', encoding='utf-8').write(hub(classi))
    for d in classi.values():
        os.makedirs(os.path.join(RAD, d['percorso']), exist_ok=True)
        open(os.path.join(RAD, d['percorso'], 'index.html'), 'w', encoding='utf-8').write(indice(d))
        print("Generato:", d['percorso'] + '/index.html')
    print("Generato: index.html")
