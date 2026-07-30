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
