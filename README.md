# Forord

Du kan få alle lectures i dette kursus ved at køre følgende funktion i din terminal:
>```
> python sync.py
>```
Denne vil download alle github repos inden i den mappe hvor du har sync.py.

*Note: Denne funktion kræver at du har git og python installeret på din computer.*



# KOMPLET FORELÆSNINGSPLAN – ST2 ANVENDT PROGRAMMERING

Overblik over 12 forelæsninger, der dækker grundlæggende programmering, objektorienteret design, signalbehandling og analyse af populationsdata.

---

## OVERBLIK OVER FORELÆSNINGER

| # | Forelæsning | Mappe | Primære emner |
|---|------------|-------|----------------|
| 1 | Hej C og Python | oop_1 | Programmeringssprog, grundlæggende syntaks, miljøopsætning |
| 2 | Objekter, indkapsling, interaktion | oop_2 | Klasser, metoder, dataindkapsling, objektinteraktion |
| 3 | Filer og dataindlæsning | oop_3 | Fil-I/O, CSV-parsing, kombinering af OOP og data |
| 4 | OOP-integration workshop | oop_4_workshop | Integration af OOP, fil-I/O, visualisering; overvågningssystemer til enheder |
| 5 | Signalgrundlag | signals_1 | EKG-fysiologi, statistik, peak-detektion |
| 6 | Filtrering og mekaniske signaler | signals_2 | Filtrering, SCG-fysiologi, mekanisk timing, Envelope-udtrækning |
| 7 | Feature engineering, PPG og regression | signals_3 | Feature-definition, PPG-fysiologi, lineær regression, variationsmål |
| 8 | Signalintegration og etik | signals_4_workshop | Multimodal integration, refleksion over signal-workflow, etisk analyse |
| 9 | Lineær regression med populationsdata | populations_data_1 | Lineær regression, modelvalidering, residualer |
| 10 | Datavisualisering og unsupervised læring | populations_data_2 | Datavisualisering, fordelinger, scatter plots, k-means clustering (Iris-datasæt) |
| 11 | Supervised learning: klassifikation | populations_data_3 | k-NN-klassifikation, beslutningsgrænser, modelevaluering |
| 12 | Data-integration workshop | populations_data_4_workshop | End-to-end analyse: regression, clustering, klassifikation, reproducerbarhed, formidling |

---

# FORELÆSNING 1: OOP 1 – Hej C og Python

**Mappe:** `oop_1`  
**Varighed:** 4t (2t forelæsning + 2t øvelser)  
**Jupyter Notebook:** `AP-HelloPython.ipynb`

## Primære emner dækket i notebooken

**Hvorfor både C og Python?**
- C: enkelhed men brutal fejlhåndtering, manuel hukommelsesstyring
- Python: let at lære, enkelhed, omfattende biblioteker, gratis, bruges overalt
- Hvornår bruges hvad: C til systemprogrammering, Python til datalogi og AI

**C vs Python: Centrale syntaksforskelle**
- Funktioner: C kræver eksplicitte returtyper, Python er implicit
- Arrays/lister: C statiske arrays, Python dynamiske lister med metoder
- Betingelser: C switch/case, Python if/elif/else og match
- Løkker: C for/while med eksplicit inkrementering, Python for-in med range()
- Hukommelse: C pointers og manuel styring, Python automatisk
- Typesystem: C eksplicit typning, Python dynamisk typning

**Python: Fordele og ulemper**
- Fordele: let at lære, enkelhed, stort økosystem (NumPy, SciPy, pandas, matplotlib), gratis, standard i AI/ML
- Ulemper: langsomt, ineffektivt, runtime-fejl (dynamisk typning), kræver debugger

**Udviklingsplan: Indkapsling og generaliserings-workflow**
1. Skriv et lille program uden funktioner (få det til at virke)
2. Indkapsl fungerende dele i funktioner med tydelige navne
3. Generalisér funktionerne ved at tilføje parametre
4. Gentag indtil du har fungerende funktioner
5. Refaktorér for at forbedre og reducere duplikation

**Miljøopsætning og værktøjer**
- Installation af Miniconda og conda-pakkestyring
- Anaconda Navigator til miljøstyring
- VS Code med Python-udvidelse (startet fra Navigator)
- Kørsel af scripts, Python REPL (`python`-kommando), versionskontrol (`python -V`)

**Python-grundlag dækket**
- Variabler og typer: int, float, str, bool (dynamisk typning)
- Aritmetiske og strengoperationer
- Lister og dictionaries: oprettelse, manipulation (append, remove, pop)
- Betingelser: if/elif/else, match/case
- Løkker: for (med range), while
- Funktioner: definition med def, parametre, returværdier
- F-strings til formateret output: `f"{variable=}"`
- Pakkeinstallation med conda: `conda install <package>`

## Vigtig pointe
Grundlaget for Python-programmering: forstå syntaks, brug debugger, øv simple operationer før du går videre til klasser.

---

# FORELÆSNING 2: OOP 2 – Objekter, indkapsling og interaktion

**Hvad er objekter?**
- Objekter samler data (tilstand lagret i attributter) og adfærd (metoder/funktioner)
- Objektidentitet: hver instans er unik
- Objekter modellerer virkelige entiteter (Patient, Sensor, Enhed, Monitor)

**At definere klasser i Python**
- Konstruktør `__init__(self, ...)`: initialiserer objektets tilstand
- Instansvariabler: gemmes med `self.attribute_name`
- Metoder: funktioner der arbejder på `self`
- `self`-parameteren: implicit reference til den aktuelle instans

**Indkapsling og databeskyttelse (centralt tema)**
- **Problem:** data kan ændres direkte og blive ugyldige (fx `patient.heart_rate = -500`)
- **Løsning:** brug `_`-konventionen for private attributter (fx `self._heart_rate`)
- Python håndhæver det ikke, men konventionen signalerer: "internt, tilgå ikke direkte"
- Kontrolleret adgang: brug metoder til sikkert at ændre tilstand (fx `update_heart_rate(new_hr)`)
- Validering: metoder kan indeholde regler (fx kun tillad 0 ≤ HR ≤ 250)

**Objektinteraktion**
- Objekter kommunikerer ved at kalde metoder på andre objekter
- Eksempel: `patient.update_from_sensor(sensor)` — sensor gives som parameter
- Fordele: modularitet, løs kobling, testbarhed, klar adskillelse af ansvar
- Mønster: hver klasse har ét klart ansvar

**Samlinger af objekter**
- Gem objekter i lister: `patients = [p1, p2, p3]`
- Iterér og anvend operationer: `for p in patients: p.update_from_sensor(sensor)`
- Udbredt mønster i medicinske systemer

**Etisk overvejelse: Data governance by design**
- Indkapsling håndhæver adgangspolitikker på kode-niveau
- Følsomme felter (diagnoser, målinger) skal beskyttes i designet
- Audit trails: metoder kan logge hvem der tilgår hvad
- Privacy by design: tænk adgangskontrol ind før du skriver kode

## Centrale mønstre demonstreret
- **Indkapsling:** `_private` attributter, offentlige metoder
- **Interaktion:** objekter modtager andre objekter som parametre
- **Validering:** metoder håndhæver invarianter
- **Lister:** samlinger af objekter med løkker

---

# FORELÆSNING 3: OOP 3 – Filer og dataindlæsning

**Filer som datakilde**
- Rigtige data kommer fra filer, ikke hardcodede værdier eller brugerinput
- Datakilder: medicinske enheder, logfiler, softwareeksport, eksperimenter
- **Filer er forbindelsen til virkeligheden**

**Fil-I/O grundlæggende**
- Åbning og læsning: `with open("filename", "r") as f:`
- `with`-statement: automatisk lukning af filen, fejlhåndtering
- `f.read()`: hele filen som én streng
- `f.readlines()`: filen som liste af strenge (inkluderer `\n`)
- Lukning sker automatisk med `with`

**Parsing af strukturerede data**
- Strengoperationer: `.strip()` (fjerner whitespace og `\n`), `.split(",")` (split ved delimiter)
- Typekonvertering: `int(string)`, `float(string)`, `str(value)`
- **Typisk pipeline:** læs linje → strip → split → konvertér → gem
- Eksempel: `values.append(int(line.strip()))`

**CSV-format**
- Comma-Separated Values: simpelt, bredt understøttet
- Første linje indeholder ofte header
- `skiprows=1` for at springe header over
- Flere kolonner: brug `delimiter=","` og split

**Kombinér OOP og filindlæsning**
- Data loader-klasser: indkapsler fil-læselogik
- Genanvendelig: én klasse til forskellige filer
- Adskillelse af ansvar: fil-I/O separat fra forretningslogik

**Grundlæggende datavisualisering**
- Hvorfor visualisere: se mønstre, trends, outliers og relationer med det samme
- matplotlib-workflow: `plt.plot()`, `plt.scatter()`, `plt.xlabel()`, `plt.ylabel()`, `plt.title()`, `plt.legend()`, `plt.show()`
- Plottyper: linjeplots (tidsserier), scatter plots (relationer)

**OOP til datahåndtering**
- `CSVDataLoader`-klasse: `__init__(filename)`, `load_data()`-metode
- `Signal`-klasse: `__init__(data, fs, label)`, metoder til plot
- Fordele: struktur, genanvendelighed, klarhed

**Etisk overvejelse: Dataminimering og opbevaring**
- Gem kun nødvendige data; rå biosignaler er følsomme
- Retention-politikker: hvor længe gemmes data? hvornår slettes de?
- Backup-strategi: til gendannelse, ikke uendelig opbevaring
- GDPR: retten til at blive glemt, opbevaringsgrænser


## Centrale mønstre
- **Pipeline:** `with open() → for line → strip → split → konvertér → gem`
- **Klassebaseret indlæsning:** `CSVDataLoader` med `load_data()`-metode
- **Adskillelse:** fil-I/O separat fra visualisering
- **Genanvendelighed:** én loader-klasse til forskellige filer

---

# FORELÆSNING 4: OOP 4 – OOP-integration workshop


**Mål:** Byg en komplet datapipeline, der integrerer alt fra forelæsning 1-3.

**Det store billede:**
- **Øvelse 1:** Lav et enhedsovervågningssystem, der læser målinger, gemmer dem i objekter, gemmer til fil og visualiserer
- **Øvelse 2:** Udvid til multi-enhedsscenarie: indsamling fra flere sensorer, central styring af data, gem og genindlæs med fuld round-trip-validering

**Det du øver:**
- Design af klasser (forelæsning 2): hvilke data? hvilke metoder? hvordan indkapsle?
- Objektinteraktion (forelæsning 2): objekter der kalder metoder på andre objekter
- Fil-I/O (forelæsning 3): læsning af CSV, parsing af data, skrivning af resultater
- Datavisualisering (forelæsning 1 & 3): matplotlib til at forstå og formidle resultater
- Komplet workflow: design → implementér → test → visualisér → gem/genindlæs

**Ingen nye begreber:** Alt du har brug for, er gennemgået i forelæsning 1-3. Det handler om at *integrere* idéerne i et realistisk workflow.

---

## Øvelse 1: Overvågningssystem for én enhed (1t 45m)

**Scenarie:** Du har en pulsmåler. Byg et system til at indsamle målinger, gemme dem sikkert og gemme til disk.

**Krav:**
1. Definér en `Measurement`-klasse:
   - Gemmer: værdi, tidsstempel
   - Validerer: puls skal være 40-200 bpm (afvis ugyldige data)
   - Metode: `is_valid()` returnerer True/False

2. Definér en `Device`-klasse:
   - Gemmer: navn, device_id, liste af målinger
   - Metoder: `add_measurement(measurement)`, `get_all_measurements()`, `get_stats()` (gennemsnit, min, max)
   - Indkapsling: målinger tilgås kun via metoder, ikke direkte

3. Simulér dataindsamling:
   - Opret enhed, generér 20 tilfældige målinger (nogle gyldige, nogle ugyldige)
   - Tilføj kun gyldige målinger til enheden
   - Print statistik: hvor mange accepteret vs afvist?

4. Gem til fil (forelæsning 3):
   - Skriv målinger til CSV: tidsstempel, værdi, device_id
   - Medtag metadata: enhedsnavn, antal målinger, indsamlingsdato

5. Indlæs og verificér:
   - Læs CSV ind i en ny enhed
   - Verificér at indlæste data matcher de gemte (round-trip-test)

6. Visualisér:
   - Plot målinger over tid
   - Tilføj middelværdi-linje og ±1 std-bånd
   - Label akser, titel med enhedsnavn

**Centrale færdigheder:**
- Indkapsling: datavalidering i konstruktør/metoder
- Objektinteraktion: Enhed indeholder Måling-objekter
- Fil-I/O: skriv og parse CSV
- Visualisering: matplotlib-linjeplot med bånd

---

## Øvelse 2: Data-system til flere enheder (1t 45m)

**Scenarie:** Hospitalet har flere monitorer (EKG, PPG, temperatur). Byg et system til at styre alle enheder, indsamle data og muliggøre tvær-enheds-analyse.

**Krav:**
1. Udvid fra Øvelse 1:
   - Genbrug `Device`- og `Measurement`-klasserne (ingen ændringer nødvendige)
   - Opret `DataCollector`-klasse (ny):
     - Gemmer: liste af enheder
     - Metoder: `add_device(device)`, `add_measurement(device_id, measurement)`, `get_device(device_id)`, `get_all_devices()`
     - Indkapsling: enheder tilgås gennem metoder

2. Initialisér system:
   - Opret 3 enheder: EKG (0-150 bpm), PPG (40-200 bpm), Temperatur (35-41°C)
   - Tilføj til collector
   - Generér 15-20 målinger per enhed (blanding af gyldige og ugyldige)

3. Gem alle data:
   - Skriv til én CSV: device_type, device_id, tidsstempel, værdi
   - Metadatafil (JSON): enhedsnavne, intervaller, indsamlingsdato, antal målinger per enhed

4. Indlæs og verificér:
   - Læs CSV og metadata
   - Rekonstruér enheder og målinger
   - Verificér at ingen data er tabt (sammenlign rækkeantal, værdiintervaller)

5. Analysér og visualisér:
   - Subplot: ét plot per enhed (3 subplots)
   - Hvert plot: målinger over tid med middelværdi og std
   - Sammenlign: hvilken enhed har størst variation? flest afvisninger?

6. Tvær-enheds-indsigt (bonus):
   - Korrelation mellem enheder (fx korrelerer EKG med PPG?)
   - Plot korrelations-scatter plot

**Centrale færdigheder:**
- Objektkomposition: Collector indeholder Enheder; Enheder indeholder Målinger
- Flere filoperationer: CSV-data + JSON-metadata
- Parsing og validering: rekonstruér fra gemte data
- Multi-panel-visualisering: subplots til sammenligning
- Komplet pipeline: design → implementér → gem → indlæs → analysér → visualisér

---

## Workshop-læringsmål

Når du er færdig med øvelserne, bør du kunne:
- Designe et klassehierarki: hvad skal i hver klasse?
- Bruge indkapsling: beskytte data, validere input, eksponere via metoder
- Implementere objektinteraktion: objekter der kalder metoder på andre objekter
- Læse og skrive CSV-filer korrekt
- Parse strukturerede data fra filer tilbage til objekter
- Visualisere flere datasæt side om side
- Bygge og teste en komplet end-to-end pipeline
- Verificere dataintegritet: gem, indlæs, tjek for datatab

---

# FORELÆSNING 5: Signaler 1 – Signalgrundlag, NumPy og statistik

**Etik-mini-tema: EKG som biometrisk og helbredsdata**
- EKG er unikt for individer (som fingeraftryk) → re-identifikationsrisiko
- EKG afslører latente sygdomme: arytmier, hjerteanfaldsrisiko, ukendte tilstande
- Permanent helbredshistorik: når det først er gemt, kan det ikke tages tilbage
- Scenarier: hospital (diagnostik), wearables (kontinuerlig overvågning), forskning (datadeling)
- Etiske udfordringer: informeret samtykke, dataminimering, sikker opbevaring, ansvarlig brug

**Hvorfor NumPy?**
- Python-lister er langsomme: `sum(list)/len(list)` kræver løkke
- NumPy er optimeret: `np.mean(array)` er vektoriseret og hurtigt
- Vektorisering: operationer på hele arrays uden eksplicitte løkker
- Hukommelseseffektivitet: sammenhængende hukommelsesallokering

**NumPy-grundlag**
- Opret arrays: `np.array(list)`, `np.zeros(n)`, `np.ones(n)`, `np.linspace(start, stop, n)`
- Indeksering: `arr[0]`, `arr[-1]`, `arr[1:5]`
- Slicing med step: `arr[::2]` (hver 2. værdi)
- Vektoriserede operationer: `arr + 5`, `arr * 2`, `np.sqrt(arr)`
- Broadcasting: dimensionsjustering til operationer
- Funktioner: `np.mean()`, `np.std()`, `np.min()`, `np.max()`, `np.sum()`

**Data-workflow**
1. Indlæs data
2. Inspicér (tjek struktur, range, enheder)
3. Rens (fjern artefakter, manglende værdier)
4. Visualisér (forstå mønstre)
5. Udtræk features (beregn opsummeringer)
6. Gem (gem resultater)

**EKG-fysiologi**
- Elektrisk aktivitet i hjertet: depolariserings- og repolariseringscykler
- Hovedkomponenter: P-bølge (atrium), QRS-kompleks (ventrikel), T-bølge (recovery)
- **R-peak:** største udsving i QRS, mest genkendelige feature
- **RR-interval:** tid mellem to R-peaks (slag-til-slag timing)
- **Puls:** 60 / (RR-interval i sekunder) = bpm
- **Sample rate:** hvor ofte signalet måles (Hz); påvirker opløsning

**Grundlæggende statistik**
- Middelværdi: gennemsnit, centrum af fordeling
- Varians: spredning i kvadrat
- Standardafvigelse (std): kvadratroden af varians, spredning i samme enhed som data
- Hvorfor statistik betyder noget: etabler baseline, detekter afvigelser, sammenlign grupper
- NumPy-funktioner: `np.mean()`, `np.var()`, `np.std()`

**Peak-detektion (threshold-baseret)**
- **Idé:** peaks er høj-amplitude punkter over baggrund
- **Threshold-valg:** `mean + k*std` (k typisk 2-3 for rene signaler)
- **Algoritme:** find indekser hvor værdier overstiger threshold
- Eksempel:
  ```python
  threshold = np.mean(data) + 2 * np.std(data)
  peaks = np.where(data > threshold)[0]  # indekser for peaks
  ```
- **Begrænsninger:** virker for rene signaler, fejler ved støj, artefakter, baseline drift
- **Forbedringer:** præprocessering (filtrering), lokale maxima (kontekst), validering

**Motivation for filtrering (nævnt)**
- Støjkilder: elektrisk interferens, bevægelsesartefakter, baseline drift
- Filtre fjerner uønskede komponenter
- Simpelt eksempel: glidende gennemsnit glatter signalet

**Visualisering til inspektion**
- Plot signalet med middelværdi og std-bånd for at se støj
- Visualisér statistik med søjlediagrammer
- Histogrammer viser fordelingsform

**Etisk overvejelse: EKG-privatliv**
- Biometrisk risiko: unikke mønstre muliggør re-identifikation
- Latent information: afslører helbredstilstande, som personen ikke kender
- Permanent journal: kan ikke "glemmes"
- Samtykke og brug: data bør kun bruges som aftalt

## Centrale mønstre og funktioner
- **NumPy-operationer:** vektoriseret i stedet for løkker
- **Inspektion:** plot + beregn stats for at forstå data
- **Peak-detektion:** threshold-baseret med mean + k*std
- **Klasser:** `HeartRateExtractor` med metoder til feature extraction

---

# FORELÆSNING 6: Signaler 2 – Filtrering og mekaniske signaler

**Etik: Dataproveniens og metadata**
- Metadata er essentielle: sample rate (fs), enheder, enhed/model, kalibrering, protokol
- Uden metadata: kan man ikke tolke eller verificere analysen
- Metadataintegritet: korrupte metadata gør resultater ugyldige
- Transparens: dokumentér alle processing-trin
- Audit trails: hvem gjorde hvad, hvornår, med hvilke parametre (compliance/ansvarlighed)

**Etik: Håndtering af følsomme helbredsdata (GDPR/Dansk lov)**
- Formål: definér før behandling
- Retsgrundlag: hvorfor er dette lovligt?
- Eksterne services: hvis cloud bruges, kræves databehandleraftale
- Adgangskontrol: mindst mulige rettigheder, ingen offentlige links
- Kryptering: i hvile og under transport
- Opbevaring & sletning: slet når formålet er opfyldt
- DPIA (Data Impact Assessment): kræves ved højrisiko-behandling

**Hvorfor filtrering?**
- Reelle signaler indeholder støj: 50/60 Hz elektrisk, bevægelsesartefakter, baseline drift
- Filtre fjerner uønskede komponenter og bevarer interesse-signal
- Trade-offs: udglatning reducerer støj men dæmper peaks; faseeffekter

**Glidende gennemsnitsfilter**
- Simpelt: tag gennemsnit af vindue omkring hvert punkt
- Algoritme:
  ```python
  def moving_average_filter(data, window):
      smoothed = np.zeros_like(data)
      half_window = window // 2
      for i in range(len(data)):
          start = max(0, i - half_window)
          end = min(len(data), i + half_window + 1)
          smoothed[i] = np.mean(data[start:end])
      return smoothed
  ```
- Fjerner højfrekvent støj men glatter peaks
- Vinduesstørrelse bestemmer hvor meget glatning der sker

**SciPy signalbehandling**
- `scipy.signal.butter()`: design af Butterworth-filter
- `scipy.signal.filtfilt()`: nul-fase filtrering (ingen tidsforskydning)
- Filtertyper: lowpass, highpass, bandpass, bandstop
- Eksempel:
  ```python
  b, a = butter(2, 20, fs=fs, btype='lowpass')
  filtered = filtfilt(b, a, signal)
  ```

**PCG/SCG-fysiologi**
- **PCG:** Fonokardiografi (hjertelyde fra stetoskop)
- **SCG:** Seismokardiografi (mekaniske vibrationer fra hjerteslag)
- Frekvensindhold: 50 Hz < audio < 20.000 Hz; hjertelyde 20-300 Hz
- **S₁ (Lub):** første hjertelyd når mitral-/trikuspidalklapper lukker, markerer systolens start
- **S₂ (Dub):** anden hjertelyd når aorta-/pulmonalklapper lukker, markerer diastolens start
- Timing: S₁ → S₂ er systole (kort), S₂ → næste S₁ er diastole (lang)

**Envelope-udtrækning**
- Formål: fremhæve amplitudevariationer (hvor de vigtige hændelser er)
- Algoritme:
  1. Fjern middelværdi
  2. Rektificér (absolutværdi)
  3. Glidende maksimum over vindue
  4. Tilføj middelværdi tilbage
- Bruges til at detektere S₁ og S₂ ved at finde peaks i Envelopeen

**Peak-detektion i Envelope**
- Brug `scipy.signal.find_peaks()` med parametre:
  - `height=np.std(envelope)`: minimum peak-højde
  - `distance=int(0.15*fs)`: minimum distance mellem peaks
- Returnerer indekser for detekterede peaks

**S₁/S₂-klassifikation**
- Baseret på intervaller mellem peaks:
  - **S₁:** kommer efter lang pause (diastole)
  - **S₂:** kommer efter kort pause (systole)
- Fysiologisk regel:
  ```
  IF interval[i] < interval[i+1]:
      peak[i] er S₁
  ELSE:
      peak[i] er S₂
  ```

**Validering via histogrammer**
- Plot intervaller mellem detekterede peaks
- S₁-intervaller (systole) bør være kortere
- S₂-intervaller (diastole) bør være længere
- Histogram viser om klassifikationen giver mening

**Data-workflow for SCG/PCG**
1. Indlæs data
2. Inspicér (plot, tjek fs, enheder)
3. Rens (filtrér med passende parametre)
4. Visualisér (med subplots, flere signaler)
5. Udtræk features (Envelope, peak-detektion)
6. Klassificér (S₁ vs S₂ med timing-regler)
7. Validér (histogrammer, visuel inspektion)
8. Gem (gem resultater med metadata)

## Centrale mønstre
- **Filtrering:** Butterworth nul-fase (filtfilt)
- **Feature extraction:** Envelope → peak-detektion
- **Klassifikation:** fysiologiske regler baseret på timing
- **Validering:** histogrammer for at sikre at resultater giver mening
- **Metadata:** dokumentér altid fs, filterparametre, thresholds

---

# FORELÆSNING 7: Signaler 3 – Feature engineering, PPG og regression


**Hvad er en feature?**
- Definition: funktion $f(signal)$ der mapper data til et tal (eller få tal)
- Mål: opsummere *relevant* information og ignorere støj
- Kvalitetskriterier:
  - **Fortolkelig:** kan forklares fysiologisk
  - **Robust:** ændrer sig ikke drastisk ved små artefakter
  - **Reproducerbar:** samme data + samme pipeline = samme tal
  - **Brugbar:** hjælper med at besvare et konkret spørgsmål

**Feature vs filter**
- **Filter:** signal → signal (ændrer signalet, fjerner støj)
- **Feature:** signal/beat → tal (opsummerer, skaber tabel)
- Feature er et "informationsfilter" der bevarer relevant og kasserer resten

**Syntetisk eksempel: amplitude, periode, fase**
- Simpel sinus: $A\sin(2\pi f t + \varphi)$
- 3 features definerer signalet fuldt: amplitude $A$, frekvens $f$, fase $\varphi$
- Viser at få tal kan beskrive komplekse signaler

**PPG-fysiologi**
- **Fotopletysmografi:** lysabsorption ved ændringer i blodvolumen
- Hvorfor PPG: portabel (finger, håndled), non-invasiv, nem at måle, udbredt
- Signal domineret af arterielle blodpulser
- Egenskaber varierer med: perfusion (blodflow), arterietryk, bevægelse, sensorkontakt
- **Pulse landmarks:**
  - **Foot:** pulsstart (begyndelse af systolisk stigning)
  - **Systolic peak:** maksimum (højeste blodvolumen)
  - **Dicrotic notch:** sekundært peak (aortaklappens lukning)

**Feature-typer**
- **Beat-niveau:** amplitude (peak - foot), rise time (foot → peak), bredde, areal
- **Interval-niveau:** RR-interval, IBI (inter-beat interval), timing
- **Aggregerede:** gennemsnitlig HR, HRV (heart rate variability), artefakt-procent
- **Kontekstuelle:** afhænger af tilstand (stilling, aktivitet, tidspunkt)
- **Afledte:** kombinerede features (fx HR fra RR, kontraktilitetsindeks)

**Feature-extraction pipeline**
1. Indlæs og inspicér: tjek enheder, fs, manglende værdier
2. Filtrér/glat: valgfri præprocessering for bedre peak-detektion
3. Segmentér i beats: find pulse onset (foot) og peaks
4. Beregn features per beat: amplitude, rise time osv.
5. Kvalitetskontrol: flag dårlige beats (lav amplitude, uregelmæssigheder, artefakter)
6. Aggreger: byg feature-tabel (én række per beat)
7. Gem med metadata: sikr reproducerbarhed

**Forskel på feature og filter**
- **Filter**-output er et signal (waveform)
- **Feature**-output er et tal (eller vektor)
- Eksempel: low-pass filter gør PPG glattere; amplitude-feature udtrækker ét tal per beat

**Variation og error bars**
- **Standard deviation (SD):** spredning i målinger (hvor variable beats er)
- **Standard error (SEM):** usikkerhed på middelværdi (SEM = SD/√n)
- **95% confidence interval (CI):** plausibelt interval for sand middelværdi
- God praksis: vis både datapunkter og error bars; forklar hvad de betyder

**Introduktion til pandas**
- Hvorfor DataFrame: strukturerede data, navngivne kolonner, klar semantik, nem analyse
- Én række per beat, kolonner = features: intuitivt for beat-niveau data
- Oprettelse: `pd.DataFrame(list_of_dicts)` eller `pd.DataFrame(dict_of_lists)`
- Operationer: `.describe()` (opsummeringsstatistik), `.isna()` (manglende), `.to_csv()` (gem)

**Lineær regression**
- Motivation: forudsiger en variabel en anden? (fx relaterer HR til PPG-amplitude?)
- Fitting: find linje $y = mx + b$ der minimerer kvadrerede fejl
- Implementering: `sklearn.linear_model.LinearRegression()` eller `scipy.stats.linregress()`
- Evaluering:
  - **R²:** 0 = ingen relation, 1 = perfekt fit
  - **Residualer:** forskel mellem line og data (bør være tilfældig)
- Fortolkning: hældning (ændringshastighed), skæring (baseline), R² (styrke)
- Begrænsninger: korrelation ≠ kausalitet, ekstrapolation er usikker

**Data-skema og metadata**
- Kolonnenavne: beskrivende, konsistente, inkluder enheder
- Identitetsfelter: subject ID, session, tidsstempel
- Metadatafil: fs, filterparametre, analysedato, analytiker
- Versionering: skema-version, pipeline-version, software-versioner
- Reproducerbarhed: metadata muliggør gentagelse

**Etisk overvejelse: Privacy by design**
- Gem features, ikke rå signaler: reducerer følsomhed og lagring
- Rå PPG muliggør re-identifikation (unikke mønstre); features er mindre identificerende
- Pseudonymiser IDs: ingen navne, hospitals-ID'er eller direkte identifikatorer
- Metadata governance: hvad skal indfanges (reproducerbarhed), hvad skal gemmes (compliance), hvornår slettes
- Adgangskontrol: hvem ser features? rå data? metadata?
- Samtykke: brug data kun som aftalt

## Centrale mønstre
- **Feature:** opsummerer beat til tal
- **Kvalitet:** flag dårlige beats før features beregnes
- **Skema:** klare kolonner, metadata til reproducerbarhed
- **Privatliv:** gem features, ikke rå signal

---

# FORELÆSNING 8: Signaler 4 – Integrationsworkshop

Dette er en 2-øvelses workshop, der integrerer signalbehandling (forelæsning 5-7) med OOP-design (forelæsning 1-4):

### **Øvelse 1 (2t): "Komplet signalanalyse-pipeline"**

**Scenarie:** Givet rå EKG-, PCG- og PPG-datafiler, byg et komplet signalbehandlings-workflow: indlæs, filtrér, udtræk features, validér og gem resultater.

**Opgaver:**
1. Indlæs flere signaler fra CSV-filer (forelæsning 3)
2. Visualisér rå signaler (forelæsning 5): inspicér kvalitet, støj, artefakter
3. Anvend filtrering (forelæsning 6): brug Butterworth eller glidende gennemsnit til at rense signaler
4. Udtræk features (forelæsning 7):
   - EKG: detekter R-peaks, beregn puls
   - PCG: udtræk Envelope, detekter S₁/S₂-hændelser
   - PPG: udtræk beat-level features (amplitude, rise time)
5. Byg feature-tabel (forelæsning 7): én række per beat/hændelse, kolonner = features
6. Validér resultater (forelæsning 6): histogrammer, sammenligning med rå signaler, tjek outliers
7. Gem med metadata: features til CSV, metadata (fs, filterparametre, datoer) til JSON

**Leverancer:**
- Plots der viser rå → filtreret → features for hver signaltype
- Feature-CSV med validerede resultater
- Metadata-JSON der dokumenterer alle parametre
- Kort analyse: hvilke mønstre ser du? Hvad kan gå galt?

**Øvede færdigheder:**
- Fil-I/O og dataparsing (forelæsning 3)
- Signal-visualisering og inspektion (forelæsning 5)
- Filtrering og Envelope-udtrækning (forelæsning 6)
- Feature extraction og kvalitetskontrol (forelæsning 7)
- Metadata og reproducerbarhed (forelæsning 7)

---

### **Øvelse 2 (2t): "Refaktorering til OOP-design"**

**Scenarie:** Tag din fungerende signalanalyse-kode fra Øvelse 1 og refaktorér den til vel-designede OOP-klasser. Byg genanvendelige, testbare komponenter.

**Krav:**
1. Design signalbehandlingsklasser (forelæsning 2):
   - `Signal`-klasse: gemmer data, fs, metadata; metoder til plot, filtrering, feature extraction
   - `ECGAnalyzer`-klasse: specialiseret til EKG (peak-detektion, HR-beregning)
   - `PCGAnalyzer`-klasse: specialiseret til PCG (Envelope, S₁/S₂-detektion)
   - `PPGAnalyzer`-klasse: specialiseret til PPG (beat-detektion, feature extraction)

2. Implementér indkapsling (forelæsning 2):
   - Private attributter: `_raw_data`, `_filtered_data`
   - Offentlige metoder: `filter()`, `extract_features()`, `get_stats()`
   - Validering i konstruktører: tjek fs, enheder, dataområde

3. Fil-I/O med OOP (forelæsning 3):
   - `SignalLoader`-klasse: indlæs CSV, returnér Signal-objekter
   - `FeatureSaver`-klasse: skriv features og metadata til filer
   - Adskillelse af ansvar: I/O-logik separat fra analyse

4. Refaktorér din Øvelse 1-kode:
   - I stedet for: indlæs → for-løkke → filtrér → udtræk → gem
   - Brug: loader.load() → analyzer.filter() → analyzer.extract_features() → saver.save()

5. Test og verificér:
   - Kør analyse med OOP-klasser
   - Verificér at resultater matcher Øvelse 1 (samme features, samme metadata)
   - Dokumentér klasse-interfaces (hvilke metoder, parametre, returtyper)

**Leverancer:**
- Python-modul med Signal-, ECGAnalyzer-, PCGAnalyzer-, PPGAnalyzer-klasser
- Opdateret analysescript med OOP (kortere, klarere end Øvelse 1)
- Verifikation: samme resultater som Øvelse 1, vist side om side
- Kort refleksion: fordele ved OOP? Ulemper? Hvornår vil du bruge det?

**Øvede færdigheder:**
- Klassedesign og indkapsling (forelæsning 2)
- Objektinteraktion: analyzers der kalder andre metoder (forelæsning 2)
- Fil-I/O med objektorienteret tilgang (forelæsning 3)
- Funktioner som byggesten (forelæsning 1)
- Refaktorering: tag fungerende kode og forbedr struktur (forelæsning 1-4)

---

## Workshop-læringsmål

Når du er færdig med øvelserne, bør du kunne:
- Bygge komplette signalbehandlings-workflows fra rå data til validerede features
- Anvende filtrering, feature extraction og valideringsteknikker fra forelæsning 5-7
- Designe genanvendelige klasser der indkapsler signalbehandlingslogik
- Adskille ansvar: indlæsning (I/O) → analyse (processing) → gem (I/O)
- Dokumentere API'er: hvilke metoder findes, inputs/outputs, antagelser
- Refaktorere fungerende kode til renere, mere vedligeholdbar OOP-struktur
- Verificere at refaktorering giver identiske resultater (ingen fejl introduceret)
- Værdsætte OOP: modularitet, genanvendelighed, testbarhed

---

# FORELÆSNING 9: Lineær regression med populationsdata


**Lineær regression – repetition og udvidelse**
- Opsamling fra signals_3: fit linjen $y = mx + b$ ved at minimere kvadrerede fejl
- Nu anvendt på populationsdata med flere individer (én række per person)
- Hvorfor regression på populationsniveau: forudsige udfald, forstå relationer, identificere risikofaktorer

**Forberedelse af populationsdata**
- Én række per person, én kolonne per feature/måling
- Manglende data: håndter med pandas (`dropna()`, `fillna()`)
- Outliers: identificér og beslut (fjern eller undersøg)
- Normalisering: skaler features hvis de har forskellige ranges

**Model-fit og evaluering**
- Fit: `LinearRegression().fit(X, y)`
- Forudsigelser: `y_pred = model.predict(X)`
- Metrikker:
  - **R²:** andel af varians forklaret (0=ingen fit, 1=perfekt fit)
  - **RMSE (Root Mean Squared Error):** gennemsnitlig fejl i originale enheder
  - **Residualer:** forskelle mellem observerede og forudsagte
- Fortolkning: hældning (effektstørrelse), skæring (baseline)

**Validering og residualer**
- Plot residualer vs forudsagte: bør være tilfældig spredning (ingen mønster = godt fit)
- Histogram af residualer: bør være omtrent normal
- Q-Q-plot: residualer vs normalfordeling
- Ikke-tilfældige residualer indikerer at modellen mangler noget (ikke-lineær relation, manglende variabler, subgrupper)

**Flere features (multiple lineær regression)**
- Brug flere kolonner som prædiktorer: `X = df[['age', 'weight', 'activity']]`
- Fit og fortolkning: hver koefficient er effekten af en feature, når de andre holdes konstante
- Multikollinearitet: hvis features korrelerer stærkt, bliver koefficienter ustabile
- Feature selection: hvilke features betyder noget? (korrelation, baglæns elimination, domæneviden)

**Forudsigelse og usikkerhed**
- Punktestimat: `y_pred = model.predict(X_new)`
- Konfidensintervaller: plausibelt interval omkring forudsigelse (større ved ekstrapolation)
- Begrænsninger: ekstrapolér ikke langt uden for træningsdata-området

**Reproducerbarhed med metadata**
- Registrér: feature-navne, enheder, fit-dato, analytiker, software-versioner
- Gem model til genbrug: `pickle.dump(model, open('model.pkl', 'wb'))`
- Dokumentér antagelser: linearitet, uafhængighed, normalitet af residualer

## Centrale mønstre
- Forbered data: rens, tjek manglende/outliers
- Fit model: visualisér data først
- Evaluer: R², RMSE, residualer fortæller historien
- Validér antagelser: residualplots er diagnostiske
- Dokumentér: metadata for reproducerbarhed

---

# FORELÆSNING 10: Datavisualisering og unsupervised læring

**Hvorfor visualisering for populationsdata?**
- Tidsserier er mindre nyttige: populationsdata er tværsnitsdata (mange personer, ét tidspunkt pr. person)
- Opsummeringsstatistik skjuler struktur: visualisering afslører mønstre, Clusterr, outliers
- Exploratory Data Analysis (EDA): forstå før modellering

**Grundlæggende visualisering**
- **Scatter plot:** to kontinuerte variable; se korrelation, outliers, Clusterr
- **Fordelingsplot (histogram):** én variabel; se form, center, spredning, skævhed
- **Box plot:** fordeling pr. gruppe; sammenlign median og spredning på tværs af kategorier
- **Bar plot:** kategoriske data; sammenlign antal eller gennemsnit

**Matplotlib og Seaborn basics**
- matplotlib: lav-niveau kontrol, `plt.scatter()`, `plt.hist()`, `plt.plot()`
- seaborn: high-level, pænere defaults, `sns.scatterplot()`, `sns.histplot()`, `sns.boxplot()`
- Subplots: `fig, ax = plt.subplots(1, 2)` til flere plots
- Tilpasning: labels, legend, titler, farver

**Når tidsserier IKKE giver mening**
- Tidsserier antager data sorteret efter tid (EKG-samples, signaler)
- Populationsdata: rækkefølge er irrelevant (personer er uafhængige)
- Visualisering af populationsdata som tidsserier: misvisende trends, falske mønstre
- Rette tilgang: scatter plots, histogrammer, box plots (rækkefølge-uafhængig)

**unsupervised læring: introduktion**
- Mål: find struktur i data uden labels
- Anvendelser: opdage subgrupper, detektere anomalier, komprimering
- Forskellig fra supervised: ingen ground truth labels at fitte til

**k-Means clustering**
- Idé: opdel data i k Clusterr ved at minimere varians inden for Clusterr
- Algoritme:
  1. Initialisér k tilfældige Clustercentre
  2. Tildel hvert punkt til nærmeste center
  3. Opdatér centre som middel af tildelte punkter
  4. Gentag indtil konvergens
- Valg af k: elbow plot (varians inden for Clusterr vs k), domæneviden
- Implementering: `sklearn.cluster.KMeans(n_clusters=3).fit(X)`

**Iris-datasæt**
- Klassisk datasæt: 150 blomster, 4 features (sepal length/width, petal length/width)
- 3 arter (setosa, versicolor, virginica)
- Hvorfor iris til clustering: visualiserbar (brug 2 features), kendt ground truth til validering, fortolkelig
- Clustering uden at bruge arts-labels: unsupervised udfordring

**Visualisering af Cluster**
- Scatter plot med farver efter Clustertildeling
- Feature-par: plot (feature1, feature2) med Clusterfarver
- Sammenlign med sande labels: silhouette score, purity
- Silhouette-koefficient: -1 (dårlig), 0 (på grænsen), +1 (vel-Clustert)

**Clusterfortolkning**
- Hvad repræsenterer Clusterrne? Beregn gennemsnits-features pr. Cluster
- Er Clusterrne meningsfulde? Tjek om de er sammenhængende (biologisk, statistisk)
- Stabilitet: genkør med forskellige initialiseringer (k-means er tilfældig)

## Centrale mønstre
- EDA: visualisér før modellering
- Scatter plots: se korrelationer og Clusterr
- Histogrammer: forstå fordelinger
- unsupervised: ingen labels, opdag mønstre
- k-means: opdel data i k grupper

---

# FORELÆSNING 11: Supervised learning – klassifikation

**Supervised vs unsupervised**
- **Supervised:** har ground truth labels, lærer at forudsige nye labels
- **unsupervised:** ingen labels, opdager struktur
- Denne forelæsning: supervised klassifikation (forudsige diskrete kategorier)

**Klassifikationsproblem**
- Mål: givet features (X), forudsige klasselabel (y)
- Eksempler: iris-arter fra målinger, patientsygdom fra biomarkører, signalkvalitet (god/dårlig)
- Outputs: forudsagt klasse, confidence/sandsynlighed pr. klasse

**k-Nearest Neighbors (k-NN)**
- Idé: et punkt klassificeres ud fra de k nærmeste naboer
- Algoritme:
  1. Gem alle træningsdata
  2. For nyt punkt, find k nærmeste (afstand, typisk euklidisk)
  3. Forudsig: flertalsklasse blandt de k naboer
- Valg af k: lille k = fleksibel men støjfølsom, stor k = glat men kan underfite; typisk 3-10
- Implementering: `sklearn.neighbors.KNeighborsClassifier(n_neighbors=5).fit(X_train, y_train)`

**Afstand og feature-skalering**
- k-NN afhænger af afstand: features med store ranges dominerer
- Løsning: normaliser/standardisér features
  - **Standardisering:** (x - mean) / std (mean=0, std=1)
  - **Normalisering:** (x - min) / (max - min) (range 0-1)
- `sklearn.preprocessing.StandardScaler()` til nem skalering
- Fit altid scaler på træningsdata, anvend på testdata

**Train-test split**
- Evaluer aldrig på træningsdata: memorering, ikke generalisering
- Split: 70-80% træning, 20-30% test
- Random split for at undgå rækkefølge-bias
- `sklearn.model_selection.train_test_split()`

**Modelevaluering**
- **Accuracy:** (korrekte forudsigelser) / (samlede forudsigelser)
- **Confusion matrix:** true positives, false positives, true negatives, false negatives
- **Precision:** TP / (TP + FP) — af positive forudsigelser, hvor mange er korrekte?
- **Recall:** TP / (TP + FN) — af sande positive, hvor mange findes?
- **F1-score:** harmonisk gennemsnit af precision og recall
- Vælg metric ud fra omkostning: medicinsk diagnose (recall), spam-detektion (precision)

**Visualisering: beslutningsgrænser**
- Plot 2D-features (eller 2D PCA-projektion) med farvede regioner
- Hver region er en forudsagt klasse
- k-NN-grænser er lokale og ujævne (ikke-lineære)
- Viser hvordan klassifikatoren opdeler feature space

**Overfitting og generalisering**
- Overfitting: model memoriserer træningsdata, fejler på nye data (høj træningsaccuracy, lav testaccuracy)
- k-NN-overfitting: meget lille k (k=1 memoriserer)
- Løsning: krydsvalidering for at finde god k

**Krydsvalidering**
- k-fold cross-validation: split data i k folds, træn k gange (én fold holdes ude hver gang)
- Evaluer på den udeladte fold, gennemsnit resultater
- Mere stabilt estimat end enkelt train-test split
- `sklearn.model_selection.cross_val_score()`

**Iris-klassifikation med k-NN**
- Træn på iris-features, forudsig arter
- Sammenlign forudsigelser med sande labels
- Visualisér: 2D-projektioner med beslutningsgrænser
- Confusion matrix: hvilke arter forveksles med hvilke?


## Centrale mønstre
- Supervised: brug labels til træning
- k-NN: simpelt, kræver skalerede features
- Train-test split: forebyg overfitting
- Evaluér: accuracy, precision, recall, confusion matrix
- Krydsvalidering: stabil modelvalg

---

# FORELÆSNING 12: Data-integration workshop


Dette er en integrerende workshop, der anvender begreber fra forelæsning 9-11 uden at introducere nye emner.

### **Øvelse 1 (1t 30m): "Fra features til forudsigelser"**

**Scenarie:** Givet et populationsdatasæt med flere features og en target-variabel, byg en end-to-end analyse-pipeline.

**Opgaver:**
- Indlæs data og udforsk med visualiseringer (histogrammer, scatter plots fra forelæsning 10)
- Rens data (håndtér manglende værdier, outliers)
- Fit lineær regressionsmodel til at forudsige kontinuerligt udfald (forelæsning 9)
- Evaluer med R², RMSE, residualplots
- Dokumentér analysen: metoder, fund, begrænsninger

**Integrations-elementer:**
- Visualiseringsvalg fra forelæsning 10 informerer feature selection
- Regressionsmodel fra forelæsning 9 forudsiger target
- Metadata og reproducerbarhed hele vejen igennem

---

### **Øvelse 2 (1t 30m): "unsupervised opdagelse og supervised forudsigelse"**

**Scenarie:** Givet iris- eller lignende populationsdatasæt, kombiner clustering og klassifikation.

**Opgaver:**
- Anvend k-means clustering (forelæsning 10) til at opdage grupper uden labels
- Visualisér Clusterr (scatter plots fra forelæsning 10)
- Træn k-NN-klassifikator (forelæsning 11) til at forudsige arter/grupper fra features
- Sammenlign: matcher k-NN-forudsigelser k-means-Clusterr?
- Evaluer k-NN med train-test split, confusion matrix, krydsvalidering (forelæsning 11)
- Diskutér: hvornår er unsupervised (clustering) nyttigt vs supervised (k-NN)?

**Integrations-elementer:**
- Visualisering (forelæsning 10) viser Clusterstruktur
- Clustering (forelæsning 10) finder naturlige grupper
- Klassifikation (forelæsning 11) forudsiger gruppetilhørsforhold
- Krydsvalidering sikrer generalisering

---

## Workshop-temaer

- **Pipeline:** indlæs → visualisér → rens → modellér → evaluer → dokumentér
- **Visualisering:** informerer forståelse og feature selection
- **unsupervised:** opdager struktur (clustering fra forelæsning 10)
- **Supervised:** forudsiger med labels (klassifikation fra forelæsning 11, regression fra forelæsning 9)
- **Reproducerbarhed:** dokumentér metoder, parametre, software-versioner
- **Fortolkning:** hvad betyder resultaterne? Begrænsninger? Næste skridt?

## Centrale resultater
- Hands-on erfaring med fuld dataanalyse-workflow
- Integration af regression, clustering og klassifikation
- Øvelse i visualisering til beslutningstagning
- Reproducerbarhed og dokumentationsvaner
- Refleksion over metodevalg
