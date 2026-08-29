
## Unità 01 — Funzione, dominio, codominio, insieme immagine
- Parole: 384 su circa 1,5 pagine di traccia (pagina 2 intera + inizio pagina 3, prima che inizi l'unità 2 su iniettive/suriettive)
- Rettifica: nessuna, il contenuto era corretto così com'era.
- Aggiunta: nessuna oltre alle parole di collegamento fra i passaggi già presenti; niente esempi, dimostrazioni o tabelle nuove.

## Unità 02 — Funzioni iniettive, suriettive, biunivoche e funzione inversa
- Parole: 419 su circa 2,5 pagine di traccia (da "Funzioni iniettive, suriettive e biunivoche" a metà pagina 3, fino a fine pagina 5, prima che inizi il campo di esistenza a pagina 6)
- Rettifica: nessuna, il contenuto era corretto così com'era. Verificato con SymPy che $f(a)=f(b)\Rightarrow a=b$ per $f(x)=3x+2$ (biunivoca) e che $f(-2)=f(2)=4$ per $f(x)=x^2$ (non iniettiva).
- Aggiunta: nessuna oltre alle parole di collegamento fra i passaggi già presenti; il commento su perché $y=x^2$ non è biunivoca esplicita un fatto implicito nel contrasto fra i due esempi della traccia.

## Unità 04 — Funzioni pari e dispari
- Parole: 250 su 2 pagine di traccia (pagine 7–8)
- Rettifica: nessuna, il contenuto era corretto così com'era. Verificato con SymPy che $f(-x)=f(x)$ per $f(x)=x^2$ e che $f(-x)=-f(x)$ per $f(x)=x^3+x$.
- Aggiunta: nessuna oltre alle parole di collegamento fra i passaggi già presenti.

## Unità 03 — Funzioni numeriche, campo di esistenza, zeri e intersezioni
- Parole: 337 su circa 2,3 pagine di traccia (dalla fine di pagina 5, dopo gli esempi di retta e parabola già assorbiti nell'unità 2, a inizio pagina 7, prima che cominci l'unità 4 su funzioni pari e dispari)
- Rettifica: nessuna, il contenuto era corretto così com'era. Verificato con SymPy che $x^2+3x+2=(x+1)(x+2)$, che gli zeri sono $-2$ e $-1$, e che $f(0)=2$.
- Aggiunta: nessuna oltre alle parole di collegamento fra i passaggi già presenti.

## Unità 05 — Funzioni definite a tratti
- Parole: 269 su 1 pagina di traccia (pagina 9)
- Rettifica: nessuna, il contenuto era corretto così com'era. Verificato con SymPy che la scrittura a tratti di $y=|x|$ coincide con $\text{Abs}(x)$ su vari valori, e che nell'esempio con tre pezzi ($3x$, $x^2$, $\sqrt{x}+8$) i valori non coincidono agli estremi: $3\cdot(-5)=-15\ne(-5)^2=25$ e $7^2=49\ne\sqrt7+8\approx10{,}6$, confermando i due salti mostrati nel grafico della traccia.
- Aggiunta: la formulazione generale a $n$ pezzi con la notazione $I_1,I_2,\dots$ è solo un'esplicitazione della graffa già usata nella traccia per $|x|$ e per l'esempio a tre pezzi, non un contenuto nuovo.

## Unità 06 — Funzioni composte
- Parole: 301 su 2 pagine di traccia (pagine 10–11)
- Rettifica: nei due diagrammi a insiemi della traccia (pagina 10) l'arco composito in alto è etichettato seguendo l'ordine di lettura dei passaggi (prima la mappa scritta a sinistra, poi quella a destra) invece della convenzione standard, per cui $(f\circ g)(x)=f(g(x))$ significa applicare prima $g$. Ho ridisegnato un solo diagramma A→B→C con $g$ poi $f$, etichettato $f\circ g$ in modo coerente con le formule della traccia, che sono invece corrette: verificato con SymPy che per $f(x)=2x+3$, $g(x)=1/x$ si ha $(f\circ g)(x)=2/x+3$ e $(g\circ f)(x)=1/(2x+3)$; e che per $f(x)=3x^2-2x$, $g(x)=x-3$ si ha $(f\circ g)(x)=3x^2-20x+33$ e $(g\circ f)(x)=3x^2-2x-3$.
- Aggiunta: la frase sul dominio della composta ("$x$ deve stare nel dominio di $g$ e $g(x)$ nel dominio di $f$") esplicita una condizione già implicita nel diagramma a insiemi (il percorso $A\to B\to C$ richiede che l'immagine di $g$ ricada nel dominio di $f$); non introduce un contenuto nuovo.

## Unità 07 — Trasformazioni geometriche e grafici: traslazioni
- Parole: 394 su 2 pagine di traccia (pagine 12–13)
- Rettifica: a pagina 12 la formula della traslazione era scritta con il segno sbagliato, $f'(x)=f(x+3)+2$, e verificata con un calcolo numerico ($f'(3)=38$) che in realtà non controlla nulla; a pagina 13 la traccia stessa la corregge in $f'(x)=f(x-3)+2$, la incornicia in rosso e la verifica correttamente mostrando che $f'(3)=2$ è la quota attesa del vertice. Ho scritto solo la versione corretta di pagina 13. Verificato con SymPy che $(x-3)^2+2=x^2-6x+11$, che $f'(3)=2$, e che applicando un'ulteriore traslazione $(2,-2)$ a $f'(x)=x^2-6x+11$ si ottiene $x^2-10x+25=(x-5)^2$.
- Aggiunta: nessuna oltre alle parole di collegamento. Il piccolo schizzo preliminare della traccia (due punti A,B spostati per rotazione e traslazione, prima di specializzare al caso della traslazione di un grafico) è reso solo a parole nella frase di apertura, non ridisegnato in SVG, perché non aggiunge contenuto oltre all'idea già espressa lì.

## Unità 08 — Angoli in radianti e angoli orientati
- Parole: 352 su 2 pagine di traccia (pagine 14–15)
- Rettifica: nessuna, il contenuto era corretto così com'era. Verificato con SymPy che $60^\circ$ corrisponde a $\pi/3$ radianti tramite la proporzione $\alpha^\circ/360^\circ=\alpha_{rad}/2\pi$.
- Aggiunta: nessuna oltre alle parole di collegamento fra i passaggi già presenti.

## Unità 09 — Seno e coseno: circonferenza goniometrica, grafici, periodicità
- Parole: 508 su circa 3,3 pagine di traccia (pagine 16–18, più il breve riquadro di sintesi in cima a pagina 19 prima che inizi l'unità 10 sulla prima relazione fondamentale)
- Rettifica: nessuna, il contenuto era corretto così com'era. Verificato con SymPy i quattro valori notevoli (sin e cos di 0, π/2, π, 3π/2), l'identità di parità sin(−α)=−sinα, cos(−α)=cosα, e la periodicità sin(α+2π)=sinα, cos(α+2π)=cosα.
- Aggiunta: nessuna oltre alle parole di collegamento fra i passaggi già presenti. Il diagramma dei quattro quadranti unisce in un solo disegno le quattro piccole circonferenze separate della traccia (una per ciascun valore notevole), senza aggiungere informazione.

## Unità 10 — Prima relazione fondamentale
- Parole: 252 su 1 pagina di traccia (pagina 19)
- Rettifica: nessuna, il contenuto era corretto così com'era. Verificato con SymPy l'esempio: da sinα=7/25 con 0<α<π/2 si ricava cos²α=1-49/625=576/625 e cosα=24/25 (radice positiva, primo quadrante).
- Aggiunta: nessuna oltre alle parole di collegamento fra i passaggi già presenti. Il disegno rifà il triangolo rettangolo inscritto già presente nella traccia, con le coordinate ricalcolate perché fosse geometricamente coerente (punto B davvero sulla circonferenza).

## Unità 11 — Tangente, cotangente, secante e cosecante
- Parole: 491 su 3 pagine di traccia (pagine 20–22)
- Rettifica: nessuna, il contenuto era corretto così com'era. Verificato con SymPy che tan α e 1/cot α coincidono identicamente, che tan(π/6)=√3/3, tan(π/3)=√3, tan(π/4)=1 come nei calcoli della pagina successiva, e che i domini dei quattro reciproci corrispondono agli zeri di seno e coseno.
- Aggiunta: nessuna oltre alle parole di collegamento fra i passaggi già presenti. Lo strumento interattivo unisce in un solo disegno manovrabile i due schizzi separati della traccia (il segmento della tangente a pagina 20 e quello della cotangente a pagina 22), mostrando entrambi insieme al variare dello stesso angolo, senza introdurre informazione nuova.

## Unità 12 — Angoli particolari
- Parole: 193 su circa 1,5 pagine di traccia (dalla seconda metà di pagina 22, dove inizia "Angoli particolari" dopo la cotangente dell'unità 11, a fine pagina 23, prima che inizi l'unità 13 sugli angoli associati a pagina 24).
- Rettifica: nessuna, il contenuto era corretto così com'era. Verificato con SymPy tutti i dodici valori (sin, cos, tan, cot per π/6, π/4, π/3) e la coerenza di tan=sin/cos, cot=1/tan in ciascun caso, incluso il passaggio di razionalizzazione 1/√3=√3/3.
- Aggiunta: nessuna oltre alle parole di collegamento fra i passaggi già presenti. Per 60° e 45° la traccia dà i quattro valori senza riderivare i passaggi (già fatti per 30°): ho rispettato questa scelta, senza ripetere la derivazione.

## Unità 13 — Angoli associati
- Parole: 385 su 2 pagine di traccia (pagine 24–25)
- Rettifica: nessuna, il contenuto era corretto così com'era. Verificato con SymPy tutte le otto identità (2π−α, −α, π−α, π+α, π/2−α, π/2+α, 3π/2−α, 3π/2+α) tramite sviluppo simbolico di seno e coseno, confermando che coincidono esattamente con i valori della traccia.
- Aggiunta: nessuna oltre alle parole di collegamento fra i passaggi già presenti. La traccia disegna una figura completa (con segmenti di tangente e cotangente) solo per il primo caso e figure essenziali (solo i due raggi) per gli altri sette; ho reso tutte le otto figure nello stesso stile essenziale già usato nelle unità precedenti (raggio e proiezioni di seno/coseno), per coerenza visiva con il resto del percorso, senza aggiungere contenuto.

## Unità 14 — Formule di addizione e sottrazione
- Parole: 332 su 3 pagine di traccia (pagine 26–28)
- Rettifica: nessuna, il contenuto era corretto così com'era. Verificato con SymPy tutte le sei identità (coseno e seno di somma e differenza, tangente di somma e differenza) tramite sviluppo simbolico, e il controesempio numerico cos(π/2−π/6)=1/2 contro cos(π/2)−cos(π/6)=−√3/2.
- Aggiunta: nessuna oltre alle parole di collegamento fra i passaggi già presenti. La formula del coseno della differenza è citata nella traccia con rimando al libro di testo (pag. 787-788) e non dimostrata: l'ho lasciata come enunciato, senza aggiungere una dimostrazione che non compare. Le altre cinque formule seguono invece le derivazioni per sostituzione già presenti nella traccia.

## Unità 15 — Formule di duplicazione
- Parole: 215 su 2 pagine di traccia (pagine 29–30)
- Rettifica: nessuna, il contenuto era corretto così com'era. Verificato con SymPy le identità sin 2α = 2 sin α cos α, le tre forme equivalenti di cos 2α, e tan 2α = 2 tan α/(1 − tan²α), tramite sviluppo simbolico e verifica numerica su valori casuali; verificato anche l'esempio con α = π/3 (sin 120° = √3/2, cos 120° = −1/2).
- Aggiunta: un solo esempio numerico con α = 60°, perché in queste due pagine la traccia deriva solo le tre formule senza applicarle a un caso concreto: la regola consente un esempio quando l'unità non ne contiene nessuno.

## Unità 16 — Formule di bisezione
- Parole: 301 su 2 pagine di traccia (pagine 31–32)
- Rettifica: nessuna, il contenuto era corretto così com'era. Verificato con SymPy le identità cos²(α/2)=(1+cosα)/2, sin²(α/2)=(1−cosα)/2, la dimostrazione di tan(α/2)=sinα/(1+cosα) per moltiplicazione e semplificazione, e l'esempio con α=30°: cos15°=(√6+√2)/4 e tan15°=2−√3, entrambi confermati simbolicamente.
- Aggiunta: un solo esempio numerico (α=30° per calcolare cos15° e tan15°), perché queste due pagine derivano solo le formule senza applicarle a un caso concreto. Aggiunta anche una breve nota sul criterio di scelta del segno ±, indispensabile per capire come si usano le formule della radice.

## Unità 17 — Formule parametriche
- Parole: 178 su 2 pagine di traccia (pagine 33–34)
- Rettifica: nessuna, il contenuto era corretto così com'era. Verificato con SymPy l'identità sinα = 2t/(1+t²) e cosα = (1−t²)/(1+t²) con t = tan(α/2), per sostituzione simbolica a partire dalle formule di duplicazione, ed è confermato l'esempio con tan(α/2)=2, da cui sinα=4/5 e cosα=−3/5.
- Aggiunta: nessuna oltre alle parole di collegamento fra i passaggi già presenti. La condizione di applicabilità (α ≠ π + 2kπ), scritta in cima a pagina 35 subito prima del titolo dell'unità successiva, è stata inclusa qui perché riguarda esclusivamente le formule parametriche.

## Unità 18 — Formule di prostaferesi e di Werner
- Parole: 268 su 4 pagine di traccia (pagine 35–38)
- Rettifica: nessuna, il contenuto era corretto così com'era. Verificato con SymPy tutte le quattro identità di prostaferesi ottenute da somma/sottrazione delle formule di addizione, le quattro formule finali dopo la sostituzione p=α+β, q=α−β, l'esempio sin(π/4)−sin(π/12)=2cos(π/6)sin(π/12), e le tre formule di Werner.
- Aggiunta: nessuna oltre alle parole di collegamento fra i passaggi già presenti.

## Unità 19 — Distanza fra due punti, punto medio, baricentro
- Parole: 254 su 1,5 pagine di traccia (pagina 39 e prima metà di pagina 40)
- Rettifica: nessuna, il contenuto era corretto così com'era. Verificato con SymPy la distanza AB=2√13 fra A(2;2) e B(8;6), il punto medio M(5;4), e il baricentro D(−1/3;0) del triangolo A(−3;−2), B(4;0), C(−2;2).
- Aggiunta: nessuna oltre alle parole di collegamento fra i passaggi già presenti. La seconda metà di pagina 40 (equazione generale della retta) è stata lasciata all'unità 20.

## Unità 20 — Equazione della retta: forma implicita, esplicita, casi particolari
- Parole: 581 su 3,5 pagine di traccia (seconda metà di pagina 40, dopo la parte sul baricentro lasciata all'unità 19, più le pagine 41, 42 e 43, fino a dove inizia l'unità 21 a pagina 44 con "equazione di una retta passante per un punto con coefficiente angolare noto")
- Rettifica: nessuna, il contenuto era corretto così com'era. Verificato con SymPy il passaggio da ax+by+c=0 a y=mx+q con m=-a/b, q=-c/b; la disparità di y=mx (f(-x)=-f(x)) e la parità di y=k; e i due esempi di tracciamento y=(3/2)x+1 (da (0;1) a (2;4)) e y=-(1/2)x+3 (da (0;3) a (2;2)).
- Aggiunta: nessuna oltre alle parole di collegamento fra i passaggi già presenti. Lo strumento interattivo (cursori per m e q sulla retta y=mx+q) riunisce in un solo grafico manovrabile ciò che la traccia mostra in più disegni statici (fascio per l'origine, bisettrici, retta generica, esempi di tracciamento), senza introdurre contenuto nuovo.

## Unità 21 — Retta per un punto, rette parallele e perpendicolari
- Parole: 223 su 1 pagina di traccia (pagina 44; la pagina 43 continua l'unità 20, come già annotato nel registro dell'unità 20, e le pagine 45–46 sono bianche)
- Rettifica: nessuna, il contenuto era corretto così com'era. Verificato con SymPy il passaggio y=mx+q, y_P=m x_P+q → y-y_P=m(x-x_P), e l'esempio P(1;2), m=3/4 → y=(3/4)x+(5/4).
- Aggiunta: le condizioni di parallelismo (m1=m2) e perpendicolarità (m1·m2=-1), enunciate senza dimostrazione in una sola nota. Non compaiono scritte nelle pagine 43–44, ma il titolo dell'unità le nomina esplicitamente e l'unità 20 (già pubblicata) le cita già come contenuto previsto per questa unità ("...e per riconoscere quando due rette sono parallele o perpendicolari"); inoltre servono a breve termine (unità 25, tangenti a una circonferenza). Ho aggiunto solo l'enunciato, senza derivarlo, trattandolo come regola indispensabile e non come dimostrazione mancante.

## Unità 22 — Definizione ed equazione della circonferenza
- Parole: 317 su 3 pagine di traccia (pagine 47–49; la pagina 46 è bianca, la pagina 50 apre già l'unità 23 "dall'equazione al grafico")
- Rettifica: nessuna, il contenuto era corretto così com'era. Verificato con SymPy la derivazione $x^2+y^2=r^2\cos^2\theta+r^2\sin^2\theta=r^2$, l'esempio $x^2+y^2=25\Rightarrow r=5$, l'esempio $(x+1)^2+(y-3)^2=4\Rightarrow C(-1;3), r=2$, e lo sviluppo di $(x-\alpha)^2+(y-\beta)^2=r^2$ in $x^2+y^2+ax+by+c=0$ con $a=-2\alpha$, $b=-2\beta$, $c=\alpha^2+\beta^2-r^2$.
- Aggiunta: nessuna oltre alle parole di collegamento fra i passaggi già presenti.

## Unità 23 — Dall'equazione al grafico: centro, raggio, condizione di realtà
- Parole: 221 su 2 pagine di traccia (pagine 50–51; la pagina 49 chiude l'unità 22 e la pagina 52 apre già l'unità 24 "rette e circonferenze")
- Rettifica: nessuna, il contenuto era corretto così com'era. Verificato con SymPy l'inversione $a=-2\alpha,\,b=-2\beta\Rightarrow \alpha=-a/2,\,\beta=-b/2$, la formula $r=\sqrt{a^2/4+b^2/4-c}$, e l'esempio $x^2+y^2-4x+2y-4=0\Rightarrow a=-4,\,b=2,\,c=-4\Rightarrow C(2;-1),\,r=3$.
- Aggiunta: nessuna oltre alle parole di collegamento fra i passaggi già presenti. Nella traccia l'esercizio numerico precede l'enunciato generale delle formule; nella pagina ho invertito l'ordine (prima le formule, poi l'esempio) per coerenza con il criterio "prima si capisce, poi si formalizza", senza aggiungere alcun contenuto nuovo.

## Unità 24 — Posizione di una retta rispetto a una circonferenza
- Parole: 337 su 2 pagine di traccia (pagine 52–53; la pagina 51 chiude l'unità 23 con la condizione di realtà, e la pagina 54 apre già l'unità 25 "rette tangenti a una circonferenza")
- Rettifica: nessuna, il contenuto era corretto così com'era. Verificato con SymPy l'esempio $x^2+y^2+3x-3y-2=0$, $3x-2y+1=0$: la sostituzione $y=\frac32x+\frac12$ dà $\frac{13}{4}x^2-\frac{13}{4}=0\Rightarrow x=\pm1$, con punti $A(1;2)$ e $B(-1;-1)$; verificata anche la coerenza con il confronto $d,r$: $d=\sqrt{13}/2\approx1{,}80 < r=\sqrt{26}/2\approx2{,}55$, secante.
- Aggiunta: nessuna oltre alle parole di collegamento fra i passaggi già presenti.

## Unità 25 — Rette tangenti a una circonferenza: i quattro metodi
- Parole: 572 su 7 pagine di traccia (pagine 54–60; la pagina 53 chiude l'unità 24 e la pagina 61 apre già l'unità 26 "determinare l'equazione di una circonferenza")
- Rettifica: nessuna, il contenuto era corretto così com'era. Verificato con SymPy tutti e quattro i metodi: primo metodo (circonferenza x²+y²−12x+2y+17=0, P=(0;1)) → discriminante nullo dà m=−2 e m=1/2; secondo metodo (circonferenza x²+y²−2x=0, P=(9/4;0)) → distanza dal centro dà m=±4/3; terzo metodo (circonferenza x²+y²−4x−2y−3=0, P=(4;3) sulla circonferenza) → centro C(2;1), pendenza di PC=1, tangente perpendicolare m'=−1, retta y=−x+7; quarto metodo, formule di sdoppiamento (circonferenza x²+y²−2x−4y−20=0, P=(4;6)) → retta 3x+4y−36=0. Tutti i risultati coincidono esattamente con la traccia.
- Aggiunta: nessuna oltre alle parole di collegamento fra i passaggi già presenti. Ho cercato online un quesito di maturità reale sulle tangenti a una circonferenza (argomento ammesso per la matematica di terza), ma non ho trovato un quesito d'esame verificabile con anno e sessione su questo tema specifico: ho preferito ometterlo piuttosto che inventarne uno.

## Unità 26 — Determinare l'equazione di una circonferenza
- Parole: 283 su 2 pagine di traccia (pagine 61–62; la pagina 60 chiude l'unità 25 con il quarto metodo delle tangenti, e la pagina 63 apre già l'unità 27 "posizione di due circonferenze")
- Rettifica: nessuna, il contenuto era corretto così com'era. Verificato con SymPy entrambi gli esempi: primo esempio, centro C=(4;3) e P=(1;2) → sistema -a/2=4, -b/2=3, 1+4+a+2b+c=0 dà a=-8, b=-6, c=15, con r²=10>0; secondo esempio, A=(-8;18), B=(6;20), centro sull'asse y (a=0) → sistema 18b+c=-388, 20b+c=-436 dà b=-24, c=44, con r²=100>0.
- Aggiunta: nessuna oltre alle parole di collegamento fra i passaggi già presenti.

## Unità 27 — Posizione di due circonferenze e asse radicale
- Parole: 456 su 3 pagine di traccia (pagine 63–65; la pagina 62 chiude l'unità 26 e la pagina 66 apre già l'unità 28 "parabola")
- Rettifica: nessuna, il contenuto era corretto così com'era. Verificato con SymPy: la differenza fra le equazioni generali dà $(a-a')x+(b-b')y+(c-c')=0$; nell'esempio 1, $x^2+y^2+2x-4y-11=0$ e $x^2+y^2+2x-16y+13=0$ danno per sottrazione $12y-24=0\Rightarrow y=2$, e la sostituzione nella prima circonferenza dà $x^2+2x-15=0\Rightarrow x=-5,3$; nell'esempio 2, $x^2+y^2+8x-6y=0$ intersecato con $x=0$ dà $y^2-6y=0\Rightarrow y=0,6$. Tutti i risultati coincidono con la traccia.
- Aggiunta: una frase di collegamento nell'esempio 2 per chiarire che il metodo di mettere a sistema una retta con una circonferenza si applica anche quando la retta non è un asse radicale ma un asse cartesiano; nessun contenuto matematico nuovo.

## Unità 28 — Definizione, fuoco, direttrice, asse e vertice
- Parole: 251 su 1 pagina di traccia (pagina 66; la pagina 65 chiude l'unità 27 con l'ultimo esempio sull'asse radicale, e la pagina 67 apre già l'unità 29 "parabola con vertice nell'origine" con la derivazione dell'equazione $y=ax^2$)
- Rettifica: nessuna, il contenuto era corretto così com'era.
- Aggiunta: nessuna oltre alle parole di collegamento fra i passaggi già presenti. Non ho aggiunto esempi numerici: la traccia su questa pagina è puramente definitoria (nessun esempio, nessun calcolo), e l'equazione della parabola non è ancora stata introdotta, quindi non c'era modo di costruirne uno senza anticipare l'unità 29. Verificato con SymPy, solo come controllo di coerenza interna (non pubblicato in pagina), che la relazione di equidistanza $\overline{PF}=\overline{PH}$ enunciata qui è esattamente la condizione che l'unità 29 tradurrà nell'equazione $y=x^2/(4\delta)$.

## Unità 29 — Parabola con vertice nell'origine
- Parole: 254 su 1,3 pagine di traccia (pagine 67–68; la pagina 66 chiude l'unità 28, la pagina 68 contiene solo la conclusione dell'esempio numerico e la pagina 69 è bianca, la pagina 70 apre già l'unità 30 "rette e parabola")
- Rettifica: nessuna, il contenuto era corretto così com'era. Verificato con SymPy l'intera derivazione: PF²−PH² = x²−4cy, quindi PF=PH ⇔ x²=4cy ⇔ y=x²/(4c); posto a=1/(4c), per l'esempio y=2x² si ha a=2, c=1/(4·2)=1/8, coerente con fuoco F=(0;1/8) e direttrice y=−1/8 riportati nella traccia.
- Aggiunta: uno strumento interattivo con cursore su $a$ che mostra come la parabola $y=ax^2$ e la posizione del fuoco/direttrice variano al variare di $a$ — visualizza solo la relazione $c=1/(4a)$ già derivata, nessun contenuto matematico nuovo.

## Unità 30 — Rette e parabola: posizioni reciproche
- Parole: 310 su 1,4 pagine di traccia (pagina 70 e la prima metà della pagina 71, fino alla fine dell'esempio; la seconda metà della pagina 71 apre già l'unità 31 "rette tangenti a una parabola" con i tre disegni P esterno/sulla parabola/interno, non trattati qui; la pagina 69 è bianca)
- Rettifica: nessuna, il contenuto era corretto così com'era. Verificato con SymPy il sistema fra $y=-\frac12x^2+2x$ e $y=x-4$: sympy.solve conferma le soluzioni $(4;0)$ e $(-2;-6)$, coerenti con la traccia.
- Aggiunta: nessuna oltre alle parole di collegamento fra i passaggi già presenti. Il caso della retta verticale $x=k$ era in figura nella traccia senza commento esplicito sul perché dia un solo punto: ho aggiunto una riga che lo spiega (sostituzione diretta, nessuna equazione di secondo grado).

## Unità 31 — Rette tangenti a una parabola
- Parole: 392 su 4,5 pagine di traccia (seconda metà della pagina 71, dove inizia il titolo "Rette tangenti a una parabola" con i tre disegni P esterno/sulla parabola/interno, più le pagine 72–75; la prima metà della pagina 71 chiude l'unità 30 con l'ultimo esempio di posizione retta-parabola, e la pagina 76 apre già l'unità 32 "determinare l'equazione di una parabola")
- Rettifica: nessuna, il contenuto era corretto così com'era. Verificato con SymPy entrambi i metodi: per le tangenti da P=(1;-5) a y=x²-2, il sistema dà x²-mx+(m+3)=0 e Δ=0 ⇒ m=-2,6, con rette y=-2x-3 e y=6x-11, coerenti con la traccia; per la tangente in un punto della curva, la derivazione generale con la somma delle radici conferma la formula m=2ax₀+b, e per l'esempio y=(1/2)x²-2x+3 in P=(4;3) si ha m=2 e retta y=2x-5, con discriminante della risolvente verificato nullo.
- Aggiunta: nessuna oltre alle parole di collegamento fra i passaggi già presenti. Ho ridisegnato in SVG i tre schizzi della traccia (P esterno con due tangenti, P sulla parabola con una tangente, P interno senza tangenti); nessun contenuto nuovo.

## Unità 32 — Determinare l'equazione di una parabola
- Parole: 330 su 3,5 pagine di traccia (pagine 76–79; la pagina 79 contiene solo l'esempio 2 e due osservazioni finali, occupando circa metà pagina; la pagina 75 chiude l'unità 31 con l'ultimo esempio di tangente in un punto, e la pagina 80 apre già l'area successiva "Esponenziali")
- Rettifica: nessuna, il contenuto era corretto così com'era. Verificato con SymPy le formule generali di vertice e fuoco; per l'esempio 1 (punto P=(-1;2), fuoco F=(-2;5/4)) sympy.solve sul sistema conferma le due soluzioni (a,b,c)=(1,4,5) e (-1/4,-1,5/4), cioè y=x²+4x+5 e y=-¼x²-x+5/4, coerenti con la traccia; per l'esempio 2 (vertice V=(0;9), punto P=(6;5)) sympy.solve conferma l'unica soluzione (a,b,c)=(-1/9,0,9), cioè y=-⅑x²+9.
- Aggiunta: nessuna oltre alle parole di collegamento fra i passaggi già presenti. Ho cercato online un quesito di maturità reale su questo argomento specifico (determinare l'equazione di una parabola da vertice/fuoco/punto, risolubile con i soli strumenti elementari), ma non ho trovato un quesito autonomo verificabile con anno e sessione: ho preferito ometterlo piuttosto che inventarne uno.

## Unità 33 — Ellisse come luogo geometrico e sua equazione
- Parole: 409 su circa 2,5 pagine di traccia (pagina 113 intera e pagina 114 intera, più la prima metà della pagina 115 fino all'equazione canonica riquadrata; la seconda metà della pagina 115 apre già l'unità 34 "Vertici, fuochi ed eccentricità" con il titolo "Vertici dell'ellisse"; la pagina 112 chiude l'unità 51 sulle disequazioni esponenziali risolubili con i logaritmi — nel quaderno l'ellisse è stata aggiunta in coda dopo i logaritmi, come indicato nelle note del percorso)
- Rettifica: nessuna, il contenuto era corretto così com'era. Verificata con SymPy l'intera derivazione algebrica: partendo da PF₁+PF₂=2a con F₁=(-c;0), F₂=(c;0), le due elevazioni al quadrato successive portano a x²(a²-c²)+a²y²=a²(a²-c²); con b²=a²-c² la forma canonica x²/a²+y²/b²=1 è stata verificata anche numericamente con a=5, c=3, b=4 sul punto (3;16/5), che soddisfa l'equazione.
- Aggiunta: nessuna oltre alle parole di collegamento fra i passaggi già presenti. Non ho inserito un quesito d'esame: è la prima unità sull'ellisse, la traccia non contiene ancora esempi svolti (arrivano nell'unità 35), quindi nessun quesito era alla portata.

## Unità 34 — Vertici, fuochi ed eccentricità dell'ellisse
- Parole: 284 su 1,5 pagine di traccia (seconda metà della pagina 115, dal titolo "Vertici dell'ellisse" fino alla fine, più tutta la pagina 116 con fuochi ed eccentricità; la prima metà della pagina 115 chiude l'unità 33 con l'equazione canonica riquadrata; la pagina 117 apre già l'unità 35 "Ellisse e rette" con i tre casi esterna/tangente/secante e il primo esempio numerico)
- Rettifica: nessuna, il contenuto era corretto così com'era. Verificato con SymPy: risolvendo x²/a²+y²/b²=1 per y=0 si ottiene x=a (vertice), per x=0 si ottiene y=b; da b²=a²-c² risolto per c si ottiene c=√(a²-b²), coerente con la traccia; verificato anche il caso limite c=0 ⇒ b²=a².
- Aggiunta: nessuna oltre alle parole di collegamento fra i passaggi già presenti. Nessun quesito d'esame: è ancora la seconda unità sull'ellisse, senza esempi numerici nella traccia (arrivano nell'unità 35).

## Unità 35 — Ellisse e rette; determinare l'equazione di un'ellisse
- Parole: 297 su 4 pagine di traccia (pagine 117–120: pagina 117 "Ellissi e Rette" con i tre casi e il sistema col discriminante più l'inizio dell'esempio 1, pagina 118 chiude l'esempio 1, pagina 119 apre "Determinare l'equazione di un'ellisse" con l'esempio 2, pagina 120 chiude l'esempio 2; la pagina 116 chiude l'unità 34 con l'eccentricità, la pagina 121 apre già l'unità 36 "Iperbole" con la definizione come luogo geometrico)
- Rettifica: nessuna, il contenuto era corretto così com'era. Verificato con SymPy entrambi gli esempi: per l'ellisse x²/18+y²/9=1 e la retta x+2y-6=0, la sostituzione x=-2y+6 dà 6y²-24y+18=0 con soluzioni y=1,3 e punti A=(0;3), B=(4;1), coerenti con la traccia; per l'ellisse passante per P=(5√5/3;2) con eccentricità 4/5, sympy.solve sul sistema conferma a=5, b=3, cioè x²/25+y²/9=1.
- Aggiunta: nessuna oltre alle parole di collegamento fra i passaggi già presenti. Nessun quesito d'esame: è ancora una delle prime unità sull'ellisse (solo la terza), quindi nessun quesito era alla portata.

## Unità 36 — Iperbole: definizione ed equazione
- Parole: 306 su 2 pagine di traccia (pagine 121–122: pagina 121 con la definizione come luogo geometrico e il disegno dei due rami con F1, F2 e P; pagina 122 con l'equazione canonica, il disegno del triangolo a-b-c e l'eccentricità; la pagina 120 chiude l'unità 35 con l'ultimo esempio sull'ellisse, e non esiste una pagina 123: il quaderno si ferma qui, le unità 37-39 sull'iperbole sono ex novo come indicato nelle note del percorso)
- Rettifica: nessuna, il contenuto era corretto così com'era. Verificato con SymPy che e=c/a=sqrt(a²+b²)/a è la forma semplificata corretta, e che c>a sempre per b>0 (quindi e>1), coerente con la traccia; controllato numericamente con a=5, b=3: c=sqrt(34)≈5,83, e≈1,166, e verificato che il vertice (5;0) soddisfa x²/25-0²/9=1.
- Aggiunta: nessuna oltre alle parole di collegamento fra i passaggi già presenti. La traccia non contiene la derivazione algebrica dalla definizione all'equazione (a differenza dell'ellisse nell'unità 33): l'ho lasciata assente, mantenendo solo definizione ed equazione come nel quaderno. Ho aggiunto una sola riga di confronto esplicito con l'ellisse (b²=a²-c² contro c²=a²+b²) perché il quaderno stesso disegna il triangolo senza commentarlo, e il confronto rende leggibile perché qui l'ipotenusa è c anziché un cateto.

## Unità 37 — Asintoti dell'iperbole
- Parole: 294 (unità ex novo, come indicato nelle note del percorso: le pagine 121–122 del quaderno si fermano alla definizione e all'equazione dell'iperbole, unità 36, senza trattare gli asintoti)
- Rettifica: nessuna, non essendoci traccia da correggere.
- Aggiunta: l'intera unità è ex novo per costruzione (autorizzata dalle note del percorso). Contenuto limitato a ciò che serve per introdurre gli asintoti in coerenza con l'unità 36: derivazione algebrica delle equazioni $y=\pm(b/a)x$ dall'equazione canonica, il metodo del rettangolo per disegnarli, un esempio numerico e uno strumento interattivo con cursori su $a$ e $b$ che mostra i rami avvicinarsi alle diagonali. Verificato con SymPy che $\lim_{x\to+\infty}\big[(b/a)\sqrt{x^2-a^2}-(b/a)x\big]=0$ e, numericamente, che a $x=100$ (con $a=4$, $b=3$) la differenza fra ramo e asintoto è già scesa a circa 0,06. Nessun quesito d'esame: è la prima delle tre unità ex novo sull'iperbole e introduce solo la nozione, senza ancora l'iperbole equilatera né la funzione omografica.

## Unità 38 — Iperbole equilatera e iperbole riferita agli asintoti
- Parole: 305 (unità ex novo, come indicato nelle note del percorso: il quaderno si ferma alla definizione dell'iperbole, unità 36; le unità 37-39 sono ex novo)
- Rettifica: nessuna, non essendoci traccia da correggere.
- Aggiunta: l'intera unità è ex novo per costruzione (autorizzata dalle note del percorso), in continuità diretta con l'unità 37 (asintoti generali). Contenuto: caso particolare $a=b$, eccentricità $e=\sqrt2$ costante, e derivazione per rotazione degli assi della forma $XY=k$ con $k=a^2/2$. Un solo esempio numerico ($a=2\Rightarrow XY=2$), come da regola quando la traccia non ne contiene nessuno. Verificato con SymPy: $e=\sqrt{a^2+b^2}/a$ con $b=a$ dà $\sqrt2$; le pendenze degli asintoti $1$ e $-1$ hanno prodotto $-1$ (perpendicolarità); la rotazione $x=(X+Y)/\sqrt2$, $y=(X-Y)/\sqrt2$ trasforma $x^2-y^2=a^2$ in $2XY=a^2$, cioè $XY=a^2/2$. Nessun quesito d'esame: è la seconda delle tre unità ex novo sull'iperbole, prima della funzione omografica dove i quesiti sono più frequenti.

## Unità 39 — Funzione omografica
- Parole: 394 (unità ex novo, come indicato nelle note del percorso: chiude le tre unità 37-39 sull'iperbole aggiunte in coda al quaderno)
- Rettifica: nessuna, non essendoci traccia da correggere.
- Aggiunta: l'intera unità è ex novo per costruzione (autorizzata dalle note del percorso), diretta continuazione dell'unità 38: dalla forma $Y=k/X$ riferita agli asintoti si arriva per divisione polinomiale alla funzione omografica generale $y=(ax+b)/(cx+d)$, con centro $(-d/c;\,a/c)$ e condizione di non degenerazione $ad-bc\neq0$. Un solo esempio numerico ($y=(2x+3)/(x-1)$, centro $(1;2)$), come da regola quando non c'è traccia. Uno strumento interattivo con cursori sul centro, per mostrare la sola traslazione rigida della curva (concetto già introdotto nell'unità 7). Verificato con SymPy: la divisione $y=a/c+[(bc-ad)/c^2]/(x+d/c)$ è algebricamente identica al rapporto originale (differenza simbolica nulla); per l'esempio numerico, centro $(1;2)$ e $k=5$ riproducono esattamente $y(2)=7$ sia dalla forma diretta sia da quella traslata. Ho cercato online un quesito di maturità reale su questo argomento specifico, ma ho trovato solo risorse didattiche generiche, senza un quesito autonomo verificabile con anno e sessione: ho preferito ometterlo piuttosto che inventarne uno.

## Unità 40 — Potenze a esponente intero, razionale e reale
- Parole: 389 su 2 pagine di traccia (pagine 80–81 del quaderno: pagina 80 con i tre casi dell'esponente intero e gli esempi numerici, pagina 81 con i tre casi dell'esponente razionale; la pagina 79 chiude l'unità 32 sulla parabola, la pagina 82 apre l'unità 41 sulla funzione esponenziale)
- Rettifica: nessuna. Verificato con SymPy tutti gli esempi della traccia: (-√2)³=-2√2, (-2/3)⁻²=(-3/2)²=9/4, 7^(3/4)=radice quarta di 7³, (√3)^(-1/2)=1/radice quarta di 3, 0^(7/6)=0; tutti confermati corretti così come scritti, nessuna correzione necessaria.
- Aggiunta: una sola frase di chiusura sull'esponente reale (assente come caso a sé nella traccia, che tratta esplicitamente solo intero e razionale), necessaria perché il titolo dell'unità dichiarato nel percorso include "e reale" e perché serve da premessa alla condizione a>0 su cui si apre l'unità 41 sulla funzione esponenziale. Ho tenuto la frase strettamente qualitativa, senza sviluppare la definizione di potenza a esponente reale, che non compare nel quaderno. Nessun quesito d'esame: è la prima unità della sezione, introduce solo le condizioni di esistenza.

## Unità 41 — La funzione esponenziale: grafico, dominio, monotonia
- Parole: 485 su 3 pagine di traccia (pagine 82–84 del quaderno: pagina 82 con la definizione di funzione esponenziale, i casi particolari 1^x, 0^x, a^0, a^(-r) e la premessa sulla base positiva; pagina 83 col disegno degli insiemi Q e R, il riquadro con la condizione a≥0 e il grafico dei due casi a>1/0<a<1 con il punto (0,1); pagina 84 coi due esempi numerici di verifica della monotonia con 2^x e (1/2)^x; la pagina 81 chiude l'unità 40 sull'esponente razionale, la pagina 85 apre già l'unità 42 con le proprietà delle potenze e il numero e)
- Rettifica: nessuna. Verificato con SymPy entrambi gli esempi: 2^5=32 e 2^√3≈3,32 (quindi y1>y2, coerente con la crescenza), (1/2)^5=1/32≈0,03 e (1/2)^√3≈0,30 (quindi y2>y1, coerente con la decrescenza); tutti i valori della traccia erano già corretti.
- Aggiunta: nessuna oltre alle parole di collegamento fra i passaggi già presenti. Lo strumento interattivo (cursore sulla base a) è la stessa coppia di grafici già disegnata a mano nella traccia, resa manovrabile invece di duplicarla in due figure statiche separate. Nessun quesito d'esame: è la seconda unità della sezione esponenziali e richiede solo definizione e monotonia, strumenti insufficienti per un quesito di maturità tipico (che richiede equazioni o disequazioni, trattate nelle unità 44-45).

## Unità 42 — Proprietà delle potenze e il numero e
- Parole: 193 su 1 pagina di traccia (pagina 85 del quaderno: le cinque proprietà delle potenze con esponente reale e l'introduzione del numero di Nepero; la pagina 84 chiude l'unità 41 sulla funzione esponenziale, la pagina 86 apre già l'unità 43 sul dominio delle funzioni [f(x)]^g(x))
- Rettifica: nessuna. Verificato con SymPy numericamente le cinque identità (prodotto, quoziente, potenza di potenza, prodotto e quoziente di basi diverse con lo stesso esponente) su valori casuali di a,b,x,y: tutte confermate. Verificato anche il valore di e=2,71828182845905, coincidente con quello scritto nella traccia.
- Aggiunta: nessuna oltre alle parole di collegamento. Nessun esempio numerico, perché la traccia non ne contiene per questa pagina. Nessun quesito d'esame: la pagina è solo un elenco di proprietà e la definizione del numero e, senza gli strumenti (equazioni, disequazioni) che renderebbero un quesito di maturità alla portata; questi arrivano nelle unità 44-45.

## Unità 43 — Dominio delle funzioni del tipo [f(x)]^g(x)
- Parole: 542 su 3 pagine di traccia (pagine 86–88 del quaderno: pagina 86 col caso 1 base costante/esponente variabile e i primi tre esempi, pagina 87 col caso 2 base variabile/esponente costante e i suoi tre esempi, pagina 88 col caso 3 base ed esponente entrambi variabili con l'unico esempio; la pagina 85 chiude l'unità 42 sulle proprietà delle potenze, la pagina 89 apre già l'unità 44 sulle equazioni esponenziali)
- Rettifica: nessuna. Verificato con SymPy tutti i domini della traccia: x≥1 per 3^√(x-1); x²-1≥0 → x≤-1∨x≥1; x²-4>0 → x<-2∨x>2; (x+3)/(x-1)≥0 → x≤-3∨x>1; 4x²-1>0 → x<-1/2∨x>1/2, intersecato con x≥0 dà x>1/2. Tutti confermati identici a quanto scritto nel quaderno.
- Aggiunta: nessuna oltre alle parole di collegamento fra un passaggio e l'altro. Lo studio del segno del terzo esempio del caso 2 (frazione elevata a π) è stato reso con la tabella dei segni già usata in altre unità del percorso, al posto dello schema a mano libera della traccia, per coerenza di stile col resto del sito. Nessun quesito d'esame: l'argomento è puramente di determinazione del dominio, propedeutico alle equazioni e disequazioni esponenziali delle unità 44-45, dove i quesiti di maturità sono alla portata.
