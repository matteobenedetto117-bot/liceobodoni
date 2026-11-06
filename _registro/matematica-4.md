# Registro — Matematica quarta

## Unità 01 — Equazioni goniometriche elementari
- Parole: 631 su 6 pagine di traccia
- Rettifica: nessuna, i calcoli (sin x=√3/2, cos x=-1/2, tan x=√3/3) sono stati verificati con SymPy e coincidono con la traccia.
- Aggiunta: nessuna.
- Revisione (04/11/2026, regole 13/10): parole circa 516 → 140 (formule $$ e didascalie escluse). Pagina mai revisionata: impaginazione a quaderno, tolti sommario, titoletto «Che cos'è un'equazione goniometrica», prosa ripetuta e nota sulla tangente (ridotta a voce d'elenco); definizione ed esempi/controesempi in elenco, tre forme elementari in .eq, casi in forma caso → conseguenza, soluzione generale di sin e cos in .def con le condizioni −1 ≤ a ≤ 1, −1 ≤ b ≤ 1; titoletti brevi $\sin x=a$, $\cos x=b$, $\tan x=c$, «Angoli con lo stesso seno». Nessuna comparsa da togliere. Correzioni: la figura della tangente mostrava l'angolo π/4 (punto e retta a 45°) invece di π/6; per sin x = 0 la frase «la retta tocca la circonferenza in un solo punto» era errata (due punti, 0 e π): ora «basta una sola famiglia di soluzioni». Calcoli verificati con SymPy. Figure rifatte da script: circonferenza con cursore a in [−1,3; 1,3] (punti x₁, x₂, valori in rad, «impossibile» per |a| > 1), tre casi particolari, cos x = −1/2, tan x = √3/3 con i due punti opposti. Nessun esempio tolto (i tre casi svolti sono legati alle figure), nessuna figura decorativa.

## Unità 02 — Angoli associati ed equazioni riconducibili a elementari
- Parole: 335 (prosa, formule escluse) su 5 pagine di traccia
- Rettifica: nessuna, tutti i passaggi (i due esempi su seno e coseno con angoli associati, l'esempio con tangente, l'esempio 2sin²x+5cosx-4=0) sono stati verificati con SymPy e coincidono con la traccia.
- Aggiunta: nessuna.
- Revisione (04/11/2026, regole 13/10): parole circa 283 → 137 (formule $$ e didascalie escluse). Pagina mai revisionata: impaginazione a quaderno, tolti sommario, rimando «la regola era», titoletti «Stesso seno», «Stesso coseno», «Stessa tangente» (le tre regole ora in elenco e in un unico .def «Angoli associati», con le condizioni di esistenza della tangente); tenuti «Funzioni diverse ai due membri», «Equazioni riconducibili a elementari», «Esempio 1», «Esempio 2»; procedimento in tre voci brevi. Esempi tolti (regola dei due esempi): cos(3π/4 − 4x) = cos(2x − π/3) → x = 13π/72 − kπ/3 ∨ x = 5π/24 − kπ, e tan x = tan(2x + π/4) → x = −π/4 − kπ. Nessuna comparsa da togliere. Correzione: nella figura il pannello destro mostrava angoli di circa 147° e 55°, non supplementari (seni diversi); ridisegnata da script con α' = 43°, 147° e α = π − α' (stessa altezza, segmento tratteggiato). Calcoli e identità verificati con SymPy. Nessuna figura decorativa.

## Unità 03 — Equazioni lineari in seno e coseno
- Parole: 543 (prosa e formule) su 7 pagine di traccia
- Rettifica: nessuna. Tutti i passaggi sono stati verificati con SymPy: la soluzione tanx=√3 di sinx-√3cosx=0; la sostituzione parametrica di sinx+cosx-1=0 (t=0∨t=1, x=2kπ∨x=π/2+2kπ); il sistema retta-circonferenza di √3sinx+cosx=2 (Δ=0, sinx=√3/2, cosx=1/2); il metodo dell'angolo aggiunto su sinx-√3cosx+1=0 (r=2, α=-π/3, x=3π/2+2kπ∨x=13π/6+2kπ). Tutto coincide con la traccia.
- Aggiunta: nessuna.
- Revisione (04/11/2026, regole 13/10): parole circa 378 → 140 (formule $$ e didascalie escluse; sommario incluso prima). Pagina mai revisionata: impaginazione a quaderno, tolti sommario e prosa; definizione in .def con la condizione a = 0 o b = 0; caso c = 0 in elenco caso → conseguenza; formule parametriche con la condizione x ≠ π + 2kπ in elenco e nota sull'errore tipico; metodo grafico con sistema e casi secante/tangente/esterna in elenco; angolo aggiunto in .def. Titoletti: «Caso c = 0», «Formule parametriche (c ≠ 0)», «Metodo grafico», «Angolo aggiunto», «Esempio 1», «Esempio 2». Esempi: tenuti sin x + cos x − 1 = 0 (parametriche) e sin x − √3 cos x + 1 = 0 (angolo aggiunto); l'esempio sin x − √3 cos x = 0 è ridotto alla didascalia della sua figura; tolto l'esempio grafico √3 sin x + cos x = 2 (Δ = 0, x = π/3 + 2kπ). Nessuna comparsa da togliere. Correzioni: cos x = 0 per x = π/2 + kπ (non + 2kπ), con a·(±1) = 0; angolo aggiunto definito da cos α = a/r, sin α = b/r (tan α = b/a da sola non individua il quadrante); figure: retta per l'origine a π/4 invece di π/3, punti della retta del metodo grafico non sulla circonferenza, raggi a 7π/6 e 11π/6 errati (lunghezza e angolo) e retta y = −1/2 disegnata sull'asse x. Calcoli verificati con SymPy. Figure rifatte da script (statiche): tan x = √3, retta X + Y − 1 = 0 dell'esempio 1, sin(x − π/3) = −1/2. Nessuna figura decorativa.

## Unità 04 — Funzioni goniometriche inverse
- Parole: 354 (prosa e formule) su circa 2,5 pagine di traccia (pagina 19 condivisa con la fine dell'unità 03)
- Rettifica: nessuna. Le uniche informazioni numeriche sono i domini e i codomini di seno, coseno, tangente ristretti e delle loro inverse, e i nove valori usati nello strumento interattivo (sin di -π/2,-π/3,-π/4,-π/6,0,π/6,π/4,π/3,π/2 e il loro ritorno con arcoseno): tutti verificati con SymPy e coincidono con la traccia.
- Aggiunta: nessuna. Lo strumento interattivo (il punto (x,sin x) che si scambia in (sin x,x)) visualizza esattamente il passaggio "inverto x e y" già scritto nella traccia, non introduce un contenuto nuovo.
- Revisione (04/11/2026, regole 13/10): parole circa 331 → 73 (formule $$ e didascalie escluse; sommario incluso prima). Pagina mai revisionata: impaginazione a quaderno, tolti sommario, titoletto «Perché restringere il dominio» (ridotto a tre voci d'elenco) e prosa; per ciascuna funzione restrizione in .eq e inversa in .def con dominio e codominio; nota sull'errore tipico in una frase; tenuti i titoletti «Arcoseno», «Arcocoseno», «Arcotangente». Nessuna comparsa da togliere, nessun esempio. Nessuna correzione concettuale (domini, codomini e i nove valori del cursore verificati con Python). Figure: grafici Plotly riscritti in SVG da script (tre coppie funzione ristretta/inversa, asintoti in rosso tratteggiato); strumento interattivo (x, sin x) → (sin x, x) rifatto con cursore su nove angoli e valori a fianco. Nessuna figura decorativa.

## Unità 05 — Equazioni omogenee di secondo grado in seno e coseno
- Parole: 396 su 4 pagine di traccia
- Rettifica: nessuna. Tutti i passaggi sono stati verificati con SymPy: le soluzioni di cosx sinx-√3sin²x=0 (x=kπ ∨ x=π/6+kπ, confermate anche per enumerazione in [0,2π)); il discriminante Δ=(1+√3)²-4√3=4-2√3=(1-√3)² dell'equazione tan²x-(1+√3)tanx+√3=0 con radici tanx=1 e tanx=√3; le tre formule di duplicazione finali (sin²x, cos²x, sinx cosx in funzione di 2x). Tutto coincide con la traccia.
- Aggiunta: nessuna. Il riquadro "errore tipico" riprende il controllo che la traccia stessa mostra passo per passo (verifica che x=π/2+kπ non sia soluzione, prima di dividere per cosx o per cos²x); non introduce un contenuto nuovo.
- Revisione (04/11/2026, regole 13/10): parole circa 293 → 121 (formule $$ e didascalie escluse; sommario incluso prima). Pagina mai revisionata: impaginazione a quaderno, tolti sommario e prosa; definizione in .def, casi a = 0 e c = 0 in elenco caso → conseguenza con i due raccoglimenti in .eq, condizione x = π/2 + kπ (non soluzione se a ≠ 0) in elenco, nota sull'errore tipico in una frase; titoletti «Un coefficiente nullo», «Nessun coefficiente nullo», «Formule di duplicazione» (accorciati), «Esempio 1», «Esempio 2». Tolto il rimando all'unità precedente. Nessuna comparsa da togliere, nessun esempio tolto, nessuna figura. Nessuna correzione concettuale (soluzioni, Δ = (1 − √3)² e formule di duplicazione verificati con SymPy).

## Unità 06 — Disequazioni goniometriche elementari
- Parole: 541 (prosa e formule, SVG esclusi) su 6 pagine di traccia (26–31)
- Rettifica: nessuna. Tutte le soluzioni sono state verificate per enumerazione numerica (oltre che a mano) con Python: l'esempio guida sinx<1/2; i quattro esempi elementari (2sinx-√3>0, 2cosx+1≤0, tanx>1, sin(x-π/6)≥0); i quattro esempi non elementari (√2sin²x-sinx≥0, 4cos²x-4cosx-3≤0 con Δ=64 e radici cosx=3/2 impossibile ∨ cosx=-1/2, il sistema -√3/2<cosx<1/2, 3tan²x+√3tanx≥0 con radici tanx=0 ∨ tanx=-√3/3 ed esclusione x≠π/2+kπ). Tutto coincide con la traccia.
- Aggiunta: nessuna. Lo strumento interattivo (cursore sulla soglia a in sinx<a, con l'arco soluzione ridisegnato) rende dinamico solo l'esempio guida già svolto nella traccia (sinx<1/2); non introduce contenuto nuovo. Il riquadro "un modo più compatto" riprende la nota finale della traccia (pagina 32) sul riscrivere con periodo π invece di 2π.
- Revisione (04/11/2026, regole 13/10): parole circa 470 → 136 (formule $$ e didascalie escluse; sommario incluso prima). Pagina mai revisionata: impaginazione a quaderno, tolti sommario, prosa, riquadri .esempio e nota «Un modo più compatto» (ridotta a «periodo π → +kπ» nell'esempio della tangente); forme elementari in .def, due metodi in elenco, procedimento in quattro voci numerate, metodi per le non elementari in elenco. Titoletti: «Metodo della circonferenza», «Esempio 1», «Disequazioni non elementari», «Esempio 2». Esempi tenuti: tan x > 1 e 4cos²x − 4cos x − 3 ≤ 0. Esempi tolti (regola dei due esempi): 2sin x − √3 > 0 → π/3 + 2kπ < x < 2π/3 + 2kπ; 2cos x + 1 ≤ 0 → 2π/3 + 2kπ ≤ x ≤ 4π/3 + 2kπ; sin(x − π/6) ≥ 0 → π/6 + 2kπ ≤ x ≤ 7π/6 + 2kπ; √2sin²x − sin x ≥ 0 → π/4 + 2kπ ≤ x ≤ 3π/4 + 2kπ ∨ π + 2kπ ≤ x ≤ 2π + 2kπ; −√3/2 < cos x < 1/2 → π/3 + 2kπ < x < 5π/6 + 2kπ ∨ 7π/6 + 2kπ < x < 5π/3 + 2kπ; 3tan²x + √3tan x ≥ 0 → kπ ≤ x ≤ 5π/6 + kπ, x ≠ π/2 + kπ (con le loro figure). Nessuna comparsa da togliere. Nessuna correzione concettuale (soluzioni verificate per enumerazione numerica con Python); «parabola positiva verso l'alto» → «valori compresi fra le radici». Figure rifatte da script: circonferenza con cursore su a in [−0,9; 0,9] (retta Y = a, estremi vuoti, arco rosso, x₁ e x₂ ordinati in [0, 2π)), tan x > 1 con retta a π/4 ed estremi π/2, 3π/2 esclusi, cos x ≥ −1/2 con retta X = −1/2. Nessuna figura decorativa.

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
- Revisione (04/11/2026, regole 13/10): parole circa 261 → 96 (formule $$ e didascalie escluse; sommario incluso prima). Pagina mai revisionata: impaginazione a quaderno, tolti sommario e prosa; procedimento delle fratte in quattro voci, metodo dei sistemi in tre voci, soluzioni delle singole disequazioni in elenco caso → conseguenza, formule in .eq. Titoletti: «Disequazioni fratte», «Esempio 1», «Sistemi di disequazioni», «Esempio 2». Esempi tenuti: tan x ≥ 1/(2cos x) e il sistema 4sin²x − 3 ≥ 0 ∧ tan x ≥ 1. Esempio tolto (regola dei due esempi): sistema cos x > 0 ∧ cot²x − 3 ≥ 0 ∧ 2sin x − 1 ≤ 0 → −π/6 + 2kπ ≤ x ≤ π/6 + 2kπ, x ≠ 2kπ (con le sue figure). Nessuna comparsa da togliere. Nessuna correzione concettuale (soluzioni verificate per enumerazione numerica con Python). Figure rifatte da script in due figure a tre pannelli: N ≥ 0, D > 0 e segno del quoziente; le due soluzioni del sistema e l'intersezione su archi concentrici, ora con entrambi i rami di periodo π (prima solo quello del primo quadrante). Nessuna figura decorativa.

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
- Revisione (04/11/2026, regole 13/10): parole circa 218 → 105 (formule $$ e didascalie escluse; sommario incluso prima). Pagina mai revisionata: impaginazione a quaderno, tolti sommario, titoletto «Notazione» (ridotto a tre voci d'elenco) e prosa; enunciati dei teoremi in una riga di raccordo + .def; risoluzione in elenco con la condizione «due dati, di cui almeno un lato»; esempi in forma Dati/Calcolare con una .eq. Titoletti: «Primo teorema», «Secondo teorema», «Risoluzione», «Esempio 1», «Esempio 2». Esempi tenuti: 1 (a = 40, b = 110 → α ≈ 20,0°, β ≈ 70,0°, c ≈ 117) e 4 (c = 28,3, α = 58° → β = 32°, a ≈ 24,0, b ≈ 15,0). Esempi tolti: 2 (a = 21,13, c = 50 → α ≈ 25,0°, β ≈ 65,0°, b ≈ 45,3) e 3 (a = 8, α = 28° → β = 62°, b ≈ 15,0, c ≈ 17,0). Nessuna comparsa da togliere. Correzione concettuale: nel disegno del secondo teorema a destra (b = a cot α) l'arco segnato α era quello fra asse y e ipotenusa, cioè β; ora α è misurato dall'asse x (e ripetuto al vertice alto, angoli alterni), coerente con b = a cot α (verificato: 110·cot(arctan(110/60)) = 60). Figure rifatte da script: notazione; primo teorema con cursore su α (20°–70°) e valori di sin α, cos α a fianco; secondo teorema in due pannelli; triangoli degli esempi in proporzione coi dati (prima tutti uguali). Nessuna figura decorativa.

## Unità 09 — Area di un triangolo e teorema della corda
- Parole: 331 su 2 pagine di traccia (41–42)
- Rettifica: nella dimostrazione del teorema della corda, l'angolo retto è in A (D̂AB, angolo alla base sul diametro DB, per il teorema di Talete), non in D come una prima lettura della traccia lasciava intendere: verificato numericamente piazzando i quattro punti su una circonferenza di prova (coordinate polari) e calcolando gli angoli con il prodotto scalare. Con l'angolo retto in D il calcolo non tornava; con l'angolo retto in A, DB=2r come ipotenusa e α come angolo in D, si ottiene esattamente AB=DB sinα=2r sinα, coerente con la formula finale della traccia. Verificata anche l'identità sin(180°-α)=sinα usata per l'altezza nel caso ottuso della formula dell'area (SymPy, semplificazione simbolica a zero).
- Aggiunta: nessuna. Le due figure per il caso acuto e ottuso dell'altezza ridisegnano le due costruzioni della traccia a pagina 41; le due figure del teorema della corda ridisegnano quelle di pagina 42.
- Revisione (04/11/2026, regole 13/10): parole circa 209 → 112 (formule $$ e didascalie escluse; sommario incluso prima). Pagina mai revisionata: impaginazione a quaderno, tolti sommario e prosa; altezza CH in tre voci caso → conseguenza (aggiunto il caso α retto, H = A), formule dell'area in .def; dimostrazione del teorema della corda in quattro voci d'elenco. Titoletti: «Area di un triangolo», «Teorema della corda». Nessuna comparsa da togliere, nessun esempio. Precisazione aggiunta (verificata numericamente): con C sull'arco minore l'angolo è 180° − α, stesso seno, la formula vale per ogni C. Correzioni ai disegni: nelle vecchie figure della corda i punti B, C e D non stavano sulla circonferenza. Figure rifatte da script: notazione; altezza nei casi acuto e ottuso (con 180° − α); corda AB con cursore su C lungo l'arco maggiore (angolo in C calcolato, sempre 50°); costruzione della dimostrazione con il diametro BD e l'angolo retto in A. Nessuna figura decorativa.

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
- Revisione (04/11/2026, regole 13/10): parole circa 409 → 103 (formule $$ e didascalie escluse; sommario incluso prima). Pagina mai revisionata: impaginazione a quaderno, tolti sommario, titoletto «Raggio della circonferenza circoscritta», prosa, dimostrazione ripetuta e riquadro verde duplicato; teorema dei seni in .def con il rapporto 2r e la formula r = a/(2 sin α). Titoletti: «Esempio 1», «Esempio 2». Esempi tenuti: α = 30°, β = 105°, a = 6 → γ = 45°, c = 6√2 ≈ 8,49; distanza Terra–Luna (angoli 80°, 99°, 1° in elenco) → d ≈ 3,6·10⁵ km (prima «≈ 360 000 km»; calcolo 360 952 km). Esempio tolto: parallasse trigonometrica con la sua figura (angolo 1″, r = 1,50·10⁸ km → D ≈ 3,09·10¹³ km ≈ 3,27 a.l. = 1 parsec). Nessuna correzione concettuale (verifica numerica). Figure rifatte da script: triangolo inscritto con cursore sul vertice A e i tre rapporti lato/seno calcolati (sempre 2,00 con r = 1); schema Terra–Luna in un solo pannello (il secondo ripeteva lo stesso triangolo), angolo di 80° in scala, distanze non in scala (dichiarato in didascalia).

## Unità 11 — Teorema del coseno
- Parole: 332 su 3 pagine di traccia (47–49)
- Rettifica: nessuna. Verificato con SymPy che la dimostrazione (CH=b sinα, AH=b cosα, HB=c−b cosα, Pitagora nel triangolo CHB) si riduce identicamente a a²=b²+c²−2bc cosα. Verificati con Python tutti i risultati numerici della traccia: Esempio 1 (c²=7, c=√7); Esempio 2 (γ=80°, a≈7,83, b≈10,55); Esempio 3 (a≈24,50, cosβ≈0,77, β≈40°, γ≈120°). Tutto coincide con la traccia.
- Aggiunta: nessuna. Il riquadro finale "seni o coseno" riprende la nota conclusiva della traccia a pagina 49 ("per cercare lati → seni, per cercare angoli → coseno, il coseno non ha ambiguità sugli angoli, li individua univocamente"), riformulata in una frase.
- Revisione (04/11/2026, regole 13/10): parole circa 300 → 118 (formule $$ e didascalie escluse; sommario incluso prima). Pagina mai revisionata: impaginazione a quaderno, tolti sommario, titoletti «Enunciato» ed «Esempi», enunciato a parole (resta la formula in .def), prosa e riquadri .esempio; caso α = 90° (Pitagora) in una frase; dimostrazione in tre voci d'elenco + una .eq (condizione «H fra A e B» mantenuta); nota «Seni o coseno» ridotta a una frase. Titoletti: «Dimostrazione», «Esempio 1», «Esempio 2». Esempi tenuti: a = 3, b = 2, γ = 60° → c = √7; b = 46, c = 62, α = 20° → a ≈ 24,50, β ≈ 40°, γ ≈ 120°. Esempio tolto (regola dei due esempi; usava solo il teorema dei seni): c = 12, α = 40°, β = 60° → γ = 80°, a ≈ 7,83, b ≈ 10,55. Nessuna comparsa da togliere. Nessuna correzione concettuale (dimostrazione verificata con SymPy, risultati con Python). Figure rifatte da script: triangolo con b = 4, c = 5 e cursore su α (30°–140°), cos α e a calcolati a fianco, «Pitagora» in verde a 90°; altezza CH con AH = b cos α e HB = c − b cos α. Nessuna figura decorativa.

## Unità 12 — Risoluzione dei triangoli e caso ambiguo
- Parole: 398 su 3 pagine di traccia (50–52)
- Rettifica: nessuna. Verificato con Python/SymPy: Esempio 4 (c=56,2, a=39, γ=59°) dà sinα=0,5948≈0,59, α=arcsin(0,59)≈36,50°≈36° (soluzione acuta accettata perché γ<90° e c>a); Esempio 5 (a=58,6, b=77, c=70) dà cosβ≈0,2931 → β≈72,95°≈73°, cosα≈0,6860 → α≈46,69°≈47°, γ=180°-α-β≈60,36°≈60°. Tutto coincide con la traccia. Verificata anche la logica geometrica dello schema dei casi (intersezioni di un cerchio di raggio a con la semiretta base) per ricontrollare i confini fra 0, 1 e 2 soluzioni al variare di a rispetto ad altezza b·sinα e al lato b.
- Aggiunta: nessuna. Lo strumento interattivo (cursore sul lato a) rende dinamico esattamente lo schema dei casi già enumerato nella traccia a pagina 50-51 (le due figure con β₁ e β₂ accettabili/non accettabili); non introduce un criterio nuovo, solo la stessa condizione geometrica resa manovrabile.
- Revisione (04/11/2026, regole 13/10): parole circa 372 → 127 (formule $$ e didascalie escluse; sommario incluso prima). Pagina mai revisionata: impaginazione a quaderno, tolti sommario, titoletto «Il caso ambiguo» (ripeteva il titolo), «Esempi», prosa e riquadri .esempio; sin β = (b/a) sin α in .eq; casi in elenco caso → conseguenza; esempi rinumerati (4 → 1, 5 → 2) in forma Dati/Calcolare. Nessuna comparsa da togliere, nessun esempio tolto. Correzione concettuale: per α ≥ 90° il testo diceva «resta solo β₁»; vale solo se b < a, con b ≥ a non c'è soluzione (es. α = 120°, a = 5, b = 5,5: sin β ≈ 0,95, β₁ ≈ 72°, α + β₁ > 180°); tolta la clausola vaga «a meno che non ne escluda una qualche altra informazione». Schema dei casi verificato con Python su 200 000 terne casuali. Esempi verificati (sin α ≈ 0,5948, α ≈ 36,5°; con 0,59 della traccia ≈ 36°, lasciato; β ≈ 72,95°, α ≈ 46,69°, γ ≈ 60,36°). Figura interattiva rifatta da script con le variabili di colore (prima colori fissi): b = 6, α = 35°, cursore su a (1,5–8), cerchio di raggio a ritagliato nel riquadro, B₁ blu, B₂ rosso tratteggiato, numero di soluzioni e angoli a fianco («due soluzioni» in verde); scala ridotta perché B restasse nel riquadro fino ad a = 8. Nessuna figura decorativa.

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
- Revisione (04/11/2026, regole 13/10): parole circa 451 → 131 (formule $$ e didascalie escluse; sommario incluso prima). Pagina mai revisionata: impaginazione a quaderno, tolti sommario, prosa e riquadro .esempio; titoletti ridotti a «Traslazioni», «Dilatazioni e contrazioni», «Esempio» (tolti i quattro titoletti per singola trasformazione); trasformazioni in elenco caso → conseguenza, periodo T = 2π/k in .eq, forma generale y = A sin(k(x−c)) + d in .eq; due note ridotte a una frase. Esempio: y = sin(2x+π)+1 → T = π, sfasamento x = −π/2, d = +1, in forma Dati/Calcolare. Nessuna comparsa da togliere, nessun esempio tolto. Precisazioni: aggiunte le ipotesi k > 0 e A > 0 (il periodo 2π/k e l'ampiezza A valgono così); verificato con SymPy: sin(2x+π)+1 = 1 − sin 2x, periodi π e 4π, cot(x+π/2) = −tan x. Figure rifatte da script (prima tracciati fissi con colori in esadecimale): cinque figure statiche come prima (pannelli affiancati per traslazioni orizzontali, verticali, periodo; ampiezza; esempio), legende spostate nelle didascalie, asintoti tratteggiati per tangente e cotangente; grafici a partire da x = 0 (salvo tangente e cotangente) perché le etichette dell'asse y non si sovrapponessero alle curve; strumento con quattro cursori (A, k, c, d) ridisegnato nello stile a quaderno, periodo 2π/k a fianco. Nessuna figura decorativa.

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
- Revisione (04/11/2026, regole 13/10): parole circa 232 → 76 (formule $$ e didascalie escluse; sommario incluso prima). Pagina mai revisionata: impaginazione a quaderno, tolti sommario, titoletti «Simmetria rispetto all'asse y», «Simmetria rispetto all'asse x» (le tre simmetrie ora in un elenco caso → conseguenza), prosa; titoletto «Funzione inversa» tenuto (argomento distinto); definizione del grafico dell'inversa in .def con la condizione di biunivocità; restrizioni sin → arcsin e x² → √x in elenco; nota ridotta a una frase. Nessuna comparsa da togliere, nessun esempio presente. Nessuna correzione concettuale (verificato con SymPy sin(−x) = −sin x, tan(−x) = −tan x, arcsin(sin 0,7) = 0,7, √(1,3²) = 1,3). Figure rifatte da script (prima tracciati fissi): seno e tangente con le simmetriche rispetto all'asse y (curve simmetriche rosse tratteggiate, asintoti grigi), coseno e −cos x, seno ristretto/arcoseno e parabola ristretta/radice con bisettrice tratteggiata e croci sul ramo escluso; legende nelle didascalie. Pagina sotto le 100 parole: contenuto tutto in elenchi e figure, nulla da aggiungere. Nessuna figura decorativa.

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
- Revisione (04/11/2026, regole 13/10): parole circa 454 → 106 (formule $$ e didascalie escluse; sommario incluso prima). Pagina mai revisionata: impaginazione a quaderno, tolti sommario, prosa e titoletti «Il valore assoluto attorno a tutta la funzione», «Il valore assoluto dentro l'argomento»; |f(x)| e f(|x|) in elenco caso → conseguenza; titoletto «Ordine delle trasformazioni» tenuto (argomento distinto) con i due casi in elenco; le due costruzioni per casi diventano «Esempio 1» (sin(|x|−π)) ed «Esempio 2» (cos(|x|+π/2)), sistemi in .eq; osservazione finale ridotta all'identità sin(t−π) = cos(t+π/2) = −sin t; nota ridotta a una frase. Nessuna comparsa da togliere, nessun esempio tolto. Nessuna correzione concettuale (verificato con SymPy: sin(t−π) = cos(t+π/2) = −sin t, cos(−x+π/2) = cos(x−π/2), cos x + 1/2 < 0 per x ∈ (2π/3, 4π/3)). Figure rifatte da script (prima SVG fissi e widget Plotly): |cos x|, sin|x|, due pannelli per l'ordine delle trasformazioni, esempio 1 con cursore su x che muove il punto sulla curva già disegnata e indica il ramo attivo e il valore; legende nelle didascalie. Nessuna figura decorativa.

## Unità 16 — Trasformazioni di retta, parabola, esponenziale e logaritmo
- Parole: 809 su 3 pagine di traccia (61–63)
- Rettifica: nessuna in senso stretto. Per non appesantire le figure ho unificato due coppie di curve che nella traccia illustrano la stessa trasformazione già mostrata altrove nella stessa unità (la parabola intermedia (x+3)² a pagina 61, assorbita nel disegno finale (x+3)²+2; e (x+2)² a pagina 62, ridondante con la traslazione orizzontale già vista in (x+3)²+2): nessun contenuto è stato tolto, solo una ripetizione grafica dello stesso tipo di spostamento. Verificato con SymPy: (-x+2)²≡(x-2)² (semplificazione scritta anche nella traccia); lo zero di e^x-3 in x=ln3≈1,0986; il minimo ln2 di ln(|x|+2) in x=0; il punto d'incontro (0,4) dei due rami di (|x|+2)².
- Aggiunta: nessuna.
- Revisione (04/11/2026, regole 13/10): parole circa 456 → 197 (formule $$ e didascalie escluse; sommario incluso prima). Pagina mai revisionata: impaginazione a quaderno, tolti sommario e prosa; titoletti «Retta», «Parabola», «Esponenziale», «Logaritmo» tenuti (quattro funzioni distinte, nome al singolare per «Esponenziali»/«Logaritmi»); ogni trasformazione in elenco caso → conseguenza, costruzione per casi di (|x|+2)² in .eq; frase d'apertura unica. Nessuna comparsa da togliere, nessun esempio presente. Nessuna correzione concettuale; precisati i valori già impliciti nella traccia: radici 3 ± √2 di (x−3)²−2, vertice (−3;2) di (x+3)²+2 (verificato con SymPy, insieme a ln3 ≈ 1,10, ln2, (−x+2)² = (x−2)²). Figure rifatte da script (prima SVG fissi e widget Plotly), stesse nove figure: retta (traslazione/dilatazione; |x−2| e |x|−2), parabola (tre trasformazioni; |(x−3)²−2|; (|x|+2)² per casi), esponenziale (simmetrie ed e^|x| in due pannelli; e^|x−a| con cursore su a; |e^x−3| con asintoti y = ±3 tratteggiati), logaritmo (simmetrie e traslazioni in due pannelli con asintoto x = 1; ln|x|, ln(|x|+2), |ln|x|| in tre pannelli); legende nelle didascalie. Pagina vicina al limite (197 parole) per i quattro argomenti distinti. Nessuna figura decorativa.

## Unità 17 — Piano cartesiano nello spazio: distanze, punto medio, baricentro
- Parole: 269 su circa 1,3 pagine di traccia (86–87, pagina condivisa con l'inizio dell'unità 18)
- Rettifica: nessuna. Le formule di distanza, punto medio e baricentro (estensione diretta delle formule 2D con l'aggiunta della quota) sono state verificate con SymPy; l'esempio numerico è stato ricalcolato con SymPy: A(1;2;2), B(4;6;2), C(7;4;5) danno AB=5, M=(2,5;4;2), G=(4;4;3), coincide con quanto scritto in pagina.
- Aggiunta: un esempio numerico (distanza, punto medio, baricentro sugli stessi tre punti), perché la traccia in queste due pagine non contiene alcun esempio numerico, solo le formule.
- Revisione (04/11/2026, regole 13/10): parole circa 173 → 78 (formule $$ e didascalie escluse; sommario incluso prima). Pagina mai revisionata: impaginazione a quaderno, tolti sommario, prosa e titoletti «Il punto nello spazio», «Distanza tra due punti», «Punto medio di un segmento», «Baricentro di un triangolo» (formule in tre .def etichettati); tolta la formula della distanza nel piano (ripetizione); ascissa, ordinata, quota in elenco; esempio con «Dati: … Calcolare …» e tre .eq. Nessuna comparsa da togliere, nessun esempio tolto. Nessuna correzione concettuale (ricalcolati AB = 5, M = (2,5; 4; 2), G = (4; 4; 3)). Figura rifatta da script (prima SVG fisso, con la proiezione sull'asse z non coerente con la prospettiva): punto P(3; 4; 3) in proiezione obliqua calcolata, parallelepipedo delle coordinate tratteggiato. Nessuna figura decorativa.

## Unità 18 — Vettori nello spazio e prodotto scalare
- Parole: 348 su circa 1,5 pagine di traccia reale (87–88, la seconda metà di pagina 87 dopo il baricentro dell'unità 17, fino a prima dell'equazione del piano che apre l'unità 19)
- Rettifica: nessuna. Verificato con SymPy: dati u(2;1;-2) e v(1;-2;0), u+v=(3;-1;-2), |u|=3, u·v=0 (perpendicolari), coincide con quanto riportato in pagina.
- Aggiunta: un esempio numerico (somma, modulo, prodotto scalare e verifica di perpendicolarità), perché la traccia in queste pagine definisce le operazioni ma non le applica a numeri.
- Revisione (04/11/2026, regole 13/10): parole circa 243 → 87 (formule $$ e didascalie escluse; sommario incluso prima). Pagina mai revisionata: impaginazione a quaderno, tolti sommario (con rimando all'unità successiva), prosa e titoletti «Componenti e modulo», «Vettore individuato da due punti»; modulo e somma in una .eq, vettore AB con |AB| = AB in una .eq; titoletto «Prodotto scalare» tenuto; condizione di perpendicolarità in .def con l'ipotesi «vettori non nulli»; esempio con «Dati: … Calcolare …» e due .eq. Nessuna comparsa da togliere, nessun esempio tolto. Nessuna correzione concettuale (ricalcolati u+v = (3; −1; −2), |u| = 3, u·v = 0). Figura rifatta da script (prima SVG fisso con le componenti tracciate a occhio): versori i, j, k e vettore a = (2; 4; 3) con le componenti tratteggiate, proiezione obliqua calcolata. Nessuna figura decorativa.

## Unità 19 — Il piano: equazione generale e casi particolari
- Parole: 506 su circa 3 pagine di traccia (seconda metà di pagina 88, pagine 89–90, prima metà di pagina 91)
- Rettifica: nessuna. Verificato con SymPy: il piano per P0(2;-3;1) normale a n(4;1;-1) dà 4x+y-z-4=0; il sistema per il piano passante per A(2;0;0), B(0;1;0), C(0;0;3) dà a=-d/2, b=-d, c=-d/3 e, con d=-6, 3x+6y+2z-6=0 — entrambi coincidono esattamente con quanto scritto in pagina.
- Aggiunta: nessuna. Lo strumento interattivo (superficie 3D con cursori su a, b, d) rende dinamica esattamente la classificazione dei casi particolari già scritta nella traccia (piano parallelo a un asse quando manca una variabile, piano per l'origine quando d=0); non introduce un esempio o un caso nuovo.
- Revisione (04/11/2026, regole 13/10): parole circa 338 → 139 (formule $$ e didascalie escluse; sommario incluso prima). Pagina mai revisionata: impaginazione a quaderno, tolti sommario, prosa, riquadri .esempio e titoletto «Equazione generale del piano»; definizione in una frase, equazione generale in .def con «a, b, c non tutti nulli»; casi particolari in elenco caso → conseguenza (esempio del caso con una variabile mancante allineato ai pannelli: c = 0); titoletti «Casi particolari», «Piano per tre punti», «Esempio 1», «Esempio 2». Nessuna comparsa da togliere, nessun esempio tolto. Correzione: nel vecchio pannello «c = 0» il vettore normale era disegnato quasi parallelo alla traccia del piano; ora è perpendicolare (traccia di 2x + y − 4 = 0, normale (2; 1)). Ricalcolati con SymPy 4x + y − z − 4 = 0 e 3x + 6y + 2z − 6 = 0 (A, B, C verificati). Figure rifatte da script: piano con P₀, n e P in proiezione obliqua; tre pannelli calcolati; figura interattiva Plotly riscritta in SVG (cursori su a, b, d, tratto di piano calcolato, asse z in scala ridotta, scritta verde nei casi particolari). Nessuna figura decorativa.

## Unità 20 — Posizione reciproca di due piani e distanza punto-piano
- Parole: 401 su 2 pagine di traccia (92–93)
- Rettifica: nessuna. Verificato con Python/SymPy: il prodotto scalare dei normali dei piani 2x-y+2z+7=0 e 3x+2y-2z-1=0 dà 6-2-4=0, confermando la perpendicolarità; la distanza di P(0;1;-1) dal piano x-y+2z-1=0 dà |0-1-2-1|/√6 = 4/√6 = (2/3)√6, coincidente con la traccia. Nessun quesito di maturità inserito: le tracce reperite sulla distanza punto-piano richiedono anche la posizione piano-sfera, argomento non ancora disponibile a questo punto del percorso (unità 26-27).
- Aggiunta: nessuna.
- Revisione (04/11/2026, regole 13/10): parole circa 287 → 96 (formule $$ e didascalie escluse; sommario incluso prima; sotto le 100: contenuto in elenco e formule). Pagina mai revisionata: impaginazione a quaderno, tolti sommario, rimando all'unità precedente, prosa e riquadri .esempio; tre casi in elenco caso → conseguenza; perpendicolarità e distanza punto-piano in .def; titoletti «Piani perpendicolari», «Distanza punto-piano», «Esempio 1», «Esempio 2». Aggiunta l'ipotesi «rapporti con denominatore non nullo» per il confronto dei coefficienti. Nessuna comparsa da togliere, nessun esempio tolto. Nessuna correzione concettuale (ricalcolati 6 − 2 − 4 = 0 e D = 4/√6 = (2/3)√6 ≈ 1,63, aggiunto il valore approssimato). Figura rifatta da script: piani z = 0 e y = 0 con retta comune e normali in proiezione obliqua (prima SVG fisso con le normali entrambe verticali, non perpendicolari fra loro). Nessuna figura decorativa.

## Unità 21 — La retta nello spazio: equazioni parametriche e cartesiane
- Parole: 559 su 6 pagine di traccia (94–99)
- Rettifica: nessuna. Verificato con SymPy: l'equivalenza algebrica (x-6)/-2 = (6-x)/2 e (x-5)/(0-5) = (5-x)/5 usate nel passaggio a forma con denominatori positivi; la verifica del passaggio di B(0;1;-1) per la retta AB con A(5;0;1) dà 1=1=1; la condizione di allineamento per P(2;-3;2), A(1;0;3), B(-1;6;5) dà -1/2=-1/2=-1/2, tutto coincidente con la traccia. Nessun quesito di maturità inserito: è la prima unità sulla sola equazione della retta, senza ancora gli strumenti di posizione reciproca e distanza (unità 23–25) con cui i quesiti reali di questa area combinano piani, rette e sfere.
- Aggiunta: nessuna.
- Revisione (05/11/2026, regole 13/10): parole circa 447 → 149 (formule $$ e didascalie escluse; sommario incluso prima). Pagina mai revisionata: impaginazione a quaderno, tolti sommario, prosa, riquadri .esempio e i titoletti «Equazione parametrica», «Casi particolari», «Condizione di allineamento di tre punti»; definizione in una frase d'apertura, equazione parametrica, cartesiana e retta per due punti in .def; casi con componenti nulle in elenco caso → conseguenza; allineamento in una riga; nota sulla componente nulla in due frasi. Aggiunta l'ipotesi «denominatori non nulli» nella retta per due punti. Titoletti: «Equazione cartesiana», «Retta per due punti», «Esempio 1», «Esempio 2». Esempi tenuti: retta per A(5;0;1), B(0;1;−1) con verifica; allineamento di P(2;−3;2), A(1;0;3), B(−1;6;5). Esempi tolti (regola dei due esempi): parametrica per P(−1;2;4), v(2;−1;3) → x = −1 + 2k, y = 2 − k, z = 4 + 3k; cartesiana per P(6;−1;2), v(−2;1;7) → (6 − x)/2 = y + 1 = (z − 2)/7. Nessuna comparsa da togliere. Nessuna correzione concettuale (verificato con SymPy). Figura rifatta da script (proiezione obliqua): retta per P₀ con vettore v e cursore su k che muove P lungo la retta (verso concorde/opposto, P = P₀ per k = 0); valori P₀(1;1,4;1,4), v(−1;1;0,6) scelti per la figura. Nessuna figura decorativa.

## Unità 22 — Retta come intersezione di due piani
- Parole: 264 su 2 pagine di traccia (100–101)
- Rettifica: nessuna. Verificato con SymPy: dal sistema x+y-3z=0, x-3y+z+4=0 con z=k si ottiene x=2k-1, y=k+1, coincidente con la traccia; sostituendo k=z si torna a x-2z+1=0, y-z-1=0, anch'esso coincidente. Per l'esempio 6 (x-2y+z-1=0, 2x+y-z+1=0) i rapporti fra coefficienti 1/2, -2, -1 non sono uguali, confermando che i piani non sono paralleli.
- Aggiunta: nessuna.
- Revisione (05/11/2026, regole 13/10): parole circa 197 → 90 (formule $$ e didascalie escluse; sommario incluso prima; sotto le 100: contenuto in .def, elenco e formule). Pagina mai revisionata: impaginazione a quaderno, tolti sommario, prosa, riquadri .esempio e il titoletto «Il sistema di due piani»; sistema in .def con la condizione «a, b, c non proporzionali ad a′, b′, c′»; procedimento verso la forma parametrica e ritorno in tre voci d'elenco; esempi in forma Dati/Verificare-Scrivere con .eq. Titoletti: «Esempio 1», «Forma parametrica» (era «Dalla forma cartesiana alla forma parametrica»), «Esempio 2». Precisazione aggiunta (verificata con SymPy): z = k si può porre se ab′ − a′b ≠ 0, altrimenti si sceglie un'altra variabile. Nessun esempio tolto, nessuna comparsa da togliere, nessuna figura (nessuna presente prima). Nessuna correzione concettuale (soluzione x = 2k − 1, y = k + 1 verificata con SymPy).

## Unità 23 — Posizione reciproca di due rette
- Parole: 364 su 3 pagine di traccia (102–104)
- Rettifica: nessuna. Verificato con SymPy: per r con v(1;-1;3) e s con w(4;-2;-2), v·w=4+2-6=0 (perpendicolari) e 1/4≠-1/-2 (non parallele); risolvendo il sistema fra le equazioni parametriche di r e s si ottiene k=-4, t=0, verificato in tutte e tre le equazioni, con punto di intersezione P(-3;2;-7): tutto coincidente con la traccia.
- Aggiunta: nessuna.
- Revisione (05/11/2026, regole 13/10): parole circa 299 → 97 (formule $$ e didascalie escluse; sommario incluso prima; sotto le 100: contenuto in elenco, .def e formule). Pagina mai revisionata: impaginazione a quaderno, tolti sommario, prosa, riquadro .esempio e i titoletti «Rette parallele», «Rette incidenti o sghembe», «Rette perpendicolari»; i quattro casi (parallele/coincidenti, incidenti, sghembe) in elenco caso → conseguenza; parallelismo (con l′, m′, n′ ≠ 0) e perpendicolarità in .def; nota «perpendicolari non vuol dire incidenti» in due frasi; esempio in forma Dati/Studiare con due .eq. Titoletto: «Esempio». Nessun esempio tolto, nessuna comparsa da togliere, nessuna figura (nessuna presente prima). Nessuna correzione concettuale (verificato con SymPy: v·w = 0, k = −4, t = 0, P(−3;2;−7)).

## Unità 24 — Posizione reciproca di retta e piano
- Parole: 314 su 2 pagine di traccia (105–106)
- Rettifica: nessuna. Verificato con SymPy: per il piano x-3y-z+2=0 il vettore normale è (1;-3;-1); la retta per A(4;1;0) con v=(1;-3;-1) dà le parametriche x=4+k, y=1-3k, z=-k, coincidenti con la traccia (verificato anche che A si ottiene per k=0).
- Aggiunta: nessuna.
- Revisione (05/11/2026, regole 13/10): parole circa 201 → 86 (formule $$ e didascalie escluse; sommario incluso prima; sotto le 100: contenuto in elenco, .def e formule). Pagina mai revisionata: impaginazione a quaderno, tolti sommario, prosa, riquadro .esempio e il titoletto «Le tre posizioni possibili»; tre casi in elenco caso → conseguenza; parallelismo e perpendicolarità (con l, m, n ≠ 0) in .def; esempio in forma Dati/Scrivere con una .eq. Titoletto: «Esempio». Correzione: n·v = 0 indica retta parallela al piano oppure contenuta in esso (aggiunto «contenuta in π se ha un punto in comune con esso»). Nessun esempio tolto, nessuna comparsa da togliere. Ricalcolata con SymPy la retta x = 4 + k, y = 1 − 3k, z = −k. Figura rifatta da script (prima SVG fisso con retta e piano disegnati a occhio, senza relazione fra v e n): piano π in proiezione obliqua con normale n e retta r con direzione v; cursore sull'angolo θ fra r e n (0°–90°, passo 15°) con punto d'intersezione, tratto sotto il piano tratteggiato e scritta verde per perpendicolare (θ = 0°) e parallela (θ = 90°). Nessuna figura decorativa.

## Unità 25 — Distanza punto-retta e distanza fra rette sghembe
- Parole: 460 su 3 pagine di traccia (107–109)
- Rettifica: nessuna. Verificato con SymPy: il piano per P(9;-3;0) normale a v(-1;4;2) dà -x+4y+2z+21=0; sostituendo le parametriche di r si ottiene 21k+21=0, k=-1, H(3;-4;-1), con PH=√38, coincidente con la traccia. Per le rette sghembe, riscritte r: x=1,y=k,z=2-k e s: x=4+2t,y=t,z=-1, il sistema di perpendicolarità RS·vr=0, RS·vs=0 dà t-2k+3=0 e 5t-k+6=0, con soluzione k=1, t=-1, R(1;1;1), S(2;-1;-1), RS=3: tutto coincidente. Confermato anche con il metodo alternativo del prodotto misto (vr×vs, distanza=9/3=3) che le due rette non si intersecano e la distanza è corretta.
- Aggiunta: nessuna. Un solo disegno statico (punto, retta, piede della perpendicolare) illustra il concetto di distanza già descritto nel primo esempio; nessun quesito di maturità inserito, in continuità con le unità 17-24 di quest'area, perché entrambi gli esempi della traccia coprono già in modo completo il metodo.
- Revisione (05/11/2026, regole 13/10): parole circa 328 → 133 (formule $$ e didascalie escluse; sommario incluso prima). Pagina mai revisionata: impaginazione a quaderno, tolti sommario, prosa e i due riquadri .esempio; titoletti «Distanza di un punto da una retta», «Esempio 1», «Distanza fra due rette sghembe», «Esempio 2» (due argomenti distinti); procedimento punto-retta in tre voci; perpendicolare comune in .def col sistema RS·v_r = 0, RS·v_s = 0; esempi in forma Dati/Calcolare con .eq. Nessun esempio tolto, nessuna comparsa da togliere. Nessuna correzione concettuale (SymPy: piano −x+4y+2z+21=0, k=−1, H(3;−4;−1), PH=√38; k=1, t=−1, R(1;1;1), S(2;−1;−1), RS=3, confermato col prodotto misto; sistema r–s impossibile). Figura rifatta da script (prima SVG fisso a occhio): piano di P e r in vera grandezza, con PH = √38, angolo retto in H e cursore su k che muove Q lungo r mostrando PQ (scritta verde per Q = H, distanza minima).

## Unità 26 — Superficie sferica
- Parole: 275 su 2 pagine di traccia (110–111)
- Rettifica: nessuna. Verificato con SymPy: l'espansione di (x-x0)²+(y-y0)²+(z-z0)²-r² coincide con la forma generale x²+y²+z²+ax+by+cz+d=0 con a=-2x0, b=-2y0, c=-2z0, d=x0²+y0²+z0²-r²; la formula inversa r=√(a²/4+b²/4+c²/4-d) ricostruisce correttamente r. Esempio 1 (centro M(2;-1;1), raggio 3): sviluppo dà x²+y²+z²-4x+2y-2z-3=0, coincidente con la traccia. Esempio 2 (x²+y²+z²+2x-2y+6z=0): centro C(-1;1;-3) e r=√11, coincidenti con la traccia. Nessun quesito di maturità inserito: è la prima unità sulla sola equazione della sfera, senza ancora gli strumenti di posizione sfera-piano (unità 27) con cui i quesiti reali di quest'area combinano sfere e piani.
- Aggiunta: nessuna.
- Revisione (05/11/2026, regole 13/10): parole circa 175 → 71 (formule $$ e didascalie escluse; sommario incluso prima; sotto le 100: contenuto in .def e formule). Pagina mai revisionata: impaginazione a quaderno, tolti sommario, prosa, i due .riquadro e i due .esempio; definizione, forma generale e centro/raggio in .def; esempi in forma Dati/Scrivere-Calcolare con una .eq ciascuno. Titoletti: «Esempio 1», «Esempio 2». Aggiunta (verificata con SymPy) la condizione di realtà: superficie sferica solo se a²/4 + b²/4 + c²/4 − d > 0 (in .nota). Nessun esempio tolto, nessuna comparsa da togliere. Nessuna correzione concettuale (SymPy: sviluppo x²+y²+z²−4x+2y−2z−3=0; C(−1;1;−3), r=√11). Figura rifatta da script (prima SVG fisso con la sfera disegnata come ellisse a occhio): assi in proiezione obliqua, contorno calcolato come inviluppo dei punti proiettati della sfera, equatore tratteggiato, coordinate x₀, y₀, z₀ del centro tratteggiate, raggio CP. Nessuna figura decorativa.

## Unità 27 — Sfera e piano: posizioni reciproche e piano tangente
- Parole: 388 su 4 pagine di traccia (112–115)
- Rettifica: nessuna. Verificato con SymPy: nel primo esempio, la sfera di centro C(0;0;0) passante per P(0;7√3;7) ha raggio PC=√(147+49)=14 e quindi equazione x²+y²+z²-196=0; il sistema per il piano passante per C, P, Q(14;0;0) dà a=0, d=0, c=-√3 b, cioè y-√3z=0, tutto coincidente con la traccia. Nel secondo esempio, il vettore PC=C-P=(-1;2;-3) e il piano per P con questa normale danno -x+2y-3z+9=0, coincidente con la traccia. Un quesito di maturità non è stato cercato: per questa unità la traccia stessa fornisce un secondo esempio (piano tangente) sufficiente a coprire il metodo, e l'area di geometria analitica nello spazio si chiude qui.
- Aggiunta: una sola frase di collegamento nel primo esempio ("Poiché α passa per il centro C, la distanza d(C,α) è nulla, dunque minore di r: il piano è secante"), indispensabile perché altrimenti l'esempio della traccia (trovare il piano per tre punti) resterebbe scollegato dal criterio appena enunciato nella stessa unità.
- Revisione (05/11/2026, regole 13/10): parole circa 315 → 115 (formule $$ e didascalie escluse; sommario incluso prima). Pagina mai revisionata: impaginazione a quaderno, tolti sommario, prosa e i due riquadri .esempio; tre posizioni in elenco caso → conseguenza; piano tangente in .def con l'equazione per P(x₁;y₁;z₁) e normale PC; esempi in forma Dati/Calcolare-Scrivere con .eq. Titoletti: «Piano tangente» (era «Piano tangente a una sfera»), «Esempio 1», «Esempio 2». Nessun esempio tolto, nessuna comparsa da togliere. Correzione: il piano secante taglia la superficie sferica lungo una circonferenza (prima «in un cerchio»). Verificato con SymPy: r = 14, α: y − √3z = 0, PC = (−1;2;−3), −x + 2y − 3z + 9 = 0 (r = √14). Figura rifatta da script (prima SVG fisso a occhio con etichetta MathJax nel disegno): sezione per C perpendicolare ad α, cursore su d (0–1,5 r, passo 0,05 r) con intersezione in rosso, punto P e scritta verde «tangente» per d = r. Nessuna figura decorativa.

## Unità 28 — Disposizioni semplici e con ripetizione
- Parole: 598 su 5 pagine di traccia (116–120)
- Rettifica: nessuna. Verificato con SymPy/Python tutti i calcoli della traccia: il podio D(4,3)=24; D(5,3)=60 e, fissando la prima cifra a 8, D(4,2)=12; il lancio di moneta 2³=8; la targa 22²·10³·22²=234.256.000 (avevo inizialmente letto male la cifra a mano come 231 milioni: un doppio controllo a 200 dpi ha confermato 234.256.000, cioè la traccia era corretta e l'errore era di lettura mia, non da riportare come rettifica di contenuto); il campionato a 15 squadre D(15,5)=360.360; l'esempio con 2 cifre e 3 lettere dell'alfabeto italiano (21 lettere) 10·9·21·20·19=718.200; la Scozia 9⁶=531.441.
- Aggiunta: nessun esempio nuovo, tutti e sette quelli della traccia sono presenti (podio, numeri di 3 cifre, moneta, targa, campionato, fila di 5, Scozia). L'unico strumento interattivo (cursori su n e k) mette a confronto $D_{n,k}$ e $D'_{n,k}=n^k$ sullo stesso schermo, per rendere visibile la differenza fra i due casi appena definiti, senza introdurre combinazioni o altri concetti delle unità successive. Nessun quesito di maturità: è la prima unità dell'area, le disposizioni da sole compaiono raramente isolate nei quesiti reali (che di solito combinano anche permutazioni o combinazioni, disponibili solo dalle unità 29–30), e una ricerca mirata non ha restituito un quesito adatto al solo bagaglio di questa unità.
- Revisione (05/11/2026, regole 13/10): parole circa 493 → 160 (formule $$ e didascalie escluse; sommario incluso prima). Pagina mai revisionata: impaginazione a quaderno, tolti sommario, prosa, i cinque riquadri .esempio e la frase di raccordo agli esempi; podio in tre voci d'elenco; definizioni con k ≤ n (semplici) e k qualsiasi (con ripetizione) in .def; esempi in forma Dati/Calcolare con una .eq ciascuno. Titoletti: «Disposizioni semplici», «Disposizioni con ripetizione» (due argomenti distinti), «Esempio 1», «Esempio 2». Esempi tenuti: numeri di 3 cifre da {4,…,8} (60 e 12), targa (234 256 000); esempi tolti: campionato di 15 squadre (D₁₅,₅ = 360 360), file di 2 cifre e 3 lettere (718 200), notti in Scozia (9⁶ = 531 441). Nessuna comparsa da togliere. Nessuna correzione concettuale (Python: 24, 60, 12, 8, 234 256 000, 360 360, 718 200, 531 441). Figure: i due alberi (podio, moneta) rifatti da script a partire dalle scelte (prima SVG fissi); il riquadro interattivo n, k trasformato in figura con due cursori e le caselle delle scelte per posizione (n − i senza ripetizione, n con ripetizione; caselle rosse e «impossibile» per k > n). Figura decorativa: la targa AA000AA (tenuta, in .fig).

## Unità 29 — Permutazioni e funzione fattoriale
- Parole: 498 su 3 pagine di traccia (121–123)
- Rettifica: nessuna. Verificato con SymPy tutti i calcoli della traccia: 4!=24, 7!=5040, 0!=1; l'anagramma di CANTO P(5)=5!=120; D(5,3)=5!/2!=60, coincidente con la formula già usata nell'unità 28; l'anagramma di TETTO (non "TETO": la parola ha 5 lettere di cui 3 T ripetute, verificato rileggendo la pagina a 200 dpi) P(5)^(3)=5!/3!=120/6=20.
- Aggiunta: nessun esempio nuovo. L'unico strumento interattivo (cursori su n e k) mostra il passaggio da $P_n=n!$ a $P_n^{(k)}=n!/k!$ appena introdotto, sullo stesso schema già usato nell'unità 28 per le disposizioni. Nessun quesito di maturità: è la seconda unità dell'area, permutazioni e fattoriale da soli non compaiono isolati nei quesiti reali della seconda prova.
- Revisione (05/11/2026, regole 13/10): parole circa 464 → 162 (formule $$ e didascalie escluse; sommario incluso prima). Pagina mai revisionata: impaginazione a quaderno, tolti sommario, prosa, i due riquadri .esempio, la nota «Attenzione» (ridotta a frase di raccordo) e il rimando all'unità precedente; scelte per posto in quattro voci d'elenco; permutazioni semplici (con 0! = 1), disposizioni col fattoriale e permutazioni con ripetizione (k e k,h) in .def; esempi in forma Dati/Calcolare con una .eq ciascuno. Titoletti: «Permutazioni semplici», «Permutazioni con ripetizione» (tolto «Disposizioni e funzione fattoriale», ora .def nella prima sezione), «Esempio 1» (CANTO), «Esempio 2» (TETTO). Tolti dal testo: 7! = 5040. Nessun esempio tolto, nessuna comparsa da togliere. Nessuna correzione concettuale (Python: 24, 5040, 120, 60, 20). Figure: albero delle penne rifatto da script fino al 4° posto (prima SVG fisso con 3°–4° accorpati); EOTTT rifatta da script con le 3! permutazioni dei colori calcolate; il riquadro interattivo n, k trasformato in figura con due cursori e caselle (k uguali in rosso, k ≤ n). Nessuna figura decorativa.

## Unità 30 — Combinazioni e coefficienti binomiali
- Parole: 523 su 4 pagine di traccia (124–127)
- Rettifica: nessuna. Verificato con SymPy tutti i calcoli della traccia: D(5,3)/P(3)=60/6=10, coincidente
  con C(5,3); l'esempio delle 5 vetture e 2 piloti C(5,2)=5·4/2!=5!/(2!3!)=10; il coefficiente binomiale
  (6 2)=6!/(2!4!)=15; i casi particolari (n 0)=(n n)=(0 0)=1; la legge delle classi complementari
  verificata numericamente (n=7,k=3: 35=35); la formula di ricorrenza verificata numericamente
  (n=8,k=3: (8 4)=70=(8 3)·5/4=70).
- Aggiunta: nessun esempio nuovo, i due esempi della traccia (i 5 punti e i triangoli, le 5 vetture e i 2
  piloti) sono entrambi presenti. L'unico strumento interattivo (cursori su n e k) mette a confronto in
  tempo reale (n k) e (n, n-k), rendendo visibile la proprietà 1 appena enunciata (legge delle classi
  complementari), senza introdurre altro. Ho incluso un quesito di maturità: il quesito 4 dell'Esame di
  Stato, Liceo scientifico, corso sperimentale P.N.I., sessione ordinaria 2011 (fonte: testo ufficiale
  online.scuola.zanichelli.it, confermato da matebook.it) — "il numero delle combinazioni di n oggetti a 4
  a 4 è uguale al numero delle combinazioni degli stessi oggetti a 3 a 3: si trovi n" — risolubile con il
  solo bagaglio di questa unità (definizione di coefficiente binomiale, senza bisogno di probabilità).
  Verificato con SymPy: risolvendo 3!(n-3)!=4!(n-4)! si ottiene n-3=4, cioè n=7, e C(7,4)=C(7,3)=35.
- Revisione (05/11/2026, regole 13/10): parole circa 470 → 133 (formule $$ e didascalie escluse; sommario incluso prima). Pagina mai revisionata: impaginazione a quaderno, tolti sommario, prosa, i riquadri .esempio, le spiegazioni delle due proprietà e il cenno alla probabilità; triangoli da 5 punti in tre voci d'elenco caso → conseguenza; combinazioni, coefficiente binomiale, classi complementari e ricorrenza (con la verifica in una .eq) in .def; casi particolari in una .eq. Titoletti: «Combinazioni semplici», «Coefficienti binomiali», «Esempio 1» (vetture e piloti), «Esempio 2» (quesito P.N.I. 2011, n. 4, in forma Dati/Calcolare). Esempio tolto: (6 2) = 15. Nessuna comparsa da togliere. Nessuna correzione concettuale (Python/SymPy: 60/6 = 10, C(5,2) = 10, (6 2) = 15, (7 4) = (7 3) = 35, n = 7 unica soluzione per n ≥ 4, ricorrenza verificata simbolicamente). Figure: i cinque punti rifatti da script con cursore sui 10 triangoli (generati in ordine lessicografico, con le 6 terne ordinate a fianco; prima SVG fisso col solo ABC); il riquadro interattivo n, k trasformato in figura con due cursori (k scelti in blu, n − k esclusi in rosso, C(n,k) e C(n,n−k) a fianco). Nessuna figura decorativa.

## Unità 31 — Combinazioni con ripetizione
- Parole: 380 su 3 pagine di traccia (128–130)
- Rettifica: nessuna. Verificato con SymPy tutti i calcoli della traccia: C(3,2)=3 (TT,TC,CC), C(4,3)=4
  (TTT,TTC,TCC,CCC), C(4,2)=6 (aa,ab,ac,bb,bc,cc); l'esempio delle 6 scatole in 4 oggetti
  C'(4,6)=C(9,6)=9!/(6!3!)=84; l'esempio dei 4 dadi C'(6,4)=C(9,4)=9!/(4!5!)=126.
- Aggiunta: nessun esempio nuovo, i due esempi della traccia (distribuzione di oggetti in scatole, lancio
  di più dadi uguali) sono entrambi presenti. L'unico strumento interattivo (cursori su n e k) mostra il
  valore di C'(n,k) al variare dei due parametri, sullo stesso schema già usato nelle unità precedenti
  dell'area. Nessun quesito di maturità: ho cercato online ma i risultati trovati riguardano le
  permutazioni con ripetizione (già trattate nell'unità 29), non le combinazioni con ripetizione; il
  tema specifico di questa unità non compare isolato nei quesiti reali della seconda prova.
- Revisione (05/11/2026, regole 13/10): parole circa 330 → 135 (formule $$ e didascalie escluse; sommario incluso prima). Pagina mai revisionata: impaginazione a quaderno, tolti sommario, prosa e i riquadri .esempio; i tre casi (moneta 2 e 3 lanci, a, b, c a due a due) in elenco caso → conseguenza; definizione e formula in .def con la condizione «k può superare n». Titoletti: «Esempio 1» (scatole), «Esempio 2» (dadi), in forma Dati/Calcolare. Nessun esempio tolto. Nessuna comparsa da togliere. Correzione concettuale: nell'esempio delle scatole precisato «6 oggetti uguali» (con oggetti distinti le distribuzioni sarebbero 4^6 = 4096, non 84). Verifiche Python: C'(2,2) = 3, C'(2,3) = 4, C'(3,2) = 6, C(9,6) = 84, C(9,4) = 126, enumerazioni confermate. Figure: il riquadro interattivo n, k (prima n 2–10, k 1–10, solo valore numerico) trasformato in figura con due cursori (n 2–4, k 1–4) che elenca tutti i gruppi fra a, b, c, d e il valore C'(n,k). Nessuna figura decorativa.

## Unità 32 — Definizione classica ed eventi contrari
- Parole: 510 su 3 pagine di traccia (131–133)
- Rettifica: nessuna. Verificato con SymPy tutti i calcoli della traccia: P(E)=3/6=1/2 per l'esempio del
  dado; D(10,5)=30240; D(4,2)·D(6,3)=1440 e P(E1)=1440/30240=1/21; per l'evento senza ordine,
  D(4,2)·D(6,3)·5!/(2!3!)=14400 e P(E2)=14400/30240=10/21, coincidente con C(4,2)·C(6,3)/C(10,5)=6·20/252.
- Aggiunta: nessun esempio nuovo, i tre esempi della traccia (dado, urna con ordine, urna senza ordine)
  sono tutti presenti. L'unico strumento interattivo (cursore sul numero di casi favorevoli f) mostra
  P(E) e P(non E) al variare di f, rendendo visibile la proprietà 0≤P(E)≤1 appena enunciata, senza
  introdurre altro. Nessun quesito di maturità: è la prima unità del blocco probabilità (definizione
  classica ed evento contrario soltanto), e i quesiti reali trovati richiedono probabilità condizionata
  o eventi composti, argomenti delle unità 33-34; per coerenza con "nelle unità iniziali è normale che
  non ci sia nessun quesito" non ne ho inserito nessuno.
- Revisione (05/11/2026, regole 13/10): parole circa 470 → 138 (formule $$ e didascalie escluse; sommario incluso prima). Pagina mai revisionata: impaginazione a quaderno, tolti sommario, prosa e i riquadri .esempio; definizione classica in .def (con la condizione «numero finito di esiti ugualmente possibili»), esempio del dado in una riga + .eq, tre proprietà in elenco caso → conseguenza, evento contrario in .def. Titoletti: «Evento contrario», «Esempio 1» (urna con ordine), «Esempio 2» (urna senza ordine, con la verifica tramite combinazioni), in forma Dati/Calcolare. Nessun esempio tolto (l'esempio del dado resta come applicazione della definizione). Nessuna comparsa da togliere. Nessuna correzione concettuale (Python: D(10,5) = 30240, D(4,2)·D(6,3) = 1440, 1440/30240 = 1/21, 1440·10 = 14400, 14400/30240 = 10/21 = C(4,2)·C(6,3)/C(10,5) = 120/252). Figure: il riquadro interattivo sul dado trasformato in figura con cursore f (sei facce disegnate da script, favorevoli a E in blu, a non E in rosso, P(E) e P(non E) a fianco). Nessuna figura decorativa.

## Unità 33 — Somma logica di eventi
- Parole: 247 su 1,5 pagine di traccia (134–135, prima metà)
- Rettifica: nessuna. Verificato con SymPy/frazioni: P(E1)=1/2, P(E2)=1/2, P(E1∩E2)=1/6,
  P(E1∪E2)=1/2+1/2-1/6=5/6, coincidente con il conteggio diretto |{1,2,3,4,6}|/6=5/6.
- Aggiunta: nessun esempio nuovo, l'unico esempio della traccia (urna con palline numerate 1-6) è
  ripreso per intero, incluso il diagramma di Venn con i sei esiti posizionati, ridisegnato in SVG.
  Ho aggiunto solo l'applicazione numerica della formula ai dati E1, E2 già dati nell'esempio, per
  mostrare come si usa; non è un esempio nuovo. Nessuno strumento interattivo: la formula non ha un
  parametro naturale da far variare oltre ai dati già fissati dell'esempio, quindi il diagramma resta
  statico. Nessun quesito di maturità: è la seconda unità del blocco probabilità e tratta solo la
  somma logica fra due eventi; i quesiti reali sul tema richiedono quasi sempre probabilità
  condizionata o eventi indipendenti, argomenti delle unità 34-35, quindi non ne ho cercato uno per
  questa unità.
- Revisione (05/11/2026, regole 13/10): parole circa 160 → 100 (formule $$ e didascalie escluse; sommario incluso prima). Pagina mai revisionata: impaginazione a quaderno, tolti sommario, prosa e il riquadro .esempio; unione e intersezione in elenco caso → conseguenza; insiemi dell'urna in una .eq; formula della somma logica in .def; eventi incompatibili in .def (condizione E₁∩E₂ = ∅ nella formula, frase della nota tolta). Titoletti: solo «Esempio» (P(E₁∪E₂) = 1/2 + 1/2 − 1/6 = 5/6, con il conteggio diretto 5 su 6), in forma Dati/Calcolare. Nessun esempio tolto. Nessuna comparsa da togliere. Nessuna correzione concettuale (Python/frazioni: 3/6 + 3/6 − 1/6 = 5/6 = |{1,2,3,4,6}|/6). Figure: diagramma di Venn ridisegnato da script, con cursore «esito» 1–6 che evidenzia la pallina estratta e indica l'appartenenza a E₁, E₂, E₁∩E₂, E₁∪E₂ («sì» in verde per l'unione). Nessuna figura decorativa.

## Unità 34 — Probabilità condizionata
- Parole: 480 su 4 pagine di traccia (135–138)
- Rettifica: nell'Esempio II la traccia scrive una volta "4°B" e nel resto del brano "5°B" per la
  stessa classe (24 alunni, 11 femmine e 13 maschi): uniformato a "5ªB" ovunque, come richiesto dal
  contesto (istituto con 650 alunni, la classe è la quinta). Verificato con Python/frazioni tutti i
  calcoli: P(E2|E1) palline = (3/9·4/8)/(3/9) = (1/6)/(1/3) = 1/2, coincidente con 4/8 diretto;
  P(E2|E1) sondaggio = C(13,2)/C(24,2) = 78/276 = 13/46.
- Aggiunta: nessun esempio nuovo, entrambi gli esempi della traccia (palline senza reimmissione,
  sondaggio nella 5ªB) sono ripresi per intero. Nessuno strumento interattivo: il diagramma di Venn
  che illustra la restrizione dello spazio campione resta statico, in coerenza con l'unità 33.
  Nessun quesito di maturità: i quesiti reali sulla probabilità condizionata compaiono quasi sempre
  insieme al prodotto logico o al teorema di Bayes, argomenti delle unità 35 e 37, quindi non ne ho
  cercato uno per questa unità.
- Revisione (05/11/2026, regole 13/10): parole circa 390 → 145 (formule $$ e didascalie escluse; sommario incluso prima). Pagina mai revisionata: impaginazione a quaderno, tolti sommario, prosa e i riquadri .esempio; con/senza reimmissione in elenco caso → conseguenza (indipendenti/dipendenti); definizione in .def; derivazione r/k = P(E₁∩E₂)/P(E₁) in una frase di raccordo + .def. Titoletti: «Esempio 1» (palline, risultato diretto 4/8 e verifica con la formula nella stessa .eq), «Esempio 2» (sondaggio nella 5ªB, scritto con C₁₃,₂/C₂₄,₂ come nell'unità 32), in forma Dati/Calcolare. Nessun esempio tolto. Nessuna comparsa da togliere. Correzione concettuale: aggiunta la condizione «con P(E₁) ≠ 0» alla formula (prima mancava). Verifiche Python/frazioni: (12/72)/(3/9) = 1/2 = 4/8; C(13,2)/C(24,2) = 78/276 = 13/46; 425 + 225 = 650, 11 + 13 = 24. Figure: diagramma di Venn ridisegnato da script (E₁ in azzurro come nuovo spazio campione, U tratteggiato in grigio, intersezione tratteggiata in rosso), statico. Nessuna figura decorativa.

## Unità 35 — Prodotto logico ed eventi indipendenti
- Parole: 438 su 1,5 pagine di traccia (139 intera, 140 fino a circa metà pagina)
- Rettifica: nessuna. Verificato con Python/frazioni tutti i calcoli: P(E)=2/52=1/26 per l'esempio delle
  carte, coincidente con P(E1)·P(E2|E1)=(1/2)·(1/13)=1/26.
- Aggiunta: nessun esempio nuovo, l'unico esempio della traccia (carta nera e re da un mazzo di 52) è
  ripreso per intero. Nessuno strumento interattivo: la formula non ha un parametro naturale da far
  variare al di fuori dei dati fissati dell'esempio. Un solo riquadro di errore tipico (usare il prodotto
  delle probabilità marginali anche quando gli eventi sono dipendenti), oltre alla definizione: restano
  entrambi nel limite dei due o tre riquadri consentiti. Ho incluso un quesito di maturità: il quesito 7
  (prima parte) del questionario della sessione suppletiva 2017, Liceo scientifico (fonte: testo e
  svolgimento ufficiale online.scuola.zanichelli.it) — la probabilità che, nel gioco dado fra Alberto e
  Barbara, entrambi segnino almeno un punto — risolubile con il solo bagaglio disponibile a questa unità
  (prodotto di eventi indipendenti esteso a più lanci, evento contrario dell'unità 32, somma logica di
  eventi incompatibili dell'unità 33), senza la seconda parte del quesito (punteggio 4 a 4), che richiede
  il teorema delle prove ripetute dell'unità 36 e non è stata inclusa. Verificato con Python/frazioni:
  P(Alberto=0)=(1/3)^3=1/27, P(Barbara=0)=(2/3)^6=64/729, la loro somma è 91/729 e il complementare
  638/729 ≈ 0,875, in accordo con lo svolgimento ufficiale.
- Revisione (06/11/2026, regole 13/10): parole circa 396 → 156 (formule $$, didascalie ed etichette escluse; sommario incluso prima). Pagina mai revisionata: impaginazione a quaderno, tolti sommario, prosa, riquadri .esempio e rimando all'unità 36; prodotto logico, probabilità composta (con P(E₁) ≠ 0) ed eventi indipendenti in tre .def, indipendenti/dipendenti in elenco caso → conseguenza, nota sull'errore tipico in una frase. Titoletti: «Esempio 1», «Esempio 2». Esempi tenuti: re nero da 52 carte (1/26), quesito suppletiva 2017 prima parte (638/729 ≈ 0,875, i due casi «a zero» in elenco); nessun esempio tolto. Nessuna comparsa da togliere. Nessuna correzione concettuale (Python/frazioni). Nessuna figura (nessuna prima).

## Unità 36 — Prove ripetute e schema di Bernoulli
- Parole: 403 su 1,5 pagine di traccia (141 intera, 142 fino alla formula generale, prima di "Teorema
  di Bayes" che apre l'unità 37).
- Rettifica: nessuna. Verificato con SymPy tutti i calcoli della traccia: (1/2)^10=1/1024;
  (1/2)^10·C(10,4)=105/512; C(5,2)·(1/6)^2·(5/6)^3=625/3888, tutti coincidenti con quanto scritto.
- Aggiunta: nessun esempio nuovo, i tre esempi della traccia (10 teste su 10 lanci, 4 teste e 6 croci,
  2 sei su 5 lanci di dado) sono ripresi per intero, seguiti dalla formalizzazione generale
  P(k,n)=C(n,k)p^k q^(n-k) che la traccia stessa scrive subito dopo il terzo esempio, in cima a
  pagina 142, prima di passare al teorema di Bayes. Un solo riquadro di errore tipico (dimenticare il
  coefficiente binomiale e calcolare solo p^k q^(n-k)). Ho incluso un quesito di maturità: il quesito 7
  (seconda parte) del questionario della sessione suppletiva 2017, Liceo scientifico (fonte: testo e
  svolgimento ufficiale online.scuola.zanichelli.it) — la probabilità che il punteggio del gioco fra
  Alberto e Barbara, già introdotto nell'unità 35, sia in un certo momento di 4 a 4 — esplicitamente
  rimandato a questa unità dal registro dell'unità 35, perché richiede lo schema delle prove ripetute.
  Verificato con SymPy: C(6,4)·(2/3)^4·(1/3)^2=80/243≈0,329. L'unico strumento interattivo mostra
  l'istogramma di P(k,n) al variare di k, con due cursori per n e p; evidenzia in rosso il valore di k
  più probabile e permette di verificare a vista i due esempi con moneta (n=10, p=0,5): il massimo cade
  in k=5 (24,6%), mentre la barra per k=4 riproduce il calcolo dell'esempio, 105/512≈20,5%.

## Unità 37 — Teorema di Bayes e disintegrazione
- Parole: 506 su circa 4 pagine di traccia (142, dalla seconda metà dove inizia "Teorema di Bayes",
  fino a 146, dove finisce l'esempio del test diagnostico e comincia "Definizione statistica di
  probabilità" dell'unità 38).
- Rettifica: a pagina 146 la traccia calcola la probabilità di essere sani dato un test negativo
  usando per sbaglio, come numeratore della formula di Bayes, il termine 1/10^7 (che è invece
  P(malato e negativo)) anziché 9999²/10^8 (P(sano e negativo)), ottenendo 0,909 = 90,9%. Il calcolo
  corretto, verificato con SymPy sulle stesse frazioni scritte nella traccia (P(malato)=1/10^4,
  P(neg|malato)=1/10^3, P(sano)=9999/10^4, P(neg|sano)=9999/10^4), dà P(sano|neg) = 99980001/99980011
  ≈ 0,999999 = 99,9999%, coerente con l'intuizione che con una malattia così rara un test negativo
  è quasi una garanzia. Ho pubblicato il valore corretto senza segnalarlo in pagina. Ho anche verificato
  con SymPy il resto della traccia (P(bianca)=47/90, P(nera)=43/90, P(urna1|bianca)=27/47 nell'esempio
  delle urne; P(malato|pos)=1110/2221≈49,98% nell'esempio del test): tutti coincidenti con quanto scritto.
- Aggiunta: nessun esempio nuovo. I due esempi della traccia (le due urne con disintegrazione e
  inversione con Bayes; il test diagnostico con le due domande su esito positivo e negativo) sono
  ripresi per intero, con i due alberi delle probabilità ridisegnati in SVG al posto degli originali
  a mano libera. Un solo riquadro di errore tipico (confondere P(Ei|E) con P(E|Ei)). Nessun quesito di
  maturità: le ricerche online per quesiti ufficiali attribuibili con anno e sessione non hanno dato un
  quesito sicuramente reale e alla portata di questa sola unità (i quesiti trovati su siti didattici non
  erano riconducibili a una sessione ufficiale verificabile); ho preferito ometterlo piuttosto che
  rischiare un'attribuzione scorretta.

## Unità 38 — Definizione statistica e soggettiva
- Parole: 549 su circa 3,5 pagine di traccia (dalla seconda metà di pagina 146, dove inizia
  "Definizione statistica di probabilità", fino a pagina 149, dove finisce l'esempio della corsa di
  cavalli; a pagina 150 comincia il ripasso di esponenziali e logaritmi, escluso perché spostato in
  terza).
- Rettifica: a pagina 148 la traccia calcola le tre probabilità implicite nelle quote di scommessa
  arrotondando quella del PSG a 45% (invece di 45,45%) e poi sommando i tre valori a 106,1%. Ho
  verificato con SymPy le tre frazioni esatte (1/2,20=45,4545...%; 1/3,30=30,3030...%;
  1/3,25=30,7692...%): la somma corretta e coerente è 106,53%, non 106,1%. Ho pubblicato i tre valori
  arrotondati in modo omogeneo a due cifre decimali e la somma corrispondente, senza segnalare la
  correzione in pagina. Ho verificato anche il resto della traccia con SymPy: la tabella delle
  frequenze relative (5/80=1/16, 18/80=9/40, 22/80=11/40, 35/80=7/16, somma 1) e l'esempio di Dario
  (90/120=3/4=75%, 4/5=80%) coincidono con quanto scritto.
- Aggiunta: nessun esempio nuovo. I due esempi della traccia (la tabella delle palline colorate per
  la definizione statistica; le quote di scommessa e la corsa di cavalli per quella soggettiva) sono
  ripresi per intero. Nessuna figura SVG: la traccia in questa unità non contiene diagrammi, solo la
  tabella dei colori, resa come tabella HTML nello stesso stile già usato altrove nel percorso.
  Con questa unità si chiude interamente matematica-4 (38 unità su 38 pubblicate).
