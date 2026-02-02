# COMPLETE LECTURE PLAN – ST2 APPLIED PROGRAMMING

Overview of 12 lectures covering foundational programming, object-oriented design, signal processing, and population data analysis.

---

## LECTURE OVERVIEW

| # | Lecture | Folder | Duration | Primary Topics |
|---|---------|--------|----------|-----------------|
| 1 | Hello C and Python | oop_1 | 4h | Programming languages, basic syntax, environment setup |
| 2 | Objects, Encapsulation, Interaction | oop_2 | 4h | Classes, methods, data encapsulation, object interaction |
| 3 | Files and Data Loading | oop_3 | 4h | File I/O, CSV parsing, combining OOP with data |
| 4 | Advanced OOP | oop_4_workshop | 4h | Inheritance, polymorphism, abstract classes, design patterns |
| 5 | Signal Basics | signals_1 | 4h | ECG physiology, statistics, peak detection |
| 6 | Filtering and Mechanical Signals | signals_2 | 4h | Filtering, SCG physiology, mechanical timing, envelope extraction |
| 7 | Feature Engineering, PPG and Regression | signals_3 | 4h | Feature definition, PPG physiology, linear regression, variation metrics |
| 8 | Signal Integration and Ethics | signals_4_workshop | 4h | Multimodal integration, signal workflow reflection, ethical analysis |
| 9 | Population Data Basics | populations_data_1 | 4h | Multi-subject datasets, distributions |
| 10 | Statistical Analysis and Inference | populations_data_2 | 4h | Descriptive statistics, hypothesis testing, confidence intervals |
| 11 | Regression and Predictive Models | populations_data_3 | 4h | Linear regression, model validation, feature selection |
| 12 | Data Integration and Communication | populations_data_4_workshop | 4h | End-to-end analysis, reproducibility, results communication |

---

# LECTURE 1: OOP 1 – Hello C and Python

**Folder:** `oop_1`  
**Duration:** 4h (2h lecture + 2h exercises)  
**Jupyter Notebook:** `AP-HelloPython.ipynb`

## Primary Topics Covered in Notebook

**Why both C and Python?**
- C: simplicity but brutal error handling, manual memory management
- Python: easy to learn, simplicity, extensive libraries, free, used everywhere
- When to use each: C for systems programming, Python for data science and AI

**C vs Python: Key Syntax Differences**
- Functions: C requires explicit return types, Python is implicit
- Arrays/Lists: C static arrays, Python dynamic lists with methods
- Conditionals: C switch/case, Python if/elif/else and match
- Loops: C for/while with explicit incrementing, Python for-in with range()
- Memory: C pointers and manual management, Python automatic
- Type system: C explicit typing, Python dynamic typing

**Python Advantages and Disadvantages**
- Pros: easy to learn, simplicity, extensive ecosystem (NumPy, SciPy, pandas, matplotlib), free, AI/ML standard
- Cons: slow, inefficient, runtime errors (dynamic typing), requires debugger usage

**Development Plan: Encapsulation and Generalization Workflow**
1. Write small program without functions (get it working)
2. Encapsulate working pieces into functions with clear names
3. Generalize functions by adding parameters
4. Repeat until you have working functions
5. Refactor to improve and reduce duplication

**Environment Setup and Tools**
- Miniconda installation and conda package management
- Anaconda Navigator for environment management
- VS Code with Python extension (launched from Navigator)
- Running scripts, Python REPL (`python` command), version checking (`python -V`)

**Python Fundamentals Covered**
- Variables and types: int, float, str, bool (dynamic typing)
- Arithmetic operations and string operations
- Lists and dictionaries: creation, manipulation (append, remove, pop)
- Conditionals: if/elif/else, match/case
- Loops: for (with range), while
- Functions: definition with def, parameters, return values
- F-strings for formatted output: `f"{variable=}"`
- Package installation with conda: `conda install <package>`

## Exercise Structure
- **Exercise 1:** Variables and calculations (using debugger to understand state)
- **Exercise 2:** Math operations (addition, subtraction, multiplication, division)
- **Exercise 3:** Working with lists (create, append, remove, combine, sum)
- **Exercise 4:** Functions (define, parameters, return values, formatted output)
- **Exercise 5:** Data visualization with matplotlib (scatter plot from data)

## Key Takeaway
Foundation for Python programming: understand syntax, use debugger, practice with simple operations before moving to classes.

---

# LECTURE 2: OOP 2 – Objects, Encapsulation, and Interaction

**Folder:** `oop_2`  
**Duration:** 4h (2h lecture + 2h exercises)  
**Jupyter Notebook:** `objekter og sammenspil.ipynb`

## Primary Topics Covered in Notebook

**What Are Objects?**
- Objects bundle data (state stored in attributes) and behavior (methods/functions)
- Object identity: each instance is unique
- Objects model real-world entities (Patient, Sensor, Device, Monitor)

**Defining Classes in Python**
- Constructor `__init__(self, ...)`: initializes object state
- Instance variables: stored with `self.attribute_name`
- Methods: functions that operate on `self`
- The `self` parameter: implicit reference to current object instance

**Encapsulation and Data Protection (Key Theme)**
- **Problem:** data can be changed directly and invalidated (e.g., `patient.heart_rate = -500`)
- **Solution:** use `_` convention for private attributes (e.g., `self._heart_rate`)
- Python doesn't enforce, but convention signals: "internal, don't access directly"
- Controlled access: provide methods to safely modify state (e.g., `update_heart_rate(new_hr)`)
- Validation: methods can contain rules (e.g., only allow 0 ≤ HR ≤ 250)

**Object Interaction**
- Objects communicate by calling methods on other objects
- Example: `patient.update_from_sensor(sensor)` — sensor passed as parameter
- Benefits: modularity, loose coupling, testability, clear separation of concerns
- Pattern: each class has one clear responsibility

**Collections of Objects**
- Store objects in lists: `patients = [p1, p2, p3]`
- Iterate and apply operations: `for p in patients: p.update_from_sensor(sensor)`
- Common pattern in medical systems

**Ethics Consideration: Data Governance by Design**
- Encapsulation enforces data access policies at code level
- Sensitive fields (diagnoses, measurements) must be protected by design
- Audit trails: methods can log who accesses what
- Privacy by design: think about access control before writing code

## Exercise Structure
- **Exercise 1:** Your first class (Device with name and status)
- **Exercise 2:** Methods and state (turn_on, turn_off methods)
- **Exercise 3:** Protect internal state (_status as private)
- **Exercise 4:** Patient and measurements (PatientInfo class)
- **Exercise 5:** Sensor → Patient (HeartRateSensor measures, Patient updates from sensor)
- **Exercise 6:** Multiple patients in list (iterate, update, display)
- **Exercise 7:** Monitoring and alerts (Monitor class checks for abnormal values)

## Key Patterns Demonstrated
- **Encapsulation:** `_private` attributes, public methods
- **Interaction:** objects receive other objects as parameters
- **Validation:** methods enforce invariants
- **Lists:** collections of objects with loops

---

# LECTURE 3: OOP 3 – Files and Data Loading

**Folder:** `oop_3`  
**Duration:** 4h (2h lecture + 2h exercises)  
**Jupyter Notebook:** `AP-LoadData.ipynb`

## Primary Topics Covered in Notebook

**Files as Data Source**
- Real data comes from files, not hardcoded values or user input
- Data sources: medical devices, logfiles, software exports, experiments
- **Filer er forbindelsen til virkelighed** (Files are the connection to reality)

**File I/O Fundamentals**
- Opening and reading: `with open("filename", "r") as f:`
- `with` statement: automatic file closing, error handling
- `f.read()`: entire file as one string
- `f.readlines()`: file as list of strings (includes `\n`)
- Closing happens automatically with `with`

**Parsing Structured Data**
- String operations: `.strip()` (remove whitespace and `\n`), `.split(",")` (split by delimiter)
- Type conversion: `int(string)`, `float(string)`, `str(value)`
- **Common pipeline:** read line → strip → split → convert → store
- Example: `values.append(int(line.strip()))`

**CSV Format**
- Comma-Separated Values: simple, widely supported
- First line often contains headers
- `skiprows=1` to skip header
- Multiple columns: use `delimiter=","` and split

**Combining OOP and File Loading**
- Data loader classes: encapsulate file reading logic
- Reusable: one class for different files
- Separation of concerns: file I/O separate from business logic

**Data Visualization Fundamentals**
- Why visualize: see patterns, trends, outliers, relationships immediately
- matplotlib workflow: `plt.plot()`, `plt.scatter()`, `plt.xlabel()`, `plt.ylabel()`, `plt.title()`, `plt.legend()`, `plt.show()`
- Plot types: line plots (time series), scatter plots (relationships)

**OOP for Data Handling**
- `CSVDataLoader` class: `__init__(filename)`, `load_data()` method
- `Signal` class: `__init__(data, fs, label)`, methods for plotting
- Benefits: structure, reusability, clarity

**Ethics Consideration: Data Minimization and Retention**
- Store only necessary data; raw biosignals are sensitive
- Data retention policies: how long to keep? when to delete?
- Backup strategy: for recovery, not indefinite retention
- GDPR: right to be forgotten, retention limits

## Exercise Structure
- **Exercise 1:** Load simple numeric data from file, print stats
- **Exercise 2:** CSV with multiple columns (parse patient data)
- **Exercise 3:** Build DataLoader class for reuse
- **Exercise 4:** Visualization (scatter plot with formatting)
- **Exercise 5:** Bonus - extract and save features

## Key Patterns
- **Pipeline:** `with open() → for line → strip → split → convert → store`
- **Class-based loading:** `CSVDataLoader` with `load_data()` method
- **Separation:** file I/O separate from visualization
- **Reusability:** one loader class for different files

---

# LECTURE 4: OOP 4 – Advanced OOP, Inheritance and Polymorphism

**Folder:** `oop_4_workshop`  
**Duration:** 4h (2h lecture + 2h exercises)  
**Jupyter Notebook:** `OOP4_workshop.ipynb`

## Primary Topics Covered in Notebook

**Workshop Focus: From Device to File**
- Goal: build program that reads data, stores in memory, writes to disk
- Roles: Reader (source), DataHandler (memory), Saver (disk)
- Real workflow: data → structure → analysis → visualization → results

**Inheritance Motivation**
- **Problem:** similar classes (Patient, Doctor, Nurse, Sensor, Device) share structure
- **Solution:** base class with shared attributes/methods, derived classes specialize
- Example: `Person` base class (name, age), `Patient`, `Doctor` inherit
- Use case: medical device hierarchy

**UML Class Diagrams (Design Tool)**
- Visual representation of classes, attributes, methods, and relationships
- Class box: name (top), attributes (middle), methods (bottom)
- `+` means public, `-` means private
- Arrows show relationships and dependencies
- Top-down layout shows hierarchy

**Flowcharts (Process Tool)**
- Ovals: start/stop
- Rectangles: actions/processes
- Diamonds: decisions (yes/no)
- Arrows: flow and SequenceObject
- Purpose: visualize how program executes step-by-step

**Serial Communication and Data Streaming**
- Data from devices comes as continuous stream, not file
- `pyserial` library: `ser = serial.Serial(port, baudrate, timeout)`
- `ser.readline()`: returns bytes, stops at `\n` or timeout
- Must convert: `text = line.decode().strip()`
- Must validate: check for empty, non-numeric, invalid data
- Always close: `ser.close()`

**Design Pattern: Reader → Handler → Saver**
- **USBReader:** reads from serial port, knows only about serial, returns raw data
- **DataHandler:** holds data in memory (list), provides `add_value()`, `get_all()`
- **DataSaver:** writes data to disk (CSV, JSON), knows only about files
- **Benefits:** clear separation, easy to test, easy to extend

**Encapsulation Revisited**
- No global variables: data only in objects
- Each class has one responsibility
- Indirect access: don't modify handler data directly, use `add_value()` method

**Flowchart Example (from notebook)**
```
Start → Read data from USB → Store data in memory → Check {Enough data?}
  No → Read data from USB
  Yes → Save data to file → End
```

**Ethics Consideration: Serial Data and Health Data**
- Serial data is often health-related (sensors, devices)
- GDPR: health data is "special category" (restricted)
- Metadata is critical: sampling rate, device type, protocol, timing
- Data minimization: store only necessary features, not raw streams
- Security: access control, encryption, audit trails

## Exercise Structure (Not detailed in notebook, but referenced)
- Design class hierarchy (inheritance)
- Implement Reader, Handler, Saver classes
- Use UML diagrams to plan architecture
- Implement serial reading with validation
- Build end-to-end workflow

## Key Concepts
- **Inheritance:** base classes, derived classes, `super()`
- **Polymorphism:** different objects, same interface (all readers have `read()`)
- **Design patterns:** Strategy, Observer, Factory
- **UML:** visual design before coding
- **Flowcharts:** step-by-step logic
- **Encapsulation:** single responsibility, no globals
- **Design:** clear separation of concerns (Reader/Handler/Saver)

---

# LECTURE 5: Signals 1 – Signal Basics, NumPy, and Statistics

**Folder:** `signals_1`  
**Duration:** 4h (2h lecture + 2h exercises)  
**Jupyter Notebook:** `signals_1.ipynb`

## Primary Topics Covered in Notebook

**Ethics Mini-Topic: ECG as Biometric and Health Data**
- ECG is unique to individuals (like fingerprints) → re-identification risk
- ECG reveals latent diseases: arrhythmias, heart attack risk, unknown conditions
- Permanent health history: once stored, cannot be taken back
- Scenarios: hospital (diagnostic), wearables (continuous monitoring), research (data sharing)
- Ethical challenges: informed consent, data minimization, secure storage, responsible use

**Why NumPy?**
- Python lists are slow: `sum(list)/len(list)` requires loop
- NumPy is optimized: `np.mean(array)` is vectorized and fast
- Vectorization: operations on entire arrays without explicit loops
- Memory efficiency: contiguous memory allocation

**NumPy Basics**
- Create arrays: `np.array(list)`, `np.zeros(n)`, `np.ones(n)`, `np.linspace(start, stop, n)`
- Indexing: `arr[0]`, `arr[-1]`, `arr[1:5]`
- Slicing with step: `arr[::2]` (every 2nd element)
- Vectorized operations: `arr + 5`, `arr * 2`, `np.sqrt(arr)`
- Broadcasting: dimension alignment for operations
- Functions: `np.mean()`, `np.std()`, `np.min()`, `np.max()`, `np.sum()`

**Data Workflow**
1. Load Data
2. Inspect (check structure, range, units)
3. Clean (remove artifacts, missing values)
4. Visualize (understand patterns)
5. Extract Features (compute summaries)
6. Store (save results)

**ECG Physiology**
- Electrical activity of heart: depolarization and repolarization cycles
- Main features: P wave (atrial), QRS complex (ventricular), T wave (recovery)
- **R-peak:** largest deflection in QRS, most recognizable feature
- **RR interval:** time between consecutive R-peaks (beat-to-beat timing)
- **Heart rate:** 60 / (RR interval in seconds) = bpm
- **Sampling rate:** how often signal measured (Hz); affects resolution

**Basic Statistics**
- Mean: average, center of distribution
- Variance: spread squared
- Standard deviation (std): square root of variance, spread in same units as data
- Why statistics matter: establish baseline, detect abnormalities, compare groups
- NumPy functions: `np.mean()`, `np.var()`, `np.std()`

**Peak Detection (Threshold-based)**
- **Idea:** peaks are high-amplitude points above background
- **Threshold selection:** `mean + k*std` (k typically 2-3 for clean signals)
- **Algorithm:** find indices where values exceed threshold
- Example:
  ```python
  threshold = np.mean(data) + 2 * np.std(data)
  peaks = np.where(data > threshold)[0]  # indices of peaks
  ```
- **Limitations:** works for clean signals, fails with noise, artifacts, baseline drift
- **Improvements:** preprocessing (filtering), local maxima (context), validation

**Filtering Motivation (mentioned)**
- Noise sources: electrical interference, motion artifacts, baseline drift
- Filters remove unwanted components
- Simple example: moving average smooths signal

**Visualization for Inspection**
- Plot signal with mean and std bands to see noise
- Visualize statistics with bar plots
- Histograms show distribution shape

**Ethics Consideration: ECG Privacy**
- Biometric risk: unique patterns enable re-identification
- Latent information: reveals health conditions subject may not know
- Permanent record: cannot be "forgotten"
- Consent and use: data should only be used as agreed

## Exercise Structure
- **Exercise 1:** Inspect random signals (plot 2 signals, compare noise, amplitude, pattern)
- **Exercise 2:** Extract features from EKG (mean, std, variability)
- **Exercise 3:** Analyze noisy EKG (filter, extract HR, identify peaks)
- **Exercise 4:** Extract heart cycles (class-based approach, get specific cycle from signal)

## Key Patterns and Functions
- **NumPy operations:** vectorized instead of loops
- **Inspection:** plot + compute stats to understand data
- **Peak detection:** threshold-based using mean + k*std
- **Classes:** `HeartRateExtractor` with methods for feature extraction

---

# LECTURE 6: Signals 2 – Filtering and Mechanical Signals

**Folder:** `signals_2`  
**Duration:** 4h (2h lecture + 2h exercises)  
**Jupyter Notebook:** `signals_2_SCG_Filtering_FeatureTiming_v2.ipynb`

## Primary Topics Covered in Notebook

**Ethics: Data Provenance and Metadata**
- Metadata is essential: sampling rate (fs), units, device/model, calibration, protocol
- Without metadata: cannot interpret or verify analysis
- Metadata integrity: corrupted metadata invalidates results
- Transparency: document all processing steps
- Audit trails: who did what, when, with which parameters (compliance/accountability)

**Ethics: Handling Sensitive Health Data (GDPR/Danish Law)**
- Formål (purpose): define before processing
- Retsgrundlag (legal basis): why is this legal?
- External services: if using cloud, need data processor agreement
- Adgangskontrol (access control): least privilege, no public links
- Kryptering (encryption): at rest and in transit
- Opbevaring & sletning (retention): delete when purpose ends
- DPIA (Data Impact Assessment): required for high-risk processing

**Why Filtering?**
- Real signals contain noise: 50/60 Hz electrical, motion artifacts, baseline drift
- Filters remove unwanted components, preserve signal of interest
- Trade-offs: smoothing reduces noise but also reduces peaks; phase effects

**Moving Average Filter**
- Simple: take average of window around each point
- Algorithm:
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
- Removes high-frequency noise but smooths peaks
- Window size determines how much smoothing

**SciPy Signal Processing**
- `scipy.signal.butter()`: design Butterworth filter
- `scipy.signal.filtfilt()`: zero-phase filtering (no time shift)
- Filter types: lowpass, highpass, bandpass, bandstop
- Example:
  ```python
  b, a = butter(2, 20, fs=fs, btype='lowpass')
  filtered = filtfilt(b, a, signal)
  ```

**PCG/SCG Physiology**
- **PCG:** Phonocardiography (heart sounds from stethoscope)
- **SCG:** Seismocardiography (mechanical vibrations from heartbeat)
- Frequency content: 50 Hz < audio < 20,000 Hz; cardiac sounds 20-300 Hz
- **S₁ (Lub):** first heart sound when mitral/tricuspid valves close, marks systole start
- **S₂ (Dub):** second heart sound when aortic/pulmonic valves close, marks diastole start
- Timing: S₁ → S₂ is systole (short), S₂ → next S₁ is diastole (long)

**Envelope Extraction**
- Purpose: highlight amplitude variations (where the important events are)
- Algorithm:
  1. Remove mean
  2. Rectify (absolute value)
  3. Moving maximum over window
  4. Add mean back
- Used to detect S₁ and S₂ by finding peaks in envelope

**Peak Detection in Envelope**
- Use `scipy.signal.find_peaks()` with parameters:
  - `height=np.std(envelope)`: minimum peak height
  - `distance=int(0.15*fs)`: minimum distance between peaks
- Returns indices of detected peaks

**S₁/S₂ Classification**
- Based on intervals between peaks:
  - **S₁:** comes after long pause (diastole)
  - **S₂:** comes after short pause (systole)
- Physiological rule:
  ```
  IF interval[i] < interval[i+1]:
      peak[i] is S₁
  ELSE:
      peak[i] is S₂
  ```

**Validation via Histograms**
- Plot intervals between detected peaks
- S₁ intervals (systole) should be shorter
- S₂ intervals (diastole) should be longer
- Histogram shows if classification makes sense

**Data Workflow for SCG/PCG**
1. Load data
2. Inspect (plot, check fs, units)
3. Clean (filter with appropriate parameters)
4. Visualize (with subplots, multiple signals)
5. Extract features (envelope, peak detection)
6. Classify (S₁ vs S₂ using timing rules)
7. Validate (histograms, visual inspection)
8. Store (save results with metadata)

## Exercise Structure
- **Exercise 1:** Load and plot ECG + PCG (inspect quality)
- **Exercise 2:** Moving average filter (choose window size, discuss parameter trade-offs)
- **Exercise 3:** Understand PCG (heart sounds, what is S₁/S₂)
- **Exercise 4:** Extract envelope from PCG
- **Exercise 5:** Detect peaks in envelope
- **Exercise 6:** Classify S₁ vs S₂ using intervals
- **Exercise 7:** Validate with histograms
- **Bonus Exercise:** Use ECG R-peaks to improve SCG classification

## Key Patterns
- **Filtering:** Butterworth zero-phase (filtfilt)
- **Feature extraction:** envelope then peak detection
- **Classification:** physiological rules based on timing
- **Validation:** histograms to verify results make sense
- **Metadata:** always document fs, filter parameters, thresholds

---

# LECTURE 7: Signals 3 – Feature Engineering, PPG and Regression

**Folder:** `signals_3`  
**Duration:** 4h (2h lecture + 2h exercises)  
**Jupyter Notebook:** `signals_3.ipynb`

## Primary Topics Covered in Notebook

**What Is a Feature?**
- Definition: function f(signal) that maps data to a number (or few numbers)
- Goal: opsummere *relevant* information and ignore noise
- Quality criteria:
  - **Fortolkelig** (interpretable): can explain physiologically
  - **Robust:** doesn't change drastically with small artifacts
  - **Reproducerbar** (reproducible): same data + same pipeline = same number
  - **Brugbar** (useful): helps answer concrete question

**Feature vs Filter**
- **Filter:** signal → signal (changes signal, removes noise)
- **Feature:** signal/beat → number (summarizes, creates table)
- Feature is an "information filter" that keeps relevant, discards rest

**Synthetic Example: Amplitude, Period, Phase**
- Simple sinusoid: A*sin(2πf*t + φ)
- 3 features fully define the signal: amplitude A, frequency f, phase φ
- Demonstrates: few numbers can capture complex signal

**PPG Physiology**
- **Photoplethysmography:** light absorption by blood volume changes
- Why PPG: portable (fingertip, wrist), non-invasive, easy to measure, widely available
- Signal dominated by arterial blood pulsations
- Properties vary with: perfusion (blood flow), arterial pressure, motion, sensor contact
- **Pulse landmarks:**
  - **Foot:** pulse start (systolic rise beginning)
  - **Systolic peak:** maximum (highest blood volume)
  - **Dicrotic notch:** secondary peak (aortic valve closure)

**Feature Types**
- **Beat-level:** amplitude (peak - foot), rise time (foot → peak), width, area
- **Interval-level:** RR interval, IBI (inter-beat interval), timing
- **Aggregated:** mean HR, HRV (heart rate variability), artifact percentage
- **Contextual:** depends on state (posture, activity, time of day)
- **Derived:** combine features (e.g., HR from RR, contractility index)

**Feature Extraction Pipeline**
1. Load and inspect: check units, fs, missing values
2. Filter/smooth: optional preprocessing to improve peak detection
3. Segment into beats: find pulse onsets (foot) and peaks
4. Compute features per beat: amplitude, rise time, etc.
5. Quality control: flag bad beats (low amplitude, irregular, artifacts)
6. Aggregate: build feature table (one row per beat)
7. Save with metadata: enable reproducibility

**Difference Between Feature and Filter**
- **Filter** output is a signal (waveform)
- **Feature** output is a number (or vector)
- Example: low-pass filter makes PPG smoother; amplitude feature extracts single number per beat

**Variation and Error Bars**
- **Standard deviation (SD):** spread in your measurements (how variable beats are)
- **Standard error (SEM):** uncertainty on mean (SEM = SD/√n)
- **95% confidence interval (CI):** plausible range for true mean
- Good practice: show both data points and error bars; discuss what they mean

**Introduction to pandas**
- Why DataFrame: structured data, named columns, clear semantics, easy analysis
- One row per beat, columns = features: intuitive for beat-level data
- Creating: `pd.DataFrame(list_of_dicts)` or `pd.DataFrame(dict_of_lists)`
- Operations: `.describe()` (summary stats), `.isna()` (missing), `.to_csv()` (save)

**Linear Regression**
- Motivation: does one variable predict another? (e.g., does HR relate to PPG amplitude?)
- Fitting: find line y = mx + b minimizing squared errors
- Implementation: `sklearn.linear_model.LinearRegression()` or `scipy.stats.linregress()`
- Evaluation:
  - **R²:** 0 = no relationship, 1 = perfect fit
  - **Residuals:** differences from line (should be random)
- Interpretation: slope (rate of change), intercept (baseline), R² (strength)
- Limits: correlation ≠ causation, extrapolation unreliable

**Data Schema and Metadata**
- Column naming: descriptive, consistent, include units
- Identity fields: subject ID, session, timestamp
- Metadata file: fs, filter parameters, analysis date, analyst
- Versioning: schema version, pipeline version, software versions
- Reproducibility: metadata enables replication

**Ethics Consideration: Privacy by Design**
- Store features, not raw signals: reduces sensitivity and storage
- Raw PPG enables re-identification (unique patterns); features are less identifying
- Pseudonymize IDs: no names, hospital IDs, or direct identifiers
- Metadata governance: what to capture (reproducibility), what to retain (compliance), when to delete
- Access control: who sees features? raw data? metadata?
- Consent: use data only as subject agreed

## Exercise Structure
- **Exercise 1:** Define features for PPG (plan 3-5 features, discuss robustness)
- **Exercise 2:** Beat detection and quality checks (flag artifacts, low amplitude)
- **Exercise 3:** Extract features (IBI, HR, amplitude, rise time, etc.)
- **Exercise 4:** Build DataFrame and save (CSV + JSON metadata)

## Key Patterns
- **Feature:** summarize beat into numbers
- **Quality:** flag bad beats before computing features
- **Schema:** clear columns, metadata for reproducibility
- **Privacy:** store features, not raw signal

---

# LECTURE 8: Signals 4 – Signal Integration and Ethics

**Folder:** `signals_4_workshop`  
**Duration:** 4h (1h lecture + 3h workshop)

## Workshop Structure (Not detailed in provided notebook, but implied from lecture_content)

This is a 2-exercise workshop focused on reflection and ethical analysis:

### **Exercise 1 (2h): "From Raw Data to Clinical Insights: Documenting Your Analysis Journey"**

**Scenario:** You've extracted features from multimodal signals (ECG, SCG, PPG). Now communicate your work to clinicians, engineers, and patients.

**Create a narrative document explaining:**
- What you measured: describe signals, sampling rates, physiological meaning
- Design choices: justify filtering strategy, feature selection, parameter choices
- Validation: how did you verify results? Do detected events make physiological sense?
- Limitations: what could go wrong? What assumptions did you make?
- Metadata and reproducibility: what would someone need to replicate?

**Ethical reflection:**
- Privacy considerations and how you addressed them
- Potential misuse and safeguards
- Populations where methods might fail

### **Exercise 2 (2h): "Building a Responsible Biosignal Analysis System"**

**Scenario:** Design a wearable system that monitors PPG and computes HRV, syncs to smartphone and cloud.

**Design document addressing:**
- Architecture: what data stored locally vs cloud? What transmitted?
- Privacy: minimize re-identification risk while enabling research
- Transparency: what does user see? How communicate limitations?
- Equity: works for different skin tones? Different body types? Different activity levels?
- Consent and control: what can users opt in/out of?
- Accountability: detect misuse? What audit trails?

**Critical thinking:**
- Tensions between goals (accuracy vs privacy, convenience vs security)
- Designer responsibility
- Potential harms
- Who benefits vs who harmed

## Key Themes
- Integration: multimodal signals reveal complementary information
- Reflection: why we made design choices, limitations
- Ethics throughout pipeline: collection → storage → processing → analysis → dissemination
- Responsibility: acknowledge consequences, design safeguards
- Communication: explain to different audiences

---

# SUMMARY: LECTURES 1-8

**Programming Progression:**
- Lectures 1-4: OOP foundation (syntax, classes, files, inheritance)
- Lectures 5-8: Signal processing (NumPy, filtering, features, integration)

**Ethical Themes Throughout:**
- Data governance: consent, minimization, access control
- Privacy: biometric risk, re-identification, security
- Transparency: document decisions, metadata, audit trails
- Responsibility: consider consequences, design safeguards

**Practical Skills:**
- Working with real data from files
- Signal processing: filtering, envelope, peak detection
- Feature extraction and schema design
- Reflection and ethical analysis

---

**Note:** Lectures 9-12 (populations_data_1 through populations_data_4_workshop) were not included in provided notebooks, but the lecture_content.md overview indicates they cover:
- Lecture 9: Multi-subject datasets, pandas groupby, distributions
- Lecture 10: Statistical tests, hypothesis testing, confidence intervals
- Lecture 11: Linear regression, model validation, feature selection
- Lecture 12: End-to-end analysis, reproducibility, communication
