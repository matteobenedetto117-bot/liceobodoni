
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
