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
