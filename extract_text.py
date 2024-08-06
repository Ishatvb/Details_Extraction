import re

# Function to preprocess OCR text
def preprocess_text(text):
    text = re.sub(r'&amp;', '&', text)
    text = re.sub(r'\s+', ' ', text)  # Replace multiple spaces with a single space
    text = text.replace('\n', ' ')
    return text

# Sample OCR text
ocr_text = """
R. &amp; R. Diabetic &amp; Thyroid Clinic Dr. Abhishek Shrivastava MD, PGD, DMsc Endocrinology ECP Council American College of Physicians, India Chapter Editorial Board Member JEMR Thyroid &amp; Diabetes Hormones Specialist eeeees ЯК Sunday Holiday MeRe 0004299 : Praveen Beohar (59y, Female) - 9893043131 BP-110/70 mmHg Post Prandial Blood Sugar (PPBS) 148mg/dL Complaints: BURNING SENSATION IN LEGS Clinic: Near Madan Mahal Police Station, Opposite HP Petrol Pump, Napier Town, Jabalpur Timing: 12 Noon to 7:30 PM Regd. No. 31955 Diagnosis: DIABETES MELLITUS TYPE 2, HYPERTENSION, CAD, POST PTCA Date: 12-Dec-2022 Medicine Dosage 1) TRIVOLIB FORTE 2MG TABLET 0-1-1 Daily - 30 Days Composition : GLIMEPIRIDE 2 MG + METFORMIN 500MG + VOGLIBOSE 0.3 MG Timing : 1 - Afternoon - Before meal, 1- Night - Before meal Daily - 30 Days 2) XIGDUO XR 10MG/500MG TABLET 1-0-0 Composition : DAPAGLIFLOZIN 10 MG + METFORMIN 500 MG Timing : 1 - Before breakfast 3) GLURA SR 100 MG 1-0-0 Daily - 30 Days Composition Timing : SITAGLIPTIN 100MG : 1 - : 1- Night - After Dinner Daily - 30 Days Dr. Abhishek Shrivastava 8718035040 Appointment Time 10AM to 6.00PM. Mob: 9098215024, 9977369339, 7869022999 Powered by HealthPlix EMR, www.healthplix.com Please take an appointment. R. &amp; R. Diabetic &amp; Thyroid Clinic Dr. Abhishek Shrivastava MD, PGD, DMsc Endocrinology ECP Council American College of Physicians, India Chapter Editorial Board Member JEMR Thyroid &amp; Diabetes Hormones Specialist eeeees ЯК Sunday Off MeRe 0004299 : Praveen Beohar ( 59y , Female ) - 9893043131 BP - 110 / 70 mmHg Post Prandial Blood Sugar ( PPBS ) 148mg / dL Complaints : BURNING SENSATION IN LEGS Clinic: Near Madan Mahal Police Station, Opposite HP Petrol Pump, Napier Town, Jabalpur Timings: 12 Noon to 7:30 PM Regd. No. 31955 Diagnosis : DIABETES MELLITUS TYPE 2 , HYPERTENSION , CAD , POST PTCA Date : 12 - Dec - 2022 Medicine Dosage 1 ) TRIVOLIB FORTE 2MG TABLET 0-1-1 Daily - 30 Days Composition : GLIMEPIRIDE 2 MG + METFORMIN 500MG + VOGLIBOSE 0.3 MG Timing : 1 - Afternoon - Before meal, 1- Night - Before meal Daily - 30 Days 2 ) XIGDUO XR 10MG / 500MG TABLET 1-0-0 Composition : DAPAGLIFLOZIN 10 MG + METFORMIN 500 MG Timing : 1 - Before breakfast 3 ) GLURA SR 100 MG 1-0-0 Daily - 30 Days Composition Timing : SITAGLIPTIN 100MG : 1 - Before Breakfast 4 ) ROSULESS A 10MG CAPSULE Composition Timing 0-0-1 Daily - 30 Days : ASPIRIN 75MG + ROSUVASTATIN 10 MG : 1 - Night - After Dinner 5 ) LAREGAB NT TABLET Composition Timing 0-0-1 : GABAPENTIN 400 MG + NORTRIPTYLINE 10 MG : 1 - Night - After Dinner Daily - 30 Days Dr. Abhishek Shrivastava 8718035040 Appointment Time 10AM to 6.00PM. Mob: 9098215024, 9977369339, 7869022999 Powered by HealthPlix EMR, www.healthplix.com Please take an appointment."""

clean_text = preprocess_text(ocr_text)

# Regex patterns to extract data
med_pattern = re.compile(r'\d+\)\s?([\w\s]+(?:\d+MG\sTABLET)?)')
dose_pattern = re.compile(r'(\d-\d-\d)')
duration_pattern = re.compile(r'-\s*(\d+\s*days)')
time_pattern = re.compile(r'Timing(?:s)?\s*:\s*([^"]+?)\s*(?=\d|\w+\s*:\s*|$)')

# Find matches
medicines = re.findall(med_pattern, clean_text)
doses = re.findall(dose_pattern, clean_text)
durations = re.findall(duration_pattern, clean_text)
times = re.findall(time_pattern, clean_text)

# Organize data
medicine_dict = {}
for i in range(len(medicines)):
    medicine_name = medicines[i].strip()
    dose = doses[i].strip() if i < len(doses) else ''
    duration = durations[i].strip() if i < len(durations) else ''
    time = times[i].strip() if i < len(times) else ''

    # Update the dictionary; the latest entry will be used in case of duplicates
    medicine_dict[medicine_name] = {
        'dose': dose,
        'duration': duration,
        'time': time,
    }

# Display the extracted data
for i, (med_name, med_info) in enumerate(medicine_dict.items(), 1):
    print(f"medicine_name{i}: {med_name}")
    print(f"dose{i}: {med_info['dose']}")
    print(f"duration{i}: {med_info['duration']}")
    print(f"time{i}: {med_info['time']}")
    print()
