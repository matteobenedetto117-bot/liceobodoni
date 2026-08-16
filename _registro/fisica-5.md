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
