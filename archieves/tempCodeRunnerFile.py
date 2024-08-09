import spacy
from spacy.matcher import Matcher

# Load spaCy model
nlp = spacy.load("en_core_web_sm")

# Input text
text = """
R. &amp; R. Diabetic &amp; Thyroid Clinic DR. ABHISHEK SHRIVASTAVA MD, FACE, MMsc, DMsc Endocrinology Advisory Council Member Central Zone American College of Physicians India Chapter Editorial Board Member JEMR Thyroid, Diabetes Obesity Specialist R ЯК Sunday Off 0004299 Praveen Beohar ( 60y, Female) - 9893043131 Clinic: Near Madan Mahal Police Station, Opposite HP Petrol Pump, Napier Town, Jabalpur Timings: 12 Noon to 7:30 PM Regd. No. 31955 Date &amp; Time 28-Dec-2023 02:37 PM BP 77/53mmHg | Pulse 100bpm | Glycosylated Hemoglobin HbA1c 6.88% [28-Dec-2023] Serum Creatinine 1.36mg/dL, Serum Calcium - 7.13mg/dL, eGFR - Creatinine Clearance - 44.59mL/min/1.73m2 Complaints BREATHLESSNESS WEAKNESS Diagnosis : DIABETES MELLITUS TYPE 2, HYPERTENSION, CAD, PTCA RX Medicine Dosage Freq. - Duration 1) TRIOBIMET 2MG TABLET 1-0-1 Daily - 30 days Composition : Glimepiride 2MG + Metformin 500MG + Pioglitazone 15 MG Timings : 1 Before Breakfast, 1 Night - Before Dinner 2) LINARES E 0-1-0 Daily - 30 days Composition : LINAGLIPTIN 5MG + EMPAGLIFLOZIN 25MG Timings : 1 Afternoon - Before Dinner 3) BONJOY PLUS 0-0-1 Daily - 30 days Composition : CALCITRIOL 0, 25MCG + CALCIUM CARBONATE 500MG + ZINC 7.5MG... Timings : 1 Night - After Dinner 417. guober so with food To withden ॐ Dr. Abhishek Shrivastava Appointment time 10 AM to 6.00 PM. Mobile. 9 6267089757, 9977369339, 7869022999, 9098215024 Please take an appointment. R. &amp; R. Diabetic and Thyroid Clinic DR. ABHISHEK SHRIVASTAVA MD, FACE, MMsc, DMsc Endocrinology Advisory Council Member Central Zone American College of Physicians India Chapter Editorial Board Member JEMR Thyroid, Diabetes Obesity Specialist R ЯК Sunday Off 0004299 Praveen Beohar ( 60y, Female ) - 9893043131 Clinic: Near Madan Mahal Police Station, Opposite HP Petrol Pump, Napier Town, Jabalpur Timings: 12 Noon to 7:30 PM Regd. No. 31955 Date &amp; Time 28 - Dec - 2023 02:37 PM BP 77 / 53mmHg | Pulse 100bpm | Glycosylated Hemoglobin HbA1c 6.88 % [ 28 - Dec - 2023 ] Serum Creatinine 1.36mg / dL , Serum Calcium - 7.13mg / dL , eGFR - Creatinine Clearance - 44.59mL / min / 1.73m2 Complaints BREATHLESSNESS WEAKNESS Diagnosis : DIABETES MELLITUS TYPE 2 , HYPERTENSION , POST PTCA RX Medicine Dosage q. - Duration 1 ) TRIOBIMET 2MG TABLET 1-0-1 Daily - 30 days Composition : Glimepiride 2MG + Metformin 500MG + Pioglitazone 15 MG Timings : 1 Before Breakfast, 1 Night - Before Dinner 2 ) LINARES E 0-1-0 Daily - 30 days Composition : LINAGLIPTIN 5MG + EMPAGLIFLOZIN 25MG Timings : 1 Afternoon - Before Dinner 3 ) BONJOY PLUS 0-0-1 Daily - 30 days Composition : CALCITRIOL 0, 25MCG + CALCIUM CARBONATE 500MG + ZINC 7.5MG ... Timings : 1 Night - After Dinner 417. guober so with food To withden ॐ Dr. Abhishek Shrivastava Appointment time is 10 AM to 6 PM. Mobile: 9 6267089757, 9977369339, 7869022999, 9098215024 Please take an appointment.
"""

# Process text with spaCy
doc = nlp(text)

# Create a Matcher object
matcher = Matcher(nlp.vocab)

# Define pattern for matching medicine details
pattern = [
    {"IS_DIGIT": True},
    {"TEXT": ")"},
    {"POS": "PROPN", "OP": "+"},
    {"IS_SPACE": True, "OP": "*"},
    {"IS_DIGIT": True, "OP": "?"},
    {"TEXT": "-", "OP": "?"},
    {"IS_DIGIT": True, "OP": "?"},
    {"IS_SPACE": True, "OP": "*"},
    {"TEXT": "Daily"},
    {"TEXT": "-"},
    {"IS_DIGIT": True},
    {"TEXT": "days"},
    {"IS_SPACE": True, "OP": "*"},
    {"TEXT": "Composition"},
    {"TEXT": ":"},
    {"POS": "PROPN", "OP": "+"},
    {"IS_PUNCT": True, "OP": "*"},
    {"POS": "NUM", "OP": "*"},
    {"IS_PUNCT": True, "OP": "*"},
    {"POS": "PROPN", "OP": "*"},
    {"IS_SPACE": True, "OP": "*"},
    {"TEXT": "Timings"},
    {"TEXT": ":"},
    {"POS": "NUM", "OP": "*"},
    {"IS_SPACE": True, "OP": "*"},
    {"POS": "PROPN", "OP": "*"},
]

matcher.add("MEDICINE_PATTERN", [pattern])

# Find matches in the document
matches = matcher(doc)

medicines = {}
for match_id, start, end in matches:
    span = doc[start:end]
    # Extract information
    details = span.text.split("Composition : ")
    med_info = details[0].strip().split(" ")
    timing_info = details[1].strip().split(" Timings : ")
    
    name = " ".join(med_info[2:-4])
    dosage = med_info[-4]
    duration = med_info[-1] + " " + med_info[-2]
    composition = timing_info[0].strip()
    timing = timing_info[1].strip()
    
    medicines[f'medicine_{len(medicines) + 1}'] = [name, dosage, duration, composition, timing]

# Print the extracted medicines
for med, info in medicines.items():
    print(f"{med} : {info}")
