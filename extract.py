import re

# Function to preprocess OCR text
def preprocess_text(text):
    text = re.sub(r'&amp;', '&', text)
    text = re.sub(r'\s+', ' ', text)  # Replace multiple spaces with a single space
    text = text.replace('\n', ' ')
    return text

# Sample OCR text
ocr_text = """
R. &amp; R. Diabetic &amp; Thyroid Clinic Dr. Abhishek Shrivastava MD DMsc Endocrinology (England) Masters in Endocrinology RCP (England) Editorial Board Member Journal of Endocrinology and Metabolism Research Editorial Board Member MSD Research Publication ЯR akrilf-ch: Near Madan Mahal Police Station, Opposite HP Petrol Pump, Napier Town, Jabalpur Time :- 11 am to 7 pm Regd. No. 31955 Sunday Holiday Mob.: 7869022999, 6267089757 Ref.: 0004299: Praveen Beoher (58y, Female) - 9893043131 BP 90/60 mmHg Random Blood Sugar - RBS 258 mg/dL Complaints: NO MAJOR COMPLAINTS Diagnosis: DIABETES MELLITUS TYPE 2, HYPERTENSION, CAD, POST PTCA R Medicine 1) AMARYL M FORTE 2MG TABLET Dosage 1-0-1 Daily - 30 Days Composition : GLIMEPIRIDE 2 MG + METFORMIN 1000 MG Timing 1 - Before Breakfast, 1 - Night - Before Dinner 2) VIBITE M 50/500 1-0-1 Daily - 30 Days Composition : 1) ECOSPRIN-AV 75/10 CAPSULE 0-0-1 Daily - 30 Days Composition : ASPIRIN 75 MG + ATORVASTATIN 10 MG Timing ::1 / Night - After Food 4) CALTIVITE PLUS M 0-0-1 Daily - 30 Days Timing 1- Night - After Food MARYL M FORTE GLIVEPR MET CRM SPRIN-AV 75/15 ARIN 75 LIM TE PLUMB 4-33-8 Powered by HealthPlix EMR. www.healthplix.com Date: Date: 15-Jul-2021 Dr. Abhishek Shrivastava R. &amp; R. Diabetic &amp; Thyroid Clinic Dr. Abhishek Shrivastava MD DMsc Endocrinology ( England ) Masters in Endocrinology RCP ( England ) Editorial Board Member Journal of Endocrinology and Metabolism Research Editorial Board Member MSD Research Publication ЯR akrilf-ch: Near Madan Mahal Police Station, Opposite HP Petrol Pump, Napier Town, Jabalpur Time: 11 am to 7 pm Regd. No. 31955 Sunday Holiday Mob.: 7869022999 , 6267089757 Ref.: 0004299 : Praveen Beoher ( 58y , Female ) - 9893043131 BP 90/60 mmHg Random Blood Sugar - RBS 258 mg/dL Complaints : NO MAJOR COMPLAINTS Diagnosis : DIABETES MELLITUS TYPE 2 , HYPERTENSION , CAD , POST PTCA R Medicine 1) AMARYL M FORTE 2MG TABLET Dosage 1-0-1 Daily - 30 days Composition : GLIMEPIRIDE 2 MG + METFORMIN 1000 MG Timing 1 - Before breakfast, 1 - Night - Before dinner 2) VIBITE M 50/500 1-0-1 Daily - 30 Days Composition : METFORMIN 500 MG + VILDAGLIPTIN 50 MG Timing : purn : be before breakfast, 1 - Night - before dinner 3 ) ECOSPRIN - AV 75/10 CAPSULE 0-0-1 Daily - 30 Days Composition : ASPIRIN 75 MG + ATORVASTATIN 10 MG Timing :: 1 / Night - after dinner 4 ) CALTIVITE PLUS M 0-0-1 Daily - 30 Days Timing 1- Night - after dinner MARYL M FORTE GLIVEPR MET CRM SPRIN - AV 75/15 ARIN 75 LIM TE PLUMB 4-33-8 Powered by HealthPlix EMR . www.healthplix.com Date : Date : 15 - Jul - 2021 Dr. Abhishek Shrivastava
"""

clean_text = preprocess_text(ocr_text)

# Regex patterns to extract data
med_pattern = re.compile(r'\d+\)\s?([\w\s]+(?:\d+MG\sTABLET)?)')
dose_pattern = re.compile(r'(\d-\d-\d)')
duration_pattern = re.compile(r'-\s*(\d+\s*days)')
time_pattern = re.compile(r'Timings\s*:\s*([^"]+?)\s*(?=\d|\w+\s*:\s*|$)')

# Find matches
medicines = re.findall(med_pattern, clean_text)
doses = re.findall(dose_pattern, clean_text)
durations = re.findall(duration_pattern, clean_text)
times = re.findall(time_pattern, clean_text)

# Organize data
medicine_data = []
for i in range(len(medicines)):
    med_info = {
        'medicine_name': medicines[i].strip(),
        'dose': doses[i].strip() if i < len(doses) else '',
        'duration': durations[i].strip() if i < len(durations) else '',
        'time': times[i].strip() if i < len(times) else '',
    }
    medicine_data.append(med_info)

# Display the extracted data
for i, med in enumerate(medicine_data, 1):
    print(f"medicine_name{i}: {med['medicine_name']}")
    print(f"dose{i}: {med['dose']}")
    print(f"duration{i}: {med['duration']}")
    print(f"time{i}: {med['time']}")
    print()
