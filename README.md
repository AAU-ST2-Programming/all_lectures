# COMPLETE LECTURE PLAN – ST2 APPLIED PROGRAMMING

Overview of 12 lectures covering foundational programming, object-oriented design, signal processing, and population data analysis.

---

## LECTURE OVERVIEW

| # | Lecture | Folder | Duration | Primary Topics |
|---|---------|--------|----------|-----------------|
| 1 | Hello C and Python | oop_1 | 4h | Programming languages, basic syntax, environment setup |
| 2 | Objects, Encapsulation, Interaction | oop_2 | 4h | Classes, methods, data encapsulation, object interaction |
| 3 | Files and Data Loading | oop_3 | 4h | File I/O, CSV parsing, combining OOP with data |
| 4 | OOP Integration Workshop | oop_4_workshop | 4h | Integration of OOP, file I/O, visualization; device monitoring systems |
| 5 | Signal Basics | signals_1 | 4h | ECG physiology, statistics, peak detection |
| 6 | Filtering and Mechanical Signals | signals_2 | 4h | Filtering, SCG physiology, mechanical timing, envelope extraction |
| 7 | Feature Engineering, PPG and Regression | signals_3 | 4h | Feature definition, PPG physiology, linear regression, variation metrics |
| 8 | Signal Integration and Ethics | signals_4_workshop | 4h | Multimodal integration, signal workflow reflection, ethical analysis |
| 9 | Linear Regression with Population Data | populations_data_1 | 4h | Linear regression, model validation, residuals |
| 10 | Data Visualization and Unsupervised Learning | populations_data_2 | 4h | Data visualization, distributions, scatter plots, k-means clustering (Iris dataset) |
| 11 | Supervised Learning: Classification | populations_data_3 | 4h | k-NN classification, decision boundaries, model evaluation |
| 12 | Data Integration Workshop | populations_data_4_workshop | 4h | End-to-end analysis: regression, clustering, classification, reproducibility, communication |

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

# LECTURE 4: OOP 4 – OOP Integration Workshop

**Folder:** `oop_4_workshop`  
**Duration:** 4h (0.5h intro + 1.75h exercise 1 + 1.75h exercise 2)  
**Jupyter Notebook:** `OOP4_workshop.ipynb`

## Workshop Introduction (30 minutes)

**Goal:** Build a complete data pipeline that integrates everything from lectures 1-3.

**Big Picture:**
- **Exercise 1:** Create a device monitoring system that reads measurements, stores them in objects, saves to file, and visualizes
- **Exercise 2:** Extend to multi-device scenario: collect from multiple sensors, manage data centrally, save and reload with full round-trip validation

**What You'll Practice:**
- Designing classes (lecture 2): what data? what methods? how to encapsulate?
- Object interaction (lecture 2): objects calling methods on other objects
- File I/O (lecture 3): reading CSV, parsing data, writing results
- Data visualization (lectures 1 & 3): matplotlib to understand and communicate results
- Complete workflow: design → implement → test → visualize → save/reload

**No New Concepts:** Everything you need you learned in lectures 1-3. This is about *integrating* those ideas into a realistic workflow.

---

## Exercise 1: Single Device Monitoring System (1h 45m)

**Scenario:** You have a heart rate monitor device. Build a system to collect measurements, store them safely, and save them to disk.

**Requirements:**
1. Define a `Measurement` class:
   - Stores: value, timestamp
   - Validates: heart rate must be 40-200 bpm (reject invalid data)
   - Method: `is_valid()` returns True/False

2. Define a `Device` class:
   - Stores: name, device_id, list of measurements
   - Methods: `add_measurement(measurement)`, `get_all_measurements()`, `get_stats()` (mean, min, max)
   - Encapsulation: measurements accessed only through methods, not directly

3. Simulate data collection:
   - Create device, generate 20 random measurements (some valid, some invalid)
   - Add only valid measurements to device
   - Print stats: how many accepted vs rejected?

4. Save to file (lecture 3):
   - Write measurements to CSV: timestamp, value, device_id
   - Include metadata: device name, number of measurements, collection date

5. Load and verify:
   - Read CSV back into new device
   - Verify loaded data matches saved data (round-trip test)

6. Visualize:
   - Plot measurements over time
   - Add mean line and ±1 std band
   - Label axes, title with device name

**Key Skills Practiced:**
- Encapsulation: data validation in constructor/methods
- Object interaction: Device holds Measurement objects
- File I/O: CSV write and parse
- Visualization: matplotlib line plot with bands

---

## Exercise 2: Multi-Device Data System (1h 45m)

**Scenario:** Hospital has multiple monitors (ECG, PPG, temperature). Build a system to manage all devices, collect data, and enable cross-device analysis.

**Requirements:**
1. Extend from Exercise 1:
   - Reuse `Device` and `Measurement` classes (no changes needed)
   - Create `DataCollector` class (new):
     - Stores: list of devices
     - Methods: `add_device(device)`, `add_measurement(device_id, measurement)`, `get_device(device_id)`, `get_all_devices()`
     - Encapsulation: devices accessed through methods

2. Initialize system:
   - Create 3 devices: ECG (0-150 bpm), PPG (40-200 bpm), Temperature (35-41°C)
   - Add to collector
   - Generate 15-20 measurements per device (mix valid and invalid)

3. Save all data:
   - Write to single CSV: device_type, device_id, timestamp, value
   - Metadata file (JSON): device names, ranges, collection date, number of measurements per device

4. Load and verify:
   - Read CSV and metadata
   - Reconstruct devices and measurements
   - Verify no data lost (compare row counts, value ranges)

5. Analyze and visualize:
   - Subplot: one plot per device (3 subplots)
   - Each plot: measurements over time with mean and std
   - Compare: which device has most variation? most rejections?

6. Cross-device insight (bonus):
   - Correlate any pairs of devices (e.g., does ECG correlate with PPG?)
   - Plot correlation scatter plot

**Key Skills Practiced:**
- Object composition: Collector contains Devices; Devices contain Measurements
- Multiple file operations: CSV data + JSON metadata
- Parsing and validation: reconstruct from saved data
- Multi-panel visualization: subplots for comparison
- Complete pipeline: design → implement → save → load → analyze → visualize

---

## Workshop Learning Outcomes

By end of exercises, you should be able to:
- ✓ Design a class hierarchy: what goes in each class?
- ✓ Use encapsulation: protect data, validate inputs, expose through methods
- ✓ Implement object interaction: objects calling methods on other objects
- ✓ Read and write CSV files with proper formatting
- ✓ Parse structured data from files back into objects
- ✓ Visualize multiple datasets side-by-side
- ✓ Build and test a complete end-to-end pipeline
- ✓ Verify data integrity: save, load, check for data loss

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

# LECTURE 8: Signals 4 – Integration Workshop

**Folder:** `signals_4_workshop`  
**Duration:** 4h (2h exercise 1 + 2h exercise 2)

## Workshop Structure

This is a 2-exercise workshop that integrates signal processing (lectures 5-7) with OOP design (lectures 1-4):

### **Exercise 1 (2h): "Complete Signal Analysis Pipeline"**

**Scenario:** Given raw ECG, PCG, and PPG data files, build a complete signal processing workflow: load, filter, extract features, validate, save results.

**Tasks:**
1. Load multiple signals from CSV files (lecture 3)
2. Visualize raw signals (lecture 5): inspect quality, noise, artifacts
3. Apply filtering (lecture 6): use Butterworth or moving average to clean signals
4. Extract features (lecture 7):
   - ECG: detect R-peaks, compute heart rate
   - PCG: extract envelope, detect S₁/S₂ events
   - PPG: extract beat-level features (amplitude, rise time)
5. Build feature table (lecture 7): one row per beat/event, columns = features
6. Validate results (lecture 6): histograms, comparison to raw signals, check for outliers
7. Save with metadata: features to CSV, metadata (fs, filter params, dates) to JSON

**Deliverables:**
- Plots showing raw → filtered → features for each signal type
- Feature CSV with validated results
- Metadata JSON documenting all parameters
- Brief analysis: what patterns do you see? What might go wrong?

**Skills Practiced:**
- File I/O and data parsing (lecture 3)
- Signal visualization and inspection (lecture 5)
- Filtering and envelope extraction (lecture 6)
- Feature extraction and quality control (lecture 7)
- Metadata and reproducibility (lecture 7)

---

### **Exercise 2 (2h): "Refactoring into OOP Design"**

**Scenario:** Take your working signal analysis code from Exercise 1 and refactor it into well-designed OOP classes. Build reusable, testable components.

**Requirements:**
1. Design signal processing classes (lecture 2):
   - `Signal` class: stores data, fs, metadata; methods for plotting, filtering, feature extraction
   - `ECGAnalyzer` class: specialized for ECG (peak detection, HR computation)
   - `PCGAnalyzer` class: specialized for PCG (envelope, S₁/S₂ detection)
   - `PPGAnalyzer` class: specialized for PPG (beat detection, feature extraction)

2. Implement encapsulation (lecture 2):
   - Private attributes: `_raw_data`, `_filtered_data`
   - Public methods: `filter()`, `extract_features()`, `get_stats()`
   - Validation in constructors: check fs, units, data range

3. File I/O with OOP (lecture 3):
   - `SignalLoader` class: load CSV, return Signal objects
   - `FeatureSaver` class: write features and metadata to files
   - Separation of concerns: I/O logic separate from analysis

4. Refactor your Exercise 1 code:
   - Instead of: load → for loop → filter → extract → save
   - Use: loader.load() → analyzer.filter() → analyzer.extract_features() → saver.save()

5. Test and verify:
   - Run analysis using OOP classes
   - Verify results match Exercise 1 (same features, same metadata)
   - Document class interfaces (what methods, parameters, return types)

**Deliverables:**
- Python module with Signal, ECGAnalyzer, PCGAnalyzer, PPGAnalyzer classes
- Updated analysis script using OOP (shorter, clearer than Exercise 1)
- Verification: same results as Exercise 1, demonstrated side-by-side
- Brief reflection: advantages of OOP approach? Disadvantages? When would you use this?

**Skills Practiced:**
- Class design and encapsulation (lecture 2)
- Object interaction: analyzer methods call other methods (lecture 2)
- File I/O with object-oriented approach (lecture 3)
- Functions as building blocks (lecture 1)
- Refactoring: taking working code and improving structure (lectures 1-4)

---

## Workshop Learning Outcomes

By end of exercises, you should be able to:
- ✓ Build complete signal processing workflows from raw data to validated features
- ✓ Apply filtering, feature extraction, and validation techniques from lectures 5-7
- ✓ Design reusable classes that encapsulate signal processing logic
- ✓ Separate concerns: load (I/O) → analyze (processing) → save (I/O)
- ✓ Document APIs: what methods exist, what inputs/outputs, what assumptions
- ✓ Refactor working code into cleaner, more maintainable OOP structure
- ✓ Verify that refactoring produces identical results (no bugs introduced)
- ✓ Appreciate OOP: modularity, reusability, testability

---

# LECTURE 9: Linear Regression with Population Data

**Folder:** `populations_data_1`  
**Duration:** 4h (2h lecture + 2h exercises)  
**Jupyter Notebook:** `populations_1.ipynb`

## Primary Topics Covered in Notebook

**Linear Regression Review and Extension**
- Recap from signals_3: fit line y = mx + b to minimize squared errors
- Now applied to multi-subject population data (one row per subject)
- Why regression at population scale: predict outcomes, understand relationships, identify risk factors

**Preparing Population Data**
- One row per subject, one column per feature/measurement
- Missing data: handle with pandas (`dropna()`, `fillna()`)
- Outliers: identify and decide (remove or investigate)
- Normalization: scale features if on different ranges

**Model Fitting and Evaluation**
- Fit: `LinearRegression().fit(X, y)`
- Predictions: `y_pred = model.predict(X)`
- Metrics:
  - **R²:** proportion of variance explained (0=no fit, 1=perfect)
  - **RMSE (Root Mean Squared Error):** average prediction error in original units
  - **Residuals:** differences between observed and predicted
- Interpretation: slope (effect size), intercept (baseline)

**Validation and Residuals**
- Plot residuals vs predicted: should be random scatter (no pattern = good fit)
- Histogram of residuals: should be roughly normal
- Q-Q plot: residuals vs normal distribution
- Non-random residuals indicate model is missing something (non-linear relationship, missing variables, subgroups)

**Multiple Features (Multiple Linear Regression)**
- Use multiple columns as predictors: `X = df[['age', 'weight', 'activity']]`
- Fit and interpret: each coefficient is the effect of that feature holding others constant
- Multicollinearity: if features correlate strongly, coefficients become unstable
- Feature selection: which features matter? (correlation, backwards elimination, domain knowledge)

**Prediction and Uncertainty**
- Point estimate: `y_pred = model.predict(X_new)`
- Confidence intervals: plausible range around prediction (larger for extrapolation)
- Limitations: don't extrapolate far beyond training data range

**Reproducibility with Metadata**
- Record: feature names, feature units, fit date, analyst, software versions
- Save model for reuse: `pickle.dump(model, open('model.pkl', 'wb'))`
- Document assumptions: linearity, independence, normality of residuals

## Exercise Structure
- **Exercise 1:** Load population data, explore with scatter plots and correlations
- **Exercise 2:** Fit simple linear regression (1 predictor), evaluate R², RMSE
- **Exercise 3:** Visualize residuals, check assumptions
- **Exercise 4:** Multiple linear regression (2+ predictors), compare models
- **Exercise 5:** Prediction on new subjects, discuss confidence

## Key Patterns
- Prepare data: clean, check for missing/outliers
- Fit model: visualize data first
- Evaluate: R², RMSE, residuals tell the story
- Validate assumptions: residual plots are diagnostic
- Document: metadata for reproducibility

---

# LECTURE 10: Data Visualization and Unsupervised Learning

**Folder:** `populations_data_2`  
**Duration:** 4h (2h lecture + 2h exercises)  
**Jupyter Notebook:** `populations_2.ipynb`

## Primary Topics Covered in Notebook

**Why Visualization for Population Data?**
- Time series less useful: population data is cross-sectional (many subjects, one timepoint per subject)
- Summary statistics alone hide structure: visualization reveals patterns, clusters, outliers
- Exploratory Data Analysis (EDA): understand before modeling

**Visualization Fundamentals**
- **Scatter plot:** two continuous variables; see correlation, outliers, clusters
- **Distribution plot (histogram):** one variable; see shape, center, spread, skewness
- **Box plot:** distribution by groups; compare medians and spread across categories
- **Bar plot:** categorical data; compare counts or means

**Matplotlib and Seaborn Basics**
- matplotlib: low-level control, `plt.scatter()`, `plt.hist()`, `plt.plot()`
- seaborn: high-level, prettier defaults, `sns.scatterplot()`, `sns.histplot()`, `sns.boxplot()`
- Subplots: `fig, ax = plt.subplots(1, 2)` to create multiple plots
- Customization: labels, legends, titles, colors

**When Time Series DON'T Make Sense**
- Time series assumes data ordered by time (ECG samples, signals)
- Population data: order irrelevant (subjects independent)
- Visualizing population data as time series: misleading trends, false patterns
- Right approach: scatter plots, histograms, box plots (order-independent)

**Unsupervised Learning: Introduction**
- Goal: find structure in unlabeled data
- Applications: discover subgroups, detect anomalies, compression
- Different from supervised: no ground truth labels to fit to

**k-Means Clustering**
- Idea: partition data into k clusters minimizing within-cluster variance
- Algorithm:
  1. Initialize k random cluster centers
  2. Assign each point to nearest center
  3. Update centers to mean of assigned points
  4. Repeat until convergence
- Choosing k: elbow plot (within-cluster variance vs k), domain knowledge
- Implementation: `sklearn.cluster.KMeans(n_clusters=3).fit(X)`

**Iris Dataset**
- Classic dataset: 150 flowers, 4 features (sepal length/width, petal length/width)
- 3 species (setosa, versicolor, virginica)
- Why iris for clustering: visualizable (use 2 features), known ground truth for validation, interpretable
- Clustering without using species label: unsupervised challenge

**Visualizing Clusters**
- Scatter plot with colors by cluster assignment
- Feature pairs: plot (feature1, feature2) with cluster colors
- Compare to true labels: silhouette score, purity
- Silhouette coefficient: -1 (bad), 0 (on boundary), +1 (well-clustered)

**Cluster Interpretation**
- What do clusters represent? Compute mean features per cluster
- Are clusters meaningful? Check if coherent (biologically, statistically)
- Stability: rerun with different initializations (k-means is random)

## Exercise Structure
- **Exercise 1:** Load iris, explore with histograms and scatter plots
- **Exercise 2:** Visualize 2D projections (different feature pairs)
- **Exercise 3:** Why time series doesn't work (plot as time series to see nonsense)
- **Exercise 4:** Apply k-means with k=3, visualize clusters
- **Exercise 5:** Try different k values, use elbow plot to find "best" k
- **Exercise 6:** Compute silhouette scores, interpret cluster quality

## Key Patterns
- EDA: visualize before modeling
- Scatter plots: see correlations and clusters
- Histograms: understand distributions
- Unsupervised: no labels, discover patterns
- k-means: partition data into k groups

---

# LECTURE 11: Supervised Learning – Classification

**Folder:** `populations_data_3`  
**Duration:** 4h (2h lecture + 2h exercises)  
**Jupyter Notebook:** `populations_3.ipynb`

## Primary Topics Covered in Notebook

**Supervised vs Unsupervised**
- **Supervised:** have ground truth labels, learn to predict new labels
- **Unsupervised:** no labels, discover structure
- This lecture: supervised classification (predict discrete categories)

**Classification Problem**
- Goal: given features (X), predict class label (y)
- Examples: iris species from measurements, patient disease from biomarkers, signal quality (good/bad)
- Outputs: predicted class, confidence/probability of each class

**k-Nearest Neighbors (k-NN)**
- Idea: a point's class is determined by its k nearest neighbors
- Algorithm:
  1. Store all training data
  2. For new point, find k closest points (by distance, typically Euclidean)
  3. Predict: majority class among those k neighbors
- Choosing k: small k = flexible but noisy, large k = smooth but may underfit; typically 3-10
- Implementation: `sklearn.neighbors.KNeighborsClassifier(n_neighbors=5).fit(X_train, y_train)`

**Distance and Feature Scaling**
- k-NN depends on distance: features with large ranges dominate
- Solution: normalize/standardize features
  - **Standardization:** (x - mean) / std (mean=0, std=1)
  - **Normalization:** (x - min) / (max - min) (range 0-1)
- `sklearn.preprocessing.StandardScaler()` for easy scaling
- Always fit scaler on training data, apply to test data

**Train-Test Split**
- Never evaluate on training data: memorization, not generalization
- Split: 70-80% train, 20-30% test
- Random split to avoid order bias
- `sklearn.model_selection.train_test_split()`

**Model Evaluation**
- **Accuracy:** (correct predictions) / (total predictions)
- **Confusion matrix:** true positives, false positives, true negatives, false negatives
- **Precision:** TP / (TP + FP) — of positive predictions, how many correct?
- **Recall:** TP / (TP + FN) — of true positives, how many found?
- **F1-score:** harmonic mean of precision and recall
- Choose metric based on cost: medical diagnosis (recall), spam detection (precision)

**Visualization: Decision Boundaries**
- Plot 2D features (or 2D PCA projection) with colored regions
- Each region is a predicted class
- k-NN boundaries are local and wiggly (non-linear)
- Shows how classifier carves up feature space

**Overfitting and Generalization**
- Overfitting: model memorizes training data, fails on new data (high training accuracy, low test accuracy)
- k-NN overfitting: very small k (k=1 memorizes)
- Solution: cross-validation to find good k

**Cross-Validation**
- k-fold cross-validation: split data into k folds, train k times (leave one fold out each time)
- Evaluate on left-out fold, average results
- More stable estimate than single train-test split
- `sklearn.model_selection.cross_val_score()`

**Iris Classification with k-NN**
- Train on iris features, predict species
- Compare predicted to true labels
- Visualize: 2D projections with decision boundaries
- Confusion matrix: which species confused with which?

## Exercise Structure
- **Exercise 1:** Train k-NN on iris with different k values
- **Exercise 2:** Use train-test split, evaluate accuracy
- **Exercise 3:** Scale features, observe improvement
- **Exercise 4:** Visualize decision boundaries
- **Exercise 5:** Compute confusion matrix and precision/recall
- **Exercise 6:** Use cross-validation to select best k

## Key Patterns
- Supervised: use labels to train
- k-NN: simple, requires scaled features
- Train-test split: prevent overfitting
- Evaluate: accuracy, precision, recall, confusion matrix
- Cross-validate: stable model selection

---

# LECTURE 12: Data Integration Workshop

**Folder:** `populations_data_4_workshop`  
**Duration:** 4h (1h lecture + 3h workshop)

## Workshop Structure

This is an integrative workshop applying concepts from lectures 9-11 without introducing new topics.

### **Exercise 1 (1h 30m): "From Features to Predictions"**

**Scenario:** Given a population dataset with multiple features and a target variable, build an end-to-end analysis pipeline.

**Tasks:**
- Load data and explore with visualizations (histograms, scatter plots from lecture 10)
- Clean data (handle missing values, outliers)
- Fit linear regression model to predict continuous outcome (lecture 9 technique)
- Evaluate with R², RMSE, residual plots
- Document analysis: methods, findings, limitations

**Integration elements:**
- Visualization choices from lecture 10 inform feature selection
- Regression model from lecture 9 predicts target
- Metadata and reproducibility throughout

### **Exercise 2 (1h 30m): "Unsupervised Discovery and Supervised Prediction"**

**Scenario:** Given iris or similar population dataset, combine clustering and classification.

**Tasks:**
- Apply k-means clustering (lecture 10) to discover groups without using labels
- Visualize clusters (scatter plots from lecture 10)
- Train k-NN classifier (lecture 11) to predict species/groups from features
- Compare: do k-NN predictions match k-means clusters?
- Evaluate k-NN with train-test split, confusion matrix, cross-validation (lecture 11)
- Discuss: when would unsupervised (clustering) be useful vs supervised (k-NN)?

**Integration elements:**
- Visualization (lecture 10) shows cluster structure
- Clustering (lecture 10) finds natural groupings
- Classification (lecture 11) predicts group membership
- Cross-validation ensures generalization

### **Workshop Themes**
- **Pipeline:** load → visualize → clean → model → evaluate → document
- **Visualization:** informs understanding and feature selection
- **Unsupervised:** discovers structure (clustering from lecture 10)
- **Supervised:** predicts with known labels (classification from lecture 11, regression from lecture 9)
- **Reproducibility:** document methods, parameters, software versions
- **Interpretation:** what do results mean? Limitations? Next steps?

## Key Outcomes
- Hands-on experience with full data analysis workflow
- Integration of regression, clustering, and classification
- Practice with visualization for decision-making
- Reproducibility and documentation habits
- Reflection on method choices
