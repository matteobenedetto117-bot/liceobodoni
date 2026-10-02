# Revisione automatica di un'unità — sito "Liceo Bodoni"

Esecuzione notturna, senza nessuno presente. **Non fare domande.** Ogni dubbio si risolve con le regole del §8 e si annota nel registro.
Modelli da copiare (stile, script, figure): fisica-5 unità 01–03; fisica-4 unità 01–07; matematica-5 unità 01–03.
Il token GitHub è nel prompt dell'attività programmata, non qui. L'elenco delle unità è in `_build/coda-notturna.txt`.

---

## 0. Un'unità per esecuzione

L'attività parte ogni mezz'ora, dalle 22:00 alle 7:30. **Ogni esecuzione lavora una sola unità.**

1. **Semaforo.** Leggi `_build/stato-notturno.txt` (non versionato).
   * Se contiene `occupato <data-ora>` meno vecchio di 2 ore: un'altra esecuzione è in corso. Termina subito, senza toccare nulla, con il messaggio "esecuzione precedente ancora in corso".
   * Altrimenti scrivici `occupato <data-ora attuale ISO>` (sovrascrivendo: non cancellare file) e procedi.
2. **Coda.** In `_build/coda-notturna.txt` prendi la prima riga non di commento senza esito (`<classe> <NN>` oppure `<classe> <NN> rifare`). Se non ce ne sono: scrivi `libero` nel semaforo e termina con "coda esaurita".
3. Esegui il ciclo del §1 su quell'unità sola.
4. **Esito.** Aggiungi alla riga della coda ` | pubblicata <hash>`, ` | saltata (già revisionata)` oppure ` | non pubblicata: <motivo breve>`. La coda si versiona nello stesso commit dell'unità (o in un commit a sé se l'unità non è pubblicata).
5. **Report.** In `_registro/report-notturno.md` la sezione è quella della notte, intestata con la data della sera d'inizio (le esecuzioni fra 0:00 e 8:00 appartengono alla sera prima): aggiungi una riga con l'esito dell'unità. Nessun report "di fine sessione" a parte.
6. **Uscita**, anche in caso di errore: scrivi `libero` nel semaforo.

Un'unità saltata (già revisionata) non consuma l'esecuzione: segna l'esito e passa alla riga successiva, fino a una unità da lavorare.

---

## 1. Ciclo per l'unità

Per l'unità presa dalla coda:

1. **Salta** l'unità se in `_registro/<classe>.md` ha già la riga "Revisione:", **tranne** quando la riga della coda termina con `rifare`: in quel caso l'unità è stata revisionata con regole superate e va rifatta. Riparti dalla pagina attuale, recupera testo e titoletti tolti dalla versione precedente alla revisione (`git log` sulla cartella, poi `git show <hash>^:<file>`) e riscrivila secondo il §3; tieni impaginazione e figure interattive già fatte, correggendole solo se serve. Nel registro sostituisci la riga "Revisione:" esistente con quella nuova.
2. Individua `<classe>/argomenti/NN-slug/index.html` (il numero della cartella può non coincidere con quello dell'unità: fa fede `_dati/<classe>.json`, campo `cartella`). Leggi la pagina, la voce del registro e quella del JSON.
3. Riscrivi il testo (§3), applica l'impaginazione (§4), rifai le figure (§5).
4. Verifica (§6). Se la verifica non passa dopo 3 tentativi di correzione: **non pubblicare quell'unità**, ripristina i file (`git checkout -- <cartella>`), scrivi il motivo nel report (§7) e passa alla successiva.
5. Aggiorna registro, barra di navigazione, indici (§7), poi commit e push (§2). Un commit per unità.

Un'unità non pubblicata non blocca la coda: l'esecuzione successiva passa alla riga dopo.

---

## 2. Repository e pubblicazione

* Repo `matteobenedetto117-bot/liceobodoni`, branch `main`, pubblicato con GitHub Pages.
* Si lavora **solo** nella cartella locale collegata: `D:\Documents\Lavoro\Scuola\Bodoni\2026_2027\liceobodoni` (in `device_bash`: `$HOME/mnt/liceobodoni`). Il push dal sandbox cloud è bloccato: non provarlo.
* Se la cartella non è raggiungibile: riprova una volta; se fallisce ancora, termina e scrivi nel messaggio finale che il lavoro non è iniziato.
* Inizio esecuzione: `git pull` (via `git-sicuro.sh`). Se il repo locale ha commit non ancora inviati, il primo push li invia insieme.
* **Nessuna richiesta di permesso di cancellazione** (di notte nessuno può rispondere). Nella cartella collegata git non riesce a cancellare i propri `.lock`: **esegui ogni comando git con `bash _build/git-sicuro.sh <argomenti>`** (per esempio `bash _build/git-sicuro.sh commit -m …`), che dopo il comando sposta i `.lock` rimasti in `.git/_to_delete/`. Gli avvisi `unable to unlink … tmp_obj_…` sono innocui. Esegui i comandi git uno alla volta, mai in parallelo.
* Identità (config locale): `user.name = Claude`, `user.email = noreply@anthropic.com`.
* Commit: `<classe> unità NN: <sintesi>` + righe di attribuzione richieste dalla sessione.
* Push, token solo nell'URL del comando, mai salvato nel remote:
  `git push -q https://x-access-token:<TOKEN>@github.com/matteobenedetto117-bot/liceobodoni.git main`
* Il push può superare i 180 s di `device_bash`: lancialo in background e controlla con `git ls-remote <URL> main` confrontando l'hash con `git log --oneline -1`. Non ripetere un push già riuscito. Se al termine l'hash remoto non coincide dopo 3 controlli a distanza di un minuto, segnalalo nel report.
* Se `git pull` o il push fallisce per conflitto: `git pull --rebase`, poi riprova una volta; se persiste, non pubblicare e segnala.

### Come si modificano i file
* Piccole modifiche: script Python di lettura-modifica-scrittura su `device_bash` (mai ricopiare a mano il contenuto).
* Riscritture grandi e figure calcolate: costruisci il file nel sandbox, poi scrivilo nella cartella con `device_commit_files` (`force: true`, `stagedPath`).
* **Prima di scrivere una copia costruita nel sandbox, fai `diff` con il file sul disco** e riporta le differenze (numero unità, occhiello, piè di pagina, pulsanti precedente/successiva). Una copia vecchia ha già fatto tornare indietro numero e navigazione.

---

## 3. Testo: sintetico, schematico, ben leggibile

Gli studenti copiano la pagina sul quaderno. La pagina è una traccia: le spiegazioni le dà il docente a voce, ma ciò che è scritto deve potersi rileggere e capire da solo.

**Si mantiene**: definizioni, leggi, formule, unità di misura, esempi, figure e le frasi che collegano un passaggio al successivo quando servono a capire.
**Si elimina**: premesse lunghe, cenni storici, aneddoti, ripetizioni, rimandi ad altre unità, spiegazioni che ripetono ciò che formula o figura mostrano già.

Regole:
* **Frasi complete**, con soggetto e verbo, e ben leggibili. Niente stile telegrafico né frasi nominali in serie (non "Pressione costante: volume proporzionale a T", ma "Se la pressione resta costante, il volume è direttamente proporzionale alla temperatura assoluta").
* Sintesi sì, ma senza togliere il ragionamento: se un passaggio richiede due o tre frasi per essere chiaro, si tengono.
* Elenchi puntati dove i contenuti sono davvero un elenco (proprietà, casi, condizioni); altrimenti brevi paragrafi di due o tre frasi. Una voce di elenco può occupare fino a tre righe.
* Registro neutro e tecnico: niente frasi evocative, metaforiche o colloquiali.
* Introduzione: una o due frasi che dicono di che cosa tratta l'unità, oppure nessuna se il titolo basta.
* Definizioni e leggi in riquadro `.def`; avvertenze in `.nota` (una o due frasi).
* Formule in evidenza (§4), con la legenda dei simboli in una frase.
* Esempio: dati, formula, calcolo e risultato, con una breve frase di collegamento fra i passaggi quando serve.
* Didascalie: una frase completa.
* Nessun simbolo di proporzionalità (∝, `\propto`, `&prop;`): "direttamente proporzionale a…".
* Unità: volumi in m³ (notazione esponenziale se scomodi, oppure fattore sull'asse: "V (10⁻⁵ m³)"), pressioni in Pa o kPa, temperature in K.
* Titolo: quello attuale, in `<h1>` e `<title>` ("Titolo — Fisica quarta").
* Togli `<p class="sommario">`: restano link "← Classe", occhiello "Argomento · Unità NN", titolo.
* Togli sezioni "Nelle prossime unità".
* Le unità già revisionate indicate come modelli valgono per impaginazione, script e figure, **non per la lunghezza del testo**, che in quelle pagine è troppo ridotta.

### Titoletti
* **Si tengono gli `<h2>` che aprono una sezione dell'unità**: un nuovo concetto, una nuova legge, un caso diverso, un procedimento. Il titoletto è breve e descrittivo (per esempio "Trasformazione isobara", "Regola del prodotto").
* Si tolgono solo i titoletti superflui: quelli che coprono una o due righe, quelli che ripetono il titolo dell'unità, quelli generici ("Introduzione", "Riepilogo", "In sintesi") e "Nelle prossime unità".
* Gli esempi hanno il titoletto "Esempio" ("Esempio 1", "Esempio 2" se sono più d'uno).
* Se gli esempi sono più di due, tienine due (i più rappresentativi) e registra quali sono stati tolti.

### Controllo concettuale (obbligatorio)
Rileggi testo, formule e disegni; verifica calcoli, limiti e unità con SymPy o Python. Correggi in modo sobrio, senza citare argomenti non trattati, e registra ogni correzione. Errori già incontrati, da cercare:
* ago "indica il nord" → "si allinea approssimativamente lungo la direzione nord–sud"; "non esistono monopoli" → "non sono mai stati osservati"; linee di campo "all'esterno del magnete";
* "barometro" → "manometro" per un gas chiuso;
* rette V–t e P–t a −273,15 °C solo per gas rarefatto; nessun gas ci arriva (prima liquefa);
* leggi dei gas valide per quantità di gas data; proporzionalità con la temperatura assoluta;
* reversibile = trasformazione percorribile al contrario riportando sistema **e ambiente** allo stato iniziale;
* k ≈ 1,38×10⁻²³ J/K, N_A ≈ 6,022×10²³ mol⁻¹ (definite dal 2019);
* asintoto verticale: forma compatta con ±∞, basta uno dei quattro casi unilaterali;
* i disegni devono coincidere coi valori scritti (un ramo che parte da −1,96 non ha il pallino vuoto a −3/2).

---

## 4. Impaginazione "a quaderno"

Copia il blocco `<style>` e lo script da un'unità già revisionata (fisica-4 unità 06 per la fisica; matematica-5 unità 02 per esercizi e comandi a comparsa).

* `html{font-size:165%}`, `:root{--r:1.8rem}` (distanza fra righe). Sfondo del `body` a righe ogni `--r`, riga a `1.3rem` dall'inizio del rigo; `line-height:var(--r)`.
* `h1` 2.4rem, interlinea `2*var(--r)`, spostato giù .5rem; `h2` 1.45rem, interlinea `var(--r)`, `margin-top:var(--r)`; intestazione senza bordo.
* `.foglio` e `header.testata`: `display:flex; flex-direction:column`. `.nota` e `.def`: `display:flow-root`.
* Margini sempre multipli di `--r`.
* Formule: `<p class="eq">$$…$$</p>` in riquadro azzurro:
  `.foglio>.eq{background:var(--blu-chiaro);border-radius:10px;padding:calc(var(--r)*.5) 22px;font-size:1.1rem}`.
  Principio in rosso: `.foglio>.eq.principio{background:#f6e4e2;color:var(--rosso);font-weight:600}`.
  **`.foglio>.eq` vale solo per i figli diretti**: dentro `.def`, `.es`, `.passo` serve una regola propria, altrimenti il riquadro sparisce. Mantieni il riquadro su tutte le formule in evidenza.
* `.def`: bordo sinistro blu, fondo bianco. `.nota`: bordo sinistro rosso, fondo `#fdf6f5`. Etichetta `<span class="et">` in maiuscoletto.
* Elenchi: margini in multipli di `--r`.
* Didascalie `.fig .did`: `font-size:.9rem`, interlinea 1.4.
* **Script di allineamento** in fondo alla pagina: sposta titoli, paragrafi, elenchi, figure, note e barra di navigazione alla riga successiva. Esposto come `window.allineaQuaderno`, rilanciato a `startup.pageReady` di MathJax, a ogni ridimensionamento e dopo ogni comando che mostra o nasconde qualcosa.

---

## 5. Figure

### Regole generali
* **Non aggiungere figure.** Le esistenti si ridisegnano e si rendono interattive. Una figura solo decorativa si lascia com'è e si segnala nel report ("figura decorativa: valutare se toglierla").
* **SVG inline disegnato da script interno alla pagina**, senza librerie esterne. Le pagine con Plotly si riscrivono così. Per la matematica riusa l'aiuto di matematica-5 (`el`, `txt`, `num`, `Piano` con `X`, `Y`, `assi`, `curva`, `add`, gruppi `sotto`/`sopra`/`testo`).
* Colori dalle variabili: `--inchiostro`, `--blu`, `--blu-chiaro`, `--rosso`, `--verde`, `--grigio`, `--riga`. Magneti: N rosso, S blu; forze rosse. Grafici: curva principale inchiostro o blu; confronti e asintoti rosso tratteggiato; limite verde tratteggiato; punto mobile rosso.
* Scritte nei disegni piccole (11–14 unità del viewBox) e poche; i valori correnti stanno accanto al cursore.
* Forma **calcolata**, non tracciata a occhio: isoterme P = nRT/V; altezze del pistone proporzionali al volume; linee di campo integrate numericamente; rette dei gas in scala fino a −273,15 °C; soglie dei limiti calcolate numericamente.
* Campionamento scelto secondo la funzione (per esempio `x·sin(1/x)` uniforme in `u = 1/x`); spezza il tracciato dove la funzione non è definita o esce dal riquadro.
* Coerenza fra pannelli della stessa figura (stesso gas → stesso numero di particelle).
* Disegno più stretto della colonna: `style="width:100%;max-width:420px"`, contenuto centrato nel viewBox.
* Etichette leggibili: niente testo bianco fuori da aree colorate, niente sovrapposizioni con curve, assi o bordi.

### Figure a più parti
* Pannelli affiancati: `<div class="did-parti" style="--n:3">` con un `<p class="did">` per pannello.
* Righe sovrapposte: didascalia come testo SVG sotto la riga (`font-size="14"`, `fill="var(--grigio)"`).

### Figure interattive
Rendi interattivo ogni disegno in cui il movimento aiuta a capire.
* **Cursore oppure ▶, mai entrambi nella stessa figura.** Preferito il cursore: `input type="range"` in `div.cursore`, etichetta della grandezza e valore a fianco. Due cursori: su due righe, oppure sulla stessa riga con `style="width:min(220px,30%)"`.
* ▶ (`&#9654;`) / ↺ (`&#8634;`) solo per sequenze senza parametri da regolare: `.btn-anim`, larghezza 3rem, `aria-label` "Avvia"/"Ricomincia", stati fermo → in corso (disabilitato) → finito (↺ ripristina).
* Grafici di funzione: il cursore muove un punto sulla curva **già disegnata per intero**; a fianco compaiono $x$, $f(x)$ e le altre grandezze, con una parola in verde quando si entra nella condizione che conta. Due rami separati da un asintoto: il cursore percorre prima l'uno, poi l'altro.
* `requestAnimationFrame`; rispetto di `prefers-reduced-motion` (stato statico).
* Particelle di gas: simulazione vera (posizione e velocità in pixel al secondo, urti elastici su pareti e pistone). Modulo della velocità **indipendente dal volume**. Sempre in movimento. Quando il pistone entra nel gas, riporta le particelle dentro con un modulo. Velocità `55·(T/100)^1.8`.
* Moto fisicamente sensato (l'attrazione accelera avvicinandosi; una repulsione accelera poi rallenta per attrito; un ago su galleggiante oscilla smorzandosi; le forze compaiono quando agiscono). Scritte esplicative in dissolvenza alla fine.
* Utili: tratteggi con etichette "1" e "2" (stati iniziale e finale); piccolo pistone accanto al grafico P–V.

### Esercizi e passaggi a comparsa (matematica)
* Un risultato per volta: quesito in `.es > p.eq.quesito` (riquadro azzurro) con tasto `.btn-ris` ("risultato" / "nascondi"); risultato in riquadro verde chiaro con `hidden`. All'apertura nessun risultato è visibile.
* Tasto `.btn-tutti` ("Mostra tutti i risultati" / "Nascondi tutti i risultati") subito dopo l'introduzione.
* Catene di passaggi: ogni passaggio = riga grigia di spiegazione **brevissima** + formula; tasto "passo successivo" e ↺. All'apertura nessun passaggio visibile.
* Lista di casi: a sinistra quesito e tasto, a destra il grafico (`div.es-fig`, griglia `1fr 250px`, una colonna sotto i 700px); **tratto rosso più spesso** dove si percorre la curva per il limite richiesto.
* MathJax compone anche il contenuto `hidden`: mostra/nascondi solo con `hidden`/`display:none`, mai inserendo HTML nuovo. Dopo ogni comparsa: `window.allineaQuaderno()`.

### Modelli
* fisica-5 u.01: magnetite, ago, galleggiante, poli, taglio del magnete. u.03: tre casi della carica, cursore su θ.
* fisica-4 u.01: raffreddamento V–t, manometro P–t, immissione di particelle, siringa. u.03: compressione isoterma, isoterma in Clapeyron con pistone, famiglia di isoterme. u.04: pistone con peso, isobaro e isocoro fra isoterme, recipiente rigido.
* matematica-5 u.01: fascia ε e intorno δ, salto, esplosione con soglia M, gallerie di asintoti, smorzata con soglia c. u.02: esercizi a comparsa con grafici. u.03: salto, permanenza del segno (due pannelli), corridoio fra parabole.

---

## 6. Verifica automatica (prima di ogni commit)

Con Playwright nel sandbox cloud (Chromium in `/opt/pw-browsers/chromium`), pagina portata con `device_stage_files`:
1. Nessun `pageerror` (`node --check` sul codice se è lungo).
2. Screenshot della pagina intera e di ogni figura; per ogni figura interattiva screenshot con il cursore in almeno due posizioni.
3. Comandi a comparsa: un clic sul tasto del risultato, uno su "mostra tutti", un paio sui passaggi.
4. Esamina gli screenshot: linee di base del testo sulle righe (anche dopo le figure); etichette non sovrapposte né fuori riquadro; figure coerenti coi valori del testo; titoletti tenuti dove si apre una sezione; testo in frasi complete, non telegrafico; nessun ∝.
5. `grep` di controllo: assenza di `class="sommario"`, di "prossime unità", di `∝`, `\propto`, `&prop;`.

MathJax non si carica nel sandbox: le formule appaiono come `$...$`, è normale.

---

## 7. Chiusura di ogni unità e report finale

Per ogni unità pubblicata:
1. `_registro/<classe>.md`, voce dell'unità: riga "Revisione:" con tagli al testo, correzioni concettuali, impaginazione, figure e figure interattive; eventuali esempi tolti; eventuali figure decorative da valutare.
2. Barra `<nav class="nav-unita">` di tutte le pagine della classe: `python3 _build/nav_unita.py <classe>` (segue l'ordine di `_dati/<classe>.json`; salta le unità non pubblicate; riscrive l'intero blocco; se la pagina non ha la barra, la inserisce prima dell'ultimo `</div>`).
3. `python3 _build/genera.py` (hub e indice).
4. Commit e push (§2).

A fine esecuzione (§0):
* Riga dell'unità in `_registro/report-notturno.md`: pubblicata (commit) / saltata / non pubblicata (motivo), più i punti da controllare al mattino (figure decorative, esempi tolti, contenuti dubbi).
* Messaggio finale, una riga: unità, esito, commit.

---

## 8. Decisioni automatiche per i casi dubbi

| Caso | Decisione |
|---|---|
| Titolo | Resta quello attuale. |
| Titoletti | Si tengono quelli che aprono una sezione; si tolgono solo quelli superflui (§3). |
| Contenuto che sembra errato ma non è verificabile | Non modificarlo; segnalalo nel report. |
| Correzione concettuale certa (verificata con calcolo) | Applicala e registrala. |
| Figura decorativa | Lasciala; segnalala. |
| Più di due esempi | Tienine due; illustra quello con la funzione più semplice da leggere; caso difficile da disegnare (funzione oscillante) svolto per iscritto, senza figura. |
| Esempio numerico senza grafico | Non aggiungere figure. |
| Rimando a un'altra unità | Elimina il rimando. |
| Numero dell'unità nel testo diverso da quello del JSON | Fa fede il JSON; correggi occhiello e piè di pagina. |
| Copia nel sandbox diversa dal disco | Riparti dal file sul disco (§2). |
| Push non riuscito | Non ripetere se l'hash remoto coincide; altrimenti vedi §2; segnala nel report. |
| Qualsiasi altro dubbio | Scegli l'opzione più conservativa (meno modifiche), registrala nel report. |

Non eseguire mai: accorpamenti o spostamenti di unità, cambi di titolo, cancellazioni di cartelle (`git rm -r`), rinumerazioni. Sono operazioni da fare solo su richiesta esplicita, con la persona presente.