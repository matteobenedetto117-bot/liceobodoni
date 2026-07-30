# Registro delle modifiche — Matematica quinta

Questo file è per l'insegnante: raccoglie le correzioni fatte rispetto alla traccia manoscritta
e le eventuali variazioni di proporzione. Non è visibile agli studenti e non è collegato dalle
pagine del sito.

## Unità 01 — Definizioni di limite, intorni, limite destro e sinistro
- Nessuna rettifica: i passaggi della traccia sono corretti. Verificati con SymPy la
  semplificazione di (2x²−6x)/(x−3), il limite in 3 e l'equivalenza |2x−6|<ε ⟺ |x−3|<ε/2.
- Ricalibrazione: nessuna riduzione. La trattazione è stata ampliata sul versante esplicativo,
  costruendo l'idea intuitiva di limite prima della definizione formale.

## Unità 02 — Verifica di un limite e primo sguardo agli asintoti
- Nessuna rettifica: verificati con SymPy il limite di 1/(x−1)² in 1 e la soglia δ = 1/√M.
- Titolo modificato da "Verifica di un limite e primi asintoti" per rendere esplicito che qui
  gli asintoti sono trattati solo qualitativamente.
- Rimandato all'unità 11: ricerca sistematica degli asintoti, asintoti obliqui, e i quesiti
  d'esame che ne richiedono la determinazione con parametri.

## Unità 03 — Teoremi sui limiti: unicità, permanenza del segno, confronto
- Rettifica: nessun errore matematico nella traccia. Corretta però l'indicazione delle pagine:
  il campo del JSON indicava "11, 18–22", ma il teorema del confronto occupa solo le pagine
  18–19 (più l'inizio di pagina 20); da metà pagina 20 in poi (e nelle pagine 21–22) la traccia
  passa già ai limiti notevoli, materiale dell'unità 06. Ho quindi usato solo le pagine 18–19
  per questa unità, lasciando 20–22 all'unità 06.
- Verificati con SymPy: lim (3+cos x)/x per x→+∞ = 0; lim x²·sin(1/x) per x→0 = 0; lim k/x
  per x→+∞ = 0 (k=2,4); lim x² e lim(−x²) per x→0 = 0.
- Ricalibrazione: ampliata la parte esplicativa rispetto alla traccia, che presenta gli
  enunciati e un solo esempio (il confronto). Ho aggiunto le dimostrazioni complete di
  unicità e permanenza del segno (assenti come tali nella traccia, che riporta solo
  l'enunciato), un controesempio per la permanenza del segno (f(x)=x, l=0) e
  un'osservazione sul viceversa (disuguaglianza debole vs stretta, con f(x)=x²), oltre a un
  secondo esempio svolto sul confronto (x²·sin(1/x)) per bilanciare il peso "alto" assegnato
  all'unità nel percorso.

## Unità 04 — Calcolo dei limiti e algebra dei limiti
- Rettifica: a pagina 11 la traccia riporta $\lim_{x\to -1}\sqrt{x}=7$, ma con $x_0=-1$ la
  radice non è definita (dominio $x\geq 0$) e $\sqrt{-1}$ non è nemmeno un numero reale.
  Il valore 7 è compatibile solo con $\sqrt{49}$: ho quindi corretto il punto in $x_0=49$,
  scrivendo $\lim_{x\to 49}\sqrt{x}=7$, che è l'unica lettura sensata dell'esempio.
- Confini di pagina: la parte finale di pagina 11 ("Calcolo di limiti", funzioni continue in
  x0) appartiene a questa unità e non all'unità 03, come già indicato nel registro dell'unità 03
  stessa. Ho usato la coda della pagina 11 insieme alle pagine 12–13, fermandomi prima di
  "Forme indeterminate" che apre la pagina 14 (unità 05).
- Verificati con SymPy tutti i limiti della pagina (funzioni continue, comportamento agli
  estremi del dominio, i quattro esempi di somma/prodotto/quoziente/potenza) e l'esempio di
  sintesi aggiunto, $\lim_{x\to2}\left[\frac{x^3+1}{x+3}+\sqrt{x+2}\right]=\frac{19}{5}$.
- Ricalibrazione: nessuna riduzione. Ho aggiunto un esempio svolto per la regola del quoziente,
  assente nella traccia (che riporta solo la formula generale), e un esempio di sintesi finale
  che combina sostituzione, quoziente e somma nello stesso calcolo, per compensare il fatto che
  gli esempi della traccia sono tutti isolati e su una sola regola alla volta.
