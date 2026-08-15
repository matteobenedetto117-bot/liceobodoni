# Registro — Matematica quarta

## Unità 01 — Equazioni goniometriche elementari
- Parole: 631 su 6 pagine di traccia
- Rettifica: nessuna, i calcoli (sin x=√3/2, cos x=-1/2, tan x=√3/3) sono stati verificati con SymPy e coincidono con la traccia.
- Aggiunta: nessuna.

## Unità 02 — Angoli associati ed equazioni riconducibili a elementari
- Parole: 335 (prosa, formule escluse) su 5 pagine di traccia
- Rettifica: nessuna, tutti i passaggi (i due esempi su seno e coseno con angoli associati, l'esempio con tangente, l'esempio 2sin²x+5cosx-4=0) sono stati verificati con SymPy e coincidono con la traccia.
- Aggiunta: nessuna.

## Unità 03 — Equazioni lineari in seno e coseno
- Parole: 543 (prosa e formule) su 7 pagine di traccia
- Rettifica: nessuna. Tutti i passaggi sono stati verificati con SymPy: la soluzione tanx=√3 di sinx-√3cosx=0; la sostituzione parametrica di sinx+cosx-1=0 (t=0∨t=1, x=2kπ∨x=π/2+2kπ); il sistema retta-circonferenza di √3sinx+cosx=2 (Δ=0, sinx=√3/2, cosx=1/2); il metodo dell'angolo aggiunto su sinx-√3cosx+1=0 (r=2, α=-π/3, x=3π/2+2kπ∨x=13π/6+2kπ). Tutto coincide con la traccia.
- Aggiunta: nessuna.

## Unità 04 — Funzioni goniometriche inverse
- Parole: 354 (prosa e formule) su circa 2,5 pagine di traccia (pagina 19 condivisa con la fine dell'unità 03)
- Rettifica: nessuna. Le uniche informazioni numeriche sono i domini e i codomini di seno, coseno, tangente ristretti e delle loro inverse, e i nove valori usati nello strumento interattivo (sin di -π/2,-π/3,-π/4,-π/6,0,π/6,π/4,π/3,π/2 e il loro ritorno con arcoseno): tutti verificati con SymPy e coincidono con la traccia.
- Aggiunta: nessuna. Lo strumento interattivo (il punto (x,sin x) che si scambia in (sin x,x)) visualizza esattamente il passaggio "inverto x e y" già scritto nella traccia, non introduce un contenuto nuovo.

## Unità 05 — Equazioni omogenee di secondo grado in seno e coseno
- Parole: 396 su 4 pagine di traccia
- Rettifica: nessuna. Tutti i passaggi sono stati verificati con SymPy: le soluzioni di cosx sinx-√3sin²x=0 (x=kπ ∨ x=π/6+kπ, confermate anche per enumerazione in [0,2π)); il discriminante Δ=(1+√3)²-4√3=4-2√3=(1-√3)² dell'equazione tan²x-(1+√3)tanx+√3=0 con radici tanx=1 e tanx=√3; le tre formule di duplicazione finali (sin²x, cos²x, sinx cosx in funzione di 2x). Tutto coincide con la traccia.
- Aggiunta: nessuna. Il riquadro "errore tipico" riprende il controllo che la traccia stessa mostra passo per passo (verifica che x=π/2+kπ non sia soluzione, prima di dividere per cosx o per cos²x); non introduce un contenuto nuovo.

## Unità 06 — Disequazioni goniometriche elementari
- Parole: 541 (prosa e formule, SVG esclusi) su 6 pagine di traccia (26–31)
- Rettifica: nessuna. Tutte le soluzioni sono state verificate per enumerazione numerica (oltre che a mano) con Python: l'esempio guida sinx<1/2; i quattro esempi elementari (2sinx-√3>0, 2cosx+1≤0, tanx>1, sin(x-π/6)≥0); i quattro esempi non elementari (√2sin²x-sinx≥0, 4cos²x-4cosx-3≤0 con Δ=64 e radici cosx=3/2 impossibile ∨ cosx=-1/2, il sistema -√3/2<cosx<1/2, 3tan²x+√3tanx≥0 con radici tanx=0 ∨ tanx=-√3/3 ed esclusione x≠π/2+kπ). Tutto coincide con la traccia.
- Aggiunta: nessuna. Lo strumento interattivo (cursore sulla soglia a in sinx<a, con l'arco soluzione ridisegnato) rende dinamico solo l'esempio guida già svolto nella traccia (sinx<1/2); non introduce contenuto nuovo. Il riquadro "un modo più compatto" riprende la nota finale della traccia (pagina 32) sul riscrivere con periodo π invece di 2π.

## Unità 07 — Disequazioni fratte e sistemi di disequazioni
- Parole: 473 (prosa e formule, SVG esclusi) su 5 pagine di traccia (32–36)
- Rettifica: nessuna. Tutti i risultati sono stati verificati con SymPy/Python: l'identità
  tanx-1/(2cosx)=(2sinx-1)/(2cosx); il segno di N=2sinx-1 e D=2cosx per enumerazione numerica
  su [0,2π] e il quoziente risultante positivo esattamente su [π/6,π/2)∪[5π/6,3π/2); il sistema
  4sin²x-3≥0 ∧ tanx≥1 (intersezione [π/3,π/2) verificata campionando f e g agli estremi e
  all'interno); il sistema a tre condizioni cosx>0 ∧ cot²x-3≥0 ∧ 2sinx-1≤0, incluso il
  controllo numerico punto per punto che l'intersezione finale sia esattamente
  [-π/6,π/6]\{0}. Tutto coincide con la traccia.
- Aggiunta: nessuna. La pagina 32 apre con la nota sulla forma compatta di periodo π
  dell'ultimo esempio dell'unità 06: quella nota è già stata registrata nell'unità 06 e qui
  non viene ripetuta. I due diagrammi di sintesi (il segno del quoziente sulla circonferenza
  e le due intersezioni di sistemi con cerchi concentrici) ridisegnano in SVG esattamente le
  costruzioni grafiche della traccia (pagine 33, 35 e 36); non introducono un metodo nuovo.

## Unità 08 — Triangoli rettangoli: primo e secondo teorema
- Parole: 369 (prosa, formule e didascalie, SVG esclusi) su 4 pagine di traccia (37–40)
- Rettifica: nessuna. Le due identità dei teoremi sono state verificate simbolicamente con
  SymPy sostituendo β=π/2−α (cos β=sin α, sin β=cos α, cot β=tan α, tan β=cot α, tutte
  identicamente nulle come differenza). I quattro esempi numerici sono stati ricalcolati con
  Python: Esempio 1 (a=40, b=110) dà α=arctan(40/110)≈19,98°≈20°, β≈70°, c=√(40²+110²)≈117,05;
  Esempio 2 (a=21,13, c=50) dà α=arcsin(21,13/50)≈25,0°, β≈65°, b=√(50²−21,13²)≈45,32;
  Esempio 3 (a=8, α=28°) dà β=62°, b=8·tan62°≈15,05, c=√(8²+b²)≈17,04; Esempio 4 (c=28,3,
  α=58°) dà β=32°, a=28,3·sin58°≈24,00, b=28,3·sin32°≈15,00. Tutto coincide con la traccia.
- Aggiunta: nessuna. Il commento sotto il primo disegno (le coordinate del punto sulla
  circonferenza goniometrica) riprende esattamente l'annotazione a lato della traccia a
  pagina 37 ("c → raggio circonf. gon.", "a e b corrispondono a sin e cos moltiplicati per
  c"), riformulata in una frase. Le due costruzioni con la tangente per il secondo teorema
  ridisegnano in SVG i due schemi già presenti a pagina 38.

## Unità 09 — Area di un triangolo e teorema della corda
- Parole: 331 su 2 pagine di traccia (41–42)
- Rettifica: nella dimostrazione del teorema della corda, l'angolo retto è in A (D̂AB, angolo alla base sul diametro DB, per il teorema di Talete), non in D come una prima lettura della traccia lasciava intendere: verificato numericamente piazzando i quattro punti su una circonferenza di prova (coordinate polari) e calcolando gli angoli con il prodotto scalare. Con l'angolo retto in D il calcolo non tornava; con l'angolo retto in A, DB=2r come ipotenusa e α come angolo in D, si ottiene esattamente AB=DB sinα=2r sinα, coerente con la formula finale della traccia. Verificata anche l'identità sin(180°-α)=sinα usata per l'altezza nel caso ottuso della formula dell'area (SymPy, semplificazione simbolica a zero).
- Aggiunta: nessuna. Le due figure per il caso acuto e ottuso dell'altezza ridisegnano le due costruzioni della traccia a pagina 41; le due figure del teorema della corda ridisegnano quelle di pagina 42.

## Unità 10 — Teorema dei seni e circonferenza circoscritta
- Parole: 576 (prosa e formule, SVG esclusi) su 4 pagine di traccia (43–46)
- Rettifica: nessuna. Verificato con Python/SymPy: l'esempio con α=30°, angolo in B=105°,
  a=6 dà γ=45° e c=6·sin45°/sin30°=6√2≈8,49; l'esempio Terra-Luna con longitudini 30°E e
  50°W dà angolo al centro 80°, angolo in B=90°+9°=99°, angolo in L=1°, e d=r·sin99°/sin1°
  ≈360952 km, arrotondato nella traccia a 360000 km; l'esempio della parallasse con
  1″=1/3600°≈2,78·10⁻⁴°, angolo alla base 90°-1″≈89,9997°, dà D≈3,094·10¹³ km, e con
  1 anno luce=9,46·10¹² km si ottiene D≈3,27 a.l., coerente con la definizione di parsec
  richiamata a fine traccia. Tutto coincide con la traccia.
- Aggiunta: nessuna. I due disegni dell'esempio Terra-Luna (sezione della Terra con A, B,
  L, e il triangolo estratto per il calcolo) e il disegno della parallasse ridisegnano in
  SVG esattamente le costruzioni delle pagine 45 e 46; la frase finale sul parsec riprende
  l'annotazione "1 pc" già scritta a margine della traccia a pagina 46.

## Unità 11 — Teorema del coseno
- Parole: 332 su 3 pagine di traccia (47–49)
- Rettifica: nessuna. Verificato con SymPy che la dimostrazione (CH=b sinα, AH=b cosα, HB=c−b cosα, Pitagora nel triangolo CHB) si riduce identicamente a a²=b²+c²−2bc cosα. Verificati con Python tutti i risultati numerici della traccia: Esempio 1 (c²=7, c=√7); Esempio 2 (γ=80°, a≈7,83, b≈10,55); Esempio 3 (a≈24,50, cosβ≈0,77, β≈40°, γ≈120°). Tutto coincide con la traccia.
- Aggiunta: nessuna. Il riquadro finale "seni o coseno" riprende la nota conclusiva della traccia a pagina 49 ("per cercare lati → seni, per cercare angoli → coseno, il coseno non ha ambiguità sugli angoli, li individua univocamente"), riformulata in una frase.

## Unità 12 — Risoluzione dei triangoli e caso ambiguo
- Parole: 398 su 3 pagine di traccia (50–52)
- Rettifica: nessuna. Verificato con Python/SymPy: Esempio 4 (c=56,2, a=39, γ=59°) dà sinα=0,5948≈0,59, α=arcsin(0,59)≈36,50°≈36° (soluzione acuta accettata perché γ<90° e c>a); Esempio 5 (a=58,6, b=77, c=70) dà cosβ≈0,2931 → β≈72,95°≈73°, cosα≈0,6860 → α≈46,69°≈47°, γ=180°-α-β≈60,36°≈60°. Tutto coincide con la traccia. Verificata anche la logica geometrica dello schema dei casi (intersezioni di un cerchio di raggio a con la semiretta base) per ricontrollare i confini fra 0, 1 e 2 soluzioni al variare di a rispetto ad altezza b·sinα e al lato b.
- Aggiunta: nessuna. Lo strumento interattivo (cursore sul lato a) rende dinamico esattamente lo schema dei casi già enumerato nella traccia a pagina 50-51 (le due figure con β₁ e β₂ accettabili/non accettabili); non introduce un criterio nuovo, solo la stessa condizione geometrica resa manovrabile.

## Unità 13 — Traslazioni, dilatazioni e contrazioni
- Parole: 611 su 3 pagine di traccia (53–55)
- Rettifica: nessuna. Verificato con SymPy: sin(x-π/4) e sin(x+π/4) sono effettivamente il
  grafico del seno traslato di π/4 a destra e a sinistra (zero dell'argomento in x=π/4 e
  x=-π/4); periodicity(sin(2x))=π e periodicity(cos(x/2))=4π, coerenti con "il periodo
  diventa 2π/k"; sin(2x+π) si semplifica a -sin(2x) (stesso periodo π, sfasato di
  mezzo periodo rispetto a sin2x, verificato che il grafico tracciato è coerente con
  questa identità); cot(θ+π/2) si semplifica a -tan(θ), usato solo per controllare che il
  disegno della cotangente traslata avesse gli asintoti nel posto giusto, non riportato
  nella pagina. Tutto coincide con la traccia.
- Aggiunta: lo strumento interattivo con quattro cursori (ampiezza, fattore di periodo,
  sfasamento, traslazione verticale) applicati insieme a y=A sin(k(x-c))+d: riunisce in un
  solo grafico manovrabile le quattro trasformazioni già presenti separatamente nella
  traccia, senza introdurre alcuna trasformazione o regola che non vi compaia.

## Unità 14 — Simmetrie e funzione inversa
- Parole: 436 su 2 pagine di traccia (56–57)
- Rettifica: nessuna. Verificato con SymPy che sin(-x)=-sin(x) e tan(-x)=-tan(x)
  identicamente (le due simmetrie rispetto all'asse y disegnate nella traccia); verificato
  numericamente che arcsin(sin(x))=x per x in [-π/2,π/2] (esempio x=0,7) e che
  √(x²)=x per x≥0 (esempio x=1,3), coerenti con le due coppie funzione/inversa
  disegnate a pagina 57. Tutto coincide con la traccia.
- Aggiunta: nessuna in senso stretto. Il riquadro finale sulla biunivocità spiega a parole
  il motivo delle croci sul ramo escluso della parabola e del tratto ristretto del seno,
  entrambi già disegnati nella traccia a pagina 57; non introduce un criterio nuovo.

## Unità 15 — Valore assoluto nei grafici
- Parole: 749 su 3 pagine di traccia (58–60)
- Rettifica: nessuna. Verificato con SymPy tutte le identità usate: cos(-x+π/2) ≡
  cos(x-π/2) (parità del coseno); sin(-x-π) ≡ -sin(x-π) e sin(x-π) ≡ sin(x+π)
  (periodicità); continuità in x=0 dei due rami di sin(|x|-π) e di cos(|x|+π/2)
  (stesso valore da sinistra e da destra). Verificato inoltre che sin(t-π) e
  cos(t+π/2) coincidono identicamente con -sin(t) per ogni t: i due esempi guidati
  della traccia (sin(|x|-π) e cos(|x|+π/2)) producono quindi esattamente lo stesso
  grafico, osservazione riportata in un riquadro perché discende direttamente dai
  due procedimenti già svolti nella traccia, non da materiale esterno.
- Aggiunta: nessuna. Lo strumento interattivo (cursore su x) rende dinamica
  esattamente la costruzione per casi di sin(|x|-π) già scritta nella traccia,
  mostrando quale dei due rami è attivo e il valore corrispondente; non introduce
  un esempio o una tecnica nuova.

## Unità 16 — Trasformazioni di retta, parabola, esponenziale e logaritmo
- Parole: 809 su 3 pagine di traccia (61–63)
- Rettifica: nessuna in senso stretto. Per non appesantire le figure ho unificato due coppie di curve che nella traccia illustrano la stessa trasformazione già mostrata altrove nella stessa unità (la parabola intermedia (x+3)² a pagina 61, assorbita nel disegno finale (x+3)²+2; e (x+2)² a pagina 62, ridondante con la traslazione orizzontale già vista in (x+3)²+2): nessun contenuto è stato tolto, solo una ripetizione grafica dello stesso tipo di spostamento. Verificato con SymPy: (-x+2)²≡(x-2)² (semplificazione scritta anche nella traccia); lo zero di e^x-3 in x=ln3≈1,0986; il minimo ln2 di ln(|x|+2) in x=0; il punto d'incontro (0,4) dei due rami di (|x|+2)².
- Aggiunta: nessuna.

## Unità 17 — Piano cartesiano nello spazio: distanze, punto medio, baricentro
- Parole: 269 su circa 1,3 pagine di traccia (86–87, pagina condivisa con l'inizio dell'unità 18)
- Rettifica: nessuna. Le formule di distanza, punto medio e baricentro (estensione diretta delle formule 2D con l'aggiunta della quota) sono state verificate con SymPy; l'esempio numerico è stato ricalcolato con SymPy: A(1;2;2), B(4;6;2), C(7;4;5) danno AB=5, M=(2,5;4;2), G=(4;4;3), coincide con quanto scritto in pagina.
- Aggiunta: un esempio numerico (distanza, punto medio, baricentro sugli stessi tre punti), perché la traccia in queste due pagine non contiene alcun esempio numerico, solo le formule.

## Unità 18 — Vettori nello spazio e prodotto scalare
- Parole: 348 su circa 1,5 pagine di traccia reale (87–88, la seconda metà di pagina 87 dopo il baricentro dell'unità 17, fino a prima dell'equazione del piano che apre l'unità 19)
- Rettifica: nessuna. Verificato con SymPy: dati u(2;1;-2) e v(1;-2;0), u+v=(3;-1;-2), |u|=3, u·v=0 (perpendicolari), coincide con quanto riportato in pagina.
- Aggiunta: un esempio numerico (somma, modulo, prodotto scalare e verifica di perpendicolarità), perché la traccia in queste pagine definisce le operazioni ma non le applica a numeri.

## Unità 19 — Il piano: equazione generale e casi particolari
- Parole: 506 su circa 3 pagine di traccia (seconda metà di pagina 88, pagine 89–90, prima metà di pagina 91)
- Rettifica: nessuna. Verificato con SymPy: il piano per P0(2;-3;1) normale a n(4;1;-1) dà 4x+y-z-4=0; il sistema per il piano passante per A(2;0;0), B(0;1;0), C(0;0;3) dà a=-d/2, b=-d, c=-d/3 e, con d=-6, 3x+6y+2z-6=0 — entrambi coincidono esattamente con quanto scritto in pagina.
- Aggiunta: nessuna. Lo strumento interattivo (superficie 3D con cursori su a, b, d) rende dinamica esattamente la classificazione dei casi particolari già scritta nella traccia (piano parallelo a un asse quando manca una variabile, piano per l'origine quando d=0); non introduce un esempio o un caso nuovo.

## Unità 20 — Posizione reciproca di due piani e distanza punto-piano
- Parole: 401 su 2 pagine di traccia (92–93)
- Rettifica: nessuna. Verificato con Python/SymPy: il prodotto scalare dei normali dei piani 2x-y+2z+7=0 e 3x+2y-2z-1=0 dà 6-2-4=0, confermando la perpendicolarità; la distanza di P(0;1;-1) dal piano x-y+2z-1=0 dà |0-1-2-1|/√6 = 4/√6 = (2/3)√6, coincidente con la traccia. Nessun quesito di maturità inserito: le tracce reperite sulla distanza punto-piano richiedono anche la posizione piano-sfera, argomento non ancora disponibile a questo punto del percorso (unità 26-27).
- Aggiunta: nessuna.

## Unità 21 — La retta nello spazio: equazioni parametriche e cartesiane
- Parole: 559 su 6 pagine di traccia (94–99)
- Rettifica: nessuna. Verificato con SymPy: l'equivalenza algebrica (x-6)/-2 = (6-x)/2 e (x-5)/(0-5) = (5-x)/5 usate nel passaggio a forma con denominatori positivi; la verifica del passaggio di B(0;1;-1) per la retta AB con A(5;0;1) dà 1=1=1; la condizione di allineamento per P(2;-3;2), A(1;0;3), B(-1;6;5) dà -1/2=-1/2=-1/2, tutto coincidente con la traccia. Nessun quesito di maturità inserito: è la prima unità sulla sola equazione della retta, senza ancora gli strumenti di posizione reciproca e distanza (unità 23–25) con cui i quesiti reali di questa area combinano piani, rette e sfere.
- Aggiunta: nessuna.

## Unità 22 — Retta come intersezione di due piani
- Parole: 264 su 2 pagine di traccia (100–101)
- Rettifica: nessuna. Verificato con SymPy: dal sistema x+y-3z=0, x-3y+z+4=0 con z=k si ottiene x=2k-1, y=k+1, coincidente con la traccia; sostituendo k=z si torna a x-2z+1=0, y-z-1=0, anch'esso coincidente. Per l'esempio 6 (x-2y+z-1=0, 2x+y-z+1=0) i rapporti fra coefficienti 1/2, -2, -1 non sono uguali, confermando che i piani non sono paralleli.
- Aggiunta: nessuna.

## Unità 23 — Posizione reciproca di due rette
- Parole: 364 su 3 pagine di traccia (102–104)
- Rettifica: nessuna. Verificato con SymPy: per r con v(1;-1;3) e s con w(4;-2;-2), v·w=4+2-6=0 (perpendicolari) e 1/4≠-1/-2 (non parallele); risolvendo il sistema fra le equazioni parametriche di r e s si ottiene k=-4, t=0, verificato in tutte e tre le equazioni, con punto di intersezione P(-3;2;-7): tutto coincidente con la traccia.
- Aggiunta: nessuna.

## Unità 24 — Posizione reciproca di retta e piano
- Parole: 314 su 2 pagine di traccia (105–106)
- Rettifica: nessuna. Verificato con SymPy: per il piano x-3y-z+2=0 il vettore normale è (1;-3;-1); la retta per A(4;1;0) con v=(1;-3;-1) dà le parametriche x=4+k, y=1-3k, z=-k, coincidenti con la traccia (verificato anche che A si ottiene per k=0).
- Aggiunta: nessuna.

## Unità 25 — Distanza punto-retta e distanza fra rette sghembe
- Parole: 460 su 3 pagine di traccia (107–109)
- Rettifica: nessuna. Verificato con SymPy: il piano per P(9;-3;0) normale a v(-1;4;2) dà -x+4y+2z+21=0; sostituendo le parametriche di r si ottiene 21k+21=0, k=-1, H(3;-4;-1), con PH=√38, coincidente con la traccia. Per le rette sghembe, riscritte r: x=1,y=k,z=2-k e s: x=4+2t,y=t,z=-1, il sistema di perpendicolarità RS·vr=0, RS·vs=0 dà t-2k+3=0 e 5t-k+6=0, con soluzione k=1, t=-1, R(1;1;1), S(2;-1;-1), RS=3: tutto coincidente. Confermato anche con il metodo alternativo del prodotto misto (vr×vs, distanza=9/3=3) che le due rette non si intersecano e la distanza è corretta.
- Aggiunta: nessuna. Un solo disegno statico (punto, retta, piede della perpendicolare) illustra il concetto di distanza già descritto nel primo esempio; nessun quesito di maturità inserito, in continuità con le unità 17-24 di quest'area, perché entrambi gli esempi della traccia coprono già in modo completo il metodo.
