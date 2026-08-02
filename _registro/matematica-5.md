# Registro delle modifiche — Matematica quinta

File per l'insegnante: raccoglie correzioni e aggiunte rispetto alla traccia manoscritta.
Non è visibile agli studenti e non è collegato dalle pagine del sito.

## Calibrazione di riferimento
Circa 200 parole per pagina di traccia manoscritta. Le unità 01 e 02 sono lo standard
approvato: rispettivamente 1124 parole su 6 pagine (187/pagina) e 632 su 4 pagine (158/pagina).

## Unità 01 — Definizioni di limite, intorni, limite destro e sinistro
- Parole: 1124 su 6 pagine di traccia (1–6)
- Rettifica: nessuna. Verificati con SymPy la semplificazione di (2x²−6x)/(x−3), il limite in 3
  e l'equivalenza |2x−6|<ε ⟺ |x−3|<ε/2.
- Aggiunta: nulla di contenuto. Solo le frasi di spiegazione dei passaggi già presenti, più un
  interattivo epsilon-delta.
- Rimosso in revisione: tabella di valori attorno a 3, secondo widget di avvicinamento, e i
  paragrafi di commento eccedenti (versione precedente 2248 parole).

## Unità 02 — Verifica di un limite e primo sguardo agli asintoti
- Parole: 632 su 4 pagine di traccia (7–10)
- Rettifica: nessuna. Verificati con SymPy il limite di 1/(x−1)² in 1 e la soglia δ = 1/√M.
- Titolo modificato da "Verifica di un limite e primi asintoti" per rendere esplicito che gli
  asintoti sono qui trattati solo qualitativamente.
- Aggiunta: nulla di contenuto. Le due gallerie di grafici riproducono i disegni della traccia.
- Rimosso in revisione: la sezione di sintesi "Uno schema per orientarsi", assente dalla
  traccia, e i riquadri di commento in eccesso (versione precedente 1479 parole).

## Unità 03, 04, 05 — annullate e da rifare
Le prime versioni contenevano materiale non presente nella traccia: dimostrazioni complete dei
teoremi di unicità, permanenza del segno e confronto (la traccia riporta solo gli enunciati con
un disegno, alle pagine 11 e 18–19), esempi motivanti inventati, tabelle riassuntive e widget
aggiuntivi. Sono state rimosse e verranno riscritte con la calibrazione corretta.
Nella traccia l'unica dimostrazione sviluppata di questo blocco è quella di sin(x)/x tramite il
teorema del confronto, a pagina 21.

## Unità 03 — Teoremi sui limiti: unicità, permanenza del segno, confronto
- Parole: circa 495 su 3 pagine di traccia equivalenti (coda di pag. 10, pag. 11 intera, testa di
  pag. 18–20 fino all'inizio di "Limiti notevoli").
- Rettifica: nessuna. Verificato con SymPy che 2/x ≤ (3+cos x)/x ≤ 4/x per x>0 e che entrambi i
  limiti dei bordi valgono 0 per x→+∞.
- Aggiunta: nulla di contenuto. Solo le frasi che spiegano il ruolo di ciascuna ipotesi, più
  un interattivo che mostra la stretta della disequazione 2/x ≤ (3+cos x)/x ≤ 4/x al crescere di M.
- Nota sul confine: il teorema di unicità è disegnato in coda a pag. 10 (dopo il materiale
  dell'unità 02, mai usato lì) e la dimostrazione di sin x/x che segue il teorema del confronto a
  pag. 20–21 appartiene invece all'unità 06 (Limiti notevoli): qui restano solo l'enunciato del
  confronto e l'unico esempio svolto prima di quell'intestazione.
- Nessuna dimostrazione: la traccia riporta unicità, permanenza del segno e confronto come soli
  enunciati con disegno, senza dimostrarli; restano così anche qui.

## Unità 04 — Calcolo dei limiti e algebra dei limiti
- Parole: 441 su circa 2,4 pagine di traccia equivalenti (coda di pag. 11 — sezione "Calcolo di
  limiti / Funzioni continue in x0", mai usata nell'unità 03 — più pagine 12–13).
- Rettifica: nessuna negli enunciati. Il caso $\lim_{x\to-1}\sqrt{x}$ della traccia è segnato con
  un simbolo di "non esiste": ho reso esplicito il motivo (−1 fuori dal dominio di $\sqrt{x}$),
  che nella traccia non è scritto ma è implicito nel simbolo. Verificati con SymPy tutti i 13
  limiti per sostituzione e i tre esempi di algebra dei limiti (somma 2+7=9, prodotto 3·2=6,
  potenza (−1)²=1).
- Aggiunta: nulla di contenuto nuovo. Ho rietichettato con $n$ l'esponente costante nella regola
  della potenza per evitare la collisione col simbolo $m$ già usato per $\lim g(x)$ — la traccia
  usa $m$ per entrambi i casi, ambiguità solo notazionale. L'unico interattivo riusa le stesse
  $f,g$ dell'esempio sulla somma per mostrare in tempo reale anche prodotto e quoziente.

## Unità 05 — Forme indeterminate
- Parole: 523 su 4 pagine di traccia (14–17)
- Rettifica: nessuna. Verificati con SymPy tutti i sette limiti: $x^4-3x^2+1\to+\infty$,
  $x-\sqrt{x^2+1}\to0$, $(1-\sin x)\tan x\to0$ in $\pi/2^-$, i tre limiti $\infty/\infty$
  ($-\infty$, $-2/3$, $0$), il limite $0/0$ in $3$ (fattorizzazione $2x^2-9x+9=(x-3)(2x-3)$
  confermata) e $x^{1/\ln x}\to e$.
- Aggiunta: nulla di contenuto nuovo. Ho reso esplicito in una riga il criterio generale che
  emerge dai tre esempi $\infty/\infty$ già presenti (confronto fra i gradi), senza introdurre
  esempi ulteriori. L'unico interattivo riusa il secondo esempio $\infty/\infty$ della traccia
  per mostrare l'avvicinamento all'asintoto $y=-2/3$.

## Unità 06 — Limiti notevoli
- Parole: circa 420 (conteggio totale token, prosa e formule) su 4 pagine di traccia (20–23).
- Rettifica: nessuna. Verificati con SymPy tutti i sette limiti notevoli (sin x/x, (1-cos x)/x,
  (1-cos x)/x², (1+1/x)^x → e, ln(1+x)/x, (e^x-1)/x, ((1+x)^k-1)/x), l'identità
  (1-cos x)/x = sin²x/(x(1+cos x)) e la catena di disuguaglianze sin x < x < tan x per x
  piccolo positivo con verifica numerica.
- Confine rispettato: la dimostrazione di sin x/x tramite il teorema del confronto, che nella
  traccia segue immediatamente l'enunciato del teorema (pag. 18–21), è stata lasciata fuori
  dall'unità 03 e collocata qui, come da nota già presente nel registro.
- Aggiunta: nulla di contenuto nuovo. Solo le frasi che spiegano perché la funzione sin x/x è
  pari, il passaggio ai reciproci che inverte le disuguaglianze, e il cambio di variabile
  y = 1/x nel quinto limite. L'unico interattivo mostra la stretta cos x < sin x/x < 1
  chiudersi verso 1 al variare del cursore.
- Nessuna dimostrazione aggiunta per i limiti notevoli 4, 6 e 7: la traccia li presenta come
  risultati riquadrati senza sviluppo, così restano anche qui.

## Unità 07 — Infinitesimi e infiniti, gerarchia, principio di sostituzione
- Parole: 649 su circa 4,5 pagine di traccia equivalenti (coda di pag. 23, dopo il limite notevole
  n.7 già coperto dall'unità 06, più le pagine 24–27 intere).
- Rettifica: nessuna. Verificati con SymPy tutti i limiti: ln(1+5x)/sin(2x) → 5/2; (ln x)^3/x^2 → 0;
  (log_2 x)^100/√x → 0; x^4/2^x → 0; x^x/e^x → +∞; e le cinque equivalenze notevoli per x→0
  (sin x ~ x, ln(1+x) ~ x, e^x−1 ~ x, 1−cos x ~ x²/2, (1+x)^k−1 ~ kx, quest'ultima con k=3/7).
- Aggiunta: una riga di chiarimento sul ruolo degli esponenti/basi nella gerarchia
  (ln x)^a < x^a < a^x < x^x (a>0 per l'esponente, a>1 per la base dell'esponenziale), assente
  nella traccia ma necessaria a rendere leggibile la disuguaglianza. Nessun esempio nuovo:
  l'unico interattivo riusa le quattro funzioni della gerarchia (ln x, x², 2^x, x^x) già disegnate
  nella traccia, mostrandone i sorpassi al crescere di x su scala logaritmica.

## Unità 08 — Continuità in un punto e in un intervallo
- Parole: 413 su 4 pagine di traccia (28–31)
- Rettifica: nessuna. Verificato con SymPy che il dominio di $\sqrt{x+2}$ è $x\geq-2$ (soluzione di
  $x+2\geq0$) e che $\lim_{x\to-2^+}\sqrt{x+2}=0$.
- Aggiunta: una riga che collega la continuità bilatera alle due continuità unilaterali (già
  disponibile dall'unità 01 sui limiti destro e sinistro, non esplicitata nella traccia in questo
  punto ma immediata conseguenza di quanto già introdotto). Nessun esempio nuovo: l'unico
  interattivo mostra $f(x)=x^2$ con il valore in $x_0=1$ spostabile a mano, per far vedere dal vivo
  quando il punto cade sulla curva (continuità) e quando se ne stacca pur restando il limite
  invariato.

## Unità 09 — Weierstrass, valori intermedi, esistenza degli zeri
- Parole: 551 su 3 pagine di traccia (32–34)
- Rettifica: nessuna. Verificato con SymPy che $f(x)=x^3-x-1$ è continua su $\mathbb{R}$, che
  $f(1)=-1$, $f(2)=5$ e che l'unica soluzione reale dell'equazione è $\approx1{,}3247$, interna a
  $(1,2)$ come richiesto dal teorema.
- Aggiunta: un solo esempio (la traccia non ne contiene alcuno in queste tre pagine), applicando il
  teorema di esistenza degli zeri a $x^3-x-1=0$ su $[1,2]$; l'unico interattivo riusa la stessa
  funzione con un cursore sull'estremo $b$, per far vedere dal vivo quando il cambio di segno
  garantisce lo zero. Nessun quesito di maturità reale inserito: il quesito standard su questo
  teorema (Maturità 2017, quesito 9, su $\arctan x+x^3+e^x=0$) chiede anche l'unicità della
  soluzione, che richiede lo studio del segno della derivata prima, non ancora disponibile a
  questo punto del percorso (arriva nell'unità 22); un rimando in tal senso è stato aggiunto in
  coda alla pagina al posto del quesito.
- La figura che nella traccia introduce la definizione di massimo/minimo assoluto e quella che
  illustra il teorema di Weierstrass sono la stessa figura (mostrano lo stesso tipo di curva),
  perciò sono state unificate in un solo grafico invece di duplicarle.

## Unità 10 — Punti di discontinuità e di singolarità
- Parole: 538 su 5 pagine di traccia (35–39)
- Rettifica: nella traccia (pag. 39), l'esempio di singolarità eliminabile su
  $f(x)=(1-x^2)/(x-1)$ assegna il valore $-1$ a $x=1$ nella funzione ridefinita, ma il limite
  calcolato subito sopra, e verificato con SymPy, vale $-2$ (da $-(x+1)$ per $x\to1$). Corretto
  silenziosamente a $-2$ nella pagina. Verificati con SymPy anche il salto dell'esempio 1
  (−6 e 1, salto 7) e i quattro limiti laterali dell'esempio 2 su $5/(x^2-1)$.
- Aggiunta: nulla di contenuto nuovo. L'unico interattivo riusa la funzione dell'esempio 3
  (il caso corretto a $-2$), con un cursore sul valore assegnato in $x=1$ per mostrare dal vivo
  quando il buco viene tappato. Le otto figure statiche in galleria riproducono a coppie
  (discontinuità/singolarità) i disegni della traccia per le tre specie; la figura a tre rami
  dopo l'esempio 2 riprende lo stesso disegno con asintoto doppio che compare in testa a pag. 38.

## Unità 11 — Asintoti verticali, orizzontali e obliqui
- Parole: 606 su circa 5,5 pagine di traccia equivalenti (coda di pag. 39, dopo l'ultimo esempio
  dell'unità 10, più le pagine 40–44 intere).
- Rettifica: nessuna. Verificati con SymPy tutti i limiti dell'esempio verticale/orizzontale su
  $f(x)=(4x^2+3)/(x^2-1)$ (asintoti $x=1$, $x=-1$, $y=4$) e dell'esempio obliquo su
  $f(x)=(3x^2-2x+1)/(x-1)$ ($m=3$, $q=1$, $y=3x+1$, e il limite $-\infty$ a sinistra), oltre alla
  distanza $f(x)-(3x+1)=2/(x-1)$ usata nell'interattivo.
- Aggiunta: nulla di contenuto nuovo. Solo la frase che distingue quando è l'ascissa e quando è
  l'ordinata a tendere all'infinito nella definizione generale di asintoto. Le quattro gallerie
  statiche riproducono le terne e coppie di schizzi della traccia (definizione generale, verticali,
  orizzontali, obliqui); l'unico interattivo mostra la distanza fra la curva e l'asintoto obliquo
  destro chiudersi verso zero al crescere di $x$.
- Nessuna dimostrazione: il teorema che dà $m$ e $q$ è riportato in traccia come solo enunciato,
  senza sviluppo; resta così anche qui.

## Unità 12 — Grafico probabile e funzioni con parametri
- Parole: 417 su 5 pagine di traccia (45–49)
- Rettifica: nessuna. Verificati con SymPy tutti i passaggi di entrambi gli esempi: la disparità
  di $f(x)=(x^2-1)/x$, gli zeri $\pm1$, il segno $-1<x<0 \lor x>1$, i limiti in $x=0$
  ($+\infty$ e $-\infty$), $m=1$ e $q=0$ per l'asintoto $y=x$; e per la funzione con parametro
  $y=(x^3+p)/(x+q)^2$ la soluzione $p=-1$, $q=2$, i due limiti $-\infty$ in $x=-2$ e l'asintoto
  obliquo $y=x-4$ (con $m=1$, $q=-4$).
- Aggiunta: nulla di contenuto nuovo. I sei passi dello schema sono ripresi nell'ordine della
  traccia; l'unico interattivo riusa il primo esempio ($f(x)=(x^2-1)/x$), mostrando la distanza
  fra la curva e l'asintoto obliquo chiudersi verso zero, sullo stesso modello dell'interattivo
  dell'unità 11. Nessun quesito di maturità inserito: senza le derivate, disponibili solo
  dall'unità 13, i quesiti reali sul grafico di una funzione richiedono lo studio del segno della
  derivata prima, non ancora nel bagaglio a questo punto del percorso.

## Unità 13 — Rapporto incrementale, definizione di derivata, significato geometrico
- Parole: 450 su 4 pagine di traccia (50–53), conteggio del solo testo prosastico (formule
  escluse).
- Rettifica: nessuna. Verificati con SymPy sia il rapporto incrementale di $f(x)=x^2-x$ in
  $h+5$ e il limite $f'(3)=5$, sia il rapporto e il limite di $f(x)=4x^2$ in un punto generico,
  $4h+8x\to8x$: entrambi coincidono con i passaggi della traccia.
- Aggiunta: nulla di contenuto nuovo. Solo le frasi che spiegano perché $\Delta y/\Delta x$ è il
  coefficiente angolare della secante (sottrazione delle due equazioni di retta, già presente in
  traccia) e il collegamento fra il limite del rapporto incrementale e la pendenza della
  tangente. L'unico interattivo riusa la funzione e il punto $c=3$ del primo esempio, con un
  cursore su $h$ che fa vedere dal vivo la secante ruotare verso la tangente disegnata nella
  traccia.
- Nessun quesito di maturità: è la prima unità sulle derivate, limitata alla definizione; i
  quesiti reali su tangenti e derivate richiedono le regole di derivazione dell'unità 14 e
  arriveranno dall'unità 17 in poi.

## Unità 14 — Derivate fondamentali e regole di derivazione
- Parole: 336 su 4 pagine di traccia (54–57).
- Rettifica: nessuna. Verificati con SymPy tutte le derivate fondamentali e tutti gli esempi:
  $D(5x^8)=40x^7$, $D(-3\ln x)=-3/x$, $D(\tfrac{2}{3}\cos x)=-\tfrac{2}{3}\sin x$; le somme
  $y=x+2\sin x$ e $y=2e^x-3\cos x+1$; i prodotti $y=x\sin x$ e $y=x^3e^x$; i reciproci
  $y=1/\sin x$ e $y=5/(x^3-2)$; il quoziente $y=(3x^2-1)/(x^2+x)$, che dà $y'=(3x^2+2x+1)/(x^2+x)^2$
  come in traccia; e le derivate di $\tan x$ e $\cot x$ ($1+\tan^2x$ e $-1-\cot^2x$).
- Aggiunta: nulla di contenuto nuovo. La dimostrazione della regola del quoziente è quella
  della traccia (prodotto per il reciproco). L'unico interattivo riusa l'esempio della regola
  del prodotto, $y=x\sin x$: un cursore sposta il punto $x_0$ e mostra la retta tangente con
  pendenza uguale al valore di $f'(x_0)=\sin x_0+x_0\cos x_0$ calcolato con la regola, a
  conferma del significato geometrico visto nell'unità 13. Nessun quesito di maturità: questa
  unità è solo il repertorio di regole, senza ancora funzioni composte o studio di funzione.

## Unità 15 — Funzioni composte, funzione inversa, goniometriche inverse
- Parole: 338 su 5 pagine di traccia (58–62).
- Rettifica: nessuna. Verificati con SymPy tutti i passaggi: le tre derivate di funzioni
  composte ($\ln(x^2+2)$, $(x^3+2x)^3$, $e^{2x+1}$), la potenza di funzione
  $(x^2+2x+7)^4$, la catena tripla $e^{(2x+1)^2}$, le derivate di arcoseno e arcocoseno
  ottenute dalla regola della funzione inversa (e il confronto con arctan e arccot della
  tabella), la derivazione logaritmica di $x^x$ e $x^{2x+1}$, e la derivata del prodotto
  triplo $x^2\ln x\,e^{2x}$.
- Aggiunta: nulla di contenuto nuovo. Solo le frasi che spiegano perché nella regola della
  catena si moltiplicano due derivate valutate in punti diversi, e perché le pendenze di $f$
  e $f^{-1}$ sono reciproche (simmetria rispetto alla bisettrice, non sviluppata come
  dimostrazione formale ma solo richiamata come idea, assente anch'essa nella traccia oltre
  al disegno implicito del ribaltamento). L'unico interattivo mostra la tangente a
  $y=\arcsin x$ con pendenza $1/\sqrt{1-x_0^2}$, la stessa formula appena derivata, e fa
  vedere la pendenza crescere senza limite avvicinandosi agli estremi del dominio. Nessun
  quesito di maturità: l'unità è un repertorio di regole di derivazione, senza ancora lo
  studio di funzione in cui questi quesiti compaiono di solito.

## Unità 16 — Domini e derivate di ordine superiore
- Parole: 201 su 3 pagine di traccia (63–65), conteggio del solo testo prosastico (formule
  escluse).
- Rettifica: nessuna. Verificato con SymPy che per $f(x)=x^3-2x+1$ si ha $f'(x)=3x^2-2$,
  $f''(x)=6x$, $f'''(x)=6$, $f''''(x)=0$, come in traccia.
- Aggiunta: nulla di contenuto nuovo. Le due righe di commento sulla potenza a esponente
  variabile e sulla potenza a esponente irrazionale spiegano perché servono due condizioni
  insieme (lettura come $e^{g(x)\ln f(x)}$) e perché il segno di $\alpha$ cambia la condizione
  sulla base, cose implicite nella tabella ma non scritte a parole. Nessun interattivo: la
  pagina è una tabella di riferimento più un unico esempio, senza nulla da far vedere in modo
  dinamico che non sia già chiaro dai due esempi statici. Nessun quesito di maturità: come
  l'unità 14, questa è solo un repertorio (domini e notazione delle derivate successive), non
  ancora uno studio di funzione.

## Unità 17 — Retta tangente, retta normale, punti stazionari
- Parole: 731 su 4 pagine di traccia (66–69), conteggio del testo visibile incluse le
  formule inline (il solo testo prosastico è nettamente inferiore).
- Rettifica: nessuna. Verificati con SymPy tutti i passaggi: $f(x)=x^2+2x$ dà $f(1)=3$,
  $f'(x)=2x+2$, $f'(1)=4$, tangente $y=4x-1$ e normale $y=-\frac14x+\frac{13}{4}$; il
  sistema di tangenza fra $f(x)=x^3-x^2-2x$ e $g(x)=x^3+x^2+\frac12$ ha come unica
  soluzione $x_0=-\frac12$, con verifica numerica del passaggio di cancellazione dei
  termini di terzo e secondo grado.
- Aggiunta: nulla di contenuto nuovo. L'unico interattivo mostra la retta tangente a
  $f(x)=x^2+2x$ al variare del punto $x_0$, la stessa costruzione appena vista nell'esempio
  numerico, resa dinamica per far vedere che la pendenza segue $f'(x_0)$. I tre schemi di
  minimo, massimo e flesso e il disegno delle due curve tangenti ridisegnano quanto già
  presente in traccia. Nessun quesito di maturità: l'unità introduce solo le equazioni di
  tangente e normale, senza ancora lo studio di funzione completo in cui questi quesiti
  compaiono di solito.

## Unità 18 — Tangenti da un punto esterno e angolo fra due curve
- Parole: 409 su 3 pagine di traccia (70–72), conteggio del testo visibile incluse le
  formule inline.
- Rettifica: la traccia scrive $\gamma=\arctan\frac67=40^\circ$ usando un segno di
  uguale; verificato con SymPy che $\arctan(6/7)\approx40{,}6^\circ$, quindi nella pagina
  ho scritto $\approx40^\circ$. Confermati con SymPy anche tutti gli altri passaggi: $c=1$
  nel primo esempio, la fattorizzazione $(x+1)(x^2-4x+7)$ con discriminante $-12<0$, e i
  valori $m_1=-1/4$, $m_2=1/2$, $\tan\gamma=6/7$.
- Aggiunta: nulla di contenuto nuovo. Le due righe introduttive di ciascuna sezione
  spiegano perché il punto di tangenza è incognito nel primo esempio (il punto dato non
  sta sul grafico) e perché l'angolo fra due curve si riduce all'angolo fra due rette (le
  tangenti nel punto comune), idee implicite nei calcoli della traccia ma non scritte a
  parole. Nessun interattivo: entrambi gli esempi sono casi singoli senza un parametro che
  la traccia fa variare. Nessun quesito di maturità: l'unità applica la retta tangente già
  introdotta, senza aggiungere strumenti nuovi verso cui orientare un quesito.

## Unità 19 — Derivabilità e punti di non derivabilità
- Parole: 593 su 5 pagine di traccia (73–77), conteggio del testo visibile incluse le
  formule inline.
- Rettifica: nessuna. Verificati con SymPy tutti i passaggi: $f'_-(0)=-1$, $f'_+(0)=+1$
  per $f(x)=|x|$; $y'=\frac13(x-1)^{-2/3}$ con limite $+\infty$ da entrambi i lati in
  $x=1$; nell'esempio $y=|x^2-4|/(x-2)+2x^2$, i due rami semplificati $2x^2-x-2$ e
  $2x^2+x+2$, il valore comune $8$ in $x=-2$, e le derivate laterali $f'_+(-2)=-9$,
  $f'_-(-2)=-7$, tutti confermati anche con derivata numerica.
- Aggiunta: nulla di contenuto nuovo. Le uniche righe oltre al calcolo spiegano perché il
  limite della derivata di $\sqrt[3]{x-1}$ è $+\infty$ da entrambi i lati (il quadrato al
  denominatore è sempre positivo) e che cosa mostra l'esempio di $|x|$ (le due derivate
  laterali non coincidono), passaggi impliciti nella traccia ma non scritti a parole. I
  tre schemi di classificazione (flesso a tangente verticale, cuspide, punto angoloso)
  ridisegnano le sei figure già presenti in traccia, con le stesse etichette. Nessun
  interattivo: la pagina è già densa di schemi statici e nessuno di essi dipende da un
  parametro che la traccia fa variare. Nessun quesito di maturità: la classificazione dei
  punti di non derivabilità compare di norma dentro uno studio di funzione completo
  (unità 29–30), non come quesito isolato a questo punto del percorso.

## Unità 20 — Teorema di Rolle
- Parole: 417 su circa 3 pagine di traccia (78–79 intere, più la parte iniziale di 80 e
  la parte finale di 81, secondo la ripartizione già fissata in `_dati/matematica-5.json`
  fra questa unità e l'unità 21 sul teorema di Lagrange).
- Rettifica: nessuna. Verificati con SymPy tutti i passaggi dell'esempio: $f(-1)=f(1)=-1$,
  $f'(x)=4x^3-4x=4x(x+1)(x-1)$, radici $x=-1,0,1$.
- Aggiunta: un solo riquadro di nota, dopo l'esempio, che distingue i tre punti stazionari
  trovati algebricamente da quello garantito dal teorema (l'unico interno all'intervallo
  aperto, $x=0$): la traccia calcola le tre radici senza segnalare che due cadono sugli
  estremi, distinzione che si presta a un fraintendimento comune sulla portata della tesi.
  Nessun altro contenuto nuovo: le didascalie delle figure e le due righe sulle ipotesi
  spiegano a parole ciò che i disegni della traccia mostrano già. Nessun quesito di
  maturità: il teorema di Rolle isolato non è materia di quesito, e in questo punto del
  percorso non è ancora disponibile il teorema di Lagrange con cui viene tipicamente
  intrecciato.

## Unità 21 — Teorema di Lagrange e sue conseguenze
- Parole: 466 su circa 2 pagine di traccia (fondo di 80, i due terzi iniziali di 81, e
  tutta la 82; il resto di 81 — Teorema 1 — era già stato pubblicato nell'unità 20, e la
  parte finale di 83 — Teorema III sulla monotonia — apre l'unità 22).
- Rettifica: nessuna. La sola verifica richiesta era di coerenza logica: derivando
  entrambi i membri di $f(x)=g(x)+k$ si ottiene $f'(x)=g'(x)$, confermato anche
  simbolicamente con SymPy (`diff(g(x)+k, x) == diff(g(x), x)`).
- Aggiunta: nulla di contenuto nuovo. La frase che collega Teorema 1 e Teorema 2 ("Il
  primo... lo abbiamo già dimostrato") richiama in una riga un risultato già pubblicato
  nell'unità 20, senza ripeterne il riquadro, così da non duplicare contenuto già
  presente sul sito. Le quattro figure ridisegnano le quattro immagini della traccia
  (interpretazione geometrica con uno e con due punti, i due controesempi sulla necessità
  delle ipotesi, il disegno di $f$ e $g$ traslate di $k$). Nessun interattivo: nessuna
  delle costruzioni dipende da un parametro che la traccia fa variare. Nessun quesito di
  maturità: il teorema di Lagrange isolato non è materia di quesito, e il suo uso più
  frequente (De L'Hôpital, unità 24) non è ancora disponibile a questo punto del
  percorso.

## Unità 22 — Monotonia e segno della derivata prima
- Parole: 334 su circa 1,7 pagine di traccia (da "Teorema III" a fine pagina 83 fino a
  circa due terzi di pagina 84; il resto di 83 apparteneva già all'unità 21, e il fondo
  di 84 con l'invertibilità apre l'unità 23).
- Rettifica: nessuna. Verificati con SymPy $y'=12x^2-2x=2x(6x-1)$ per $y=4x^3-x^2+1$, gli
  zeri $x=0,\,x=1/6$ e il segno di $y'$ nei tre intervalli (positivo per $x<0$, negativo
  per $0<x<1/6$, positivo per $x>1/6$): tutto coincide con la traccia.
- Aggiunta: nulla di contenuto nuovo. La sola riga oltre l'enunciato e l'esempio spiega
  a parole che cosa fa il criterio (trasforma un confronto fra valori della funzione in
  uno studio di segno), idea implicita ma non scritta nella traccia. Un solo riquadro di
  nota sulla differenza fra disuguaglianza debole e stretta nella monotonia, distinzione
  che nella traccia compare come tabella ma senza il chiarimento sui punti isolati di
  annullamento. Nessun disegno: la traccia per questa unità non ne contiene (solo la
  tabella dei segni, resa come tabella HTML). Nessun interattivo: l'unico esempio è un
  caso singolo, senza parametro da far variare. Nessun quesito di maturità: un esercizio
  isolato di crescenza e decrescenza non compare come quesito a sé; la sua applicazione
  più ricca è dentro lo studio di funzione completo, ancora da venire.

## Unità 23 — Invertibilità e funzione inversa
- Parole: 364 su 4 pagine di traccia (85–88).
- Rettifica: nessuna. Verificati con SymPy tutti i passaggi: $f'(x)=1/(2\sqrt{5-x})$,
  $\lim_{x\to-\infty}f(x)=-\infty$, $\lim_{x\to5^-}f(x)=2$, la costruzione algebrica di
  $f^{-1}(x)=-x^2+4x+1=-(x-2)^2+5$ (vertice in $(2,5)$), e la verifica incrociata
  $f(f^{-1}(x))=2-\sqrt{(x-2)^2}=2-|x-2|=x$ per $x\le2$, coerente col dominio trovato
  tramite i limiti.
- Aggiunta: un solo riquadro di nota, che ribadisce lo scambio di dominio e codominio
  fra $f$ e $f^{-1}$ — già presente nella traccia come richiamo esplicito (evidenziato
  in blu) — senza introdurre contenuto nuovo. La traccia non contiene un enunciato
  formale del criterio di invertibilità, solo l'elenco puntato delle due condizioni da
  verificare (continuità e monotonia stretta) applicato all'esempio: il riquadro
  "Criterio" in apertura formalizza in poche righe quell'elenco, senza aggiungere
  nulla che l'esempio non usi. I due grafici (di $f$ e di $f^{-1}$) ridisegnano le due
  figure della traccia con coordinate calcolate esattamente dalla funzione, invece
  degli schizzi a mano libera. Nessun interattivo: l'unico esempio non dipende da un
  parametro variabile. Nessun quesito di maturità: l'invertibilità isolata non compare
  come quesito a sé in questo punto del percorso.

## Unità 24 — Teorema di Cauchy e teorema di De L'Hôpital
- Parole: 667 su 6 pagine di traccia (89–94).
- Rettifica: nessuna. Verificati con SymPy tutti e cinque gli esempi: il limite
  $(4x^2-4)/\ln x$ per $x\to1$ (risultato 8, sia diretto sia via De L'Hôpital); il
  limite $(3x+\ln x)/(2x+1)$ per $x\to+\infty$ (risultato $3/2$); il limite
  $(2x+\sin x)/(7x)$ per $x\to\pm\infty$ (risultato $2/7$ per via diretta, mentre il
  rapporto delle derivate $(2+\cos x)/7$ non ha limite, confermando che De L'Hôpital
  non è applicabile in quel caso pur non contraddicendo l'esistenza del limite
  originario); il limite $1/\sin x - 3/x$ per $x\to0^+$ (risultato $-\infty$, con
  derivata del numeratore che tende a $-2$ e del denominatore a $0^+$); il limite
  $(e^x-1)^{2x}$ per $x\to0^+$ (risultato 1, verificato anche il doppio passaggio di
  De L'Hôpital sull'esponente, con il passo intermedio $-4x/e^x\to0$).
- Aggiunta: due frasi di collegamento, nessuna delle quali introduce contenuto nuovo.
  La prima osserva che ponendo $g(x)=x$ il teorema di Cauchy si riduce al teorema di
  Lagrange (unità 21), collegamento già suggerito dalla struttura stessa delle due
  ipotesi e dalla progressione del percorso; la seconda riformula a parole, in una
  riga, che cosa fa concretamente De L'Hôpital (sostituire un limite complicato con
  quello, spesso più semplice, del rapporto delle derivate). La traccia per questa
  unità non contiene disegni: nessuna figura è stata aggiunta. Nessun interattivo:
  tutti gli esempi sono calcoli su funzioni singole, senza parametro variabile.
  Nessun quesito di maturità: i due teoremi isolati non compaiono come quesito a sé,
  e il loro impiego più ricco (dentro lo studio di funzione completo) non è ancora
  disponibile a questo punto del percorso.

## Unità 25 — Definizioni, teorema di Fermat, ricerca di massimi e minimi
- Parole: 573 su 5 pagine di traccia (95–99).
- Rettifica: nessuna. Verificati con SymPy la fattorizzazione $f'(x)=3x^2-3=3(x-1)(x+1)$,
  i punti stazionari $x=\pm1$, il segno di $f'$ sui tre intervalli (positivo per $x<-1$
  e $x>1$, negativo altrove, confermato numericamente in $x=-2,0,2$), i valori
  $f(-1)=2$ e $f(1)=-2$, e i limiti $\lim_{x\to-\infty}f(x)=-\infty$,
  $\lim_{x\to+\infty}f(x)=+\infty$: tutto coincide esattamente con la traccia.
- Aggiunta: un solo riquadro di nota, sul caso in cui il segno di $f'$ non cambia
  attorno a un punto stazionario (flesso a tangente orizzontale anziché estremo).
  Non è contenuto nuovo: la traccia stessa lo mostra a pagina 98 con lo schizzo "se
  avessi ottenuto..." accanto al segno + | +; il riquadro riformula quello schizzo con
  una mini-figura SVG e la tabella dei segni corrispondente. La figura d'apertura con i
  quattro tipi di estremo ridisegna in SVG lo schizzo di pagina 95, con etichette al
  posto delle frecce a mano libera. Nessun interattivo: l'unico esempio è un caso
  singolo, senza parametro da far variare. Nessun quesito di maturità: è la prima unità
  dell'area massimi-minimi-flessi, e la sua applicazione più ricca è dentro lo studio di
  funzione completo, ancora da venire.

## Unità 26 — Estremi di funzioni non derivabili o discontinue
- Parole: 515 su 4 pagine di traccia (100–103).
- Rettifica: nessuna. Verificati con SymPy la derivata di $|x|$ ($+1$ per $x>0$,
  $-1$ per $x&lt;0$) e i limiti $\lim_{x\to\pm\infty}|x|=+\infty$; verificati per
  sostituzione diretta (il limite simbolico su Piecewise di SymPy dava un risultato
  errato per bug noto della libreria) i valori dell'esempio finale: $f(-2)=-2$,
  $f(x)\to3$ per $x\to2^-$, $f(x)\to0$ per $x\to0^-$, $f(x)\to1$ per $x\to0^+$. Tutto
  coincide con la traccia.
- Aggiunta: nessuna. Le quattro figure dei casi di discontinuità e le due figure dei
  segni generali (estremo / flesso a tangente verticale) ridisegnano in SVG gli schizzi
  di pagina 101–102, senza aggiungere casi non presenti. Nessun interattivo: il
  contenuto è qualitativo e non ha un parametro naturale da far variare. Nessun quesito
  di maturità: gli estremi in punti singolari non compaiono come quesito isolato, e il
  loro impiego più ricco è dentro lo studio di funzione completo, ancora da venire.

## Unità 27 — Concavità, derivata seconda e flessi
- Parole: 609 su circa 4,4 pagine di traccia equivalenti (104–107 intere, più la prima metà
  di 108, fino alla conclusione dell'esempio $\sqrt[3]{x-2}$; la seconda metà di 108, che
  apre con "Ricerca di massimi, minimi e flessi con le derivate successive", appartiene
  all'unità 28).
- Rettifica: nessuna. Verificati con SymPy e per via numerica (radice cubica reale, la
  potenza frazionaria di SymPy su base negativa segue il ramo principale complesso e non è
  utilizzabile qui) tutti i passaggi: $f''=2$ e $f''=-2$ per le due paraboie di apertura;
  $f(x)=2x^3-5$ con $f'=6x^2$, $f''=12x$, flesso in $x=0$; $f(x)=4x^3-3x+1$ con
  $f'=12x^2-3$, $f''=24x$, $f'(0)=-3$, flesso obliquo; $y=\sqrt[3]{x-2}$ con
  $y'=1/(3\sqrt[3]{(x-2)^2})$, $y''=-2/(9\sqrt[3]{(x-2)^5})$, $y''>0$ per $x<2$ e $y''<0$
  per $x>2$ (verificato numericamente con derivate a differenze finite), e
  $\lim_{x\to2^\pm}y'(x)=+\infty$, che conferma il flesso verticale in $x=2$ scritto in
  traccia.
- Aggiunta: nulla di contenuto nuovo. L'unico interattivo riusa l'esempio $f(x)=2x^3-5$
  della traccia, con un cursore su $x_0$ che mostra la tangente e il valore di $f''(x_0)$
  cambiare segno attraversando il flesso in $0$, la stessa idea del disegno statico della
  traccia resa dinamica. La figura dei tre tipi di flesso (orizzontale, verticale, obliquo)
  ridisegna in SVG i tre schizzi della traccia. Nessun quesito di maturità: ho cercato
  quesiti reali isolati su concavità e flessi (non innestati in uno studio di funzione
  completo con parametri o altri strumenti) senza trovarne uno adatto al solo bagaglio di
  questa unità; un quesito di questo tipo è più naturale una volta disponibile lo studio di
  funzione completo (unità 29–30).

## Unità 28 — Derivate successive e tangente inflessionale
- Parole: 356 su circa 2,5 pagine di traccia equivalenti (seconda metà di 108, dove
  inizia "Ricerca di massimi, minimi e flessi con le derivate successive", più 109 e 110
  intere, fino alla fine dell'esempio della tangente inflessionale).
- Rettifica: nessuna. Verificati con SymPy tutti i calcoli: $f(x)=x^8-x^7+x^3$ con
  $f'=8x^7-7x^6+3x^2$, $f''=56x^6-42x^5+6x$, $f'''=336x^5-210x^4+6$, e
  $f'(0)=f''(0)=0$, $f'''(0)=6$; $f(x)=4x^3-3x+1$ con $f'(0)=-3$, $f(0)=1$ e tangente
  inflessionale $y=1-3x$.
- Aggiunta: nulla di contenuto nuovo. La figura a tre pannelli (massimo, minimo, flesso
  orizzontale) ridisegna in SVG gli schizzi di pagina 108 con le condizioni su $f'$ e
  $f''$ già scritte in traccia. Non ho ridisegnato i due pannelli di pagina 109 su flesso
  verticale e obliquo, perché la loro classificazione (stesse condizioni su $f'$ e $f''$)
  è già nella figura e nel riquadro "Classificazione" dell'unità 27: ripeterla qui sarebbe
  stata un'aggiunta di forma, non di contenuto. Nessun interattivo: il criterio delle
  derivate successive è un procedimento discreto (si deriva finché non si trova un valore
  non nullo), senza un parametro continuo naturale da mettere su un cursore. Nessun
  quesito di maturità: l'argomento, isolato dal resto dello studio di funzione, non è
  materia di un quesito a sé; il suo impiego naturale è dentro lo studio completo delle
  unità 29–30.

## Unità 29 — Schema generale in otto passi
- Parole: 408 su 4 pagine di traccia (111–114).
- Rettifica: nessuna. Verificati con SymPy le derivate e gli zeri dell'esempio
  $f(x)=x-x^3$: $f'(x)=1-3x^2$, zeri $x=\pm1/\sqrt3$, con $f(\pm1/\sqrt3)=\pm2\sqrt3/9
  \approx\pm0{,}385$ (arrotondato a $\pm0{,}4$ in traccia); $f''(x)=-6x$, zero $x=0$,
  segno concorde con lo schizzo (concavità verso l'alto per $x<0$, verso il basso per
  $x>0$).
- Aggiunta: nulla di contenuto nuovo. Ho reso la lista degli otto passi con una
  numerazione a cerchietti invece del semplice "1) 2) 3)..." della traccia, per
  leggibilità, ma i passi e il loro contenuto sono esattamente quelli della traccia. La
  figura dell'esempio ridisegna in SVG lo schizzo di pagina 114 (grafico con zeri in
  $-1,0,1$, punti di massimo e minimo con $y\approx\pm0,4$, schema di segno di $f'$).
  Nessun interattivo: questa unità è un elenco procedurale di controllo, non una
  costruzione che varia con un parametro.

## Unità 30 — Studio completo svolto: f(x) = x − x³
- Parole: 468 su 3 pagine di traccia (115–117).
- Rettifica: nessuna. Verificati con SymPy tutti i passaggi: $f'(x)=1-3x^2$ con zeri
  $x=\pm1/\sqrt3$ e $f(\pm1/\sqrt3)=\pm2\sqrt3/9\approx\pm0{,}385$ (arrotondato a
  $\pm0{,}4$, come in traccia); $f''(x)=-6x$, zero $x=0$, $f'(0)=1$, tangente
  inflessionale $y=x$; limiti $\lim_{x\to\pm\infty}f(x)=\mp\infty$ e
  $\lim_{x\to+\infty}f(x)/x=-\infty$, quindi nessun asintoto orizzontale né obliquo,
  coerente con la traccia. Confermata anche la tabella dei segni di $x(1+x)(1-x)$.
- Aggiunta: un quesito d'esame (punto 5 della struttura richiesta per la matematica di
  quinta), rimandato esplicitamente dalle unità 27 e 28 a "quando sarà disponibile lo
  studio di funzione completo (29–30)". Ho scelto il quesito 1 del questionario di
  Esame di Stato 2019, sessione ordinaria, liceo scientifico (fonte: testo ufficiale
  del questionario, riportato anche su matematica.it a cura di L. Tomasi), perché
  richiede solo strumenti già disponibili a questo punto del percorso: ricostruzione di
  una funzione razionale da asintoti e intersezioni, derivata con la regola del
  quoziente, massimi e minimi relativi dal segno di $f'$. Verificato con SymPy:
  $f(x)=(5x^2-12x)/(x^2-9)$, $f'(x)=6(x-6)(2x-3)/(x^2-9)^2$, massimo relativo in
  $x=3/2$ con $f(3/2)=1$, minimo relativo in $x=6$ con $f(6)=4$, in accordo con la
  soluzione ufficiale. Nessuna figura nuova: il grafico completo della funzione
  dell'unità resta quello già disegnato nell'unità 29, qui solo richiamato a parole;
  nessun interattivo, perché la pagina è un elenco di calcoli su un caso già fissato,
  senza un parametro naturale da variare.

## Unità 31 — Primitive, integrale indefinito, proprietà
- Parole: 306 su 3 pagine di traccia (118–120).
- Rettifica: nessuna. Verificati con SymPy $D(x^2+C)=2x$, $D(x^2+2)=2x$, $D(x^2+12)=2x$ e
  $D(\sin x+C)=\cos x$, in accordo con la traccia.
- Aggiunta: nulla di contenuto nuovo. La figura a tre insiemi annidati (integrabili,
  continue, derivabili) ridisegna in SVG lo schema di pagina 120, riusando la stessa
  coppia di ellissi già impiegata per continue/derivabili nell'unità 19, con
  un'ellisse esterna in più per le integrabili. Il riquadro "Attenzione" riporta le
  due uguaglianze di prodotto e quoziente barrate in rosso nella traccia, presentate
  come ciò che NON vale: è materiale già presente, solo reso in prosa. Nessun
  interattivo: l'unità è fatta di sole definizioni e proprietà, senza un oggetto che
  vari con un parametro. Nessun quesito di maturità: l'unità introduce solo notazione
  e proprietà generali, senza calcolo di un integrale specifico su cui costruirne uno.

## Unità 32 — Integrali immediati
- Parole: 237 su 3 pagine di traccia (121–123).
- Rettifica: nessuna. Verificati con SymPy tutti gli integrali della tavola e i sette
  esempi svolti: $\int\sqrt{x^3}\,dx=\tfrac{2}{5}\sqrt{x^5}+C$, $\int 2x^3\,dx=x^4/2+C$,
  $\int(3x^2+2)/x\,dx=\tfrac32x^2+2\ln|x|+C$, $\int(2e^x+5^x)\,dx=2e^x+5^x/\ln5+C$,
  $\int(3\sin x-4/\cos^2x)\,dx=-3\cos x-4\tan x+C$, e
  $\int(1/(3\sqrt{1-x^2})+7/(1+x^2))\,dx=\tfrac13\arcsin x+7\arctan x+C$: tutti
  coincidono con la traccia.
- Aggiunta: nulla di contenuto nuovo. La tavola raccoglie in una sola tabella (stesso
  formato `.tabellina` già usato nell'unità 14 per le derivate) le dodici formule
  boxate in verde nella traccia, comprese le due righe di arccos e arccot presentate
  come "segno opposto" delle righe di arcsin e arctan, così come compaiono affiancate
  nella traccia. Il riquadro "Attenzione" spiega solo perché arccos e arccot non sono
  formule indipendenti, un chiarimento implicito nella disposizione della traccia.
  Nessun disegno: l'unità è una tavola di formule senza schemi. Nessun interattivo:
  non c'è un parametro naturale da far variare. Nessun quesito di maturità: l'unità è
  strumentale (tavola di consultazione), come già l'unità 14 con le derivate.

## Unità 33 — Integrali di funzioni composte
- Parole: 243 su 1,4 pagine di traccia (124, e la parte superiore di 125 fino agli esempi
  di tangente e cotangente incluso).
- Rettifica: nessuna. Verificati con SymPy tutti i passaggi: $D[(\sin x)^5/5]=(\sin x)^4\cos x$
  (da cui l'errore evidenziato in rosso nella traccia, dove $(\sin x)^5/5$ viene proposto e
  poi scartato come primitiva di $(\sin x)^4$ da solo); $\int 3x^2(x^3+2)^2\,dx=(x^3+2)^3/3+C$
  (derivata verificata uguale a $3x^2(x^3+2)^2$); $\int(2x-3)^2\,dx=(2x-3)^3/6+C$ (derivata
  uguale a $(2x-3)^2$); $\int\tan x\,dx=-\ln|\cos x|+C$ e $\int\cot x\,dx=\ln|\sin x|+C$
  (derivate uguali a $\tan x$ e $\cot x$ rispettivamente, fuori dai punti di annullamento
  di seno e coseno). Tutto coincide con la traccia.
- Aggiunta: nulla di contenuto nuovo. Il riquadro "Attenzione" ripropone l'errore già
  presente nella traccia (barrato in rosso) come esempio guida, invece di limitarsi a
  descriverlo: è lo stesso materiale, solo introdotto per primo perché è il punto di
  partenza del ragionamento nella traccia stessa. Non ho incluso l'inizio del paragrafo
  "Integrazione per sostituzione" che compare in fondo a pagina 125: appartiene
  all'unità 35, che lo tratta per intero. Nessun disegno: la traccia non ne contiene.
  Nessun interattivo: non c'è un parametro naturale da far variare, sono esempi puntuali
  di riconoscimento di struttura. Nessun quesito di maturità: l'unità introduce solo la
  tecnica del riconoscimento $f'(x)\cdot g(f(x))$ su casi elementari, senza un problema
  autosufficiente a questo livello.

## Unità 34 — Integrazione per parti
- Parole: 228 su 2 pagine di traccia (126–127).
- Rettifica: nessuna. Verificati con SymPy entrambi gli esempi: $D[(x^2/2)\ln x - x^2/4] =
  x\ln x$ e $D[x\ln x - x] = \ln x$, in accordo con la traccia.
- Aggiunta: nulla di contenuto nuovo. La derivazione della formula dalla regola del
  prodotto è quella della traccia, così come i due esempi $\int x\ln x\,dx$ e
  $\int\ln x\,dx$. Non ho riportato la tabellina f/g/f'/g' della traccia in forma di
  tabella, ma inline nel testo: stesso contenuto, un formato più compatto. Nessun
  disegno: la traccia non ne contiene. Nessun interattivo: sono due esempi puntuali
  di una tecnica, senza un parametro naturale da variare. Nessun quesito di maturità:
  l'unità introduce solo la tecnica su casi elementari, come già le unità 31-33.

## Unità 35 — Integrazione per sostituzione
- Parole: circa 100 su 0,5 pagine di traccia (la metà inferiore di pagina 125, dopo
  gli integrali di tangente e cotangente dell'unità 33 e prima dell'inizio
  dell'integrazione per parti a pagina 126).
- Rettifica: nessuna. Verificato con SymPy l'unico esempio della traccia: con la
  sostituzione $t=\sqrt x$, $x=t^2$, $dx=2t\,dt$, si ha
  $\int\frac{1}{1+\sqrt x}\,dx=2\sqrt x-2\ln(\sqrt x+1)+C$; la derivata di questa
  primitiva, semplificata, coincide con $1/(1+\sqrt x)$. Coincide con la traccia.
- Aggiunta: nulla di contenuto nuovo. La traccia contiene solo il titolo e questo
  unico esempio svolto, senza una formula generale del cambio di variabile: la pagina
  segue lo stesso taglio, con il solo esempio commentato passo per passo. Nessun
  disegno: la traccia non ne contiene. Nessun interattivo: un solo esempio puntuale
  non offre un parametro naturale da far variare. Nessun quesito di maturità: l'unità
  è troppo breve e circoscritta a un'unica tecnica su un caso elementare.
