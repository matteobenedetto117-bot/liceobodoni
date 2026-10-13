# Revisione automatica delle unità — sito "Liceo Bodoni"

Esecuzione notturna, senza nessuno presente. **Non fare domande.** Ogni dubbio si risolve con le regole del §8 e si annota nel report.
Regole in vigore dal 13/10/2026: **testo più breve, sul modello di fisica quarta**, e **nessuna formula a comparsa**: tutto è visibile all'apertura della pagina.
Il token GitHub è nel prompt dell'attività programmata, non qui. L'elenco delle unità è in `_build/coda-notturna.txt`.

---

## 0. Due unità per esecuzione

L'attività parte ogni mezz'ora, dalle 22:00 alle 7:30. **Ogni esecuzione lavora due unità**, una dopo l'altra.

1. **Semaforo.** Leggi `_build/stato-notturno.txt` (non versionato).
   * Se contiene `occupato <data-ora>` meno vecchio di 2 ore: un'altra esecuzione è in corso. Termina subito, senza toccare nulla, con il messaggio "esecuzione precedente ancora in corso".
   * Altrimenti scrivici `occupato <data-ora attuale ISO>` (sovrascrivendo: non cancellare file) e procedi.
2. **Coda.** In `_build/coda-notturna.txt` prendi la prima riga non di commento senza esito (`<classe> <NN>` oppure `<classe> <NN> rifare`). Se non ce ne sono: scrivi `libero` nel semaforo e termina con "coda esaurita".
3. Esegui il ciclo del §1 su quell'unità, poi ripeti dal punto 2 per la seconda.
4. **Esito.** Accanto alla riga della coda: ` | pubblicata <hash>`, ` | saltata (già revisionata)` oppure ` | non pubblicata: <motivo breve>`. Coda e report si versionano in un commit finale a parte ("Coda e report notturno: …"), dopo i commit delle unità, così l'hash è già noto.
5. **Report.** In `_registro/report-notturno.md` la sezione è quella della notte, intestata con la data della sera d'inizio (le esecuzioni fra 0:00 e 8:00 appartengono alla sera prima): una riga d'avvio dell'esecuzione e una riga per unità. Nessun report "di fine sessione" a parte.
6. **Uscita**, anche in caso di errore: scrivi `libero` nel semaforo.

Un'unità saltata (già revisionata) non consuma il turno: segna l'esito e passa alla riga successiva.

---

## 1. Ciclo per l'unità

1. **Salta** l'unità se in `_registro/<classe>.md` ha già una riga "Revisione:" datata 13/10/2026 o successiva, **tranne** quando la riga della coda termina con `rifare`. Una riga "Revisione:" più vecchia non conta: la pagina va rifatta con le regole attuali.
2. Individua `<classe>/argomenti/<cartella>/index.html` (fa fede `_dati/<classe>.json`, campo `cartella`; il numero della cartella può non coincidere con quello dell'unità). Leggi la pagina, la voce del registro e quella del JSON.
3. **Pagina già revisionata in passato** (ha già l'impaginazione a quaderno): riparti dalla pagina attuale. Tieni impaginazione, figure e figure interattive; accorcia il testo (§3); rendi visibili formule, passaggi e risultati a comparsa (§5). Non recuperare testo dalle versioni precedenti.
   **Pagina mai revisionata**: riscrivi il testo (§3), applica l'impaginazione (§4), rifai le figure (§5).
4. Verifica (§6). Se la verifica non passa dopo 3 tentativi di correzione: **non pubblicare quell'unità**, ripristina i file (`git checkout -- <cartella>`), scrivi il motivo nel report e passa alla successiva.
5. Aggiorna registro, barra di navigazione, indici (§7), poi commit (§2). Un commit per unità.

Un'unità non pubblicata non blocca la coda.

---

## 2. Repository e pubblicazione

* Repo `matteobenedetto117-bot/liceobodoni`, branch `main`, pubblicato con GitHub Pages.
* Si lavora **solo** nella cartella locale collegata: `D:\Documents\Lavoro\Scuola\Bodoni\2026_2027\liceobodoni` (in `device_bash`: `$HOME/mnt/liceobodoni`). Il push dal sandbox cloud è bloccato: non provarlo.
* Se la cartella non è raggiungibile: riprova una volta; se fallisce ancora, termina e scrivi nel messaggio finale che il lavoro non è iniziato.
* Inizio esecuzione: `git pull` (via `git-sicuro.sh`). Se il repo locale ha commit non ancora inviati, il push di fine esecuzione li invia insieme.
* **Nessuna richiesta di permesso di cancellazione** (di notte nessuno può rispondere). Nella cartella collegata git non riesce a cancellare i propri `.lock`: **esegui ogni comando git con `bash _build/git-sicuro.sh <argomenti>`**, che dopo il comando sposta i `.lock` rimasti in `.git/_to_delete/`. Gli avvisi `unable to unlink … tmp_obj_…` sono innocui. Comandi git uno alla volta, mai in parallelo.
* Identità (config locale): `user.name = Claude`, `user.email = noreply@anthropic.com`.
* Commit: `<classe> unità NN: <sintesi>` + righe di attribuzione richieste dalla sessione.
* Push, una sola volta a fine esecuzione, token solo nell'URL del comando, mai salvato nel remote né scritto in file o commit:
  `git push -q https://x-access-token:<TOKEN>@github.com/matteobenedetto117-bot/liceobodoni.git main`
* Il push può superare i 180 s di `device_bash`: lancialo in background e controlla con `git ls-remote <URL> main` confrontando l'hash con `git rev-parse HEAD`. Non ripetere un push già riuscito. Se l'hash remoto non coincide dopo 3 controlli a distanza di un minuto, segnalalo nel report.
* Se `git pull` o il push fallisce per conflitto: `git pull --rebase`, poi riprova una volta; se persiste, non pubblicare e segnala.

### Come si modificano i file
* Piccole modifiche (togliere frasi, togliere tasti a comparsa): script Python di lettura-modifica-scrittura su `device_bash` (mai ricopiare a mano il contenuto).
* Riscritture grandi e figure calcolate: costruisci il file nel sandbox, poi scrivilo nella cartella con `device_commit_files` (`stagedPath` sotto `/mnt/user-data/outputs/`, `expectedMtimeMs` preso dallo staging).
* **Prima di scrivere una copia costruita nel sandbox, fai `diff` con il file sul disco** e controlla numero unità, occhiello, piè di pagina, pulsanti precedente/successiva.

---

## 3. Testo: breve, sul modello di fisica quarta

Gli studenti copiano la pagina sul quaderno; le spiegazioni le dà il docente a voce. La pagina è fatta di **disegni e calcoli**, tenuti insieme da **poche frasi di raccordo e spiegazione**. Il modello è fisica quarta (per esempio unità 06–07), **ancora un po' più asciutta**.

**Si mantiene**: definizioni, leggi, formule, unità di misura, esempi svolti, figure.
**Si elimina**: introduzioni lunghe, cenni storici, aneddoti, ripetizioni, rimandi ad altre unità, frasi che ripetono ciò che formula o figura mostrano già, commenti finali ("è la conservazione dell'energia applicata a…") quando non aggiungono nulla.

Regole:
* **Lunghezza**: indicativamente 120–180 parole di testo per unità (formule, didascalie e scritte nei disegni escluse). Una pagina sopra le 220 parole va accorciata; una più lunga del necessario solo perché l'argomento è ampio può arrivare a 250.
* **Fra due elementi** (titoletto, formula, figura, riquadro) al massimo **una o due frasi**. Mai paragrafi di tre o più frasi.
* Frasi **brevi ma complete**, con soggetto e verbo: niente stile telegrafico ("Se la pressione resta costante, il volume è direttamente proporzionale alla temperatura assoluta", non "P costante: V ∝ T").
* Elenchi puntati solo per contenuti che sono davvero un elenco (proprietà, casi, condizioni); una voce non supera due righe.
* Registro neutro e tecnico.
* Introduzione: **una frase**, oppure nessuna se il titolo basta.
* Definizioni e leggi in riquadro `.def` (enunciato in una o due frasi, poi la formula); avvertenze in `.nota` (una frase, al massimo due).
* Formule in evidenza (§4), con la legenda dei simboli in una sola frase.
* **Esempio**: una frase con i dati e la domanda, poi i calcoli in riquadri `.eq` uno sotto l'altro, poi il risultato. Le frasi di collegamento fra i passaggi si scrivono solo se il passaggio non è evidente, e sono di poche parole.
* Didascalie: una frase breve.
* Nessun simbolo di proporzionalità (∝, `\propto`, `&prop;`): "direttamente proporzionale a…".
* Unità: volumi in m³ (notazione esponenziale se scomodi, oppure fattore sull'asse: "V (10⁻⁵ m³)"), pressioni in Pa o kPa, temperature in K.
* Titolo: quello attuale, in `<h1>` e `<title>` ("Titolo — Fisica quarta").
* Togli `<p class="sommario">`, le sezioni "Nelle prossime unità" / "Dove si continua": restano link "← Classe", occhiello "Argomento · Unità NN", titolo.

### Titoletti
* Si tengono gli `<h2>` che aprono una sezione: un nuovo concetto, una nuova legge, un caso diverso, un procedimento. Titoletto breve e descrittivo.
* Si tolgono quelli che coprono una o due righe, quelli che ripetono il titolo, quelli generici ("Introduzione", "Riepilogo", "In sintesi") e "Nelle prossime unità".
* Gli esempi hanno il titoletto "Esempio" ("Esempio 1", "Esempio 2").
* Se gli esempi sono più di due, tienine due (i più rappresentativi) e registra quali sono stati tolti.

### Controllo concettuale (obbligatorio)
Rileggi testo, formule e disegni; verifica calcoli, limiti e unità con SymPy o Python. Correggi in modo sobrio, senza citare argomenti non trattati, e registra ogni correzione. Accorciando, **non togliere ipotesi e condizioni di validità** (per esempio "per una quantità di gas data", "x_A ≠ x_B", "f derivabile due volte"). Errori già incontrati, da cercare:
* ago "indica il nord" → "si allinea approssimativamente lungo la direzione nord–sud"; "non esistono monopoli" → "non sono mai stati osservati"; linee di campo "all'esterno del magnete";
* "barometro" → "manometro" per un gas chiuso;
* rette V–t e P–t a −273,15 °C solo per gas rarefatto; nessun gas ci arriva (prima liquefa);
* leggi dei gas valide per quantità di gas data; proporzionalità con la temperatura assoluta;
* reversibile = trasformazione percorribile al contrario riportando sistema **e ambiente** allo stato iniziale;
* conservazione della carica per un sistema **isolato**; forza elastica di richiamo, opposta all'allungamento;
* k ≈ 1,38×10⁻²³ J/K, N_A ≈ 6,022×10²³ mol⁻¹, e ≈ 1,60×10⁻¹⁹ C (definite dal 2019);
* asintoto verticale: forma compatta con ±∞, basta uno dei quattro casi unilaterali;
* i disegni devono coincidere coi valori scritti; le frecce delle forze nel verso giusto.

---

## 4. Impaginazione "a quaderno"

Copia il blocco `<style>` e lo script di allineamento da un'unità di fisica quarta già revisionata (per esempio unità 34–35).

* `html{font-size:165%}`, `:root{--r:1.8rem}` (distanza fra righe). Sfondo del `body` a righe ogni `--r`, riga a `1.3rem` dall'inizio del rigo; `line-height:var(--r)`.
* `h1` 2.4rem, interlinea `2*var(--r)`, spostato giù .5rem; `h2` 1.45rem, interlinea `var(--r)`, `margin-top:var(--r)`; intestazione senza bordo.
* `.foglio` e `header.testata`: `display:flex; flex-direction:column`. `.nota` e `.def`: `display:flow-root`.
* Margini sempre multipli di `--r`.
* Formule: `<p class="eq">$$…$$</p>` in riquadro azzurro:
  `.foglio>.eq{background:var(--blu-chiaro);border-radius:10px;padding:calc(var(--r)*.5) 22px;font-size:1.1rem}`.
  Principio o legge finale in rosso: `.eq.principio{background:#f6e4e2;color:var(--rosso);font-weight:600}`.
  **`.foglio>.eq` vale solo per i figli diretti**: dentro `.def`, `.es` serve una regola propria, altrimenti il riquadro sparisce.
* `.def`: bordo sinistro blu, fondo bianco. `.nota`: bordo sinistro rosso, fondo `#fdf6f5`. Etichetta `<span class="et">` in maiuscoletto.
* Didascalie `.fig .did`: `font-size:.9rem`, interlinea 1.4.
* **Script di allineamento** in fondo alla pagina: sposta titoli, paragrafi, elenchi, figure, note e barra di navigazione alla riga successiva. Esposto come `window.allineaQuaderno`, rilanciato a `startup.pageReady` di MathJax e a ogni ridimensionamento.

---

## 5. Figure, esercizi e calcoli

### Tutto visibile (nessuna comparsa a comando)
* **Formule, passaggi, quesiti e risultati sono tutti visibili all'apertura della pagina.** Niente tasti "risultato", "Mostra tutti i risultati", "passo successivo", niente `hidden` né `display:none` su formule o testo.
* Nelle pagine che li hanno già (soprattutto matematica-5 e matematica-2): togli i tasti `.btn-ris`, `.btn-tutti`, `.btn-passo`, la `.barra-ris`, gli attributi `hidden` su `.ris`, `.passo` e simili, e il codice JavaScript che li gestiva; tieni il contenuto. Resta lo script di allineamento.
* Esercizi: quesito in `p.eq.quesito` (riquadro azzurro), subito sotto il risultato in riquadro verde chiaro (`p.eq.ris`). Catene di passaggi: riga grigia di spiegazione **brevissima** (o nessuna) + formula, tutte una sotto l'altra.
* Lista di casi con grafico: a sinistra quesito e risultato, a destra il grafico (`div.es-fig`, griglia `1fr 250px`, una colonna sotto i 700px); **tratto rosso più spesso** dove si percorre la curva per il limite richiesto.

### Regole generali delle figure
* **Non aggiungere figure.** Le esistenti si ridisegnano e, se serve, si rendono interattive. Una figura solo decorativa si lascia e si segnala nel report.
* Nelle pagine già revisionate le figure **restano come sono**, salvo errori.
* **SVG inline disegnato da script interno alla pagina**, senza librerie esterne. Le pagine con Plotly si riscrivono così. Per la matematica riusa l'aiuto di matematica-5 (`el`, `txt`, `num`, `Piano` con `X`, `Y`, `assi`, `curva`, `add`, gruppi `sotto`/`sopra`/`testo`).
* Colori dalle variabili: `--inchiostro`, `--blu`, `--blu-chiaro`, `--rosso`, `--verde`, `--grigio`, `--riga`. Magneti: N rosso, S blu; forze rosse. Grafici: curva principale inchiostro o blu; confronti e asintoti rosso tratteggiato; limite verde tratteggiato; punto mobile rosso.
* Scritte nei disegni piccole (11–14 unità del viewBox) e poche.
* Forma **calcolata**, non tracciata a occhio (isoterme P = nRT/V, linee di campo integrate numericamente, soglie dei limiti calcolate…). Campionamento adatto alla funzione; spezza il tracciato dove la funzione non è definita o esce dal riquadro.
* Disegno più stretto della colonna: `style="width:100%;max-width:420px"`, contenuto centrato nel viewBox, senza grandi spazi vuoti.
* Etichette leggibili: niente sovrapposizioni con curve, assi, bordi o altri oggetti, in nessuna posizione del cursore.
* Pannelli affiancati: `<div class="did-parti" style="--n:3">` con un `<p class="did">` per pannello.

### Figure interattive (restano)
L'interattività riguarda solo i disegni, non le formule.
* **Cursore oppure ▶, mai entrambi nella stessa figura.** Preferito il cursore: `input type="range"` in `div.cursore`, etichetta della grandezza e valore a fianco.
* ▶ (`&#9654;`) / ↺ (`&#8634;`) solo per sequenze senza parametri: `.btn-anim`, larghezza 3rem, `aria-label` "Avvia"/"Ricomincia".
* Grafici di funzione: il cursore muove un punto sulla curva **già disegnata per intero**; a fianco compaiono i valori, con una parola in verde quando si entra nella condizione che conta.
* `requestAnimationFrame`; rispetto di `prefers-reduced-motion` (stato statico finale).
* Particelle di gas: simulazione vera, modulo della velocità indipendente dal volume, sempre in movimento, velocità `55·(T/100)^1.8`.

---

## 6. Verifica automatica (prima di ogni commit)

Con Playwright nel sandbox cloud (Chromium in `/opt/pw-browsers/chromium`), pagina e `assets/stile.css` portati con `device_stage_files`:
1. Nessun `pageerror`.
2. Screenshot della pagina intera e di ogni figura; per ogni cursore due posizioni (minimo e massimo); per ogni ▶ a metà e alla fine.
3. Esamina gli screenshot: testo sulle righe (anche dopo le figure); etichette non sovrapposte né fuori riquadro; figure coerenti coi valori del testo; **tutte le formule e i risultati visibili all'apertura**.
4. `grep` di controllo: assenza di `class="sommario"`, "prossime unità", `∝`, `\propto`, `&prop;`, `btn-ris`, `btn-tutti`, `btn-passo`, `barra-ris`, ` hidden` su elementi di testo o formule.
5. Conteggio parole del testo (paragrafi, voci di elenco e riquadri; formule e didascalie escluse): se supera 220, accorcia ancora (vedi §3) o motiva nel report.

MathJax non si carica nel sandbox: le formule appaiono come `$...$`, è normale.

---

## 7. Chiusura di ogni unità e report

Per ogni unità pubblicata:
1. `_registro/<classe>.md`, voce dell'unità: riga "Revisione (<data>, regole 13/10):" con parole prima → dopo, tagli al testo, comparse tolte, correzioni concettuali, figure; eventuali esempi tolti; eventuali figure decorative. Se esiste già una riga "Revisione:", sostituiscila.
2. `python3 _build/nav_unita.py <classe>` (barra `<nav class="nav-unita">` di tutta la classe).
3. `python3 _build/genera.py` (hub e indice).
4. Commit dell'unità (§2).

A fine esecuzione (§0): commit di coda e report, push, semaforo `libero`.
* Riga dell'unità in `_registro/report-notturno.md`: pubblicata (commit) / saltata / non pubblicata (motivo), parole prima → dopo, più i punti da controllare al mattino.
* Messaggio finale, una riga per unità: unità, esito, commit.

---

## 8. Decisioni automatiche per i casi dubbi

| Caso | Decisione |
|---|---|
| Titolo | Resta quello attuale. |
| Titoletti | Si tengono quelli che aprono una sezione; si tolgono solo quelli superflui (§3). |
| Frase utile ma che allunga la pagina | Se ripete una formula o una figura, toglila; se contiene un'ipotesi o una condizione, tienila in forma breve. |
| Formule o risultati a comparsa | Rendili visibili, togli tasti e script relativi. |
| Contenuto che sembra errato ma non è verificabile | Non modificarlo; segnalalo nel report. |
| Correzione concettuale certa (verificata con calcolo) | Applicala e registrala. |
| Figura decorativa | Lasciala; segnalala. |
| Più di due esempi | Tienine due; caso difficile da disegnare svolto per iscritto, senza figura. |
| Esempio numerico senza grafico | Non aggiungere figure. |
| Rimando a un'altra unità | Eliminalo. |
| Numero dell'unità nel testo diverso da quello del JSON | Fa fede il JSON; correggi occhiello e piè di pagina. |
| Copia nel sandbox diversa dal disco | Riparti dal file sul disco (§2). |
| Push non riuscito | Non ripetere se l'hash remoto coincide; altrimenti vedi §2; segnala nel report. |
| Qualsiasi altro dubbio | Scegli l'opzione più conservativa (meno modifiche), registrala nel report. |

Non eseguire mai: accorpamenti o spostamenti di unità, cambi di titolo, cancellazioni di cartelle (`git rm -r`), rinumerazioni. Sono operazioni da fare solo su richiesta esplicita, con la persona presente.
