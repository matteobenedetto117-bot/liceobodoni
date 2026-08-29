
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
