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

## Unità 12 — Percentuali
- Parole: 224 (incl. titolo/nav/footer) su 2 pagine di traccia (pag. 29–30 di matematica-1.pdf;
  pag. 28 chiude già gli esempi dell'unità 11; pag. 30, in fondo, con l'intestazione "Numeri Reali
  R", apre già l'unità 13).
- Rettifica: nessuna. Verificato con SymPy: 20% di 3600 = 720; 15% di A = 180 → A = 1200; 621 è il
  27% di 2300 — tutti conformi alla traccia.
- Aggiunta: nessuna.

## Unità 13 — Numeri irrazionali e numeri reali
- Parole: 353 (incl. titolo/nav/footer) su 3 pagine di traccia (pag. 30–32 di matematica-1.pdf;
  la parte alta di pag. 30, con le percentuali, era già assorbita nell'unità 12 — l'unità 13
  inizia dalla sezione "Numeri Reali R" in fondo alla pagina; pag. 33, con l'intestazione
  "Monomi", apre già l'unità 14).
- Rettifica: nessuna. Verificato con SymPy: $\sqrt2$ non è razionale (sympy.sqrt(2).is_rational
  = False), e il passaggio $a=2m \Rightarrow 4m^2=2b^2 \Rightarrow 2m^2=b^2$ della dimostrazione
  per assurdo torna algebricamente.
- Aggiunta: nessuna.

## Unità 14 — Monomi: definizione, forma normale, grado
- Parole: 317 (incl. titolo/nav/footer) su 3 pagine di traccia (pag. 33–35 di matematica-1.pdf;
  pag. 36, con l'intestazione "Monomi simili, opposti e uguali", apre già l'unità 15).
- Rettifica: nessuna. Verificato con SymPy: la riduzione $a^2\cdot\frac12\cdot b\cdot 3a^3=\frac32a^5b$
  e il calcolo del grado complessivo $3+1+2=6$ tornano entrambi.
- Aggiunta: nessuna.

## Unità 15 — Monomi simili, opposti e uguali
- Parole: 171 (incl. titolo/nav/footer) su 1 pagina di traccia (pag. 36 di matematica-1.pdf;
  le due righe iniziali di pagina, "i numeri sono monomi di grado 0" e "0 non ha grado", erano
  già state assorbite nell'unità 14; pag. 37 apre già l'unità 16, "Operazioni con i monomi").
- Rettifica: nessuna. Verificato con SymPy: 9/3 = 3, quindi $3xy^2$ e $\frac93xy^2$ hanno
  davvero lo stesso coefficiente e sono monomi uguali, come nella traccia.
- Aggiunta: nessuna.

## Unità 16 — Operazioni con i monomi
- Parole: 472 su 3 pagine di traccia (pagg. 37–39 di matematica-1.pdf; pag. 40 apre
  già l'unità 17, "MCD e mcm").
- Rettifica: nessuna. Verificati con SymPy tutti i conti della traccia: il prodotto
  $\frac45a^2b\cdot(-\frac18bc^2)\cdot(-10a)=a^3b^2c^2$ (i coefficienti danno 40/40 = 1),
  le sei divisioni della pagina 38, le due non eseguibili comprese, e le quattro potenze
  di pagina 39, incluso $(-2x^4y^2)^3=-8x^{12}y^6$.
- Aggiunta: un solo riquadro "Errore da evitare" sulla condizione di divisibilità — la
  traccia segna con due cerchiature in rosso e un "NO" i due casi non divisibili senza
  dire che cosa vada guardato, ed è la distinzione su cui si sbaglia. Nessun esempio,
  nessuna dimostrazione, nessuna tabella di sintesi aggiunti.

## Unità 17 — MCD e mcm fra monomi
- Parole: 619 su 3 pagine di traccia (40–42), pari a 206 parole per pagina
- Rettifica: nessuna. I due calcoli della traccia (MCD = 2ab², mcm = 12a³b⁴c²) sono stati verificati con SymPy e sono corretti.
- Aggiunta: nessuna. Lo schema per colonne della traccia è stato ridisegnato in SVG e riprodotto due volte, una per il MCD e una per il mcm, perché nella traccia il secondo schema è ricopiato per esteso. La verifica delle tre divisioni per il MCD (3a²bc², 2ab²c, 6) è un controllo sui dati già presenti, non un esempio nuovo.

## Unità 18 — Polinomi: definizione, forma normale, grado
- Parole: 682 su 4 pagine di traccia (43–46), pari a 171 parole per pagina. Il JSON assegna
  all'unità le pagine 43–45, ma la trattazione del grado prosegue senza stacco fino a fine
  pagina 46, e le operazioni cominciano a pagina 47: l'unità è stata chiusa a pagina 46.
- Rettifica: nessuna. Verificati con SymPy la riduzione $6y^4-2y+y^4=7y^4-2y$, le forme
  normali $3aba^2+4a^2b=3a^3b+4a^2b$ e $7a^2ba+ab^2=7a^3b+ab^2$, i gradi rispetto ad $a$ e
  a $b$ di $2a^3b^2+3ab^5$ (3 e 5), il grado complessivo 6 di $9x^4y-x^2+2x^3y^3$ e
  l'omogeneità di $3x^3y-x^2y^2$ (4 e 4) contro $a^3b^2-7a^2b$ (5 e 3).
- Aggiunta: un solo riquadro "Errore da evitare", che ricorda di ridurre in forma normale
  prima di contare i termini e calcolare il grado; usa l'esempio $6y^4-2y+y^4$ già presente
  nella traccia. Nessun esempio nuovo, nessuna dimostrazione, nessuna tabella di sintesi.
  I due schemi della traccia (il monomio più il monomio nullo, e le graffe sui gradi dei
  tre termini) sono stati ridisegnati in SVG.

## Unità 19 — Operazioni con i polinomi
- Parole: 257 su 2 pagine di traccia (47 e prima metà di 48), pari a circa 170 parole per
  pagina effettiva. Il JSON assegna all'unità le pagine 45–46, ma quelle pagine chiudono la
  trattazione del grado (unità 18): le operazioni cominciano a pagina 47 e si fermano dove
  a pagina 48 si apre il titolo «Prodotti notevoli», che è l'unità 20. La pagina è stata
  costruita su quell'intervallo. La traccia è quasi tutta formule, quindi il conteggio è
  basso in valore assoluto ma il rapporto è in linea con le unità vicine.
- Rettifica: nessuna. Verificati con SymPy i tre esempi della traccia:
  $(\tfrac12 y+x^2)+(-x^2+1+y)=\tfrac32 y+1$;
  $(a^4-3a^2)-(2a-a^2+\tfrac34 a^4)=\tfrac14 a^4-2a^2-2a$;
  $(-8ax)(9a-\tfrac34 x^3)=-72a^2x+6ax^4$; $(3x+y)(x-2y)=3x^2-5xy-2y^2$.
- Aggiunta: un solo riquadro "Errore da evitare" sul segno meno davanti a una parentesi,
  costruito sul secondo esempio della traccia, e lo schema SVG dei quattro prodotti
  $ac,ad,bc,bd$, che rende visibile la regola già scritta nella traccia. Nessun esempio
  nuovo, nessuna dimostrazione, nessuna tabella di sintesi.

## Unità 20 — Quadrato di binomio e somma per differenza
- Parole: 437 su 2,5 pagine di traccia (PDF 48–50, metà)
- Rettifica: nessuna. Tutti i risultati della traccia verificati con SymPy: $(3x^2+5y)^2$, $(2z-a)^2$, $(x+7y)(x-7y)$, $(x+2)(-x+2)$, $(-3+x)(-3-x)$ sono corretti così come scritti.
- Aggiunta: nessuna. Conservati i due prodotti notevoli, la derivazione per moltiplicazione diretta che la traccia svolge, l'avvertenza "$(A+B)^2 \neq A^2+B^2$" e tutti e cinque gli esempi, nessuno di più.
- Nota: aggiornato il link "successiva" dell'unità 19, che puntava all'indice.

## Unità 21 — Cubo di binomio e quadrato di trinomio
- Parole: 429 su 1,5 pagine di traccia (PDF 50, metà inferiore, e 51), pari a circa 286
  parole per pagina effettiva.
- Rettifica: nessuna. Verificati con SymPy tutti e cinque i risultati della traccia:
  $(2a+y)^3=8a^3+12a^2y+6ay^2+y^3$; $(x^2-2)^3=x^6-6x^4+12x^2-8$;
  $(2x+y+3z)^2=4x^2+y^2+9z^2+4xy+12xz+6yz$;
  $(3a+b-2x)^2=9a^2+b^2+4x^2+6ab-12ax-4bx$;
  $(-c+2x-5z)^2=c^2+4x^2+25z^2-4cx+10cz-20xz$.
- Aggiunta: un solo riquadro "Errore da evitare" sui tre doppi prodotti del trinomio, e lo
  schema SVG della griglia tre per tre dei nove prodotti, che ridisegna le sottolineature
  colorate con cui la traccia raggruppa i termini uguali. Nessun esempio nuovo, nessuna
  dimostrazione in più, nessuna tabella di sintesi. Conservate entrambe le derivazioni per
  moltiplicazione diretta che la traccia svolge.
- Nota: aggiornato il link "successiva" dell'unità 20, che puntava all'indice.

## Unità 22 — Insiemi: definizione e rappresentazioni
- Parole: 476 su 2 pagine di traccia (pp. 52–53), circa 238 parole per pagina.
- Rettifica: nessuna. Il contenuto della traccia è corretto così com'è; nessun calcolo da
  verificare in questa unità.
- Aggiunta: un solo riquadro "Da tenere presente" che distingue fra criterio difficile da
  verificare e criterio non oggettivo, perché la traccia presenta il controesempio dei
  cinque film senza chiarire dove stia esattamente il difetto. Ridisegnato in SVG il
  diagramma di Eulero-Venn delle vocali che la traccia disegna a mano. Nessun esempio
  nuovo: restano quelli della traccia (naturali fra 2 e 7, lettere dell'alfabeto, i cinque
  film, $-15 \in \mathbb{Z}$, $\sqrt{3} \notin \mathbb{Q}$, le vocali, i naturali maggiori
  di 3). Nessuna tabella di sintesi, nessuna proprietà anticipata.

## Unità 23 — Insieme vuoto, cardinalità, sottoinsiemi
- Parole: 417 su 2 pagine di traccia (pp. 54–55), circa 209 parole per pagina.
- Rettifica: nessuna. Il contenuto della traccia è corretto; l'unico dato numerico
  presente, $|V|=5$ per le vocali dell'alfabeto italiano, è verificato.
- Aggiunta: un solo riquadro "Errore da evitare" sulla differenza fra $\subseteq$ e
  $\subset$, perché la traccia introduce i due simboli di seguito senza dire esplicitamente
  che $A \subset A$ è scorretto. Ridisegnato in SVG il diagramma koala–mammiferi–animali.
  Nessun esempio nuovo: restano quelli della traccia (lettere dell'alfabeto, numeri pari,
  vocali, koala–mammiferi–animali). Nessuna dimostrazione aggiunta: in particolare non è
  giustificato perché l'insieme vuoto sia sottoinsieme di qualsiasi insieme, come nella
  traccia. Nessuna tabella di sintesi.
- Nota: aggiornato il link "successiva" dell'unità 22, che puntava all'indice.

## Unità 24 — Unione, intersezione e differenza
- Parole: 842 su 5 pagine di traccia (pp. 56–60), circa 168 parole per pagina.
- Contenuto: il titolo dell'unità nomina le tre operazioni, ma l'intervallo di pagine
  assegnato dal file di classe comprende anche "Insiemi uguali" e "Insieme delle parti"
  (pp. 56–57), che l'unità 23 non tratta e l'unità 25 (pp. 61–62, complementare e
  prodotto cartesiano) non raggiunge. Sono quindi stati inclusi qui, per non perderli.
- Rettifica: nessuna. Verificati con SymPy i dati numerici della traccia: con i naturali
  compresi fra 0 e 10 esclusi, A = {2;4;6;8}, B = {3;6;9}, A∪B = {2;3;4;6;8;9},
  A∩B = {6}; l'insieme delle parti di {a;b;c} ha effettivamente 8 elementi e quello di
  {0;1;2;3} ne ha 2⁴ = 16.
- Aggiunta: un riquadro "Errore da evitare" sulla non simmetria della differenza, con
  B − A = {3;9} calcolato sugli stessi due insiemi dell'esempio della traccia — la
  traccia definisce A − B ma non mette in guardia sull'inversione. Uno strumento
  interattivo (tre pulsanti che evidenziano a turno unione, intersezione e differenza
  sullo stesso diagramma), che mostra le tre zone già disegnate separatamente nella
  traccia. Nessun esempio nuovo: restano quelli della traccia (a;b;c, {0;1;2;3},
  multipli di 2 e di 3, B ⊆ A, animali vertebrati e invertebrati). Nessuna dimostrazione
  aggiunta: in particolare la regola |P(A)| = 2ⁿ resta enunciata e non giustificata,
  come nella traccia. Nessuna tabella di sintesi.
- Non trattato qui, perché ricade nelle pagine dell'unità 25: le proprietà della
  differenza per insiemi disgiunti (A − B = A) e per A ⊆ B (A − B = ∅), a p. 61.

## Unità 25 — Complementare e prodotto cartesiano
- Parole: 558 su 2 pagine di traccia (pp. 61–62), 279 per pagina.
- Contenuto della traccia, per intero e nel suo ordine: i due casi particolari della
  differenza rimasti in sospeso dall'unità 24 (A − B = A per insiemi disgiunti,
  A − B = ∅ per A ⊆ B, p. 61) con i due diagrammi; la definizione di complementare
  B̄_A con il diagramma tratteggiato; la definizione di prodotto cartesiano con la
  scrittura per caratteristica; l'esempio A = {4;5;6}, B = {1;2}; le due proprietà
  A × B ≠ B × A e |A × B| = |A| · |B| con il conto 3 · 2 = 6.
- Rettifica: nessuna. Le sei coppie dell'esempio e il conto della cardinalità sono stati
  verificati e corrispondono alla traccia.
- Aggiunta: un riquadro "Errore da evitare" sulla condizione B ⊆ A, necessaria perché la
  scrittura B̄_A abbia senso — la traccia pone la condizione nella definizione ma non
  segnala il caso in cui cade. Uno strumento interattivo (due cursori per |A| e |B| che
  ridisegnano la griglia delle coppie) per la sola proprietà |A × B| = |A| · |B|, che
  nella traccia è enunciata senza figura. Nessun esempio nuovo, nessuna dimostrazione
  aggiunta, nessuna tabella di sintesi.

## Unità 26 — Equazioni: definizioni, forma normale, grado
- Parole: 552 su 2 pagine di traccia (pp. 63–64), 276 per pagina.
- Contenuto della traccia, per intero e nel suo ordine: la definizione di equazione come
  uguaglianza fra espressioni letterali con le incognite; l'esempio 4x − 1 = 3x + 1 con
  la risoluzione per trasporto e cambio di segno fino a x = 2; lo schema algebriche /
  trascendenti e intere / fratte con i sei esempi della traccia; la forma normale
  P(x) = 0 con l'esempio 3x³ + 2x + 1 = 0; la definizione di grado; i tre esempi di
  I, II e III grado.
- Rettifica: nessuna. Verificati con SymPy: x = 2 risolve 4x − 1 = 3x + 1 (entrambi i
  membri valgono 7); i gradi dei tre esempi finali sono 1, 2, 3; il grado di
  3x³ + 2x + 1 è 3.
- Aggiunta: la verifica per sostituzione della soluzione x = 2 (due righe, il valore era
  ricavato nella traccia senza controllo) e un riquadro "Errore da evitare" sul fatto che
  il grado si legge solo dopo la riduzione in forma normale — la traccia dice "ridotto in
  forma normale" ma non segnala il caso in cui i termini di grado massimo si elidono.
  Formulato senza introdurre esempi nuovi. Nessuna dimostrazione aggiunta, nessuno
  strumento interattivo, nessuna tabella di sintesi.
- Nota: i tre esempi di I, II e III grado stanno in cima a p. 65, cioè nelle pagine
  dell'unità 27, ma completano la definizione di grado e sono stati inclusi qui. L'unità
  27 parte dal titolo "Risoluzione di equazioni numeriche intere di I grado", più sotto
  nella stessa pagina.

## Unità 27 — Risoluzione di equazioni numeriche intere di primo grado
- Parole: 312 su 2 pagine di traccia nominali (pp. 65–66), in pratica circa 1,2 pagine:
  la parte alta di p. 65 (i tre esempi di I, II e III grado) è già stata usata
  nell'unità 26, e la parte bassa di p. 66 apre le "Proprietà", cioè i principi di
  equivalenza dell'unità 28. Rapporto effettivo circa 260 parole per pagina.
- Contenuto della traccia, per intero e nel suo ordine: la frase di metodo (si svolgono i
  calcoli da entrambi i lati dell'uguale come se fossero una coppia di espressioni);
  l'unico esempio, 1/3x + 2x − 1 = 4x − 6x + 1/3x + 7/3x + 6, con le due righe di
  riduzione fino a 7/3x − 1 = 2/3x + 6; la regola del trasporto con cambio di segno e il
  disegno delle due frecce sopra e sotto l'uguale, ridisegnato in SVG; le righe
  7/3x − 2/3x = 1 + 6 e 5/3x = 7; la frase sulla moltiplicazione per opportuni valori
  numerici, con 3·(5/3)x = 7·3, 5x = 21 e x = 21/5.
- Rettifica: nessuna. Verificati con SymPy: il primo membro si riduce a 7/3x − 1 e il
  secondo a 2/3x + 6 come nella traccia; l'unica soluzione è x = 21/5, e sostituendola
  entrambi i membri valgono 44/5.
- Aggiunta: nessun esempio, nessuna dimostrazione, nessuna tabella di sintesi, nessuno
  strumento interattivo. Un solo riquadro "Errore da evitare" sul fatto che il fattore
  moltiplicativo va applicato a tutti i termini di entrambi i membri, e non al solo
  termine da eliminare; formulato senza introdurre esempi nuovi. Aggiunta anche, in una
  riga, la divisione finale per 5 come passaggio esplicito: nella traccia il passaggio
  da 5x = 21 a x = 21/5 è indicato solo dalle cancellature a margine.

## Unità 28 — Principi di equivalenza
- Parole: 383 su 2 pagine di traccia nominali (pp. 66–67); in pratica circa 1,5 pagine,
  perché la parte alta di p. 66 (isolamento della x nell'esempio con i denominatori) è
  già stata usata nell'unità 27. Rapporto effettivo circa 255 parole per pagina.
- Contenuto della traccia, per intero e nel suo ordine: le tre proprietà — sommare e
  sottrarre uno stesso termine da entrambi i lati, eliminare termini uguali a lati
  opposti, moltiplicare tutti i termini per un numero diverso da zero — ciascuna con i
  soli esempi della traccia: 2x + 3x + 3 = 6x + 8 + 2x → 5x + 3 = 8x + 8;
  7x + 12 − 3x − 6 = 12 + 8x − 3x + 14 → 7x − 6 = 8x + 14 (le cancellature colorate a
  margine sono state ridisegnate in SVG); 2·(3x + 1/2 + x − 2 = −3/2x + 7/2) →
  6x + 1 + 2x − 4 = −3x + 7; 1/2·(4x + 6 = −8x + 2) → 2x + 3 = −4x + 1.
- Rettifica: nessuna. Verificati con SymPy: in tutti e quattro gli esempi l'insieme
  delle soluzioni non cambia fra la riga di partenza e quella di arrivo (x = −5/3,
  x = −20, x = 10/11, x = −1/3), e ogni riduzione dei termini simili è esatta.
- Aggiunta: nessun esempio nuovo, nessuna dimostrazione, nessuna tabella di sintesi,
  nessuno strumento interattivo. Due riquadri "Errore da evitare": uno sul fatto che
  termini uguali si cancellano solo se stanno a lati opposti — nello stesso membro si
  sommano — e uno sul perché il fattore moltiplicativo deve essere diverso da zero.
  Aggiunta anche una riga che collega la prima proprietà al trasporto con cambio di
  segno già usato nell'unità 27: nella traccia il legame è implicito.

## Unità 29 — Equazione determinata, impossibile, indeterminata
- Parole: 278 su 1 pagina di traccia (p. 68). Rapporto 278 parole per pagina: la pagina
  manoscritta è quasi tutta simboli, tre righe di esempi e tre etichette, quindi le
  parole di spiegazione pesano più del solito rispetto alla traccia.
- Contenuto della traccia, per intero e nel suo ordine: i tre risultati possibili con i
  soli esempi presenti — x = 7/3 determinata; x + 2 = x + 3 → 2 = 3, cioè 0 = 1,
  impossibile; 2x + 2 = 2x + 6 − 4 → 2x + 2 = 2x + 2 → 0 = 0, indeterminata. Le
  cancellature colorate del quaderno sono rese come passaggi scritti.
- Rettifica: nessuna. Verificati con SymPy: x + 2 = x + 3 non ha soluzioni;
  2x + 2 = 2x + 6 − 4 si riduce all'identità 0 = 0 ed è soddisfatta da ogni x.
- Aggiunta: nessun esempio nuovo, nessuna dimostrazione, nessuna tabella di sintesi,
  nessuno strumento interattivo, nessun disegno (la traccia non ne ha). Un solo riquadro
  "Errore da evitare", sulla confusione fra 0 = 0 e x = 0, che è lo sbaglio tipico di
  questo punto del programma.

## Unità 30 — Polinomi come funzioni e zeri di un polinomio
- Parole: 546 su 2 pagine di traccia (pp. 69–70 di matematica-1.pdf), cioè 273 per
  pagina. La pagina 69 è per metà occupata da due diagrammi a frecce, che qui sono
  ridisegnati in SVG e richiedono ciascuno una didascalia.
- Contenuto della traccia, per intero e nel suo ordine: il diagramma di una relazione
  generica fra A e B; la definizione di funzione come relazione che a ogni elemento di A
  associa un solo elemento di B; P(x) = x² con lo schema x ∈ A → P(x) ∈ B e il secondo
  diagramma (A = {−1, 1, 2, 3} → B = {1, 4, 5, 9, 12}); P(x) = x³ − 4x con P(2) = 0, la
  definizione di zero, P(0) = 0, P(−2) = 0, la conclusione che −2, 0, 2 sono zeri, e
  P(1) = −3.
- Rettifica: nessuna. Verificati con SymPy tutti i valori: per x³ − 4x si ha P(2) = 0,
  P(0) = 0, P(−2) = 0, P(1) = −3, e l'insieme completo degli zeri è {−2, 0, 2}; per x²
  le immagini di −1, 1, 2, 3 sono 1, 1, 4, 9, coerenti con le frecce del quaderno.
- Aggiunta: nessun esempio nuovo, nessuna dimostrazione, nessuna tabella di sintesi,
  nessuno strumento interattivo. Due righe di commento non presenti nella traccia: che
  due frecce possono arrivare nello stesso elemento di B mentre non ne possono partire
  due dallo stesso elemento di A (il secondo diagramma lo mostra ma non lo dice), e che
  in P(−2) la potenza dispari conserva il segno — rimando all'unità 7, dove la regola è
  stata introdotta. Un solo riquadro, sulla confusione fra il valore provato e il
  risultato del calcolo.

## Unità 31 — Divisione fra polinomi
- Parole: 858 su 4 pagine di traccia (pagine 71–74 di _fonti/matematica-1.pdf), 215 per pagina.
- Contenuto della traccia riportato per intero e nel suo ordine: le tre domande di
  divisibilità (24 per 8, x²+x per x, x²+x per x²), la definizione di divisibilità con
  A:B=Q e B·Q=A, i due esempi di divisione per un monomio, la divisione in colonna
  (8x³+6x²−5x−3):(2x²+x−1) con le etichette dividendo/divisore/quoziente/resto, i quattro
  passi del procedimento, l'esempio (8x⁴+6x³+1):(x²+x) con i termini nulli di posto, la
  verifica delle due divisioni e il teorema A = B·Q + R.
- Rettifica: nessuna. Verificati con SymPy entrambi i quozienti e i resti — (4x+1, −2x−2)
  e (8x²−2x+2, −2x+1) — le due divisioni per monomio e le due moltiplicazioni di verifica,
  che restituiscono esattamente i dividendi.
- Aggiunta: nessun esempio nuovo, nessuna dimostrazione, nessuna tabella di sintesi,
  nessuno strumento interattivo. Un solo riquadro, sul cambio di segno del passo 2, che è
  l'errore che fa fallire la divisione; nella traccia il cambio di segno è scritto ma non
  motivato. Una riga per dire perché ci si ferma (grado del resto minore del grado del
  divisore), esplicitando il criterio già enunciato al passo 4.

## Unità 32 — Regola di Ruffini
- Parole: 494 su 2 pagine di traccia (pagine 75–76 di _fonti/matematica-1.pdf), 247 per pagina.
- Contenuto della traccia riportato per intero e nel suo ordine: l'esempio guida
  (1−5x²−6x+3x³):(x−2) con il riordino dei monomi e lo schema completo, la condizione sul
  divisore x±a, il grado del quoziente inferiore di uno, il resto come numero, l'esempio
  (3x³+7x²−8):(x+2) con lo zero di posto, e il caso del divisore ax+b con
  (3x³−2x²+2):(3x+1). I tre schemi di Ruffini sono ridisegnati in SVG inline.
- Rettifica: nell'ultimo esempio la traccia dà come resto 5/9, che è il resto della
  divisione ridotta (x³−⅔x²+⅔):(x+⅓) e non di quella di partenza. Il resto corretto di
  (3x³−2x²+2):(3x+1) è 5/3 — verificato con SymPy, insieme ai quozienti e ai resti degli
  altri due esempi (3x²+x−4, R=−7 e 3x²+x−2, R=−4). Nella pagina compare 5/3, senza
  segnalazione al lettore.
- Aggiunta: nessun esempio nuovo, nessuna dimostrazione, nessuna tabella di sintesi,
  nessuno strumento interattivo. Un solo riquadro di attenzione, che è la sede della
  rettifica: spiega perché lo schema restituisce 5/9 e perché va rimoltiplicato per 3.
  Una riga sul coefficiente 0 da scrivere al posto del termine mancante, che nella traccia
  compare nello schema ma non è commentata.

## Unità 33 — Teorema del resto e teorema di Ruffini
- Parole: 399 su 2 pagine di traccia (77–78)
- Rettifica: nessuna. Entrambi gli esempi verificati con SymPy: (3x²−7x−10):(x−2) dà quoziente 3x−1 e resto −12, e P(2)=−12; (x⁴−2x³):(x−2) dà resto 0 con P(2)=0.
- Aggiunta: nulla di contenuto. Un solo riquadro di attenzione sul segno di a (x+3 significa a=−3), che è l'errore tipico su questo passaggio. La traccia enuncia entrambi i teoremi senza dimostrazione e la pagina li lascia così.

## Unità 34 — Raccoglimento totale e parziale
- Parole: 656 su 3 pagine di traccia dichiarate (79–81 di _fonti/matematica-1.pdf), 219 per pagina.
  In pratica le pagine coperte sono 79 e 80: pagina 81 apre il trinomio speciale, che
  prosegue a pagina 82 e che il file di classe assegna anche all'unità 35 (81–84). Per non
  spezzarlo a metà l'ho lasciato per intero all'unità 35, lasciandone qui solo un rimando.
- Contenuto della traccia riportato per intero e nel suo ordine: la scomposizione in fattori
  con l'esempio x³−7x+6, riducibile e irriducibile con l'esempio y³+2y²−9y−18 e il fattore
  y²−9 da scomporre ancora; il raccoglimento totale con tutti e cinque gli esempi, compreso
  quello a coefficienti frazionari; il raccoglimento parziale con i tre esempi, nei due
  raggruppamenti alternativi dello stesso polinomio 3ax+3bx+ay+by.
- Rettifica: nessuna. Tutte e nove le identità della traccia verificate con SymPy.
- Aggiunta: nessun esempio nuovo, nessuna dimostrazione, nessuna tabella di sintesi, nessuno
  strumento interattivo, nessun disegno (la traccia non ne contiene). Un solo riquadro di
  attenzione, sull'1 che resta in parentesi quando si raccoglie un termine per intero, che è
  l'errore tipico del raccoglimento totale. Poche righe di commento dove la traccia scrive
  solo il risultato: come si sceglie il fattore da raccogliere (MCD, minimo esponente) e
  perché nell'ultimo esempio va raccolto −3x e non 3x.

## Unità 35 — Scomposizione con i prodotti notevoli
- Parole: 614 su 4 pagine di traccia (81–84 di _fonti/matematica-1.pdf), 154 per pagina.
  Le pagine 81–82 sono il trinomio speciale, che l'unità 34 aveva lasciato per intero qui
  per non spezzarlo; le pagine 83–84 sono i prodotti notevoli letti al contrario.
- Contenuto della traccia riportato per intero e nel suo ordine: il trinomio speciale
  ricavato da x²+5x+6 con il raccoglimento parziale, la scrittura generale (x+a)(x+b) da cui
  nascono S e P, i quattro esempi (x²−5x+6, y²−8y+15, x²+5x−24, b²+5b−14) e il caso con
  coefficiente davanti a x² (3x²−10x+8); quadrato di binomio con i tre esempi; differenza di
  quadrati con i quattro esempi; quadrato di trinomio con i quattro esempi, compresi quelli a
  coefficienti frazionari; cubo di binomio con le due formule e i quattro esempi.
- Rettifica: nessuna. Tutte e ventuno le identità della traccia verificate con SymPy,
  compresi i due esempi con i termini in ordine sparso (1+12x⁶−8x⁹−6x³ e a³−8b³−6a²b+12ab²).
- Aggiunta: nessun esempio nuovo, nessuna dimostrazione, nessuna tabella di sintesi, nessuno
  strumento interattivo, nessun disegno (la traccia non ne contiene). Lo schema riassuntivo
  di pagina 85 non è stato anticipato: appartiene all'unità 36. Un solo riquadro di
  attenzione, sul modo di leggere i segni di a e b dal segno di P e di S, che è l'errore
  tipico del trinomio speciale. Per il resto solo righe di commento su passaggi già presenti:
  come si controlla il doppio prodotto, perché la somma di quadrati non rientra nella
  formula, e perché le due formule del cubo sono la stessa con −B al posto di B.

## Unità 36 — Come scegliere il metodo di scomposizione
- Parole: 455 su 2 pagine di traccia (85–86)
- Rettifica: nessuna. Verificati con SymPy entrambi gli schemi di Ruffini: (x³+4x²−3):(x+1) dà quoziente x²+3x−3 e resto 0; (a³−3a²+2a−6):(a−3) dà a²+2 e resto 0.
- Aggiunta: nessuna. L'esempio a³−3a²+2a−6 sta in cima a p. 87 ma chiude la trattazione di Ruffini, non apre l'unità 37 (che parte dal titolo "Somma e differenza di cubi"): è stato incluso qui. Il riquadro "Attenzione" sul conteggio dei termini è l'unico commento non presente nella traccia.

## Unità 37 — Somma e differenza di cubi
- Parole: 363 su 2 pagine di traccia (87–88; la sezione comincia a metà della 87)
- Rettifica: nessuna. Tutti i passaggi della traccia verificati con SymPy: la scomposizione di $x^3-8$, le due formule generali, i quattro esempi e la riduzione finale dell'esempio 4 a $9x(x^2-x+1)$ sono corretti.
- Aggiunta: nessuna. Nessuna dimostrazione, nessun esempio e nessuna tabella oltre a quanto presente nella traccia; l'unico riquadro di avvertenza riguarda la confusione fra $A^2-AB+B^2$ e il quadrato di binomio.

## Unità 38 — Frazioni algebriche: definizione, condizioni di esistenza, zeri
- Parole: 405 su 2 pagine di traccia
- Rettifica: a pagina 89 la traccia scrive che per determinare le condizioni di esistenza «troviamo i valori che annullano la frazione e li scartiamo»; i valori da scartare sono quelli che annullano il *denominatore*. Corretto nella pagina senza segnalarlo al lettore (la formulazione giusta compare del resto già nella riga precedente della traccia stessa).
- Aggiunta: nessuna. Enunciati, esempi e riquadro d'avvertenza corrispondono al contenuto della traccia; il riquadro «Attenzione» esplicita in parole la cancellatura in rosso con cui la traccia scarta x=3 dagli zeri.

## Unità 39 — Semplificazione di frazioni algebriche
- Parole: 247 su 1 pagina di traccia (p. 91)
- Rettifica: nessun errore di contenuto. Il file di classe assegna a questa unità le pagine 91–93, ma il quaderno dedica alla semplificazione la sola p. 91: p. 92 apre già "Riduzione allo stesso denominatore", che è l'unità 40. Ho lavorato sulla sola p. 91 e tarato la lunghezza su una pagina di traccia. Verificati con SymPy entrambi gli esempi: $1-4a^2=(1-2a)(1+2a)$, $a-2a^2+a^3-2a^4=a(1-2a)(a^2+1)$ con C.E. $a\neq0\wedge a\neq 1/2$ e risultato $(1+2a)/(a(a^2+1))$; $(x^2-6x+9)/(x^2-9)=(x-3)/(x+3)$.
- Aggiunta: il solo risultato finale dell'esempio 2, che nella traccia si interrompe dopo la scomposizione perché finisce la pagina. Nessun esempio nuovo, nessuna dimostrazione, nessuna tabella. Un solo riquadro di avvertenza, sulla differenza fra cancellare un fattore e cancellare un addendo: è l'errore tipico del capitolo.
