DROWSINESS DETECTION SYSTEM  
-----------------------------------------

1. PROJECT OVERVIEW  
This project detects human drowsiness in real-time using a webcam.  
It tracks eye landmarks using MediaPipe Face Mesh and calculates the Eye Aspect Ratio (EAR).  
If the eyes remain closed for a certain duration, the system plays an alert sound.  
This prevents accidents caused by fatigue.  
Compatible with both Windows and macOS.

-----------------------------------------

2. TECHNOLOGIES USED  
- Python 3.9 / 3.10 / 3.11  
- OpenCV → webcam & image processing  
- MediaPipe → face & eye landmark detection  
- NumPy → numerical processing  
- SciPy → EAR calculation  
- Pygame → alarm sound playback  

-----------------------------------------

3. FILES INCLUDED  
- Drowsiness_Detection.py  → Main script  
- music.wav                → Alarm sound  
- assets/                  → Sample images  
- models/                  → *EMPTY* (model file NOT included due to size limit)

⚠ NOTE:  
The original file "shape_predictor_68_face_landmarks.dat" (68 MB)  
is NOT included in the ZIP due to upload restrictions.  
This project uses MediaPipe, so the .dat model is not required.

-----------------------------------------

4. REQUIRED INSTALLATIONS (WINDOWS & MAC)

Before running the project, install dependencies:

pip install opencv-python  
pip install mediapipe  
pip install numpy  
pip install scipy  
pip install pygame  

(Recommended but optional)
pip install imutils  

-----------------------------------------

5. HOW TO RUN (WINDOWS)

1. Open the project folder in File Explorer.  
2. Click the address bar → type `cmd` → press Enter.  
3. Run the script:

   python Drowsiness_Detection.py

4. Webcam window opens.  
5. Press 'Q' anytime to quit.

-----------------------------------------

6. HOW TO RUN (MACOS)

1. Right-click project folder → "New Terminal at Folder"  
2. (OPTIONAL) Create virtual environment:
     python3 -m venv venv  
     source venv/bin/activate  

3. Install packages (same as Windows):

     pip install opencv-python mediapipe numpy scipy pygame

4. Run the script:
     python3 Drowsiness_Detection.py  

5. Press 'Q' to exit webcam.

-----------------------------------------

7. HOW IT WORKS (IN SIMPLE TERMS)

1. MediaPipe detects face landmarks (468 points).  
2. We extract eye landmarks.  
3. EAR (Eye Aspect Ratio) = a formula that checks how open/closed eyes are.  
4. If EAR is LOW for multiple frames → eyes are closed → user is sleepy.  
5. System plays a loud alarm sound through pygame.

-----------------------------------------

8. REAL-WORLD USE CASES

- Driver drowsiness alert system  
- Machine operators safety  
- Office night-shift monitoring  
- Factory workers fatigue detection  
- Security / surveillance enhancements

-----------------------------------------

9. IMPORTANT NOTE ABOUT ZIP SIZE  
The original model file (68MB) is intentionally removed from the ZIP  
to meet the Google Form upload limit (10 MB).  
The project works fully without it because this version uses MediaPipe.
