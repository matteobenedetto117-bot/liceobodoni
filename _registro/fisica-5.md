# Registro — Fisica quinta

## Unità 01 — Magneti, poli e assenza di monopoli
- Parole: 436 su 3 pagine di traccia
- Rettifica (revisione concettuale): l'ago libero si allinea solo approssimativamente lungo nord–sud geografico; specificato che il polo nord è l'estremità rivolta al Nord geografico; aggiunto nel testo che vicino al Polo Nord geografico c'è un polo sud magnetico; i monopoli "non sono mai stati osservati" e la fisica classica ne assume l'assenza (prima: "non esistono"); la magnetizzazione avviene per contatto o strofinio.
- Grafica: testo della pagina ingrandito per la lettura alla lavagna e allineato alle righe di sfondo come su un quaderno (scritte dei disegni alla dimensione originale); resi visibili i nomi dei poli nella figura "poli uguali / poli opposti" e frecce orizzontali.
- Animazione: la prima figura (magnetite e ferro) è animata; con il pulsante play i pezzi di ferro si muovono accelerando fino ad attaccarsi alla magnetite.
- Animazione: la seconda figura mostra l'ago strofinato sulla magnetite che si magnetizza; poi la limatura di ferro si raccoglie ai due estremi (poli) e quasi non si muove al centro.
- Animazione: la terza figura mostra, vista dall'alto, l'ago su un galleggiante in una bacinella che oscilla e si ferma lungo nord–sud; poi compaiono polo nord e polo sud. Ricominciando, l'ago parte ogni volta da una posizione diversa.
- Animazione: la quarta figura mostra un magnete che si avvicina a un altro: con poli uguali affacciati viene respinto, con poli opposti viene attirato fino al contatto.
- Animazione: la quinta figura mostra il magnete tagliato due volte (1 → 2 → 4 pezzi); a ogni taglio compaiono i nuovi poli e ogni pezzo resta un magnete completo.
- Aggiunta: nessuna. Nessuna formula presente nella traccia, quindi nessuna verifica SymPy necessaria.

## Unità 02 — Il campo magnetico e le linee di campo
- Parole: 172 su 1 pagina di traccia
- Rettifica: a pagina 4 la traccia afferma che l'intensità del campo "diminuisce linearmente con la distanza dal magnete". Non è corretto (il campo di un dipolo decresce con una potenza della distanza, non linearmente): nella pagina ho tolto "linearmente", lasciando solo che il campo diminuisce allontanandosi dal magnete.
- Aggiunta: nessuna. Nessuna formula quantitativa presente, quindi nessuna verifica SymPy necessaria.
- Revisione: testo impaginato come un quaderno (righe) e ingrandito per la lavagna. Figura del campo rifatta con linee calcolate numericamente per un magnete a barra sottile (modello a cariche magnetiche sulle facce), con le linee che partono a ventaglio dal polo N e rientrano nel polo S; campo debole ai lati: linee chiuse, uscenti da N ed entranti in S all'esterno, da S a N all'interno, più fitte vicino ai poli. Nell'elenco precisato «all'esterno del magnete».

## Unità 03 — Interazione fra campo magnetico e carica elettrica
- Parole: 473 su 2,3 pagine di traccia (pagine 5–6 intere, più l'esempio numerico in cima a pagina 7, prima dell'inizio della sezione "Forza di Lorentz" che appartiene all'unità 04)
- Rettifica: nessuna. Il calcolo numerico di B = F/(q·v⊥) e la verifica dimensionale che porta al tesla sono stati controllati con SymPy e risultano corretti così come nella traccia.
- Aggiunta: nessuna.
- Revisione: tolti sottotitolo e titoletti (resta «Esempio»); tolti i simboli di proporzionalità, sostituiti da «direttamente proporzionale»; impaginazione a quaderno come le unità 01–02. Figura dei tre casi animata (carica ferma, v parallela, v perpendicolare con comparsa di F uscente); figura dell'angolo resa interattiva con cursore e animazione su θ da 0° a 180°, con componenti di v e barra dell'intensità della forza.
- Didascalie divise: nella figura dei tre casi ogni pannello ha la propria didascalia; stessa cosa per la figura dei poli uguali/opposti dell'unità 01 (una didascalia per riga).
- Revisione 2 (testo schematico): tre casi in elenco, v⊥ = v sinθ in formula, dipendenze di F in elenco, F = q v⊥ B e B = F/(q v⊥) in .def, tesla in .def con l'equivalenza in kg/(C·s); esempio ridotto a dati → formula → risultato, arrotondato a 5,3×10⁻³ T (due cifre significative come i dati). Didascalie accorciate. Figura dell'angolo: tolto il tasto ▶, resta solo il cursore con il valore di θ accanto. Scelte dell'utente: titolo invariato, h2 solo «Esempio», brevi frasi di raccordo.

## Unità 04 — La forza di Lorentz
- Parole: 357 su 1,7 pagine di traccia (seconda metà di pagina 7, dalla sezione "Forza di Lorentz" in poi, più pagina 8 intera)
- Rettifica: nessuna. Il modulo F = qvB sinθ è stato verificato con SymPy come coerente con |q v × B| e con la relazione F = qv⊥B già vista nell'unità 03.
- Aggiunta: nessuna.
- Revisione: corretto il modulo in F = |q|vB sinθ (θ fra 0° e 180°); regola della mano destra precisata (medio perpendicolare a pollice e indice); per le cariche negative spiegato che il verso si inverte perché cambia il segno di q. Rifatti i disegni, che mostravano F nello stesso piano di v e B (errato) e, nel secondo, non mostravano F: ora vista in prospettiva con il piano di v e B e F perpendicolare. Tolti sottotitolo e simboli di riquadro, formule in display, impaginazione a quaderno come l'unità 03. Figura 1 interattiva con cursore su θ (0°–180°) e barra dell'intensità; figura 2 animata (F cresce verso l'alto per la carica positiva e verso il basso per la negativa), didascalie divise.
- Revisione 2 (testo schematico, stesso modello dell'unità 03): tolto l'h2 «Definizione»; forza di Lorentz in .def; modulo F = |q|vB sinθ in formula con due voci in elenco (valore assoluto, legame con v⊥); direzione e verso con la mano destra in elenco; carica negativa in una frase. Didascalie accorciate. Figura 1: tolto il tasto ▶, resta solo il cursore con il valore di θ accanto.

## Unità 05 — Moto di particelle cariche in campo elettrico e magnetico uniforme
- Parole: 240 su 1 pagina di traccia (pagina 9)
- Rettifica: nessuna. Verificato con SymPy: a=F/m=qE/m e la forza di Lorentz con θ=0 dà
  qvB·sin(0)=0, coerenti con la traccia.
- Aggiunta: nessuna. Ho accorpato in un'unica figura i quattro schemi della traccia sui casi
  accelerazione/decelerazione per carica positiva e negativa (che per simmetria mostrano la
  stessa fisica) in due soli casi con carica positiva, spiegando a parole che per una carica
  negativa i due casi si scambiano: nessun contenuto nuovo, solo una figura più compatta.
- Revisione: titolo e titoletti invariati (scelta dell'utente). Corretto il primo disegno, che mostrava la forza perpendicolare al campo elettrico: ora $\vec F$ è parallela a $\vec E$ (verso del campo per la carica positiva). Corretta la parabola, che era tracciata a occhio e nel tratto finale tornava indietro contro $\vec v_0$: ora è calcolata ($x=at^2/2$, $y=v_0t$). Precisati: modulo $a=|q|E/m$, verso della forza per cariche positive e negative, moto rettilineo uniformemente accelerato solo con velocità iniziale parallela al campo, forza magnetica nulla anche per $\theta=180°$ ($F=|q|vB\sin\theta$). Tolto il sottotitolo, formule in riquadro azzurro, impaginazione a quaderno come l'unità 04. Tre figure interattive con cursore sul tempo e posizioni a intervalli uguali: carica che accelera e carica che rallenta, si ferma e torna indietro (didascalie per riga); moto parabolico con $\vec v$ tangente e $\vec F$ costante; moto rettilineo uniforme parallelo a $\vec B$.
- Dall'ex unità 06 "Moto circolare e raggio di curvatura" (pagina 10), accorpata:
  - Parole: 255 su 1 pagina di traccia (pagina 10)
  - Rettifica: nessuna. Verificato con SymPy che da $qvB=mv^2/r$ segue $r=mv/(qB)$, coerente con la traccia.
  - Aggiunta: una frase che spiega come il raggio dipende da massa, velocità, carica e campo, indispensabile per dare senso alla formula appena ricavata; nessun contenuto fisico ulteriore.
- Revisione dell'accorpamento: titolo invariato, titoletti "Velocità perpendicolare al campo" e "Il raggio di curvatura" mantenuti (scelta dell'utente), unità successive rinumerate. Corretto il disegno del moto circolare: con B entrante e carica positiva la forza era disegnata verso il centro ma con v orientata in modo da dare una forza verso l'esterno, e il verso di percorrenza era indicato come orario; ora la carica gira in verso antiorario con F verso il centro. Precisato r = mv/(|q|B) e il modulo |q|vB. Figura interattiva con cursore sul tempo: la carica percorre la circonferenza con v tangente, F verso il centro, raggio tratteggiato e posizioni a intervalli uguali.
- Revisione 2 (testo schematico come unità 03–04): forza e accelerazione nel campo elettrico in un'unica formula, segno della carica in elenco, conseguenze del moto circolare (modulo costante, lavoro nullo) in elenco, raggio r = mv/(|q|B) in .def; didascalie accorciate.

## Unità 06 — Spettrometro di massa
- Parole: 155 su 1 pagina di traccia (pagina 11)
- Rettifica: nessuna. Verificato con SymPy che da $r=mv/(qB)$ segue $m=qBr/v$, coerente con la traccia.
- Aggiunta: nessuna. La traccia contiene solo titolo, la definizione "strumento che serve per misurare la massa di particelle cariche" e uno schema incompleto (un riquadro con una velocità entrante); ho ridisegnato lo schema in modo leggibile e collegato la definizione alla formula del raggio di curvatura già ricavata nell'unità 05, risolta rispetto a m, che è esattamente ciò che la descrizione dell'unità nel file di classe indica come contenuto ("misurare la massa sfruttando il raggio di curvatura"). Nessun esempio numerico presente nella traccia, quindi nessuno aggiunto.
- Revisione: titolo invariato (scelta dell'utente), nessun titoletto. Precisati $r=mv/(|q|B)$ e $m=|q|Br/v$, e che la velocità è perpendicolare al campo. Aggiunta: la frase sulla distanza $2r$ dall'ingresso e quella sul raggio direttamente proporzionale alla massa a parità di carica e velocità, necessarie per leggere la figura. Rifatto lo schema (un riquadro con una velocità entrante): regione con B entrante, lastra, semicirconferenza calcolata, punto d'arrivo e quota 2r; cursore sulla massa, con raggio e punto d'arrivo che si spostano, v tangente e F verso il centro. Tolto il sottotitolo, formule in riquadro azzurro, impaginazione a quaderno.
- Revisione 2 (testo schematico): massa m = |q|Br/v in .def, testo ridotto a tre frasi; didascalia accorciata.

## Unità 07 — Selettore di velocità

- Aggiunta su richiesta del docente (13/10/2026), dopo lo spettrometro di massa, dagli appunti «5S_Fisica_Teoria.pdf». Testi riportati identici; solo adattamento al formato (formule in riquadri, velocità selezionata in .def, tre casi in elenco).
- Figure: selettore con cursore sulla velocità (traiettoria calcolata con la forza di Lorentz più la forza elettrica, F_B proporzionale a v); due pannelli per v > E/B e v < E/B.
- Rettifica: nel disegno degli appunti la piastra positiva era in alto ma il campo E e la forza F_E verso l'alto; nel disegno la piastra positiva è in basso, coerente con E verso l'alto.
- Le unità successive sono state rinumerate (+1).

## Unità 08 — Campo magnetico generato da un filo percorso da corrente
- Parole: 240 su 1 pagina di traccia (pagina 12)
- Rettifica: nessuna. La traccia è puramente qualitativa (nessuna formula quantitativa: la legge di Biot-Savart arriva solo nell'unità 11), quindi nessuna verifica SymPy necessaria; ho verificato solo la coerenza fisica del verso di circolazione del campo nei due disegni (corrente verso l'alto → campo antiorario, corrente verso il basso → campo orario), coerente con la regola della mano destra.
- Aggiunta: nessuna. Ho ridisegnato in SVG i due schemi della traccia (il filo con la linea di campo circolare e l'ago magnetico, e la coppia di fili con corrente invertita) e riportato la regola della mano destra così com'è enunciata nella traccia.
- Revisione: rifatta con le regole aggiornate. Titolo invariato; nessun titoletto (la versione originale non ne aveva; l'unità è un'unica sezione). Testo telegrafico riscritto in frasi complete: due paragrafi su campo del filo e ricostruzione delle linee con gli aghi (recuperato il ragionamento della versione precedente alla revisione), frase introduttiva alla regola, regola della mano destra in riquadro come frase unica, frase finale sull'inversione della corrente. Correzione: nella didascalia «gli aghi si allineano lungo la direzione nord–sud» → «approssimativamente lungo la direzione nord–sud». Ripristinata la didascalia della seconda figura (verso antiorario/orario visto dall'alto, verificato con la regola della mano destra). Impaginazione a quaderno invariata, margine di una riga sopra ogni paragrafo. Figure interattive invariate (cursore sulla corrente; coppia di fili). Nessun esempio, nessuna figura decorativa.
- Revisione 2 (testo schematico): definizione e aghi in due frasi, regola della mano destra in una riga nel .def; didascalie accorciate.

## Unità 09 — Forza su un filo percorso da corrente
- Parole: 248 su 1 pagina di traccia (pagina 13)
- Rettifica: nessuna. Verificato con SymPy che sostituendo $q=iL/v$ in $F=qvB\sin\theta$ la velocità di deriva si semplifica e si ottiene esattamente $F=BiL\sin\theta$, coerente con la traccia (dove il passaggio è annotato a mano con le stesse cancellazioni).
- Aggiunta: nessuna. Ho ridisegnato in SVG i due schemi della traccia: la coppia di fili con corrente invertita (con la convenzione entrante/uscente già usata nelle unità precedenti al posto della freccia F nel piano, per coerenza con il resto del percorso) e lo schema generale del filo di lunghezza L nel campo B con angolo θ usato per la derivazione.
- Revisione: rifatta con le regole aggiornate. Titolo invariato; introduzione di due frasi ripristinata; ripristinato il titoletto «Esperienza di Faraday» e aggiunto «Forza su un tratto di filo» per la derivazione. Testo telegrafico riscritto in frasi complete: esperienza di Faraday e inversione della forza, tratto di filo e carica di deriva, passaggi $q=i\,\Delta t$, $\Delta t=L/v$, $q=iL/v$ con frasi di collegamento, semplificazione di $v$, legenda della legge, frase che introduce la regola della mano destra e sue tre voci; didascalie in frasi complete. Nessuna nuova correzione ($F=BiL\sin\theta$ riverificata; verso $\vec L\times\vec B$ entrante nella figura 1 riverificato). Figure con cursore invariate (corrente da −3 A a +3 A; θ da 0° a 180°). Nessun esempio, nessuna figura decorativa.
- Revisione 2 (testo schematico): ricavo di q = iL/v in elenco, legenda di F = BiL sinθ in una riga, regola della mano destra in elenco compatto; tolta la frase introduttiva prima della regola. Figura dell'angolo: il simbolo della forza (⊙) si sovrapponeva al vettore B intorno a θ = 125°, spostato nell'angolo in alto a destra.

## Unità 10 — Spire di corrente e momento torcente magnetico
- Parole: 411 su 2,7 pagine di traccia (pagina 14 intera, pagina 15 intera, la sezione "Esempio" in cima a pagina 16, prima dell'inizio di "Legge di Ampère" che appartiene all'unità 10)
- Rettifica: nessuna. Verificato con SymPy: la derivazione $M_{TOT}=2\cdot ihB\cdot(d/2)=ihBd=iAB$ è algebricamente esatta; l'esempio numerico $M_{max}=Ni\pi r^2B$ con $N=200$, $r=3{,}0\cdot10^{-2}$ m, $i=1{,}6$ A, $B=0{,}35$ T dà $0{,}3167$ N·m, coerente con lo $0{,}32$ N·m arrotondato della traccia.
- Aggiunta: nessuna. Ho ridisegnato in SVG i tre schemi della traccia (la spira rettangolare vista di fronte con le forze entrante/uscente, e le due posizioni estreme di momento massimo e minimo) e riportato la spiegazione già presente sul perché compare $\sin\theta$ e su quando la spira raggiunge l'equilibrio.
- Revisione: rifatta con le regole aggiornate. Titolo invariato; introduzione di una frase; ripristinato il titoletto «Spira rettangolare in campo uniforme» e aggiunto «Spira inclinata rispetto al campo» per la formula generale. Testo telegrafico riscritto in frasi complete: forze sui lati $d$ e $h$, braccio $d/2$ e somma dei momenti con frasi di collegamento, braccio $\frac{d}{2}\sin\theta$, estensione a spire di forma qualsiasi e a $N$ avvolgimenti, legenda della formula, casi θ = 90° e θ = 0°; esempio con i dati in forma discorsiva; didascalie in frasi complete. Nessuna nuova correzione (M = iAB sin θ con θ dalla normale e 0,3167 → 0,32 N·m riverificati). Figure invariate (spira con ⊗/⊙; vista dall'alto con cursore su θ da 0° a 180°). Nessun esempio tolto, nessuna figura decorativa.
- Revisione 2 (testo schematico): elenchi per le forze sui lati e per i casi θ = 90°/0°, legenda del momento torcente in una riga, esempio ridotto a dati → formula → risultato (0,32 N·m verificato).

## Unità 11 — Legge di Ampère
- Parole: 534 su 3 pagine di traccia (pagine 16–18; l'esempio in cima a pagina 16 appartiene all'unità 09, non contato qui)
- Rettifica: nessuna. Verificato con SymPy che la somma $\sum B\,\Delta l$ su un percorso circolare con $B=ki/r$ dà $2\pi k i$, coerente con il passaggio a mano della traccia (dove la $r$ si semplifica con la circonferenza $2\pi r$).
- Aggiunta: nessuna. Ho ridisegnato in SVG i quattro schemi della traccia (percorsi concatenato/non concatenato, il percorso concatenato in un piano qualunque, il percorso circolare con $B$ tangente, la scomposizione di $\vec B$ in $B_\parallel$, e i due esempi con più fili) e riportato la derivazione e la generalizzazione così come compaiono, fermandomi dove si ferma la traccia (senza scrivere $B=\mu_0 i/2\pi r$, che compare solo a inizio pagina 19, già unità 11).
- Revisione (13/10/2026, regole 13/10): parole 415 → 173. Tolti l'introduzione, il titoletto «Percorsi concatenati e non concatenati» (apre la pagina), le frasi che ripetevano la formula della circuitazione e la legenda delle unità; concatenato/non concatenato e correnti non concatenate/opposte in elenco caso → conseguenza; ipotesi di simmetria e B = k·i/r in elenco; μ₀ = 2πk e la circuitazione circolare in un'unica riga nel .def; titoletti ridotti a «Percorso circolare», «Percorso qualunque», «Esempio 1», «Esempio 2»; didascalie accorciate. Nessuna formula a comparsa da togliere. Controllo concettuale: nessuna correzione (riverificati 2πk·i con k = 2·10⁻⁷ → μ₀ ≈ 4π·10⁻⁷ T·m/A). Figure invariate (cursori su posizione di γ, raggio, angolo; piano inclinato e due esempi statici). Nessun esempio tolto, nessuna figura decorativa.

## Unità 12 — Legge di Biot-Savart e forze fra fili paralleli
- Parole: 416 su 1,4 pagine di traccia (pagina 19 intera più l'inizio di pagina 20, fino a
  prima dell'avvio di "Campo magnetico generato da una spira circolare", che appartiene
  all'unità 12)
- Rettifica: nessuna. Verificato con SymPy: la soluzione di $B\cdot2\pi r=\mu_0 i$ dà
  $B=\mu_0 i/(2\pi r)$; le due espressioni $F=i_1B_2L$ e $F=i_2B_1L$ si semplificano entrambe
  a $\mu_0 i_1i_2L/(2\pi d)$, coerenti con la traccia.
- Aggiunta: nessuna. Ho ridisegnato in SVG i tre schemi della traccia (il percorso circolare
  intorno al filo con $B$ tangente, la coppia di fili con correnti concordi che genera forze
  attrattive, e la coppia con correnti discordi che genera forze repulsive) e riportato la
  derivazione così come compare.
- Revisione (14/10/2026, regole 13/10): parole 324 → 135. Titolo invariato. Introduzione «L'unità ricava…» sostituita da una domanda d'apertura; titoletti accorciati («Campo di un filo rettilineo», «Forza fra due fili paralleli»); simmetria del percorso in due voci d'elenco; legende delle grandezze nei riquadri tolte (resta μ₀ ≈ 4π×10⁻⁷ T·m/A); B₁ e B₂ in un riquadro .eq; le due espressioni della forza compattate in F = i₁B₂L = i₂B₁L; uguaglianza dei moduli, attrazione e repulsione in tre voci caso → conseguenza; didascalie abbreviate. Nessuna comparsa da togliere. Controllo concettuale: nessuna correzione; riverificati con Python B = 2·10⁻⁷·10/0,025 = 8,0·10⁻⁵ T e F = 2·10⁻⁷·5·5/0,04 ≈ 1,3·10⁻⁴ N, versi di B e F nelle due figure dei fili ricontrollati col prodotto vettoriale. Figure invariate (cursore sul raggio, cursore su i₂, correnti discordi statica). Nessun esempio tolto, nessuna figura decorativa.

## Unità 13 — Campo di una spira circolare e di una bobina
- Parole: 227 su 2 pagine di traccia (pagina 20 intera più l'inizio di pagina 21, fino al
  disegno delle tre spire attaccate, prima dell'avvio di "Campo magnetico generato da un
  SOLENOIDE", che appartiene all'unità 13)
- Rettifica: nessuna. Verificato con SymPy che $B_{bobina}=N\cdot i\mu_0/(2R)$ è
  effettivamente $N$ volte $B_{spira}=i\mu_0/(2R)$, coerente con la traccia; verificato anche
  l'esempio numerico aggiunto ($N=200$, $R=4{,}0$ cm, $i=0{,}50$ A dà $B\approx1{,}6\times10^{-3}$ T).
- Aggiunta: un esempio numerico, perché in tutta l'unità la traccia non ne contiene nessuno
  (solo i due schemi di verso della corrente e la formula riquadrata per spira e bobina).
- Revisione (14/10/2026, regole 13/10): parole 292 → 116. Titolo invariato. Introduzione «L'unità tratta…» sostituita da una domanda d'apertura; tolto il titoletto «Il campo al centro di una spira», «Il campo di una bobina con N avvolgimenti» ridotto a «Bobina»; direzione e verso del campo in elenco caso → conseguenza; legende delle formule tolte (resta μ₀ ≈ 4π×10⁻⁷ T·m/A); bobina in una frase; nota sulla validità in mezza riga; esempio ridotto a dati → formula → risultato. Nessuna comparsa da togliere. Controllo concettuale: nessuna correzione; riverificati con Python B = 4π·10⁻⁷·200·0,50/(2·0,040) ≈ 1,6×10⁻³ T, verso di B nelle due spire e nella bobina (corrente uscente in alto → B verso destra) con la regola della mano destra. Figure invariate (due spire statiche; bobina con cursore su N). Nessun esempio tolto, nessuna figura decorativa.

## Unità 14 — Campo magnetico di un solenoide
- Parole: 371 su 1,5 pagine di traccia (la parte finale di pagina 21, dal titolo "Campo
  magnetico generato da un SOLENOIDE" in poi, più pagina 22 intera, fino a prima dell'avvio
  di "Magnetismo nella materia" a inizio pagina 23, che appartiene all'unità 14; la formula
  della bobina a inizio pagina 21 appartiene all'unità 12, già pubblicata).
- Rettifica: nessuna. Verificato con SymPy che risolvendo $B\cdot L=\mu_0 N i$ rispetto a $B$
  si ottiene $B=\mu_0 N i/L=\mu_0 n i$ con $n=N/L$, coerente con il passaggio a mano della
  traccia; verificata anche la coerenza dimensionale ($[\mu_0]=\text{T}\cdot\text{m/A}$) e
  l'esempio numerico aggiunto ($N=500$, $L=25$ cm, $i=2{,}0$ A dà $n=2000\ \text{m}^{-1}$ e
  $B\approx5{,}0\times10^{-3}$ T).
- Aggiunta: un esempio numerico, perché in tutta l'unità la traccia non ne contiene nessuno
  (solo lo schema del solenoide, il disegno del campo nullo fuori/uniforme dentro, e la
  derivazione coi quattro tratti del percorso di Ampère).
- Revisione (14/10/2026, regole 13/10): parole 368 → 131. Pagina già a quaderno: apertura a domanda (con la definizione di solenoide fra parentesi), tolti l'introduzione e i titoletti «Campo interno e campo esterno», «Il percorso di Ampère» (resta «Esempio»), campo interno/esterno in elenco caso → conseguenza, nota sul solenoide ideale in una riga, costruzione del percorso in una frase, contributi dei quattro lati in elenco caso → conseguenza, legenda ridotta a n e μ₀, esempio «Dati… Calcolare…» in un'unica formula. Nessuna comparsa, nessuna correzione (B = 4π×10⁻⁷·2000·2,0 ≈ 5,0×10⁻³ T riverificato). Figure interattive invariate (didascalie accorciate). Nessun esempio tolto, nessuna figura decorativa.

## Unità 15 — Magnetismo nella materia
- Parole: 411 su 3 pagine di traccia (pagine 23–25; la pagina 26, con la temperatura di Curie e
  il geomagnetismo, appartiene all'unità 15 e non è stata trattata qui)
- Rettifica: nessuna. La traccia è qualitativa più una tabella di valori empirici di
  permeabilità relativa; verificato con SymPy/Python solo che l'ordinamento riportato
  (ferromagnetici $\gg$ paramagnetici $>1>$ diamagnetici) è coerente con i valori numerici
  della tabella.
- Aggiunta: nessuna.
- Revisione (15/10/2026, regole 13/10): parole 336 → 178 (tabella compresa). Pagina già a quaderno: apertura a domanda, tolti l'introduzione e i titoletti «Il modello atomico come piccola spira», «Tre risposte a un campo magnetico esterno», «Permeabilità magnetica relativa»; modello dell'atomo e materiale non magnetizzato in una frase ciascuno, tre comportamenti in elenco caso → conseguenza, definizione di μr ridotta alla formula con legenda di B e B₀, valori di μr per le tre famiglie in elenco. Nessuna comparsa; nessuna correzione (ordinamento dei μr della tabella riverificato). Figure invariate (didascalie accorciate); nessun esempio. Da verificare sulla fonte: μr del Ferro-Nichel (90–100), dell'aria (1,000004: i valori comuni sono ≈ 1,0000004) e dell'argento (0,999981; valori comuni ≈ 0,999976).

## Unità 16 — Temperatura di Curie e geomagnetismo
- Parole: 408 su 2 pagine di traccia (pagine 26–27)
- Rettifica: nessuna sul contenuto fisico. Ho chiarito la geometria del disegno degli strati
  terrestri: la traccia disegna due cerchi concentrici con le correnti convettive (a mano libera,
  due archi ondulati orizzontali) racchiuse quasi interamente nel cerchio più interno; ho spostato
  le correnti nell'anello del nucleo esterno (fra nucleo interno e mantello), che è dove realmente
  ha origine il campo magnetico terrestre per effetto dinamo, mantenendo le stesse tre etichette
  della traccia (nucleo interno, nucleo esterno, mantello). Verificato con SymPy che
  $B_T=0{,}5\times10^{-4}$ T corrisponde esattamente a $0{,}5$ G, coerente con l'annotazione della
  traccia ($1$ T $=10^4$ G).
- Aggiunta: nessuna. Ho ridisegnato in SVG i tre schemi della traccia (la sezione della Terra con
  nucleo e mantello, l'arrivo del vento solare sul campo magnetico terrestre, e le linee di campo
  parallele con la traiettoria elicoidale e la forza di Lorentz centripeta) senza introdurre
  contenuto fisico ulteriore rispetto a quanto scritto ed enunciato nella traccia.
- Revisione (15/10/2026, regole 13/10): titolo invariato; parole 350 → 200 (tabella compresa, 15). Pagina già a quaderno: apertura a domanda al posto della frase «L'unità tratta…»; tolto il titoletto «Temperatura di Curie» (restano «Il campo magnetico terrestre» e «Vento solare e aurore polari», argomenti distinti); definizioni di temperatura di Curie e aurora polare ridotte a una riga nel .def; sotto/sopra la temperatura di Curie, vento solare e brillamenti, particelle deviate/guidate, rotazione e avanzamento dell'elica in elenco caso → conseguenza; legenda di B_T ridotta a «Gauss (G): 1 T = 10⁴ G»; tolta la frase che presentava la tabella; didascalie accorciate. Nessuna comparsa. Nessuna correzione (conversioni in K riverificate: T + 273,15). Figure invariate (Terra con linee di dipolo; vento solare con ▶/↺; elica con cursore sul tempo). Nessun esempio, nessuna figura decorativa. Da verificare sulla fonte: temperatura di Curie del nichel (347 °C; valore usuale circa 354–358 °C), lasciata invariata.

## Unità 17 — Moto elicoidale
- Parole: 233 su 1 pagina di traccia (pagina 28)
- Rettifica: nessuna. Verificate con SymPy le tre formule della traccia: $r=mv_\perp/(qB)$,
  $T=2\pi r/v_\perp=2\pi m/(qB)$ (la semplificazione di $v_\perp$ è corretta) e
  $P=v_\parallel\cdot T=2\pi m v_\parallel/(qB)$; tutte confermate identiche a quelle scritte.
- Aggiunta: nessuna. Un solo disegno SVG, che riprende lo schema della traccia (linee di campo,
  traiettoria elicoidale, scomposizione di $v$ in $v_\perp$ e $v_\parallel$, passo $P$).
- Revisione (15/10/2026, regole 13/10): titolo invariato; parole 233 → 121. Pagina già a quaderno: apertura a domanda al posto della frase «Questa unità tratta…»; tolti i titoletti «Raggio e periodo dell'elica» e «Il passo dell'elica» (pagina breve, un solo argomento; bastano le etichette dei .def); scomposizione della velocità e composizione dei moti in elenco caso → conseguenza; origine del raggio, definizione del periodo e del passo in mezza riga; legenda del raggio in una riga (q in valore assoluto mantenuto); nota sulla semplificazione di v⊥ in una riga; didascalia accorciata. Nessuna comparsa. Nessuna correzione concettuale; formule riverificate con SymPy (T = 2πm/(qB), P = 2πmv cosθ/(qB)). Figura invariata (elica calcolata con cursore sull'angolo θ). Nessun esempio, nessuna figura decorativa.

## Unità 18 — Acceleratori di particelle: ciclotrone e sincrotrone
- Parole: 442 su 3 pagine di traccia (pagine 29–31)
- Rettifica: nessuna. Verificate con SymPy: $T=2\pi m/(qB)$ indipendente da $v$; $T/2=\pi m/(qB)$;
  $\Delta U=2nq\Delta V$ dopo $n$ cicli (coerente con $\Delta U=q\Delta V$ per semiciclo, $2n$
  semicicli in $n$ cicli); l'esempio numerico (protone, $v_0=500$ m/s, $\Delta V=800$ V, $n=5$)
  dà $v_f=\sqrt{v_0^2+4nq\Delta V/m}\approx1{,}238\times10^6$ m/s, arrotondato a
  $1{,}24\times10^6$ m/s come nella traccia. Verificata anche la coerenza dimensionale di
  $T=2\pi m/(qB)$ (secondi) e di $R=mv/(qB)$ (metri) per il sincrotrone.
- Aggiunta: nessuna. Due disegni SVG che riprendono gli schemi della traccia (le due D del
  ciclotrone con la spirale e la fessura, l'anello del sincrotrone con il raggio $R$ fisso e i
  due punti di accelerazione).
- Revisione (16/10/2026, regole 13/10): parole 421 → 186. Pagina già a quaderno: apertura a domanda con i ruoli di E e B in elenco, tolto il titoletto «Periodo ed energia guadagnata» (restano «Il ciclotrone», «Esempio», «Il sincrotrone»), struttura delle D in una frase, campo nullo nelle D, ΔV = E·d, inversione di E e spirale in elenco caso → conseguenza, legenda del periodo in mezza riga, T indipendente da v e T/2 dentro il .def, esempio in forma «Dati… Calcolare…» con due passaggi (tolto il commento finale su v₀), limite del ciclotrone e principio del sincrotrone in due voci d'elenco. Nessuna comparsa; nessuna correzione (v_f ≈ 1,238×10⁶ m/s → 1,24×10⁶ m/s riverificato con Python). Figure con cursore invariate (didascalie accorciate). Nessun esempio tolto, nessuna figura decorativa.

## Unità 19 — L'esperienza di Faraday e la forza elettromotrice indotta
- Parole: 406 su 2 pagine di traccia (pagine 32–33)
- Rettifica: nessuna. La traccia è interamente qualitativa (nessuna formula né calcolo numerico
  su queste due pagine): niente da verificare con SymPy. Ho controllato solo la coerenza della
  notazione, usando $\Delta V$ per la fem indotta come già fatto per la differenza di potenziale
  nell'unità 17.
- Aggiunta: nessuna. Due disegni SVG che riprendono gli schemi della traccia (i due circuiti
  avvolti sullo stesso anello di ferro con batteria, interruttore e amperometro; il magnete in
  avvicinamento a una bobina collegata a un amperometro), senza introdurre contenuto fisico
  ulteriore.
- Revisione (16/10/2026, regole 13/10): parole 329 → 163. Titolo invariato. Apertura a domanda al posto della frase introduttiva; tolti i titoletti «L'esperienza di Faraday» e «Che cosa cambia nei tre casi» (resta «Magnete in movimento», caso distinto); descrizione dei due circuiti e tre osservazioni in elenco caso → conseguenza (elenco numerato → puntato); confronto fra i tre casi in una frase; .def «Forza elettromotrice indotta» accorciato («direttamente proporzionale» mantenuto); nota in una riga; esperienza del magnete in elenco con la conclusione in una frase. Nessuna comparsa da togliere, nessuna correzione concettuale (contenuto qualitativo). Figure con cursore e ▶ invariate (didascalie accorciate). Nessun esempio tolto, nessuna figura decorativa.

## Unità 20 — Flusso del campo magnetico
- Parole: 254 su 1 pagina di traccia (pagina 34)
- Rettifica: nessuna. L'unica formula della traccia, $\Phi(\vec{B})=BA\cos\theta$, e i due casi
  particolari ($\theta=0\Rightarrow\Phi=BA$; $\theta=90°\Rightarrow\Phi=0$) sono stati verificati
  con SymPy (cos(0)=1, cos(pi/2)=0): coincidono con quanto scritto. Nessun calcolo numerico da
  controllare, la traccia non ne contiene.
- Aggiunta: nessun esempio nuovo (la traccia non ne contiene, e nessuno è stato inserito). Un solo
  strumento interattivo: uno slider sull'angolo theta che ruota la superficie vista di taglio e il
  vettore A rispetto a B, mostrando in tempo reale cos(theta) e il flusso corrispondente (con
  B=1 T e A=1 m² per semplicità di lettura). Mostra concretamente il passaggio continuo fra i due
  casi limite già presenti nella traccia, senza aggiungere contenuto fisico oltre alla formula
  della traccia stessa.
- Revisione (16/10/2026, regole 13/10): parole 213 → 100. Titolo invariato. Pagina già a quaderno: apertura a domanda al posto della frase introduttiva; tolto il titoletto «Vettore area e flusso» (resta «I due casi estremi»); vettore area in una riga; .def ridotto a formula e legenda dell'angolo; weber in un .def «Unità di misura» in una riga; nota in una frase; i due casi in elenco caso → conseguenza; conclusione in mezza riga. Ipotesi mantenute (superficie piana, campo uniforme). Nessuna comparsa da togliere, nessuna correzione concettuale (cos 0 = 1, cos 90° = 0). Figura con cursore invariata (didascalia accorciata). Nessun esempio, nessuna figura decorativa.

## Unità 21 — Legge di Faraday-Neumann-Lenz
- Parole: 397 su 2 pagine di traccia (pagine 35-36)
- Rettifica: nessuna. L'unico calcolo numerico della traccia,
  $\varepsilon = |0{,}110\,\text{Wb} - 0{,}850\,\text{Wb}| / 0{,}5\,\text{s}$, è stato verificato
  con SymPy: dà 1,48 V, come scritto sul quaderno. Le tre formule boxate (fem con N=1, con segno
  meno esplicito, e con N avvolgimenti) sono dimensionalmente coerenti: Wb/s = V.
- Aggiunta: un riquadro "da non confondere" sul significato del segno meno (convenzione di verso,
  non fem negativa), indispensabile perché la traccia introduce il segno meno nella legge ma non
  lo commenta subito, lasciandolo solo alla legge di Lenz qualche riga dopo. I due disegni SVG
  ridisegnano entrambe le coppie magnete-bobina della traccia (avvicinamento e allontanamento),
  senza introdurre schemi nuovi.
- Revisione (16/10/2026, regole 13/10): parole 343 → 155. Pagina già a quaderno: apertura a domanda, tolti la frase «Questa unità enuncia…» e i titoletti «La legge dell'induzione» e «Intensità della fem indotta» (restano «Esempio» e «Legge di Lenz e segno meno»), legenda di Φ_I e Φ_F in mezza riga nel .def, raccordi delle formule dell'intensità e delle N spire in una frase, volt in .def «Unità di misura» (1 V = 1 Wb/s), esempio in forma «Dati… Calcolare…» con un solo passaggio, tre casi della legge di Lenz in elenco caso → conseguenza, nota in una frase. Nessuna comparsa, nessuna correzione (0,740 Wb / 0,5 s = 1,48 V riverificato). Figura con cursore invariata (didascalia accorciata). Nessun esempio tolto, nessuna figura decorativa.

## Unità 22 — La barretta in moto: analisi della fem indotta
- Parole: 362 su 3 pagine di traccia (pagine 37-39)
- Rettifica: nessuna. Tutte le formule sono state verificate con SymPy: $\varepsilon=Bv\ell$,
  $i_{ind}=Bv\ell/R$, $F_M=iB\ell=B^2v\ell^2/R$, $P_{elettrica}=i^2R=B^2v^2\ell^2/R$,
  $P_{meccanica}=F_{est}v=B^2v^2\ell^2/R$, e l'uguaglianza $P_{elettrica}=P_{meccanica}$ è
  confermata algebricamente. Coerenza dimensionale controllata (T·m/s·m = V; A·T·m = N; A²·Ω = W).
- Aggiunta: un solo strumento interattivo, uno slider sulla velocità $v$ (con $B$, $\ell$, $R$
  fissati a valori tipici) che aggiorna in tempo reale i valori numerici di $\varepsilon$, $i$,
  $F_M$ e $P$ già derivati nella pagina, per mostrare concretamente la dipendenza lineare della
  fem e quadratica della potenza da $v$. Nessun esempio numerico nuovo oltre a questo; nessuna
  dimostrazione aggiuntiva.
- Revisione (17/10/2026, regole 13/10): parole 323 → 160. Pagina già a quaderno: apertura a domanda al posto della frase «Questa unità applica…», tolti i titoletti «Fem indotta dal moto della barretta» e «Corrente indotta» (restano «Forza magnetica frenante» e «Bilancio di potenza»), legenda della fem in mezza riga (B in T, v in m/s, ℓ in m → ε in V), verso della corrente per la legge di Lenz in una frase, forza frenante e forza esterna in elenco caso → conseguenza (R resistenza totale e attrito trascurabile mantenuti), raccordi delle potenze in mezza riga. Nessuna comparsa, nessuna correzione (0,20 V, 0,10 A, 0,010 N, 0,020 W per v = 2,0 m/s riverificati); figure con cursore invariate (didascalie accorciate). Nessun esempio tolto, nessuna figura decorativa.

## Unità 23 — Campo elettrico indotto e generatori di corrente
- Parole: circa 196 di prosa (sommario, didascalie, paragrafi) su 1 pagina di traccia (pagina 40)
- Rettifica: nessuna. La formula $E = Bv$ è stata verificata con SymPy a partire da
  $E\ell = \Delta V = Bv\ell$ (uguaglianza fra ddp lungo la barretta e fem, già ricavata
  nell'unità 21). Coerenza dimensionale controllata: T·(m/s) = V/m, corretto per un campo
  elettrico. La frase finale di pagina ("...cambia e si genera corrente") è stata inclusa come
  chiusura del paragrafo sui generatori, mentre la derivazione quantitativa di $\varepsilon =
  NBA\omega\sin\omega t$ resta nell'unità 23 come da traccia (pagina 41).
- Aggiunta: nessuna. Due soli disegni SVG che ridisegnano gli schemi della traccia (il campo
  elettrico interno alla barretta e il generatore a spira rotante fra due poli); nessun esempio
  numerico né strumento interattivo, assenti anche nella traccia su questa pagina.
- Revisione (17/10/2026, regole 13/10): parole 220 → 127. Pagina già a quaderno: tolta la frase «Questa unità mostra…», apertura a domanda con l'ipotesi B perpendicolare a barretta e velocità (mantenuta); titoletti «Il campo elettrico all'interno della barretta» e «Generatori di corrente» tenuti (argomenti distinti); raccordi delle due espressioni di ΔV in mezza riga; legenda di E = Bv ridotta a una riga con 1 T·m/s = 1 V/m; principio dei generatori in elenco caso → conseguenza (rotazione → area esposta variabile → flusso variabile → fem e corrente indotta). Nessuna comparsa, nessuna correzione (E = 1,00 V/m e ΔV = 0,20 V con B = 0,50 T, ℓ = 0,20 m, v = 2,0 m/s riverificati); figure con cursore invariate (didascalie accorciate). Nessun esempio, nessuna figura decorativa.

## Unità 24 — L'alternatore
- Parole: circa 329 (prosa, didascalie ed etichette comprese) su 2 pagine di traccia (pagine 41-42)
- Rettifica: nessuna. La formula $\varepsilon = NBA\omega\sin(\omega t)$ è verificata con SymPy
  a partire da $\Phi = NBA\cos(\omega t)$ e $\varepsilon = -d\Phi/dt$, con risultato
  $NBA\omega\sin(\omega t)$ coerente con la traccia. Il valore massimo $\varepsilon_{max} =
  NBA\omega$ (per $\sin\omega t = 1$) è riportato come nella traccia. Nessuna incongruenza
  dimensionale: $[B][A][\omega] = T\cdot m^2\cdot s^{-1} = V$.
- Aggiunta: un riquadro "da non confondere" fra $N$ come numero di spire e $N$ come polo nord,
  indispensabile perché la traccia usa la stessa lettera per entrambi nella stessa doppia
  pagina senza segnalarlo. Un solo strumento interattivo, uno slider sulla fase $\omega t$ che
  muove un punto sulla curva della fem e ruota in sincrono lo schema della spira fra i poli:
  mostra concretamente perché la fem è sinusoidale, senza introdurre nessun esempio numerico
  assente dalla traccia.
- Revisione (17/10/2026, regole 13/10): parole 278 → 147. Pagina già a quaderno: apertura a domanda al posto della frase «Questa unità ricava…» (ipotesi di asse perpendicolare al campo e ω costante mantenute), tolto il titoletto «La fem indotta in una spira rotante» (resta «Andamento sinusoidale e valore massimo»), rotazione → flusso variabile → fem e corrente in elenco caso → conseguenza, condizione iniziale (spira perpendicolare al campo per t = 0) in mezza riga, legenda delle unità e caso di N spire in serie in una riga, nota «Da non confondere» in una frase, caratteristiche dell'alternatore in elenco, fem massima in mezza riga; tolta la frase che descriveva il simbolo circuitale (lo mostra la figura). Nessuna comparsa, nessuna correzione (ε = −dΦ/dt con Φ = NBA cos ωt → NBAω sin ωt riverificato con SymPy). Figure invariate (cursore sulla fase, simbolo circuitale; didascalie accorciate). Nessun esempio, nessuna figura decorativa.

## Unità 25 — Motori elettrici in corrente alternata
- Parole: circa 266 (prosa, didascalie ed etichette comprese) su 1 pagina di traccia (pagine 42-43)
- Rettifica: nessuna. La pagina non introduce formule nuove (nessun calcolo numerico da
  verificare con SymPy): si limita a riprendere la forza $F = iLB$ già stabilita nell'unità 8
  per il filo rettilineo, applicandola concettualmente ai due lati della spira senza rideriva­rla.
  Coerente con la traccia, che su queste pagine è solo qualitativa (due schemi e un breve testo).
- Aggiunta: nessuna. Ridisegnati in SVG lo schema spira-fra-i-poli collegata tramite
  commutatore a un generatore di corrente alternata (pagina 42) e i tre istanti della rotazione
  con corrente e forza (pagina 43, incluso il terzo con l'inversione di corrente). Nessuno
  strumento interattivo: i tre pannelli statici bastano a mostrare la sequenza già disegnata
  nella traccia, e un cursore avrebbe richiesto assunzioni sulla geometria non esplicitate lì.
- Revisione (18/10/2026, regole 13/10): parole 225 → 111. Titolo invariato. Tolti introduzione «Questa unità mostra…» e i titoletti «Il generatore alla rovescia» e «Perché la spira continua a ruotare»; apertura a domanda; conversione di energia in .def di una riga; coppia di forze e ruolo del commutatore in due elenchi caso → conseguenza (condizione «piano della spira perpendicolare al campo» mantenuta); didascalie accorciate. Nessuna comparsa da togliere. Nessuna correzione concettuale (verificato: con B da N a S e corrente uscente sul lato destro, F = iL×B verso l'alto, come nel disegno). Figure invariate (schema statico; spira con cursore sull'angolo). Nessun esempio, nessuna figura decorativa.

## Unità 26 — Mutua induzione e autoinduzione
- Parole: circa 460 (prosa, didascalie ed etichette comprese) su 2 pagine di traccia (pagine
  43-44; la pagina 43 è condivisa con l'unità 24, di cui restano solo le ultime righe sulla
  rotazione del motore, e con l'unità 25 da qui in poi ("Induttanza" / "Mutua induzione")).
- Rettifica: nessuna. La pagina non contiene formule numeriche da verificare: è interamente
  qualitativa (nessun calcolo, nessuna definizione quantitativa, che arriva solo nell'unità 26
  con l'induttanza $L$). L'unico controllo possibile riguarda la coerenza fisica del grafico
  $i(t)$ disegnato nella traccia dopo la chiusura dell'interruttore: risolvendo con SymPy
  l'equazione $L\,di/dt + Ri = \varepsilon$ con $i(0)=0$ si ottiene $i(t)=(\varepsilon/R)
  (1-e^{-Rt/L})$, funzione crescente ($i'>0$) e concava verso il basso ($i''<0$), che tende
  asintoticamente a $\varepsilon/R$: coerente con la curva disegnata a mano, anche se
  quest'ultima non compare come formula esplicita nella traccia.
- Aggiunta: un solo riquadro "da non confondere" fra mutua induzione (fem indotta in un
  circuito diverso da quello che genera il campo) e autoinduzione (fem indotta nello stesso
  circuito), indispensabile perché la traccia introduce i due fenomeni uno di seguito
  all'altro, con lo stesso disegno di bobina, senza mai contrapporli esplicitamente. Ridisegnati
  in SVG lo schema delle due bobine accoppiate (pagina 43), il solenoide con le spire vicine
  (pagina 44) e i due circuiti con interruttore aperto/chiuso più il grafico $i(t)$ (pagina 44):
  nessuno schema nuovo rispetto a quelli della traccia. Nessuno strumento interattivo: i tre
  pannelli statici bastano a mostrare la sequenza già disegnata a mano.
- Revisione (18/10/2026, regole 13/10): parole 309 → 162. Pagina già a quaderno: apertura a domanda al posto della frase «Questa unità descrive…»; titoletti «Mutua induzione», «Autoinduzione» e «Chiusura di un circuito con una bobina» tenuti (tre casi distinti); mutua induzione, autoinduzione e chiusura del circuito in elenchi caso → conseguenza (bobina 2 «elettricamente separata» mantenuta), nota «Da non confondere» in una frase, didascalie accorciate. Nessuna comparsa da togliere. Nessuna correzione concettuale (i(t) = (ε/R)(1 − e^(−Rt/L)) crescente e concava già verificata con SymPy). Figure invariate (due con ▶/↺, una statica). Nessun esempio, nessuna figura decorativa.

## Unità 27 — Induttanza
- Parole: circa 256 (prosa, didascalie e riquadro compresi) su 1 pagina di traccia (pagina 45,
  interamente dedicata a questa unità: dal circuito con generatore-resistenza-bobina fino alla
  frase di chiusura sull'induttanza come caratteristica della bobina).
- Rettifica: nessuna. Verificato con SymPy che $1\,\text{H} = 1\,\text{V}\cdot\text{s}/\text{A}$
  (coerente con la definizione $L = N|\Delta\Phi(\vec B)/\Delta i|$, dimensionalmente
  $\text{Wb}/\text{A} = \text{V}\cdot\text{s}/\text{A}$, come scritto nella traccia).
- Aggiunta: nessuna. L'esempio numerico che compare in cima alla pagina 46 (calcolo di
  $\Delta t$ da $L$, $\Delta i$ ed $\varepsilon_{ind}$) non è stato incluso: la traccia lo
  colloca dopo l'intestazione "Induttanza di un solenoide" nell'indicizzazione delle pagine
  (unità 27, pagine 46-47), quindi resta di competenza di quell'unità pur non usando la formula
  del solenoide.
- Revisione (18/10/2026, regole 13/10): parole 249 → 92. Pagina già a quaderno: apertura a domanda al posto della frase «Questa unità definisce…»; tolti i titoletti «La costante di proporzionalità» e «Unità di misura» (argomento unico); proporzionalità fra flusso e corrente in elenco caso → conseguenza; ε_ind = L|Δi/Δt| in riquadro rosso da sola; tolto il passaggio intermedio con Δt·(Δt/Δi) (resta la frase «Δt si semplifica»); definizione dell'induttanza ridotta a formula + «caratteristica della bobina: forma, dimensioni, numero di spire»; henry in .def di una riga; tolta la frase «1 H: fem di 1 V quando la corrente varia di 1 A ogni secondo»; didascalia accorciata; aggiunta la regola CSS .foglio>ul+p per la riga vuota dopo l'elenco. Nessuna comparsa da togliere. Nessuna correzione concettuale (1 H = 1 Wb/A = 1 V·s/A già verificato). Figura invariata (circuito con cursore su Δi/Δt, L = 0,20 H). Nessun esempio, nessuna figura decorativa. Da controllare: la proporzionalità flusso–corrente è scritta senza la condizione «in assenza di materiali ferromagnetici» (come nella versione precedente).

## Unità 28 — Induttanza di un solenoide
- Parole: circa 363 (prosa, didascalie e riquadro compresi, formule incluse nel conteggio) su
  2 pagine di traccia (pagine 46-47: dall'esempio numerico di richiamo sull'induttanza generica,
  fino al secondo esempio con i tre calcoli L, A, B_max).
- Rettifica: nessuna. Verificato con SymPy ogni passaggio numerico: Δt = L·Δi/ε_ind ≈
  2,2×10⁻³ s (dati L=2,9×10⁻³ H, Δi=5,6 A, ε_ind=7,3 V); nel secondo esempio L = ε·Δt/Δi ≈
  1,7×10⁻³ H, A = Lℓ/(μ₀N²) ≈ 4,3×10⁻⁴ m², B_max = μ₀(N/ℓ)i_f ≈ 2,0×10⁻² T. Verificata anche
  l'equivalenza algebrica L = μ₀N²A/ℓ = μ₀n²V con n=N/ℓ e V=ℓA. Tutti i valori della traccia
  sono confermati entro l'arrotondamento.
- Aggiunta: un solo riquadro "da non confondere" fra n² (densità di spire al quadrato) e N²
  (numero di spire al quadrato), indispensabile perché la traccia stessa annota a mano questa
  distinzione nel passaggio da L = μ₀(N²/ℓ)A a L = μ₀n²ℓA, segno che è un punto in cui si
  sbaglia facilmente. Ridisegnato in SVG lo schema del solenoide con spire, asse, campo B e
  sezione A (pagina 46): nessun disegno nuovo rispetto alla traccia. Nessuno strumento
  interattivo: la pagina è quasi interamente formule ed esempi numerici già risolti a mano.
- Revisione (19/10/2026, regole 13/10): parole 302 → 132. Pagina già a quaderno: apertura a domanda; tolti i titoletti «Induttanza di un solenoide» e «Densità di spire e volume» (restano «Esempio 1» ed «Esempio 2», spostati in fondo); ipotesi del solenoide lungo (campo approssimativamente uniforme e parallelo all'asse) e flusso in elenco; L = μ₀N²A/ℓ e L = μ₀n²V in .def, legenda ridotta a μ₀; nota n²/N² in una frase; esempi con dati in una riga e calcoli in riquadri (tolte le frasi a), b), c)). Nessuna comparsa, nessuna correzione (Δt ≈ 2,2×10⁻³ s; L ≈ 1,7×10⁻³ H; A ≈ 4,3×10⁻⁴ m²; B_max ≈ 2,0×10⁻² T riverificati). Figura con cursore invariata (didascalia accorciata). Nessun esempio tolto, nessuna figura decorativa.

## Unità 29 — Circuiti RL
- Parole: circa 418 (prosa, didascalie e riquadro compresi) su 3 pagine di traccia (pagine
  48-50: dal titolo "Circuiti RL" fino all'esempio numerico con i tre subcalcoli).
- Rettifica: nella traccia (pagina 50) il secondo passaggio dell'esempio numerico è etichettato
  "L = ε/R(1-e^{-t/τ}) = ... = 0,34 A", ma la formula usata è quella della corrente di carica
  i(t), non quella dell'induttanza L (già calcolata al passaggio precedente come L = τR ≈
  0,26 H): un refuso di etichetta, non di calcolo. Verificato con SymPy: τR = 7,5×10⁻³ s ·
  35 Ω = 0,2625 H ≈ 0,26 H; i(0,03 s) = (12,2/35)(1-e^(-0,03/0,0075)) ≈ 0,342 A ≈ 0,34 A,
  entrambi coerenti con i valori scritti a mano. Nella pagina pubblicata il secondo passaggio è
  etichettato correttamente "i =". Corretta anche l'approssimazione al tempo t=τ: la traccia
  scrive "≈0,6 ε/R ~ 60%", ma 1-1/e = 0,6321: nella pagina è scritto 63%, coerente con le due
  percentuali successive (86% e 95%) già esatte nella traccia.
- Aggiunta: un solo riquadro "Attenzione" sul fatto che ε/R è un asintoto mai raggiunto in un
  tempo finito, indispensabile perché la traccia stessa lo enuncia esplicitamente con il limite
  per t→∞ → 100%, ed è un punto che si presta a fraintendimento se letto come "dopo un tempo
  finito la corrente arriva esattamente al valore di regime". Ridisegnati in SVG il circuito RL
  con interruttore aperto e le due curve i(t) di carica e scarica (pagine 48 e 50): nessun
  disegno nuovo. Un solo strumento interattivo, come da regola: uno slider su τ che ridisegna la
  curva di carica e sposta i marcatori a τ, 2τ, 3τ, per mostrare come la costante di tempo fissi
  la rapidità di salita — la stessa informazione già presente nella traccia (i tre valori
  percentuali), resa manipolabile invece che statica.
- Revisione (19/10/2026, regole 13/10): parole 327 → 150. Apertura a domanda; «Fase di carica», «Fase di scarica» ed «Esempio» tenuti; legenda dei simboli e paragrafo sul regime ridotti a un elenco di due voci (τ in secondi e rapidità della crescita; a regime fem autoindotta nulla, i = ε/R); percentuali 63%, 86%, 95% in una frase prima del riquadro i(τ); nota «Attenzione» in una frase; esempio in forma «Dati… Calcolare…» con le due .eq (L e i), tolte le righe a) e b); didascalie accorciate. Nessuna comparsa da togliere. Controllo concettuale: L = 0,2625 H ≈ 0,26 H, i(4τ) ≈ 0,342 A, 1−1/e = 0,632, 1−e⁻² = 0,865, 1−e⁻³ = 0,950, e⁻¹ = 0,368 verificati; nessuna correzione. Figure invariate (circuito, carica con cursore su τ, scarica con cursore su t). Nessun esempio tolto, nessuna figura decorativa.

## Unità 30 — Energia immagazzinata in un campo magnetico
- Parole: circa 447 (prosa, didascalie e riquadro compresi) su 3 pagine di traccia (pagine 51-53).
- Rettifica: nessuna. Verificato con SymPy sia il passaggio simbolico U = P_m·T = (1/2·Li²/T)·T =
  1/2 Li² sia la sostituzione B² = μ₀²n²i² → μ₀n²i² = B²/μ₀ che porta a U = B²Aℓ/(2μ₀) e
  u_B = B²/(2μ₀). Verificato numericamente l'esempio: da U = 3,11×10⁻³ J e L = 75,0×10⁻³ H,
  i = √(2U/L) ≈ 0,288 A (coerente con 0,288 A scritto a mano); R_tot = ε/i = 36/0,288 ≈ 125,0 Ω,
  R = R_tot − 92,5 Ω ≈ 32,5 Ω, coerente con la traccia.
- Aggiunta: un solo riquadro "Attenzione" sulla crescita quadratica (non lineare) dell'energia
  con la corrente, indispensabile perché è il punto su cui la traccia stessa fa perno passando
  da U=½Li² al caso del solenoide, e un errore comune è pensare a una proporzionalità diretta.
  Ridisegnati in SVG il circuito ideale batteria-induttanza, il grafico i(t) lineare, lo schizzo
  del solenoide per il volume e il circuito dell'esempio (pagine 51-53): nessun disegno nuovo.
  Un solo strumento interattivo, come da regola: uno slider sulla corrente i che sposta un punto
  lungo la curva U(i) = ½Li² e mostra il valore numerico, per rendere visibile la stessa
  dipendenza quadratica già presente nella formula, invece di lasciarla solo scritta.
- Revisione (19/10/2026, regole 13/10): parole 337 → 114. Apertura a domanda; tolti sommario e «Nella prossima unità» (con il rimando all'unità 31) e il rimando all'unità 28; titoletti ridotti a «Energia di un'induttanza», «Solenoide», «Esempio»; derivazione condensata in una .eq (ε = Li/T, P_m = ½Li²/T) e U = ½Li² in .eq principio; caso del solenoide in una .eq, u_B = B²/(2μ₀) in .eq principio con unità J/m³ in .def; nota «Attenzione» in una frase senza simbolo di proporzionalità; esempio in forma «Dati… Calcolare…» con due .eq, tolte le righe a) e b). Nessuna comparsa da togliere. Controllo concettuale: i = √(2U/L) = 0,2880 A, R = 36/0,288 − 92,5 ≈ 32,5 Ω verificati; risultato riportato come ≈ 32 Ω per le due cifre significative di ε = 36 V (prima 32,5 Ω). Impaginazione a quaderno; figure rifatte da script (circuito ideale ε–L, i(t) lineare con i/2 a T/2, U(i) con cursore su i, solenoide con sezione A e lunghezza ℓ, circuito dell'esempio): nessuna figura nuova. Nessun esempio tolto, nessuna figura decorativa.

## Unità 31 — Trasformatori
- Parole: circa 300 (prosa, didascalie e riquadro compresi) su 2 pagine di traccia (pagine 54-55).
- Rettifica: nessuna. Verificato con SymPy il passaggio ε_p/N_p = ε_s/N_s ⇒ ε_p/ε_s = N_p/N_s e
  l'esempio numerico ε_s = ε_p·(N_s/N_p) = 220 V·(20/100) = 44 V (coerente con 44 V scritto a
  mano); verificato i_p/i_s = ε_s/ε_p = N_s/N_p e l'esempio i_s = i_p·(N_p/N_s) = 16 A·(100/20)
  = 80 A (coerente con 80 A scritto a mano).
- Aggiunta: un solo riquadro "Attenzione" sul fatto che il rapporto fra le correnti è l'inverso
  di quello fra le tensioni, indispensabile perché è l'errore tipico (applicare lo stesso
  rapporto N_p/N_s anche alle correnti) e la traccia stessa lo evidenzia dedicando un secondo
  esempio speculare al primo proprio per mostrare l'inversione. Ridisegnato in SVG lo schema del
  trasformatore (nucleo, avvolgimenti primario e secondario, generatore, resistenza, freccia del
  campo magnetico variabile): nessun disegno nuovo, nessuno strumento interattivo (non richiesto
  dalla traccia).
- Revisione (20/10/2026, regole 13/10): parole 272 → 126. Pagina mai revisionata: tolti sommario e «Nella prossima unità» (con il rimando all'unità 32); apertura a domanda; titoletto «Due circuiti accoppiati dallo stesso flusso» tolto (ripeteva l'apertura), «Correnti e potenza» tenuto, esempi rinominati «Esempio 1» ed «Esempio 2» in forma «Dati… Calcolare…»; descrizione dei due circuiti in elenco di tre voci; derivazione in una .eq; rapporto di trasformazione e rapporto fra le correnti in .def; casi N_s > N_p / N_s < N_p in elenco; nota «Attenzione» in una frase. Nessuna comparsa da togliere. Controllo concettuale: 220 V·20/100 = 44 V, 16 A·100/20 = 80 A, potenze uguali (3520 W) verificati; precisato che P_p = P_s vale per il trasformatore ideale, senza perdite (prima «l'energia si deve conservare»). Impaginazione a quaderno; figura rifatta da script con cursore su N_s (20–200): spire disegnate in proporzione, ε_s e i_s a fianco; corretto il flusso, prima disegnato come freccia nella finestra del nucleo, ora lungo il nucleo. Nessun esempio tolto, nessuna figura decorativa.

## Unità 32 — Le prime tre equazioni di Maxwell
- Parole: circa 542 (prosa, didascalie e riquadri compresi) su 3 pagine di traccia (pagine 56-58).
- Rettifica: nella derivazione finale della legge di Faraday come circuitazione (pagina 59, che
  chiude il ragionamento aperto a pagina 57), il segno meno presente nella definizione della fem
  indotta (ε = -ΔΦ(B)/Δt, pagina 57, coerente con l'unità 20) va perso nei passaggi successivi e
  il riquadro finale riporta Γ(E) = dΦ(B)/dt senza segno meno. Corretto in pagina come
  Γ(E) = -dΦ(B)/dt, coerente con la definizione di fem indotta usata poche righe sopra nella
  stessa traccia e con la legge di Faraday-Neumann-Lenz già stabilita nell'unità 20. Verificato
  con SymPy che la definizione di derivata rispetto al tempo, su un esempio concreto
  Φ(t) = B₀A cos(ωt), dà -dΦ/dt = AB₀ω sin(ωt), coerente con il segno mantenuto.
- Aggiunta: un solo riquadro "Da non confondere" sulla differenza fra circuitazione nulla del
  campo elettrostatico e circuitazione non nulla del campo indotto, indispensabile perché è
  esattamente il punto che il passaggio finale della traccia stabilisce (Γ(E) ≠ 0) e che uno
  studente confonde facilmente con quanto visto sui campi conservativi. Ridisegnati in SVG i tre
  schemi della traccia (superficie chiusa con carica interna ed esterna per il teorema di Gauss
  elettrico, superficie chiusa che racchiude linee di campo di un magnete per il teorema di Gauss
  magnetico, percorso chiuso γ con campo elettrico indotto e spostamento della carica per la
  circuitazione): nessun disegno nuovo, nessuno strumento interattivo (non richiesto dalla
  traccia, che qui è puramente concettuale).
- Revisione (20/10/2026, regole 13/10): parole 368 → 112. Pagina mai revisionata: tolti sommario e «Nella prossima unità» (rimando all'unità 33); apertura a domanda; tre titoletti tenuti (tre leggi distinte); le tre leggi in .def «I/II/III equazione di Maxwell»; spiegazioni in prosa ridotte a frasi di raccordo e a un elenco caso → conseguenza; nota «Da non confondere» ridotta a una frase («Attenzione»). Nessuna comparsa da togliere, nessun esempio nella pagina. Controllo concettuale: «non esistono cariche magnetiche isolate» → «monopoli magnetici mai osservati»; segno meno della III equazione confermato; verso del campo indotto verificato con SymPy (B entrante in aumento: E_θ = kr/2 > 0, antiorario). Impaginazione a quaderno; figure rifatte da script: Gauss per E in due pannelli (carica interna / esterna, linee radiali con frecce calcolate nei punti d'ingresso e d'uscita dalla superficie); Gauss per B con linee di campo di un magnete a barra integrate numericamente (modello a due poli), chiuse attraverso il magnete, superficie tratteggiata attorno al polo N (prima le linee terminavano dentro la superficie); circuitazione con B entrante e E indotto tangente a γ in verso antiorario (prima frecce di E verticali che attraversavano il percorso). Nessuna figura decorativa.

## Unità 33 — Corrente di spostamento e legge di Ampère-Maxwell
- Parole: circa 499 (prosa, didascalie e riquadri compresi) su 3 pagine di traccia (pagine 59-61).
- Rettifica: nessuna. Verificato con SymPy il passaggio Q = C·ΔV = (ε₀A/d)·(Ed) = ε₀AE = ε₀Φ(E)
  di pagina 60: la semplificazione del fattore d è corretta e il risultato coincide con quanto
  scritto in traccia.
- Aggiunta: nessuna, a parte la frase di chiusura "il conto torna, e il paradosso si scioglie" per
  ricollegare esplicitamente il termine correttivo al paradosso posto a pagina 59 (S₁ e S₂ danno
  ora lo stesso risultato), passaggio lasciato implicito nella traccia. Ridisegnato in SVG lo
  schema del condensatore in carica con le due superfici S₁ e S₂ che si appoggiano sullo stesso
  contorno γ, come da disegno di pagina 59; nessuno strumento interattivo (figura puramente
  concettuale, non richiesta la manipolazione di un parametro).
- Revisione (20/10/2026, regole 13/10): parole 344 → 168 (simboli inline compresi). Pagina mai revisionata: impaginazione a quaderno (stile e script dell'unità 32), tolti sommario e «Nella prossima unità» (rimando all'unità 34), apertura a domanda; legge di Ampère in .def con la corrente concatenata in mezza riga; paradosso in elenco caso → conseguenza (S₁, S₂); derivazione Q = ε₀Φ(E) in una .eq; corrente di spostamento in .def; legge di Ampère-Maxwell in .def rosso (IV equazione); verifica su S₁ e S₂ in elenco; riepilogo delle quattro equazioni in un .def a due righe (tolti i nomi, già nell'unità 32). Titoletti tenuti: paradosso, corrente di spostamento, quattro equazioni. Nessuna comparsa, nessun esempio. Controllo concettuale (SymPy: Q = CΔV = ε₀EA, i = ε₀ dΦ(E)/dt): precisato condensatore piano nel vuoto con E uniforme; corrente di spostamento indicata come i_s (= i nel filo) invece di riusare il simbolo i; su S₁ flusso di E trascurabile esplicitato. Figura rifatta da script: superficie S₂ calcolata che scavalca l'armatura positiva e chiude fra le armature, S₁ piana bordata da γ, campo E dalla + alla −; aggiunto il filo in uscita dall'armatura negativa (prima il circuito si interrompeva). Nessuna figura decorativa.


## Unità 34 — Come si genera un'onda elettromagnetica
- Parole: circa 287 (prosa, didascalie e riquadri compresi) su 1 pagina di traccia (pagina 62).
- Rettifica: nessuna. Verificate le direzioni di campo con la regola della mano destra: corrente
  verso l'alto nell'antenna, punto di osservazione a lato del filo, campo magnetico entrante nel
  foglio (coerente con B ∝ (î_corrente × r̂) = −ẑ per r̂ nella direzione +x); campo elettrico del
  dipolo, nel piano equatoriale, opposto al momento di dipolo e quindi diretto dalla carica
  positiva verso quella negativa. Entrambe coincidono con quanto disegnato in traccia, nessuna
  correzione necessaria. La pagina non contiene formule o calcoli numerici da verificare con
  SymPy: è un'unità puramente qualitativa.
- Aggiunta: nessuna. Ridisegnati in SVG lo schema dell'antenna con generatore, cariche accumulate
  e campi $\vec E$, $\vec B$ nel punto a lato (i quattro istantanei della traccia sono resi con un
  unico cursore di fase, invece di quattro pannelli statici separati, poiché mostrano la stessa
  alternazione fisica continua descritta dalla traccia) e lo schema dell'onda che si propaga con
  $\vec E$ e $\vec B$ su piani perpendicolari.
- Revisione (20/10/2026, regole 13/10): parole 235 → 142 (simboli inline compresi). Pagina mai revisionata: impaginazione a quaderno (stile e script dell'unità 33), tolti sommario e «Nella prossima unità» (rimando all'unità 35); apertura a domanda; descrizione dell'antenna in elenco (cariche, i → B, cariche → E); versi dei campi nel punto P in elenco caso → conseguenza; proprietà dell'onda (E ⊥ B, entrambi ⊥ propagazione) in elenco; titoletto «L'antenna percorsa da corrente alternata» tolto, «Un'onda che si propaga da sola» tenuto. Nessuna formula, nessun esempio, nessuna comparsa da togliere. Controllo concettuale (SymPy: i = dq/dt; ŷ × x̂ = −ẑ per il verso di B; ŷ × ẑ = x̂ per la propagazione): la figura mostrava carica dei capi e corrente in fase (massime insieme) e il testo legava «capo superiore positivo» a «B entrante»; ora carica del capo superiore q = Q sin(fase) e corrente i = I cos(fase), sfasate di un quarto di periodo, e i versi di B (dalla corrente) e di E (dalle cariche) sono dati separatamente. Figure rifatte da script: antenna con cursore sulla fase (0–360°), numero di cariche, freccia di i, simbolo ⊗/⊙ di B e freccia di E proporzionali, valori a fianco; onda in prospettiva obliqua con E nel piano verticale e B nel piano orizzontale (prima B era disegnato come sinusoide nello stesso piano di E). Nessuna figura decorativa.

## Unità 35 — Velocità di propagazione delle onde elettromagnetiche
- Parole: 195 su 1 pagina di traccia (pagina 63)
- Rettifica: il valore numerico scritto in traccia, $c=2{,}999\times10^8$ m/s, è impreciso;
  verificato con calcolo diretto $c=1/\sqrt{\varepsilon_0\mu_0}$ con $\varepsilon_0=8{,}854\times10^{-12}$
  F/m e $\mu_0=4\pi\times10^{-7}$ T·m/A: il risultato è $c=2{,}998\times10^8$ m/s (il valore
  esatto per definizione, $299\,792\,458$ m/s, arrotonda a $2{,}998\times10^8$, non a
  $2{,}999\times10^8$). Corretto nella pagina.
- Aggiunta: nessuna. Pagina puramente testuale/storica, nessun disegno nella traccia da
  ridisegnare, nessuno strumento interattivo (non richiesto e non pertinente a un contenuto
  storico-concettuale).
- Revisione (20/10/2026, regole 13/10): parole 147 → 75. Pagina mai revisionata: impaginazione a quaderno (stile e script dell'unità 34), tolti sommario e i titoletti «Il calcolo di Maxwell» e «La conferma di Hertz»; apertura a domanda; ε₀ e μ₀ in elenco con i valori; c = 1/√(ε₀μ₀) in .def rosso, sostituzione numerica in .eq; Fizeau e Hertz in elenco caso → conseguenza, tolti gli anni (cenni storici). Nessuna comparsa, nessun esempio, nessuna figura. Controllo concettuale (Python: 1/√(8,854·10⁻¹²·4π·10⁻⁷) ≈ 2,998·10⁸ m/s): conclusione «le onde elettromagnetiche sono luce» → «la luce è un'onda elettromagnetica» (non tutte le onde e.m. sono luce visibile); μ₀ indicato come ≈ 4π×10⁻⁷ T·m/A (non più esatto dal 2019); la misura di Fizeau dà la velocità della luce «circa uguale» a c. Da verificare sulla fonte: la pagina datava al 1851 la misura di Fizeau della velocità della luce (di solito 1849; nel 1851 è l'esperimento sull'acqua in moto), data tolta.

## Unità 36 — Campi, densità di energia in un'onda
- Parole: 251 su 2 pagine di traccia (pagine 64-65).
- Rettifica: nessuna. Verificato con SymPy l'intero passaggio $u_E=\frac12\varepsilon_0(cB)^2$ con
  $c^2=1/(\varepsilon_0\mu_0)$: la sostituzione dà $u_E=B^2/(2\mu_0)=u_B$, coerente con quanto
  scritto in traccia (compresa la semplificazione di $\varepsilon_0$ a pagina 65, corretta).
- Aggiunta: nessuna. Pagina puramente formulare, nessun disegno nella traccia da ridisegnare,
  nessuno strumento interattivo (non richiesto e non pertinente a un contenuto di sole formule).
- Revisione (21/10/2026, regole 13/10): parole 203 → 93. Pagina mai revisionata, riscritta: apertura a domanda; tolti sommario, «Nella prossima unità» (con il rimando all'unità 37), titoletti «Il legame fra E e B» e «Densità di energia dell'onda» e frasi di commento; proprietà dei campi (perpendicolari, in fase, legati da c) in elenco; E = cB in .def; u_E e u_B in una .eq; sostituzione condensata in una .eq; u = ε₀E² = B²/μ₀ in .eq principio; unità di misura J/m³ in .def a sé. Nessuna comparsa da togliere. Controllo concettuale: u_E = u_B e u = ε₀E² = B²/μ₀ riverificati con SymPy; nessuna correzione. Nessuna figura (pagina formulare), nessun esempio.

## Unità 37 — Intensità e vettore di Poynting
- Parole: 382 (prosa, didascalie e riquadri compresi) su 2 pagine di traccia (pagine 66-67).
- Rettifica: nessuna. Verificata con SymPy e numericamente l'intera catena di uguaglianze:
  partendo da $u=\frac12\varepsilon_0E^2+\frac{1}{2\mu_0}B^2$ con $E=cB$ si ottiene $u=B^2/\mu_0$
  e quindi $I=uc=cB^2/\mu_0$; lo stesso risultato si ottiene da $S=EB/\mu_0$ con $E=cB$, e da
  $I=\varepsilon_0E^2c$ con $B=E/c$. Tutte le forme coincidono numericamente (controllo con
  $\varepsilon_0=8{,}854\times10^{-12}$ F/m, $\mu_0=4\pi\times10^{-7}$ T·m/A): nessun passaggio
  della traccia era errato.
- Aggiunta: nessuna, a parte le poche parole di collegamento fra un passaggio e l'altro. Ridisegnati
  in SVG lo schema della torcia con la superficie di area $A$ e la distanza $x=c\,\Delta t$ (pagina
  66), e lo schema dell'onda con $\vec E$, $\vec B$ e la terna ortogonale $(\vec B,\vec S,\vec E)$
  (pagina 67); nessuno strumento interattivo, perché la figura è puramente geometrica e non c'è un
  parametro naturale da far variare.
- Revisione (21/10/2026, regole 13/10): parole 320 → 85. Pagina mai revisionata, riscritta: impaginazione a quaderno (stile e script dell'unità 36); apertura a domanda; tolti sommario, «Nella prossima unità» (con il rimando all'unità 38), titoletto «Intensità di un'onda» e frasi di commento; intensità in .def; ΔU = uV, V = Ax, x = cΔt in elenco; I = uc in una .eq; I = uc = ε₀E²c = cB²/μ₀ in .eq principio; aggiunta l'unità di misura W/m² in .def a sé; titoletto «Vettore di Poynting» con S = E∧B/μ₀ in .def, direzione/verso/modulo in elenco, S = cB²/μ₀ in .eq, S = I in .eq principio. Nessuna comparsa da togliere. Controllo concettuale (SymPy): catena u = ε₀E² = B²/μ₀, I = uc = ε₀E²c = cB²/μ₀ ed EB/μ₀ = cB²/μ₀ riverificate. Correzioni nella figura dell'onda: E e B erano disegnati sfasati di un quarto di periodo (ora in fase) e la terna mostrava E e B sulla stessa retta (verso opposto); ora E lungo y, B lungo z (prospettiva obliqua), S = E∧B lungo x. Figure rifatte da script, statiche (torcia con volume V = Ax e quota x = cΔt; onda con vettore S). Nessun esempio (la traccia non ne ha).

## Unità 38 — Quantità di moto e pressione di radiazione
- Parole: 381 su 2 pagine di traccia (pagine 68-69).
- Rettifica: nessuna. Verificata algebricamente con SymPy l'intera catena: da $\Delta U=I\,A\,\Delta t$
  con $I=uc$ si ottiene $\Delta U=ucA\,\Delta t$; dividendo per $c$ come richiesto da $p=U/c$,
  $\Delta p=uA\,\Delta t$; da cui $F_m=\Delta p/\Delta t=uA$ e $P_R=F_m/A=u=I/c$, coerente con
  quanto scritto in traccia. Controllate anche le unità di misura di ogni passaggio (energia in
  joule, quantità di moto in kg·m/s, pressione in pascal): tutte coerenti.
- Aggiunta: nessuna, a parte le poche parole di collegamento fra un passaggio e l'altro. Nessun
  disegno nella traccia da ridisegnare (pagine puramente formulari) e nessuno strumento
  interattivo, perché non c'è un parametro naturale da far variare.
- Revisione (22/10/2026, regole 13/10): parole 280 → 74. Pagina mai revisionata, riscritta: impaginazione a quaderno (stile e script dell'unità 37); apertura a domanda; tolti sommario, «Nella prossima unità» (rimando all'unità 39), il titoletto «Quantità di moto trasportata dall'onda» e le frasi di raccordo lunghe; casi assorbente/riflettente in elenco caso → conseguenza (p = U/c, p = 2U/c); ΔU = IAΔt = ucAΔt e Δp = uAΔt in elenco; F_m = uA e P_R = u in una .eq; P_R = u = I/c in .eq principio; aggiunta l'unità di misura Pa in .def a sé. Nessuna comparsa da togliere. Controllo concettuale (SymPy): catena ΔU → Δp → F_m → P_R riverificata. Correzioni: esplicitate le ipotesi «superficie assorbente» e «perpendicolare alla propagazione» per P_R = I/c; tolto «visibile» dalla frase finale (la pressione di radiazione riguarda ogni onda elettromagnetica, non solo la luce visibile). Nessuna figura né esempio (la traccia non ne ha).

## Unità 39 — Lo spettro elettromagnetico
- Parole: 286 su 2 pagine di traccia (pagine 70-71).
- Rettifica: nessuna nel testo. Verificata con SymPy la relazione generale $v=\lambda/T=\lambda f$
  (sostituendo $T=1/f$) e la sua coerenza dimensionale. Nel disegno dello spettro, per allineare
  in una sola griglia log-log i sette valori di frequenza della traccia (da $10^8$ a $10^{20}$ Hz)
  con gli otto valori di lunghezza d'onda che comparivano nell'originale (da $10^2$ a $10^{-12}$ m,
  un tick in più rispetto alla riga delle frequenze), ho arrotondato $c\approx3\times10^8$ m/s a
  $10^8$ m/s: ogni tick di frequenza $10^n$ Hz è così abbinato a $\lambda=10^{8-n}$ m, con uno
  scarto costante di circa mezza decade rispetto al valore vero per ogni valore di $n$ (verificato
  numericamente), quindi l'ordine di grandezza e il verso della corrispondenza restano corretti.
- Aggiunta: nessuna. Ridisegnati in SVG lo schizzo dell'onda con la lunghezza d'onda $\lambda$
  segnata fra due creste (pagina 70) e la barra dello spettro con le sette bande, gli assi di
  frequenza e lunghezza d'onda, e le due onde di confronto lunga/corta (pagina 71); banda
  visibile disegnata volutamente larga per restare leggibile, come già nell'originale. Nessuno
  strumento interattivo: la pagina è già una lettura diretta di un grafico statico.
- Revisione (22/10/2026, regole 13/10): parole 202 → 93. Pagina mai revisionata, riscritta: impaginazione a quaderno (stile e script dell'unità 38); apertura a domanda; tolti sommario, «Nella prossima unità» (rimando all'unità 40), il titoletto «La relazione fra lunghezza d'onda e frequenza» e le frasi di commento; λ, T, f = 1/T in elenco; v = λ/T = λf in .eq; c = λf e λ = c/f in .eq principio; aggiunta l'unità di misura Hz in .def a sé; λ↑ ⇒ f↓ trasformato in elenco caso → conseguenza («inversamente proporzionali»); titoletto «Lo spettro» tenuto (argomento distinto). Nessuna comparsa da togliere. Controllo concettuale (SymPy): v = λ/T = λf riverificata; c/750 nm ≈ 4,0×10¹⁴ Hz, c/400 nm ≈ 7,5×10¹⁴ Hz. Correzione nella figura dello spettro: la vecchia griglia abbinava f = 10ⁿ Hz a λ = 10⁸⁻ⁿ m (c arrotondata a 10⁸ m/s, scarto di mezza decade); ora le tacche di λ = 10ᵏ m sono poste in f = c/λ con c = 2,998×10⁸ m/s, e la banda visibile ha la larghezza vera (400–750 nm, valori aggiunti in didascalia) invece di quella ingrandita. Figure rifatte da script in SVG: onda con λ fra due creste (statica); spettro su asse logaritmico con cursore su f che mostra λ = c/f e la banda. Confini fra le bande indicativi (radio/microonde 10⁹ Hz, microonde/infrarossi 10¹² Hz, UV/X 10^16,5 Hz, X/gamma 10^19,5 Hz). Nessun esempio (la traccia non ne ha).

## Unità 40 — Dalla fisica classica alla fisica moderna
- Parole: 223 su 1 pagina di traccia (pagina 72; la frase conclusiva di apertura pagina 73,
  "la relatività ristretta studia i sistemi in cui le velocità sono alte", è stata inclusa perché
  chiude il ragionamento di pagina 72 prima che inizi, più sotto nella stessa pagina 73, la
  sezione sui postulati di Einstein che appartiene all'unità 40).
- Rettifica: nessuna. Il contenuto è puramente qualitativo (nessun calcolo da verificare con
  SymPy); controllate solo le disuguaglianze $v\ll c$ e $v\sim c$ riportate come nella traccia.
- Aggiunta: nessuna, a parte le poche parole di collegamento. Ridisegnato in SVG lo schema che
  colloca la meccanica classica come caso particolare di meccanica quantistica (mondo microscopico)
  e relatività generale (campi forti, alte velocità), con la divisione fisica classica / fisica
  moderna della traccia. Nessuno strumento interattivo: non c'è un parametro naturale da far
  variare in uno schema puramente concettuale.

## Unità 41 — I postulati di Einstein e l'esperimento di Michelson-Morley
- Parole: 359 su 2 pagine di traccia (pagine 73-74).
- Rettifica: nessuna. Contenuto puramente concettuale (due postulati e un fatto storico), senza
  calcoli o formule da verificare con SymPy.
- Aggiunta: nessuna, a parte le poche parole di collegamento e un breve commento al secondo
  postulato. Ridisegnato in SVG lo schema dell'auto ferma e dell'auto in moto della traccia, con
  la composizione classica delle velocità barrata per mostrare perché il risultato v+c è
  sbagliato. Nessuno strumento interattivo: pagina puramente concettuale.

## Unità 42 — Dilatazione dei tempi
- Parole: 486 su 3 pagine di traccia (pagine 75-77).
- Rettifica: nessuna. La derivazione geometrica (teorema di Pitagora sul triangolo di lati
  $v\Delta t/2$, $d$, $c\Delta t/2$) e l'esempio numerico del treno a $v=c/3$ sono stati
  verificati con SymPy: $\Delta t_0=2d/c=2{,}00\times10^{-8}\,\text{s}$ e
  $\Delta t=\Delta t_0/\sqrt{1-1/9}\approx2{,}12\times10^{-8}\,\text{s}$ tornano esatti come
  in traccia.
- Aggiunta: nessuna, a parte le poche parole di collegamento fra un passaggio e l'altro.
  Ridisegnati in SVG l'orologio a luce fermo (fonte, specchio, raggio su e giù) e lo stesso
  orologio visto in moto (triangolo con cateti $v\Delta t/2$ e $d$, ipotenusa $c\Delta t/2$).
  Reso interattivo, con un cursore su $v/c$, il grafico di $\gamma(v)$ che compare nella
  traccia, mostrando il valore corrente di $\gamma$ e i due limiti per $v\to0$ e $v\to c$: è
  l'unico strumento interattivo dell'unità, e mostra esattamente il grafico già presente sul
  quaderno.

## Unità 43 — Dilatazione dei tempi: esempi numerici
- Parole: 191 su 1 pagina di traccia (pagina 78).
- Rettifica: nessuna. I cinque valori del fattore di Lorentz sono stati verificati con SymPy
  per $v/c=0{,}50;\,0{,}75;\,0{,}90;\,0{,}99;\,0{,}999$: risultano
  $\gamma\approx1{,}1547,\,1{,}5119,\,2{,}2942,\,7{,}0888,\,22{,}3663$, che arrotondati
  coincidono con i valori $1{,}155;\,1{,}51;\,2{,}29;\,7{,}09;\,22{,}37$ s della traccia.
- Aggiunta: nessuna, a parte una riga di commento finale sull'andamento non proporzionale del
  fattore di Lorentz rispetto a $v$.

## Unità 44 — Contrazione delle lunghezze
- Parole: 395 su 2 pagine di traccia (pagine 79-80).
- Rettifica: nessuna. Il calcolo finale $L=L_0/\gamma=25{,}3\,\text{a.l.}\cdot
  \sqrt{1-0{,}99^2}\approx3{,}57\,\text{a.l.}$ è stato verificato con SymPy (γ(0,99c) ≈
  7,0888, L ≈ 3,569) e coincide con il valore della traccia; a una prima lettura la radice
  sembrava applicata a 0,999 invece che 0,99, ma il valore v=0,99c è quello scritto in
  traccia poco sopra ed è quello coerente con il risultato 3,57 a.l.
- Aggiunta: nessuna, a parte le poche parole di collegamento fra un passaggio e l'altro e la
  frase di apertura sul limite invalicabile di c, che chiudeva la pagina 79 prima
  dell'intestazione "Contrazione delle lunghezze" e non era ancora stata usata nell'unità 42.
  Ridisegnati in SVG lo schema Terra-Vega con la distanza propria e il confronto fra distanza
  a riposo e distanza contratta vista dalla navicella. Nessuno strumento interattivo: la curva
  di γ(v) è già stata resa interattiva nell'unità 41 e qui sarebbe stata ridondante.

## Unità 45 — Il decadimento dei muoni
- Parole: 443 su 3 pagine di traccia (pagine 81-83).
- Rettifica: nessuna. Tutti i valori numerici sono stati verificati con SymPy per
  $v=0{,}995c$: $\gamma\approx10{,}0125$; distanza classica $d=v\Delta t_0\approx656{,}7$ m
  (traccia: 657 m); tempo dilatato $\Delta t=\gamma\Delta t_0\approx2{,}203\cdot10^{-5}$ s
  (traccia: $2{,}2\cdot10^{-5}$ s); distanza nel sistema Terra $d=\Delta t\,v\approx6575$ m
  (traccia: 6570 m, per arrotondamento di $\Delta t$ a due cifre); quota contratta
  $L=L_0/\gamma\approx499{,}4$ m (traccia: 499 m). Tutti coincidono con la traccia.
- Aggiunta: nessuna, a parte le poche parole di collegamento fra un passaggio e l'altro.
  Ridisegnati in SVG lo schema della pioggia di particelle prodotta dal raggio cosmico in
  atmosfera (unendo i due schizzi della traccia in un'unica figura) e il confronto fra il
  sistema Terra (tempo dilatato) e il sistema del muone (quota contratta). Nessuno strumento
  interattivo: entrambe le figure sono statiche, coerenti con lo stile delle unità vicine.

## Unità 46 — Le trasformazioni di Lorentz
- Parole: 410 su 3 pagine di traccia (pagine 84-86).
- Rettifica: nessuna. Verificata con SymPy l'intera catena algebrica che porta da
  $x'=\gamma(x-vt)$ e $x=\gamma(x'+vt')$ a $t=\gamma(t'+vx'/c^2)$: sostituendo $x$ nella
  relazione per $t$ ricavata da $x'$ e usando $1/\gamma^2=1-v^2/c^2$ si ottiene esattamente
  la formula della traccia (differenza simbolica nulla). Il passaggio analogo per $t'$ è
  lasciato per simmetria, come in traccia.
- Aggiunta: nessuna, a parte le poche parole di collegamento fra un passaggio algebrico e
  l'altro e la tabella finale che raccoglie le quattro equazioni già ricavate (non una
  sintesi nuova, ma la stessa coppia di sistemi scritta una accanto all'altra come in
  chiusura di pagina 86). Ridisegnati in SVG i due schemi degli assi $S$/$S'$ che mostrano la
  simmetria del cambio di segno della velocità. Nessuno strumento interattivo: la pagina è
  interamente algebrica, senza un grafico da manovrare.

## Unità 47 — La simultaneità dipende dal sistema di riferimento
- Parole: 240 su 1 pagina di traccia (pagina 87).
- Rettifica: nessuna. Verificata con SymPy la sottrazione $t_2'-t_1'=\gamma\frac{v}{c^2}(x_1-x_2)$
  a partire dalla trasformazione di Lorentz del tempo ricavata nell'unità 45: coincide
  esattamente con il risultato della traccia.
- Aggiunta: nessuna, a parte le poche parole di collegamento fra un passaggio e l'altro. Nessun
  disegno nella traccia, quindi nessuno SVG aggiunto; nessuno strumento interattivo, la pagina è
  interamente algebrica.

## Unità 48 — Il cono di luce e gli invarianti relativistici
- Parole: 472 su 3 pagine di traccia (pagine 88–90, limitatamente alla parte che classifica
  Δs² prima dell'inizio dell'unità 48 sulla quantità di moto relativistica).
- Rettifica: nessuna correzione di merito. Sulla pagina 88 la traccia scrive "A può essere
  causa di B" anche per la coppia A-C (probabile lapsus, dato che la frase riguarda
  esplicitamente l'invio di un segnale luminoso, cioè il caso luce fra A e C): nella pagina
  è stato scritto "A può essere causa di C". Verificata con SymPy l'invarianza dell'intervallo
  spazio-temporale: calcolando $c^2t'^2-x'^2$ a partire da $x'=\gamma(x-vt)$ e
  $ct'=\gamma(ct-\frac{v}{c}x)$ si ottiene $c^2t^2-x^2$ (differenza simbolica nulla),
  esattamente come nei passaggi della traccia, doppi prodotti compresi.
- Aggiunta: nessuna, a parte le poche parole di collegamento fra un passaggio e l'altro.
  Ridisegnato in SVG il diagramma di Minkowski con il cono di luce e i quattro punti A, B, C,
  D della traccia. Nessuno strumento interattivo: la pagina è un diagramma statico e una
  derivazione algebrica.

## Unità 49 — Quantità di moto relativistica
- Parole: 205 su 1 pagina di traccia (pagina 90).
- Rettifica: nessuna. Verificato con SymPy che $p=\gamma mv$ si riduce a $p\approx mv$ per
  $v\to0$ (serie di Taylor, termine correttivo di ordine $v^3$) e diverge per $v\to c^-$
  (controllo numerico), coerente con il grafico della traccia che mostra la curva relativistica
  staccarsi dalla retta classica e impennarsi verso l'asintoto $v=c$.
- Aggiunta: nessuna, a parte le poche parole di collegamento. Ridisegnato in SVG il grafico
  p-v della traccia (retta classica e curva relativistica con asintoto in v=c). Nessuno
  strumento interattivo: pagina breve, un solo grafico statico.

## Unità 50 — Energia relativistica ed energia a riposo
- Parole: 186 su 1 pagina di traccia (pagina 91).
- Rettifica: la traccia calcola correttamente $E_0=mc^2=0{,}12\ \text{kg}\times(3\times10^8\
  \text{m/s})^2\approx1{,}1\times10^{16}\ \text{J}$ per l'energia a riposo di una mela, ma
  poi stima che questa energia alimenterebbe una lampadina da 100 W per "50 milioni di anni".
  Verificato con SymPy: $t=E_0/P=1{,}08\times10^{14}\ \text{s}\approx3{,}4\times10^6$ anni,
  non 50 milioni. Nella pagina è stato scritto il valore corretto, circa 3,4 milioni di anni.
- Aggiunta: nessuna, a parte le poche parole di collegamento fra un passaggio e l'altro.
  Nessun disegno nella traccia (solo formule racchiuse in riquadro), quindi nessuno SVG
  aggiunto; nessuno strumento interattivo, la pagina è interamente algebrica.

## Unità 51 — Fissione nucleare
- Parole: 227 su 1 pagina di traccia (pagina 92).
- Rettifica: la traccia indica come prodotto di fissione il bario 142, ma verificato con SymPy
  il bilancio del numero di massa fra reagenti (U-235 + n, A=236) e prodotti scritti
  (Ba-142 + Kr-92 + 3n, A=237) non torna. Con Kr-92 e 3 neutroni fissati, il numero di massa
  del bario che bilancia l'equazione è 141, non 142 (236 = 141 + 92 + 3). Nella pagina è stato
  scritto bario 141. Il numero atomico invece torna già nella traccia (56 + 36 = 92).
- Aggiunta: nessuna, a parte le poche parole di collegamento. Ridisegnato in SVG lo schema della
  traccia (neutrone incidente, nucleo di uranio 235, scissione in bario 141 e kripton 92 con tre
  neutroni liberati). Nessuno strumento interattivo: pagina breve, un solo schema statico.

## Unità 52 — Energia cinetica relativistica
- Parole: 164 su 1 pagina di traccia (pagina 93).
- Rettifica: nessuna. Verificato con SymPy che K=(γ-1)mc² segue correttamente da E=E₀+K, e che
  lo sviluppo in serie di Taylor di K per v piccola rispetto a c dà K≈½mv², confermando la
  sovrapposizione con la curva classica mostrata nel grafico.
- Aggiunta: una riga che spiega perché le due curve del grafico coincidono per v piccola e
  divergono vicino a c (il grafico è già nella traccia, la spiega solo a parole). Ridisegnato in
  SVG il grafico K–v della traccia, con asintoto tratteggiato in v=c. Nessuno strumento
  interattivo: pagina di una sola facciata, interamente algebrica più un grafico.

## Unità 53 — Il corpo nero e la legge di Wien
- Parole: 396 su 2 pagine di traccia (pagine 94–95).
- Rettifica: nessuna. Verificato con SymPy il calcolo della legge di Wien alle tre temperature
  della traccia: f_picco = 1,764×10¹⁴ Hz a 3000 K, 3,528×10¹⁴ Hz a 6000 K, 7,056×10¹⁴ Hz a
  12000 K, coerente con lo spostamento verso frequenze maggiori mostrato nel grafico.
- Aggiunta: nessuna. Ridisegnati in SVG lo schema della cavità del corpo nero e il grafico delle
  tre curve di intensità della traccia. Aggiunto un cursore interattivo sulla temperatura che
  applica la legge di Wien già enunciata, spostando un indicatore sul grafico esistente: non
  introduce contenuto nuovo, solo una lettura dinamica della formula.

## Unità 54 — La catastrofe ultravioletta
- Parole: 218 su 1 pagina di traccia (pagina 96).
- Rettifica: nessuna. Verificato con SymPy che la legge di Rayleigh-Jeans I(f)=c·f²T diverge per
  f→∞ (limite infinito), mentre la distribuzione di Wien I(f)=K·f³·e^(-Kf/T) tende a zero sia per
  f→0 sia per f→∞, coerente con quanto disegnato nel grafico della traccia.
- Aggiunta: nessuna. Ridisegnato in SVG il grafico delle tre curve (Rayleigh-Jeans, sperimentale,
  Wien) della traccia. Nessuno strumento interattivo: pagina breve, un solo grafico statico.

## Unità 55 — Legge di Stefan-Boltzmann e ipotesi di Planck
- Parole: 253 su 2 pagine di traccia (pagine 97–98).
- Rettifica: nessuna. Verificato con SymPy (integrazione numerica di x³/(e^x−1) su [0,∞) = π⁴/15)
  che σ = 2π⁵k⁴/(15c²h³) = 5,670×10⁻⁸ W m⁻²K⁻⁴ con le costanti CODATA, coerente con il valore
  scritto nella traccia.
- Aggiunta: nessuna. Ridisegnato in SVG lo schizzo della traccia con l'area tratteggiata sotto la
  curva I(f), a illustrare l'integrale A∫I(f)df = P. Nessuno strumento interattivo.

## Unità 56 — L'effetto fotoelettrico
- Parole: 398 su 2-3 pagine di traccia (pagine 99–101, l'ultima molto breve).
- Rettifica: nessuna. Verificato con SymPy che K = E - L0 = h(f-f0), quindi la pendenza in
  funzione di f è h per qualunque metallo (dK/df = h), coerente con le due rette parallele a
  soglie diverse disegnate nel grafico della traccia.
- Aggiunta: nessuna, a parte le poche parole di collegamento. Ridisegnati in SVG lo schema della
  lastra colpita dalla luce con gli elettroni estratti, e il grafico energia cinetica-frequenza
  per sodio e oro. Un riquadro "da non confondere" sull'intensità che non compensa una frequenza
  sotto soglia. Nessuno strumento interattivo: pagina breve, due schemi statici.

## Unità 57 — L'esperimento della doppia fenditura
- Parole: 256 su 1 pagina di traccia (pagina 102).
- Rettifica: nessuna. Nessuna formula numerica sulla pagina: contenuto puramente concettuale
  (esperimento di Young, interferenza costruttiva e distruttiva, contrasto onda-corpuscolo),
  nulla da verificare con SymPy.
- Aggiunta: nessuna, a parte le poche parole di collegamento con l'unità precedente
  sull'effetto fotoelettrico. Ridisegnato in SVG lo schema della traccia: sorgente, fenditura
  singola con fronti d'onda circolari, doppia fenditura, e i due esiti di interferenza
  costruttiva e distruttiva. Nessuno strumento interattivo: pagina di una sola facciata,
  concettuale.

## Unità 58 — L'ipotesi di De Broglie e l'esperimento di Davisson-Germer
- Parole: 261 su 1 pagina di traccia (pagina 103).
- Rettifica: nessuna. Unica formula presente, $\lambda = h/p$, verificata dimensionalmente con
  SymPy (azione/quantità di moto = lunghezza): confermato che il risultato ha le dimensioni di
  una lunghezza, coerente con l'uso come lunghezza d'onda.
- Aggiunta: nessuna, a parte le poche parole di collegamento con l'unità precedente sulla doppia
  fenditura per la luce. Ridisegnato in SVG lo schema della traccia: fascio di elettroni, doppia
  fenditura, schermo con le bande di interferenza. Nessuno strumento interattivo: pagina di una
  sola facciata, concettuale.

## Unità 59 — Il principio di indeterminazione di Heisenberg
- Parole: 525 su 3 pagine di traccia (pagine 104–106).
- Rettifica: nessuna. Unica formula presente, $\Delta p \cdot \Delta x \geq h/(4\pi)$, verificata
  dimensionalmente con SymPy: $\Delta p \cdot \Delta x$ ha le stesse dimensioni di $h$
  (kg·m²/s), coerente con una relazione di indeterminazione.
- Aggiunta: nessuna, a parte le poche parole di collegamento. Ridisegnati in SVG lo schema
  dell'esperimento ripetuto un elettrone alla volta (stesso esito di interferenza) e un confronto
  a due pannelli fra il caso senza rivelatori (elettrone delocalizzato, interferenza) e il caso
  con rivelatori (elettrone localizzato, cumulo), che nella traccia comparivano come due disegni
  separati. Un riquadro "Da ricordare" per l'enunciato del principio. Nessuno strumento
  interattivo: contenuto concettuale, due schemi statici sufficienti.

## Unità 60 — Modelli atomici: Thomson e Rutherford
- Parole: 472 su 2 pagine di traccia (pagine 107–108).
- Rettifica: nessuna, nessuna formula presente in queste pagine.
- Aggiunta: nessuna, a parte le poche parole di collegamento fra le quattro parti (modello di
  Thomson, esperimento di Rutherford, modello planetario, problema della stabilità). Ridisegnati
  in SVG i quattro schemi della traccia: la sfera di Thomson con elettroni incastonati,
  l'apparato dell'esperimento con le tre traiettorie delle particelle alfa, il modello planetario
  con nucleo e orbite, e il collasso a spirale dell'elettrone con l'emissione di onde
  elettromagnetiche. Nessuno strumento interattivo: contenuto descrittivo, senza grandezze da far
  variare.

## Unità 61 — Gli spettri a righe
- Parole: 256 su 1 pagina di traccia (pagina 109).
- Rettifica: nessuna. Unica formula presente, $1/\lambda = R(1/n'^2 - 1/n^2)$, verificata con
  SymPy: dimensionalmente coerente ($R$ in m⁻¹, parentesi adimensionale, quindi $1/\lambda$ in
  m⁻¹), e numericamente corretta calcolando tre righe di riferimento — Balmer-alfa (n'=2, n=3) dà
  656,3 nm, Lyman-alfa (n'=1, n=2) dà 121,5 nm (UV), Paschen-alfa (n'=3, n=4) dà 1875 nm (IR) —
  tutte coerenti con i valori noti e con l'attribuzione delle tre serie alle rispettive regioni
  dello spettro data nella traccia.
- Aggiunta: nessuna, a parte le poche parole di collegamento fra la descrizione dell'esperimento e
  la formula. Ridisegnato in SVG lo schema della traccia: tubo a scarica con ΔV, prisma, righe
  disperse sullo schermo. Le tre serie (Lyman, Balmer, Paschen) presentate come nella traccia, in
  forma di tabella breve. Nessuno strumento interattivo: pagina di una sola facciata, senza
  grandezze da far variare.

## Unità 62 — Il modello atomico di Bohr
- Parole: 368 su 2 pagine di traccia (pagine 110–111).
- Rettifica: nessuna. Verificato con SymPy: la lunghezza d'onda di assorbimento n=1→n=2 dà
  121,5 nm (traccia: 122 nm, arrotondamento coerente) e quella di emissione n=3→n=2 dà 656,3 nm
  (traccia: 656 nm), in accordo con i valori di Lyman-alfa e Balmer-alfa già calcolati nel
  registro dell'unità 60. Verificata la coerenza dimensionale di $L_n = nh/2\pi$ (kg·m²/s, come
  un momento angolare) e di $|\Delta E| = hf$ (joule).
- Aggiunta: nessuna, a parte le poche parole di collegamento fra le quattro ipotesi, la
  condizione di frequenza e i due esempi di salto. Ridisegnati in SVG i due schemi della
  traccia (assorbimento n=1→n=2 con fotone di 122 nm, emissione n=3→n=2 con fotone di 656 nm).
  L'equazione di bilancio fra forza centripeta e forza elettrica, presente in fondo a pagina 111,
  è stata inclusa come chiusura della pagina (senza risolverla per il raggio, che è materia
  dell'unità 62) per rispettare esattamente il confine fra le due unità. Nessuno strumento
  interattivo: contenuto concettuale con due sole formule numeriche.

## Unità 63 — Il raggio delle orbite di Bohr
- Parole: circa 220 su 1 pagina di traccia (pagina 112).
- Rettifica: nessuna. Verificata con SymPy l'intera derivazione algebrica (dal sistema
  {v = nh/(2π m_e r_n); m_e v² = Ke²/r_n} alla formula r_n = h²n²/(4π² m_e K e²)): la soluzione
  simbolica coincide esattamente con quella della traccia. Verificato numericamente il raggio
  della prima orbita con le costanti standard (h, m_e, K, e): risultato 5,29×10⁻¹¹ m, in accordo
  con il valore noto del raggio di Bohr.
- Aggiunta: un solo esempio numerico, il calcolo di r_1, assente nella traccia per questa unità
  (che contiene solo la derivazione simbolica) — necessario per dare concretezza a una formula
  altrimenti solo letterale, come richiesto dalla cura delle grandezze per la fisica. Nessun
  disegno: la pagina 112 non ne contiene (lo schema delle forze è già stato incluso in chiusura
  dell'unità 61), quindi nessuno è stato aggiunto qui.

## Unità 64 — L'energia delle orbite e la costante di Rydberg
- Parole: circa 400 (esclusi i simboli delle formule) su 2 pagine di traccia (pagine 113–114).
- Rettifica: la traccia usa la lettera K sia per la costante di Coulomb sia, nella stessa riga,
  come etichetta dell'energia cinetica (E = K + U). Per evitare l'ambiguità con la costante di
  Coulomb già fissata come K nell'unità 62, ho scritto l'energia cinetica come E_c: è una
  correzione di notazione, non di sostanza. Verificata con SymPy l'intera catena simbolica: la
  sostituzione di v_n e r_n in E = ½m_ev² − Ke²/r_n dà E_n = −(2π²m_eK²e⁴/h²)(1/n²); con le
  costanti standard E_1 = −13,6057 eV (arrotondato a −13,6 eV come nella traccia) e la costante
  ottenuta R = 2π²m_eK²e⁴/(h³c) = 1,09737×10⁷ m⁻¹, in accordo con il valore 1,097×10⁷ m⁻¹ scritto
  nella traccia e con la costante di Rydberg misurata. Nessun errore di calcolo nella traccia.
- Aggiunta: nessuna oltre alle poche righe di collegamento fra i passaggi (perché E_c = ½·(Ke²/r_n),
  perché il segno meno indica legame, perché ΔE = hc/λ). Nessun disegno: le pagine 113–114 non ne
  contengono, solo passaggi algebrici.

## Unità 65 — L'interpretazione delle orbite: Schrödinger e De Broglie
- Parole: circa 320 su 1,2 pagine di traccia (seconda metà di pagina 114 e pagina 115; la prima
  metà di pagina 114 appartiene già all'unità 63).
- Rettifica: nessuna. Contenuto puramente qualitativo, nessuna formula da verificare con SymPy.
- Aggiunta: nessuna oltre alle poche parole di collegamento fra le due interpretazioni e la
  conclusione comune (stabilità dell'atomo), già presente nella traccia. I due disegni (nube di
  probabilità di Schrödinger; onda stazionaria/non stazionaria di De Broglie con l'analogia della
  corda fissata ai due estremi) sono la ridisegnazione in SVG di quelli della traccia, non
  aggiunte. Con questa unità si completa l'intero percorso di fisica quinta (65/65 unità).
