# Registro — Matematica prima

Rettifiche e aggiunte rispetto alla traccia manoscritta, per l'insegnante. Non compare nulla di
questo sul sito pubblico.

## Unità 01 — Gli insiemi numerici N, Z, Q, R
- Parole: 188 (incl. titolo/nav/footer), su circa un quarto di pagina di traccia (il solo diagramma
  a pagina 3 di matematica-1.pdf; il resto della pagina appartiene già all'unità 02).
- Rettifica: nessuna. La traccia riporta solo il diagramma con le quattro etichette e gli esempi
  N={0,1,2,…}, Z={…,-2,-1,0,1,2,…}, Q={-2/5, 7/4}, R={π, √2}: nessun calcolo da verificare.
- Aggiunta: la frase che lega ogni ampliamento a un'operazione che diventa possibile (sottrazione in
  Z, divisione in Q, numeri come √2 in R) non è scritta esplicitamente nella traccia ma è implicita
  negli esempi scelti nel disegno stesso; l'ho resa esplicita in una riga per rendere leggibile il
  perché della catena di inclusioni. Verificato con SymPy: sqrt(2) e pi hanno is_rational=False,
  -2/5 e 7/4 hanno is_rational=True.

## Unità 02 — Espressioni numeriche e ordine delle operazioni
- Parole: 156 su 1,5 pagine di traccia (pag. 3–4)
- Rettifica: nessuna, l'esempio numerico è corretto (verificato con SymPy: risultato 51)
- Aggiunta: nessuna

## Unità 03 — Espressioni letterali
- Parole: 224 su circa 1,3 pagine di traccia (pag. 4 intera più il primo blocco di pag. 5, fino
  al calcolo 3+4=7; il resto di pag. 5 appartiene già all'unità 04).
- Rettifica: nessuna. Verificato con SymPy: 3(2n+5)+6-4n/2 si semplifica in 4n+21, e 3a+b con
  a=1, b=4 vale 7, come nella traccia.
- Aggiunta: nessuna.

## Unità 04 — Proprietà delle operazioni e proprietà invariantiva
- Parole: 218 su 2 pagine di traccia (dal blocco "Proprietà delle operazioni in N" a pag. 5,
  fino alla proprietà invariantiva della divisione a pag. 6; l'intestazione "Potenze" a fine
  pag. 6 apre già l'unità 05).
- Rettifica: nessuna. Verificato con SymPy: (a+c)-(b+c)=a-b e (a·c)/(b·c)=a/b sono identità;
  l'esempio numerico 17-7=(17+3)-(7+3)=10 è corretto.
- Aggiunta: nessuna. Il riquadro sul verso della proprietà distributiva della divisione riprende
  la correzione già presente nella traccia stessa (la formula sbagliata è barrata in rosso con
  "NO!").

## Unità 05 — Potenze e loro proprietà
- Parole: circa 610 su 7 pagine di traccia (pagine 6–12)
- Rettifica: nessuna, i calcoli della traccia (potenze, scomposizioni, MCD/mcm, criteri di divisibilità) sono risultati corretti, verificati con SymPy/Python.
- Aggiunta: nessuna. La pagina contiene solo le regole delle potenze, la definizione di numero primo, scomposizione in fattori primi, MCD/mcm e i criteri di divisibilità presenti nelle pagine 6–12, organizzati con brevi frasi di raccordo. Il titolo dell'unità copre solo le potenze, ma la traccia in quell'intervallo di pagine include anche numeri primi, MCD/mcm e criteri di divisibilità (non trattati in nessun'altra unità del percorso): sono stati inclusi perché appartengono a quelle pagine.

## Unità 06 — Numeri interi: opposti, concordi e discordi, valore assoluto
- Parole: 261 (incl. titolo/nav/footer) su circa 1,5 pagine di traccia (pag. 13 intera più la
  sola sezione "Valore assoluto o modulo" a inizio pag. 14; il resto di pag. 14, con l'intestazione
  "Operazioni in Z", appartiene già all'unità 07).
- Rettifica: nessuna. Verificato con Python: |5|=5, |-2|=2, |-156|=156, |0|=0; +8 e +7 concordi
  (stesso segno), -5 e +3 discordi (segno opposto), come nella traccia.
- Aggiunta: nessuna.

## Unità 07 — Operazioni in Z e potenze con base negativa
- Parole: 320 (incl. titolo/nav/footer) su circa 2,5 pagine di traccia (la sezione "Operazioni
  in Z" a fine pag. 14, tutta pag. 15, tutta pag. 16; pag. 17 apre già l'unità 08 con i numeri
  razionali).
- Rettifica: nessuna. Verificato con Python: (-2)^5=-32, (-2)^4=+16, 5-2=5+(-2)=3,
  +5:(-5)=-1, +6:(+2)=+3, -2·(-7)=+14, -3·(+5)=-15, tutti conformi alla traccia.
- Aggiunta: nessuna.

## Unità 08 — Numeri razionali: frazioni, riduzione, denominatore comune
- Parole: 390 (incl. titolo/nav/footer) su 2 pagine di traccia (pag. 17–18 di matematica-1.pdf;
  pag. 19, con l'intestazione "Confronto di numeri razionali", apre già l'unità 09).
- Rettifica: nessuna. Verificato con SymPy: 10/8 = 5/4, 11/6 = 55/30, 4/15 = 8/30, mcm(6,15)=30,
  tutti conformi alla traccia.
- Aggiunta: nessuna.

## Unità 09 — Operazioni con le frazioni
- Parole: 649 (incl. titolo/nav/footer) su 6 pagine di traccia (pag. 19–24 di matematica-1.pdf;
  pag. 25, con l'intestazione "Decimale periodico", apre già l'unità 10).
- Rettifica: a pag. 24 l'ultimo esempio scrive 7,3482 = 73482/1000, ma un numero con quattro cifre
  decimali richiede denominatore 10000, non 1000 (73482/1000 = 73,482, non 7,3482). Corretto in
  73482/10000 = 36741/5000. Corretta anche l'etichetta "-1" sulla retta numerica dell'esempio di
  ordinamento (pag. 20): l'elenco dei numeri da ordinare include -1/2, non -1, e -1/2 è la
  posizione mostrata nel disegno; la retta SVG riporta -1/2. Verificato tutto con Python
  (fractions.Fraction): addizioni, sottrazioni, moltiplicazioni, divisioni, potenze con esponente
  positivo, nullo e negativo, confronti fra frazioni discordi e concordi, conversioni
  decimale-frazione, tutti conformi alla traccia (a parte le due correzioni sopra).
- Aggiunta: nessuna.

## Unità 10 — Frazioni generatrici dei numeri decimali periodici
- Parole: 172 (incl. titolo/nav/footer) su 1 pagina di traccia (pag. 25 di matematica-1.pdf; pag.
  24, con la classificazione dei decimali e il passaggio da decimale finito a frazione, era già
  stata assorbita nell'unità 09; pag. 26, con l'intestazione "Proporzioni", apre già l'unità 11).
- Rettifica: nessuna. Verificato con Python (fractions.Fraction): 233/900 = 0,25888... = 0,25
  con periodo 8; 421/99 = 4,252525... = 4 con periodo 25; 3808/990 = 3,846464... = 3,8 con periodo
  46 — tutti conformi alla traccia.
- Aggiunta: nessuna.

## Unità 11 — Proporzioni e loro proprietà
- Parole: 322 (incl. titolo/nav/footer) su 3 pagine di traccia (pag. 26–28 di matematica-1.pdf;
  pag. 25, ultima riga, chiude già l'unità 10; pag. 29, con l'intestazione "Percentuali", apre già
  l'unità 12).
- Rettifica: nessuna. Verificato con SymPy: comporre e scomporre su 2:5=4:10 e 5:2=10:4, scambio
  di estremi e di medi, inversione su 3:2=6:4, e i tre esempi finali (8:x=15:225 → x=120;
  5:14=x:63 → x=45/2; (x+2):12=10:6 → x=18) — tutti conformi alla traccia.
- Aggiunta: nessuna.
