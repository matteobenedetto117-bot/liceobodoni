# Liceo Bodoni — materiali di matematica e fisica

Appunti riorganizzati, verificati e resi interattivi.
Pagina di ingresso: `index.html`.

## Struttura

- `index.html` — hub delle classi, generato
- `matematica-5/index.html` — indice degli argomenti, generato
- `matematica-5/argomenti/NN-slug/` — le singole unità
- `_dati/matematica-5.json` — elenco delle 45 unità, fonte di verità
- `_build/genera.py` — rigenera hub e indice
- `_fonti/` — appunti manoscritti originali

Dopo ogni unità pubblicata: `python3 _build/genera.py`.
