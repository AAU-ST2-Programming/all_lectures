Below is a complete **Lecture 5–12 plan**, written as a coherent continuation of your existing course structure.  
It includes:

*   Full lecture structure for each 2h (or 1h) lecture session
*   Mini‑exercises integrated inside lectures
*   Full 2–3h exercise sessions where students know exactly what to do without prompting
*   Introductions to every new Python package (numpy, pandas, scipy, sklearn, matplotlib) right when it is first needed
*   Focus on statistics + information extraction from ECG, SCG, PPG
*   Your requirement: no emojis

This is designed so you can directly convert it into slides, Jupyter notebooks, and student handouts.

***

# OVERVIEW OF LECTURES 5–12

Lectures 1–4 covered OOP and basic Python, no numpy or pandas.  
The following introduces numerical libraries gradually and purposefully.

You can treat Lectures 5–8 as your **Signal Analysis Block**,  
and Lectures 9–12 as the **Population Data Block**.

Each lecture has 4 components:

1.  Lecture theory (2h or 1h depending on the day)
2.  Mini‑exercises inside the lecture
3.  Ethics/health‑data topic (5–10 min)
4.  Exercise set (2–3h), designed so students are fully prepared

***

# LECTURE 5

Introduction to Working With Data: ECG and Numerical Computing

Duration: 2h lecture + 2h exercises  
Focus: Normal data workflow, numpy introduction, basic statistics, simple ECG peak detection.

## Why this lecture

Students need to learn how numerical arrays work before doing real signal analysis.  
This is the first time you introduce numpy, but it is motivated by a real problem: ECG needs vectorized operations.

***

## CONTENT (Lecture)

### Part 1. Introduction to numpy (why and what)

*   Why Python lists are not suited for numerical computing.
*   What numpy arrays are.
*   How vectorization replaces loops.
*   How numpy stores data in memory.

Mini‑exercise 1 (5 min)  
Convert a Python list to a numpy array, compute mean manually vs with numpy.

Mini‑exercise 2 (10 min)  
Generate synthetic ECG‑like waveform using numpy’s linspace + sine.

### Part 2. Data workflow

*   Load → inspect → clean → visualize → extract → store
*   Why each step matters
*   Define raw data vs features

### Part 3. Introduction to ECG

*   What is the R‑peak
*   What is RR interval
*   What statistics describe variability

Mini‑exercise 3 (10 min)  
Students plot the ECG using matplotlib.  
Introduce matplotlib:

*   How to create a figure
*   How to label axes

### Part 4. Basic statistics

*   Mean, variance, standard deviation
*   Why statistics matter before extraction
*   Difference between signal noise vs physiological variability

***

## ETHICS MINI‑TOPIC (5–10 min)

Topic: What makes ECG sensitive health data  
Key points: biometric identification, latent disease markers, permanent health history.

***

## EXERCISE SESSION (2h)

Students can do everything because mini‑exercises introduced all required skills.

Exercise 1. Load ECG and compute basic stats

*   Use numpy mean, var, std
*   Interpret values physiologically

Exercise 2. Simple R‑peak detection

*   Threshold based on mean + std
*   Extract RR intervals
*   Compute heart rate

Exercise 3. Plot annotated ECG

*   Plot signal
*   Mark peaks with scatter points
*   Add grid and labels

Exercise 4. Save extracted features to csv (using basic file writing, not pandas yet)

***

***

# LECTURE 6

SCG and Mechanical Events: Filtering + Feature Timing

Duration: 2h lecture + 2–3h exercises  
Focus: scipy introduction, smoothing, peak detection, mechanical cardiac timing.

***

## CONTENT (Lecture)

### Part 1. Introduction to scipy.signal

*   Why numpy alone is not enough for filtering
*   What a basic smoothing filter is
*   Moving average and Savitzky–Golay filters

Mini‑exercise 1  
Apply moving average to synthetic noisy data.

### Part 2. Introduction to SCG

*   What mechanical cardiac events represent
*   IC, AO, AC
*   Why SCG peaks differ from ECG peaks

Mini‑exercise 2  
Identify a dominant peak visually.

### Part 3. Feature extraction workflow

*   Filtering
*   Peak detection
*   Timing intervals
*   Relating SCG to ECG

### Part 4. Regression introduction (conceptual)

*   What is a linear relationship
*   Why we might relate timing features
*   Showing simple scipy or sklearn LinearRegression

Mini‑exercise 3  
Fit a straight line to synthetic data.

***

## ETHICS MINI‑TOPIC

Topic: Data provenance and why metadata matters  
Key points: device info, sampling rate, calibration drift.

***

## EXERCISE SESSION (2–3h)

Exercise 1. Load SCG and apply smoothing filter

*   Implement simple moving average manually
*   Use scipy’s Savitzky–Golay afterwards
*   Compare visually

Exercise 2. Peak detection

*   Use scipy.find_peaks
*   Extract mechanical beats
*   Compute average mechanical interval

Exercise 3. Sync ECG + SCG

*   Provided R‑peaks from previous lecture
*   Compute R to AO timing
*   Interpret as mechanical delay

Exercise 4. Simple regression

*   Regress AO timing against beat index
*   Interpret slope (does mechanical function change?)

***

***

# LECTURE 7 — PPG + Feature Engineering (hard focus on “features”)

Duration: 2h lecture + 2h exercises  
Focus: what a *feature* is, how to design features, and how to build a beat-level feature table from PPG (filtering is assumed known).

---

## Why this lecture (the “conceptual upgrade”)
Students already know how to filter signals. Now they need to understand:

- Raw signal ≠ information: a *feature* is a *measurable summary* that preserves what you care about and discards what you don’t.
- Features are choices: they embed assumptions (physiology + noise model + sampling + sensor placement).
- A good feature is: interpretable, robust to noise/artifacts, stable across sessions, and useful for a downstream task (classification/regression/monitoring).

---

## CONTENT (Lecture, 2h)

### Part 1 (25–30 min): What is a “feature”?
Core concepts:
- Definitions: sample → signal → segment/beat → feature → feature table
- “Task-first” thinking: you choose features based on the question (stress? vasoconstriction? HRV?)
- Robustness: invariance (scale/offset), sensitivity to artifacts, sampling effects
- Feature types:
  - Beat-level: per pulse/beat (amplitude, rise time, width)
  - Window-level: summary over N seconds (mean HR, variability, percent bad beats)
  - Context/metadata features: posture, device, sampling rate, etc.

Mini‑exercise 1 (5–8 min): “Feature vs raw”
- Give students a short PPG segment and ask: “What single number best captures ‘pulse strength’ here?”  
- They propose candidates (peak-to-peak amplitude, area, RMS, slope), then discuss pros/cons.

---

### Part 2 (20–25 min): PPG physiology + artifacts (only what supports features)
- What PPG measures (blood volume changes)
- Why amplitude varies (perfusion, pressure, motion, sensor contact)
- Typical pulse landmarks:
  - Foot (pulse onset)
  - Systolic peak
  - Dicrotic notch (sometimes)
- Artifact patterns: motion spikes, baseline wander, clipping, dropped beats

Mini‑exercise 2 (5–8 min): “Spot the artifact”
- Show 3 pulses: clean / motion / clipped.  
- Ask: which feature breaks first and why?

---

### Part 3 (30–35 min): Feature extraction pipeline (you already know filtering)
Pipeline (teach as a repeatable recipe):
1) Load + inspect (units, fs, missing)
2) (Optional) smooth/low-pass (use a given Butterworth helper, no deep theory)
3) Beat segmentation (peak detection + foot detection)
4) Compute features per beat
5) Quality control flags (exclude bad beats)
6) Build feature table (pandas)
7) Save features + metadata

Mini‑exercise 3 (10–12 min): “Same signal, different features”
- Students compute amplitude + rise time from two parameter choices (e.g., different peak distance / smoothing window) and observe feature drift.

---

### Part 4 (20–25 min): From beats → feature table (pandas for real)
- Why a DataFrame matters: one row per beat, columns = features
- Minimal pandas used *for purpose*:
  - `pd.DataFrame(...)`, `describe()`, `isna()`, `to_csv()`
- “Schema thinking”: consistent column names, units, and metadata

Mini‑exercise 4 (5–8 min): “Schema design”
- Students propose a column schema: `t_peak_s`, `ibi_s`, `amp_au`, `rise_time_s`, `qc_flag`, `subject_id_pseudo`.

---

## ETHICS MINI‑TOPIC (5–10 min)
Topic: Data minimization + privacy by design (applied to biosignals)

Key points:
- Store derived features instead of raw biosignals when possible (goal-dependent).
- Raw PPG can be sensitive health data; even “anonymized” signals can carry re-identification risk when combined with metadata.
- Always capture *necessary* metadata for reproducibility (fs, device, protocol) without adding identity fields.

Tiny ethics prompt (2 min):
- “What is the minimum you need to store to reproduce your results?”

---

## EXERCISE SESSION (2h)

### Exercise 1 — Load PPG and sanity check
**Scenarie:**
Du er dataanalytiker på et hospital og har fået en PPG-optagelse til kvalitetskontrol og feature‑udtræk.

**(Fiktiv patientjournal — kun til øvelse)**
- Navn: *Sara Holm*
- Alder: 29 år
- Dato/tid: 2026-01-21 kl. 10:05
- Sted: Hjerteambulatorium (Test-rum B)
- Notat: “svimmelhed ved oprejsning”

**Du skal:**
- Indlæs PPG (og evt. timestamp)
- Plot rå signal + zoom på 10 sek
- Estimér/brug `fs` og tjek om der er clipping/missing

**Etik (1 spørgsmål):**
- Hvilke felter fra journalen må aldrig ende i din CSV/rapport?

---

### Exercise 2 — Beat detection (peaks) + QC flag
- Find systolic peaks (robust parametervalg)
- Lav et simpelt QC-flag pr. beat (fx “peak too small”, “too close”, “clipped segment”)

---

### Exercise 3 — Compute beat features
Compute per beat:
- `ibi_s` (inter-beat interval)
- `hr_bpm`
- `amp_au` (peak − foot or peak − local baseline)
- `rise_time_s` (foot → peak)
Optional “harder”:
- pulse width at 50% amplitude
- area under pulse (AUC)
- max upstroke slope (derivative-based)

---

### Exercise 4 — Build feature table + save
- Put everything in a pandas DataFrame (one row per beat)
- Save `features_ppg.csv`
- Save a tiny `metadata.json` (fs, device, filter params, date of analysis—not patient identity)

**Etik (short checklist):**
- Did you minimize stored data?
- Where is it stored (access control)?
- When will it be deleted?

---

## PhysioNet data + filenames (simple, robust convention)
PPG is a great signal for “feature” teaching because pulse shape → features is intuitive. If you want a “better” companion signal, add **ABP** (arterial blood pressure) or ECG for validation, but PPG alone is enough.

Recommended filename convention (so your downloader stays simple):
- `ppg_subject001.csv` with columns: `t_s, ppg_au`
- Optional: `ecg_subject001.csv` with columns: `t_s, ecg_au`
- Optional combined: `subject001_ppg.csv`, `subject001_features.csv`, `subject001_metadata.json`

If you tell me which PhysioNet dataset you plan to use (just the dataset name), I can propose an exact folder layout + exact output filenames to match your script in physionet_data_conversion.

***

***

# LECTURE 8

Workshop: Multimodal Signal Fusion  
ECG + SCG + PPG

Duration: 1h lecture + 3h workshop

Goal: integrate everything from Lectures 5–7.

***

## CONTENT (Lecture)

### Part 1. Cross‑correlation for alignment

*   Introduce concept of lag
*   Why multimodal data rarely aligns perfectly

Mini‑exercise  
Compute cross-correlation between two short waveforms.

### Part 2. Cardiovascular timing measures

*   R‑peak (ECG)
*   AO (SCG)
*   PPG pulse arrival
*   Compute PEP and PTT

### Part 3. Combined feature table

*   One row per beat
*   Columns: RR, AO interval, amplitude, rise time

***

## ETHICS MINI‑TOPIC

Topic: Data security  
Key points: encryption, access control, multimodal data risks.

***

## WORKSHOP (3h)

Exercise 1. Align signals

*   Compute lag between ECG and SCG
*   Shift SCG accordingly
*   Annotate alignment on plot

Exercise 2. Extract multimodal features

*   R‑peaks
*   AO points
*   PPG peaks
*   Compute PEP and PTT

Exercise 3. Create combined DataFrame

*   Store each metric
*   Export to csv
*   Write a short interpretation: what do the features say?

***

***

# LECTURE 9

Population-Level Data I: Introduction to Multi‑Subject Data

Duration: 2h lecture + 2h exercises  
Focus: cleaning datasets with multiple subjects.

***

## CONTENT (Lecture)

### Part 1. What is population data

*   Inter‑subject vs intra‑subject variability
*   Why population data is harder

### Part 2. pandas deeper intro

*   GroupBy
*   Handling missing values
*   Merging tables

Mini‑exercise  
Group data by subject ID and compute means.

### Part 3. Distributions

*   Histograms
*   Boxplots
*   Why outliers happen in medical data

***

## ETHICS MINI‑TOPIC

Topic: Anonymization limits  
Key points: re‑identification risks.

***

## EXERCISE SESSION

Exercise 1. Load dataset of 20 subjects  
Exercise 2. Clean missing values  
Exercise 3. Compute group-level statistics  
Exercise 4. Make histograms and boxplots with matplotlib

***

***

# LECTURE 10

Population Data II: Variability, Outliers, and Simple Models

Duration: 2h lecture + 2h exercises

***

## CONTENT (Lecture)

### Part 1. Variability analysis

*   Standard deviation
*   Interquartile range
*   Why medical data has heavy tails

### Part 2. Outlier detection

*   Z‑scores
*   Why this is risky in medicine

Mini‑exercise  
Identify outliers in synthetic data.

### Part 3. Simple predictive modeling

*   Linear regression revisited
*   Train/test split
*   Why population models differ from single‑subject

***

## ETHICS MINI‑TOPIC

Topic: Bias in datasets  
Key points: representativity, demographic imbalance.

***

## EXERCISE SESSION

Exercise 1. Compute variability across subjects  
Exercise 2. Detect outliers  
Exercise 3. Fit regression on entire population  
Exercise 4. Compare performance across subgroups

***

***

# LECTURE 11

Population Data III: Data Pipelines

Duration: 1h lecture + 3h exercises

***

## CONTENT (Lecture)

### Part 1. Pipeline thinking

*   Ingest → clean → extract → model → store
*   Why automation matters

### Part 2. Write your own feature extractor

*   Input: raw single subject folder
*   Output: feature csv

Mini‑exercise  
Implement a function that takes a vector and returns 3 features.

***

## ETHICS MINI‑TOPIC

Topic: Logging and accountability  
Key points: audit trails, tracking processing steps.

***

## EXERCISE SESSION

Exercise 1. Build a pipeline that reads multiple subjects  
Exercise 2. Apply your feature extractor  
Exercise 3. Produce final dataset  
Exercise 4. Visualize summary statistics

***

***

# LECTURE 12

Population Data IV: Final Integration Workshop

Duration: 1h lecture + 3h workshop

***

## CONTENT (Lecture)

### Part 1. Putting it all together

*   Signals → Features → Population statistics → Interpretation

### Part 2. Best practices

*   Folder structure
*   Documentation
*   Reproducibility

***

## ETHICS MINI‑TOPIC

Topic: The ethical lifecycle of health data  
Key points: retention, deletion, data stewardship.

***

## FINAL WORKSHOP (3h)

Exercise 1. Load full dataset  
Exercise 2. For each subject:

*   Clean signals
*   Extract features
*   Store tables

Exercise 3. Combine all subjects  
Exercise 4. Perform group‑level analysis  
Exercise 5. Write a short results summary

***

If you want, I can prepare:

*   Lecture slide outlines for all 8 lectures
*   Jupyter notebooks for each lecture
*   Student handouts
*   A compiled syllabus document

Tell me what format you prefer next.
