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

# LECTURE 7

PPG and Feature Engineering

Duration: 2h lecture + 2–3h exercises  
Focus: low‑pass filtering, pulse detection, amplitude and rise‑time metrics, pandas introduction.

***

## CONTENT (Lecture)

### Part 1. Introduction to pandas (motivation only)

*   Why CSV feature tables require a tabular library
*   DataFrame basics (columns, rows, indexing)
*   Very limited intro: read_csv, head(), describe()

Mini‑exercise 1  
Load a tiny csv and compute descriptive stats.

### Part 2. PPG and physiology

*   Why PPG amplitude varies
*   Systolic upstroke
*   Pulse arrival time (conceptually)

### Part 3. Filtering

*   Introduce low‑pass filter
*   Why PPG is susceptible to noise

Mini‑exercise 2  
Apply low‑pass filter to synthetic noisy sinusoid.

### Part 4. Feature engineering

*   Peak amplitude
*   Rise time
*   Beat‑to‑beat metrics
*   Why features matter more than raw curves

***

## ETHICS MINI‑TOPIC

Topic: Data minimization and privacy by design  
Key points: store derived features instead of raw biosignals when possible.

***

## EXERCISE SESSION (2–3h)

Exercise 1. Load PPG and filter

*   Apply low-pass filter using scipy
*   Compare raw and filtered versions

Exercise 2. Detect peaks

*   Extract pulse amplitude
*   Compute mean and variance

Exercise 3. Compute rise time per beat

*   Compute time from foot-to-peak per pulse
*   Store results in a pandas DataFrame

Exercise 4. Save features

*   Save DataFrame to csv
*   Compare file sizes vs raw signal

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
