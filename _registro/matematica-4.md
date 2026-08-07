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
