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
