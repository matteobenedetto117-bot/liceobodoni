# Registro — Fisica quinta

## Unità 01 — Magneti, poli e assenza di monopoli
- Parole: 436 su 3 pagine di traccia
- Rettifica: nessuna.
- Aggiunta: nessuna. Nessuna formula presente nella traccia, quindi nessuna verifica SymPy necessaria.

## Unità 02 — Il campo magnetico e le linee di campo
- Parole: 172 su 1 pagina di traccia
- Rettifica: a pagina 4 la traccia afferma che l'intensità del campo "diminuisce linearmente con la distanza dal magnete". Non è corretto (il campo di un dipolo decresce con una potenza della distanza, non linearmente): nella pagina ho tolto "linearmente", lasciando solo che il campo diminuisce allontanandosi dal magnete.
- Aggiunta: nessuna. Nessuna formula quantitativa presente, quindi nessuna verifica SymPy necessaria.

## Unità 03 — Interazione fra campo magnetico e carica elettrica
- Parole: 473 su 2,3 pagine di traccia (pagine 5–6 intere, più l'esempio numerico in cima a pagina 7, prima dell'inizio della sezione "Forza di Lorentz" che appartiene all'unità 04)
- Rettifica: nessuna. Il calcolo numerico di B = F/(q·v⊥) e la verifica dimensionale che porta al tesla sono stati controllati con SymPy e risultano corretti così come nella traccia.
- Aggiunta: nessuna.

## Unità 04 — La forza di Lorentz
- Parole: 357 su 1,7 pagine di traccia (seconda metà di pagina 7, dalla sezione "Forza di Lorentz" in poi, più pagina 8 intera)
- Rettifica: nessuna. Il modulo F = qvB sinθ è stato verificato con SymPy come coerente con |q v × B| e con la relazione F = qv⊥B già vista nell'unità 03.
- Aggiunta: nessuna.

## Unità 05 — Moto di particelle cariche in campo elettrico e magnetico uniforme
- Parole: 240 su 1 pagina di traccia (pagina 9)
- Rettifica: nessuna. Verificato con SymPy: a=F/m=qE/m e la forza di Lorentz con θ=0 dà
  qvB·sin(0)=0, coerenti con la traccia.
- Aggiunta: nessuna. Ho accorpato in un'unica figura i quattro schemi della traccia sui casi
  accelerazione/decelerazione per carica positiva e negativa (che per simmetria mostrano la
  stessa fisica) in due soli casi con carica positiva, spiegando a parole che per una carica
  negativa i due casi si scambiano: nessun contenuto nuovo, solo una figura più compatta.

## Unità 06 — Moto circolare e raggio di curvatura
- Parole: 255 su 1 pagina di traccia (pagina 10)
- Rettifica: nessuna. Verificato con SymPy che da $qvB=mv^2/r$ segue $r=mv/(qB)$, coerente con la traccia.
- Aggiunta: una frase che spiega come il raggio dipende da massa, velocità, carica e campo, indispensabile per dare senso alla formula appena ricavata; nessun contenuto fisico ulteriore.

## Unità 07 — Spettrometro di massa
- Parole: 155 su 1 pagina di traccia (pagina 11)
- Rettifica: nessuna. Verificato con SymPy che da $r=mv/(qB)$ segue $m=qBr/v$, coerente con la traccia.
- Aggiunta: nessuna. La traccia contiene solo titolo, la definizione "strumento che serve per misurare la massa di particelle cariche" e uno schema incompleto (un riquadro con una velocità entrante); ho ridisegnato lo schema in modo leggibile e collegato la definizione alla formula del raggio di curvatura già ricavata nell'unità 06, risolta rispetto a m, che è esattamente ciò che la descrizione dell'unità nel file di classe indica come contenuto ("misurare la massa sfruttando il raggio di curvatura"). Nessun esempio numerico presente nella traccia, quindi nessuno aggiunto.

## Unità 08 — Campo magnetico generato da un filo percorso da corrente
- Parole: 240 su 1 pagina di traccia (pagina 12)
- Rettifica: nessuna. La traccia è puramente qualitativa (nessuna formula quantitativa: la legge di Biot-Savart arriva solo nell'unità 12), quindi nessuna verifica SymPy necessaria; ho verificato solo la coerenza fisica del verso di circolazione del campo nei due disegni (corrente verso l'alto → campo antiorario, corrente verso il basso → campo orario), coerente con la regola della mano destra.
- Aggiunta: nessuna. Ho ridisegnato in SVG i due schemi della traccia (il filo con la linea di campo circolare e l'ago magnetico, e la coppia di fili con corrente invertita) e riportato la regola della mano destra così com'è enunciata nella traccia.

## Unità 09 — Forza su un filo percorso da corrente
- Parole: 248 su 1 pagina di traccia (pagina 13)
- Rettifica: nessuna. Verificato con SymPy che sostituendo $q=iL/v$ in $F=qvB\sin\theta$ la velocità di deriva si semplifica e si ottiene esattamente $F=BiL\sin\theta$, coerente con la traccia (dove il passaggio è annotato a mano con le stesse cancellazioni).
- Aggiunta: nessuna. Ho ridisegnato in SVG i due schemi della traccia: la coppia di fili con corrente invertita (con la convenzione entrante/uscente già usata nelle unità precedenti al posto della freccia F nel piano, per coerenza con il resto del percorso) e lo schema generale del filo di lunghezza L nel campo B con angolo θ usato per la derivazione.

## Unità 10 — Spire di corrente e momento torcente magnetico
- Parole: 411 su 2,7 pagine di traccia (pagina 14 intera, pagina 15 intera, la sezione "Esempio" in cima a pagina 16, prima dell'inizio di "Legge di Ampère" che appartiene all'unità 11)
- Rettifica: nessuna. Verificato con SymPy: la derivazione $M_{TOT}=2\cdot ihB\cdot(d/2)=ihBd=iAB$ è algebricamente esatta; l'esempio numerico $M_{max}=Ni\pi r^2B$ con $N=200$, $r=3{,}0\cdot10^{-2}$ m, $i=1{,}6$ A, $B=0{,}35$ T dà $0{,}3167$ N·m, coerente con lo $0{,}32$ N·m arrotondato della traccia.
- Aggiunta: nessuna. Ho ridisegnato in SVG i tre schemi della traccia (la spira rettangolare vista di fronte con le forze entrante/uscente, e le due posizioni estreme di momento massimo e minimo) e riportato la spiegazione già presente sul perché compare $\sin\theta$ e su quando la spira raggiunge l'equilibrio.

## Unità 11 — Legge di Ampère
- Parole: 534 su 3 pagine di traccia (pagine 16–18; l'esempio in cima a pagina 16 appartiene all'unità 10, non contato qui)
- Rettifica: nessuna. Verificato con SymPy che la somma $\sum B\,\Delta l$ su un percorso circolare con $B=ki/r$ dà $2\pi k i$, coerente con il passaggio a mano della traccia (dove la $r$ si semplifica con la circonferenza $2\pi r$).
- Aggiunta: nessuna. Ho ridisegnato in SVG i quattro schemi della traccia (percorsi concatenato/non concatenato, il percorso concatenato in un piano qualunque, il percorso circolare con $B$ tangente, la scomposizione di $\vec B$ in $B_\parallel$, e i due esempi con più fili) e riportato la derivazione e la generalizzazione così come compaiono, fermandomi dove si ferma la traccia (senza scrivere $B=\mu_0 i/2\pi r$, che compare solo a inizio pagina 19, già unità 12).

## Unità 12 — Legge di Biot-Savart e forze fra fili paralleli
- Parole: 416 su 1,4 pagine di traccia (pagina 19 intera più l'inizio di pagina 20, fino a
  prima dell'avvio di "Campo magnetico generato da una spira circolare", che appartiene
  all'unità 13)
- Rettifica: nessuna. Verificato con SymPy: la soluzione di $B\cdot2\pi r=\mu_0 i$ dà
  $B=\mu_0 i/(2\pi r)$; le due espressioni $F=i_1B_2L$ e $F=i_2B_1L$ si semplificano entrambe
  a $\mu_0 i_1i_2L/(2\pi d)$, coerenti con la traccia.
- Aggiunta: nessuna. Ho ridisegnato in SVG i tre schemi della traccia (il percorso circolare
  intorno al filo con $B$ tangente, la coppia di fili con correnti concordi che genera forze
  attrattive, e la coppia con correnti discordi che genera forze repulsive) e riportato la
  derivazione così come compare.

## Unità 13 — Campo di una spira circolare e di una bobina
- Parole: 227 su 2 pagine di traccia (pagina 20 intera più l'inizio di pagina 21, fino al
  disegno delle tre spire attaccate, prima dell'avvio di "Campo magnetico generato da un
  SOLENOIDE", che appartiene all'unità 14)
- Rettifica: nessuna. Verificato con SymPy che $B_{bobina}=N\cdot i\mu_0/(2R)$ è
  effettivamente $N$ volte $B_{spira}=i\mu_0/(2R)$, coerente con la traccia; verificato anche
  l'esempio numerico aggiunto ($N=200$, $R=4{,}0$ cm, $i=0{,}50$ A dà $B\approx1{,}6\times10^{-3}$ T).
- Aggiunta: un esempio numerico, perché in tutta l'unità la traccia non ne contiene nessuno
  (solo i due schemi di verso della corrente e la formula riquadrata per spira e bobina).

## Unità 14 — Campo magnetico di un solenoide
- Parole: 371 su 1,5 pagine di traccia (la parte finale di pagina 21, dal titolo "Campo
  magnetico generato da un SOLENOIDE" in poi, più pagina 22 intera, fino a prima dell'avvio
  di "Magnetismo nella materia" a inizio pagina 23, che appartiene all'unità 15; la formula
  della bobina a inizio pagina 21 appartiene all'unità 13, già pubblicata).
- Rettifica: nessuna. Verificato con SymPy che risolvendo $B\cdot L=\mu_0 N i$ rispetto a $B$
  si ottiene $B=\mu_0 N i/L=\mu_0 n i$ con $n=N/L$, coerente con il passaggio a mano della
  traccia; verificata anche la coerenza dimensionale ($[\mu_0]=\text{T}\cdot\text{m/A}$) e
  l'esempio numerico aggiunto ($N=500$, $L=25$ cm, $i=2{,}0$ A dà $n=2000\ \text{m}^{-1}$ e
  $B\approx5{,}0\times10^{-3}$ T).
- Aggiunta: un esempio numerico, perché in tutta l'unità la traccia non ne contiene nessuno
  (solo lo schema del solenoide, il disegno del campo nullo fuori/uniforme dentro, e la
  derivazione coi quattro tratti del percorso di Ampère).

## Unità 15 — Magnetismo nella materia
- Parole: 411 su 3 pagine di traccia (pagine 23–25; la pagina 26, con la temperatura di Curie e
  il geomagnetismo, appartiene all'unità 16 e non è stata trattata qui)
- Rettifica: nessuna. La traccia è qualitativa più una tabella di valori empirici di
  permeabilità relativa; verificato con SymPy/Python solo che l'ordinamento riportato
  (ferromagnetici $\gg$ paramagnetici $>1>$ diamagnetici) è coerente con i valori numerici
  della tabella.
- Aggiunta: nessuna.

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

## Unità 17 — Moto elicoidale
- Parole: 233 su 1 pagina di traccia (pagina 28)
- Rettifica: nessuna. Verificate con SymPy le tre formule della traccia: $r=mv_\perp/(qB)$,
  $T=2\pi r/v_\perp=2\pi m/(qB)$ (la semplificazione di $v_\perp$ è corretta) e
  $P=v_\parallel\cdot T=2\pi m v_\parallel/(qB)$; tutte confermate identiche a quelle scritte.
- Aggiunta: nessuna. Un solo disegno SVG, che riprende lo schema della traccia (linee di campo,
  traiettoria elicoidale, scomposizione di $v$ in $v_\perp$ e $v_\parallel$, passo $P$).

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

## Unità 19 — L'esperienza di Faraday e la forza elettromotrice indotta
- Parole: 406 su 2 pagine di traccia (pagine 32–33)
- Rettifica: nessuna. La traccia è interamente qualitativa (nessuna formula né calcolo numerico
  su queste due pagine): niente da verificare con SymPy. Ho controllato solo la coerenza della
  notazione, usando $\Delta V$ per la fem indotta come già fatto per la differenza di potenziale
  nell'unità 18.
- Aggiunta: nessuna. Due disegni SVG che riprendono gli schemi della traccia (i due circuiti
  avvolti sullo stesso anello di ferro con batteria, interruttore e amperometro; il magnete in
  avvicinamento a una bobina collegata a un amperometro), senza introdurre contenuto fisico
  ulteriore.

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

## Unità 23 — Campo elettrico indotto e generatori di corrente
- Parole: circa 196 di prosa (sommario, didascalie, paragrafi) su 1 pagina di traccia (pagina 40)
- Rettifica: nessuna. La formula $E = Bv$ è stata verificata con SymPy a partire da
  $E\ell = \Delta V = Bv\ell$ (uguaglianza fra ddp lungo la barretta e fem, già ricavata
  nell'unità 22). Coerenza dimensionale controllata: T·(m/s) = V/m, corretto per un campo
  elettrico. La frase finale di pagina ("...cambia e si genera corrente") è stata inclusa come
  chiusura del paragrafo sui generatori, mentre la derivazione quantitativa di $\varepsilon =
  NBA\omega\sin\omega t$ resta nell'unità 24 come da traccia (pagina 41).
- Aggiunta: nessuna. Due soli disegni SVG che ridisegnano gli schemi della traccia (il campo
  elettrico interno alla barretta e il generatore a spira rotante fra due poli); nessun esempio
  numerico né strumento interattivo, assenti anche nella traccia su questa pagina.

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

## Unità 25 — Motori elettrici in corrente alternata
- Parole: circa 266 (prosa, didascalie ed etichette comprese) su 1 pagina di traccia (pagine 42-43)
- Rettifica: nessuna. La pagina non introduce formule nuove (nessun calcolo numerico da
  verificare con SymPy): si limita a riprendere la forza $F = iLB$ già stabilita nell'unità 9
  per il filo rettilineo, applicandola concettualmente ai due lati della spira senza rideriva­rla.
  Coerente con la traccia, che su queste pagine è solo qualitativa (due schemi e un breve testo).
- Aggiunta: nessuna. Ridisegnati in SVG lo schema spira-fra-i-poli collegata tramite
  commutatore a un generatore di corrente alternata (pagina 42) e i tre istanti della rotazione
  con corrente e forza (pagina 43, incluso il terzo con l'inversione di corrente). Nessuno
  strumento interattivo: i tre pannelli statici bastano a mostrare la sequenza già disegnata
  nella traccia, e un cursore avrebbe richiesto assunzioni sulla geometria non esplicitate lì.

## Unità 26 — Mutua induzione e autoinduzione
- Parole: circa 460 (prosa, didascalie ed etichette comprese) su 2 pagine di traccia (pagine
  43-44; la pagina 43 è condivisa con l'unità 25, di cui restano solo le ultime righe sulla
  rotazione del motore, e con l'unità 26 da qui in poi ("Induttanza" / "Mutua induzione")).
- Rettifica: nessuna. La pagina non contiene formule numeriche da verificare: è interamente
  qualitativa (nessun calcolo, nessuna definizione quantitativa, che arriva solo nell'unità 27
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
  (unità 28, pagine 46-47), quindi resta di competenza di quell'unità pur non usando la formula
  del solenoide.

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

## Unità 32 — Le prime tre equazioni di Maxwell
- Parole: circa 542 (prosa, didascalie e riquadri compresi) su 3 pagine di traccia (pagine 56-58).
- Rettifica: nella derivazione finale della legge di Faraday come circuitazione (pagina 59, che
  chiude il ragionamento aperto a pagina 57), il segno meno presente nella definizione della fem
  indotta (ε = -ΔΦ(B)/Δt, pagina 57, coerente con l'unità 21) va perso nei passaggi successivi e
  il riquadro finale riporta Γ(E) = dΦ(B)/dt senza segno meno. Corretto in pagina come
  Γ(E) = -dΦ(B)/dt, coerente con la definizione di fem indotta usata poche righe sopra nella
  stessa traccia e con la legge di Faraday-Neumann-Lenz già stabilita nell'unità 21. Verificato
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

## Unità 36 — Campi, densità di energia in un'onda
- Parole: 251 su 2 pagine di traccia (pagine 64-65).
- Rettifica: nessuna. Verificato con SymPy l'intero passaggio $u_E=\frac12\varepsilon_0(cB)^2$ con
  $c^2=1/(\varepsilon_0\mu_0)$: la sostituzione dà $u_E=B^2/(2\mu_0)=u_B$, coerente con quanto
  scritto in traccia (compresa la semplificazione di $\varepsilon_0$ a pagina 65, corretta).
- Aggiunta: nessuna. Pagina puramente formulare, nessun disegno nella traccia da ridisegnare,
  nessuno strumento interattivo (non richiesto e non pertinente a un contenuto di sole formule).

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

## Unità 40 — Dalla fisica classica alla fisica moderna
- Parole: 223 su 1 pagina di traccia (pagina 72; la frase conclusiva di apertura pagina 73,
  "la relatività ristretta studia i sistemi in cui le velocità sono alte", è stata inclusa perché
  chiude il ragionamento di pagina 72 prima che inizi, più sotto nella stessa pagina 73, la
  sezione sui postulati di Einstein che appartiene all'unità 41).
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
  dell'intestazione "Contrazione delle lunghezze" e non era ancora stata usata nell'unità 43.
  Ridisegnati in SVG lo schema Terra-Vega con la distanza propria e il confronto fra distanza
  a riposo e distanza contratta vista dalla navicella. Nessuno strumento interattivo: la curva
  di γ(v) è già stata resa interattiva nell'unità 42 e qui sarebbe stata ridondante.

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
  a partire dalla trasformazione di Lorentz del tempo ricavata nell'unità 46: coincide
  esattamente con il risultato della traccia.
- Aggiunta: nessuna, a parte le poche parole di collegamento fra un passaggio e l'altro. Nessun
  disegno nella traccia, quindi nessuno SVG aggiunto; nessuno strumento interattivo, la pagina è
  interamente algebrica.

## Unità 48 — Il cono di luce e gli invarianti relativistici
- Parole: 472 su 3 pagine di traccia (pagine 88–90, limitatamente alla parte che classifica
  Δs² prima dell'inizio dell'unità 49 sulla quantità di moto relativistica).
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
