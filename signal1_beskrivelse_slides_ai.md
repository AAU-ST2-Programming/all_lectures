you are a lecture creator agent. 
I am teaching the class Applied Programming which is part of 2nd semester Biomedical Engineering, which is about how python can be used as a tool to solve biomedical problems.
this is the content of the lectures:

Fysiologiske signaler og basal statistik (3 kursusgange med seminarrumsemi-narrum + gruppearbejde Opgaveregning og 1 Workshop med seminar rum)
Viden:
•	Kan forklare basale principper for maskinlæring
Færdigheder:
•	Kan designe, implementere og teste programmer til 
o	simple statistiske metoder som middelværdi, spredning og lineær regression
o	basal informationsudtræk fra fysiologiske signaler
o	behandling af større mængder data og forskellige datatyper
o	grafisk præsentation af data
•	Kan vælge og implementere relevante metoder til grafisk præsentation af data



I need the to create lecture-slides. 
The whole lecture is in Danish. 
If no good or fitting translation to danish, then keep the English word.
Do not use any emojies.

Keep the methods simply.
Use numpy arrays for data storage.
use matplotlib for visualization.
use scikit-learn if needed.
Slides and exercises shall not be numbered.
All slides should have fitting headlines.
Exercises should also have a fitting name. 
Lecture should last 2H (slides), and then 2H of exercises. 
Do not make too many exercises.
The slides should be created for jupyter lab slidedeck using RISE.

During the lecture, create small conceptual exercises, i.e. make and discuss what a histogram is, to try simply individual python tools. 
There should always be an answer slide after every question. 
All exercises should include: 
1. what is the exercise about (general goal, and scene setup).
2. What students know, and will be using, and what I expect they will get from doing the exercise. 
3. Their task. Their task should be phrased so its a problem they will solve.. not a step by step guide.




# Corrections and notes to the lecture content below:
Try and use real data when possible.
I need slides that describe the different visualizations I am using.

Add the following to the slides as well: Introduce and Describe Histogram, and when its powerful. Relate to mean and std.

Keep the methods simply.
Use numpy arrays for data storage.



# lecture Content below:
# LECTURE 6

SCG and Mechanical Events: Filtering + Feature Timing

Duration: 2h lecture + 2–3h exercises  
Focus: scipy introduction, smoothing, peak detection, mechanical cardiac timing.

***

## CONTENT (Lecture)

### Part 1. Introduction to scipy.signal

*   Why numpy alone is not enough for filtering
*   What a basic smoothing filter is
*   Moving average and butterworth (plusses and minuses for both)

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


## ETHICS MINI‑TOPIC

Topic: Data provenance and why metadata matters  
Key points: device info, sampling rate, calibration drift.

***

## EXERCISE SESSION (2–3h)

Exercise 1. Load SCG and apply smoothing filter

*   Implement simple moving average manually
*   use a butterworth filter
*   Compare visually

Exercise 2. Peak detection

*   Use scipy.find_peaks
*   Extract mechanical beats
*   Compute average mechanical interval

Exercise 3. Sync ECG + SCG

*   Provided R‑peaks from previous lecture
*   Compute R to AO timing
*   Interpret as mechanical delay
