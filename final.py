import re

# Section 1: Text Preprocessing

def clean_text(text):
    """Clean the input text by removing extra whitespace."""
    return re.sub(r'\s+', ' ', text).strip()

def remove_phone_numbers(text):
    """Remove phone numbers from the text."""
    phone_number_pattern = r'\+?\d[\d\s()-]{7,}\d'
    return re.sub(phone_number_pattern, '', text)

# Section 2: Information Extraction

def get_unique_meds(text):
    """Extract unique medicine names from the text."""
    pattern = r'\d+\)\s*(\w+)'
    matches = re.findall(pattern, text)
    return list((matches))

def get_unique_dosages(text):
    """Extract dosage information from the text."""
    pattern =  r"(\d-\d-\d)\s*(?:Daily)?"
    return re.findall(pattern, text)

def get_frequencies(text):
    """Extract frequency information from the text."""
    pattern = r"(\d+\s(?:days|Days|week|Week|month|Month|year|Year))"
    return re.findall(pattern, text)

# Section 3: Data Mapping

def extend_list(lst, length, default_value=None):
    """Extend a list to a specific length with a default value."""
    return lst + [default_value] * (length - len(lst))

def map_medicines(meds, dosages, frequencies):
    """Map medicines to their respective dosages, frequencies, and timings."""
    max_length = len(meds)
    dosages = extend_list(dosages, max_length)
    frequencies = extend_list(frequencies, max_length)

    medicine_map = {}
    # Iterate through the lists
    for i in range(max_length):
        med = meds[i]
        dosage = dosages[i]
        frequency = frequencies[i]

        # Store the medicine with its dosage and frequency
        if med not in medicine_map:
            medicine_map[med] = (dosage, frequency)

    return medicine_map

# Section 4: Main Function

def process_prescription_text(text):
    """Process the prescription text and return structured data."""
    # Preprocess the text
    text = remove_phone_numbers(text)
    text = clean_text(text)

    # Extract information
    meds = get_unique_meds(text)
    dosages = get_unique_dosages(text)
    frequencies = get_frequencies(text)


    # Map extracted data
    return map_medicines(meds, dosages, frequencies)

# Section 5: Example Usage

if __name__ == "__main__":
    # Example usage
    text1 = """
    R. &amp; R. Diabetic &amp; Thyroid Clinic DR. ABHISHEK SHRIVASTAVA MD, FACE, MMsc, DMsc Endocrinology Advisory Council Member Central Zone American College of Physicians India Chapter Editorial Board Member JEMR Thyroid, Diabetes Obesity Specialist R ЯК Sunday Off 0004299 Praveen Beohar ( 60y, Female) - 9893043131 Clinic: Near Madan Mahal Police Station, Opposite HP Petrol Pump, Napier Town, Jabalpur Timings: 12 Noon to 7:30 PM Regd. No. 31955 Date &amp; Time 28-Dec-2023 02:37 PM BP 77/53mmHg | Pulse 100bpm | Glycosylated Hemoglobin HbA1c 6.88% [28-Dec-2023] Serum Creatinine 1.36mg/dL, Serum Calcium - 7.13mg/dL, eGFR - Creatinine Clearance - 44.59mL/min/1.73m2 Complaints BREATHLESSNESS WEAKNESS Diagnosis : DIABETES MELLITUS TYPE 2, HYPERTENSION, CAD, PTCA RX Medicine Dosage Freq. - Duration 1) TRIOBIMET 2MG TABLET 1-0-1 Daily - 30 days Composition : Glimepiride 2MG + Metformin 500MG + Pioglitazone 15 MG Timings : 1 Before Breakfast, 1 Night - Before Dinner 2) LINARES E 0-1-0 Daily - 30 days Composition : LINAGLIPTIN 5MG + EMPAGLIFLOZIN 25MG Timings : 1 Afternoon - Before Dinner 3) BONJOY PLUS 0-0-1 Daily - 30 days Composition : CALCITRIOL 0, 25MCG + CALCIUM CARBONATE 500MG + ZINC 7.5MG... Timings : 1 Night - After Dinner 417. guober so with food To withden ॐ Dr. Abhishek Shrivastava Appointment time 10 AM to 6.00 PM. Mobile. 9 6267089757, 9977369339, 7869022999, 9098215024 Please take an appointment.
    """
    text2 = """
    R. &amp; R. Diabetic &amp; Thyroid Clinic Dr. Abhishek Shrivastava MD DMsc Endocrinology (England) Masters in Endocrinology RCP (England) Editorial Board Member Journal of Endocrinology and Metabolism Research Editorial Board Member MSD Research Publication ЯR akrilf-ch: Near Madan Mahal Police Station, Opposite HP Petrol Pump, Napier Town, Jabalpur Time :- 11 am to 7 pm Regd. No. 31955 Sunday Holiday Mob.: 7869022999, 6267089757 Ref.: 0004299: Praveen Beoher (58y, Female) - 9893043131 BP 90/60 mmHg Random Blood Sugar - RBS 258 mg/dL Complaints: NO MAJOR COMPLAINTS Diagnosis: DIABETES MELLITUS TYPE 2, HYPERTENSION, CAD, POST PTCA R Medicine 1) AMARYL M FORTE 2MG TABLET Dosage 1-0-1 Daily - 30 Days Composition : GLIMEPIRIDE 2 MG + METFORMIN 1000 MG Timing 1 - Before Breakfast, 1 - Night - Before Dinner 2) VIBITE M 50/500 1-0-1 Daily - 30 Days Composition : 1) ECOSPRIN-AV 75/10 CAPSULE 0-0-1 Daily - 30 Days Composition : ASPIRIN 75 MG + ATORVASTATIN 10 MG Timing ::1 / Night - After Food 4) CALTIVITE PLUS M 0-0-1 Daily - 30 Days Timing 1- Night - After Food MARYL M FORTE GLIVEPR MET CRM SPRIN-AV 75/15 ARIN 75 LIM TE PLUMB 4-33-8 Powered by HealthPlix EMR. www.healthplix.com Date: Date: 15-Jul-2021 Dr. Abhishek Shrivastava R. &amp; R. Diabetic &amp; Thyroid Clinic Dr. Abhishek Shrivastava MD DMsc Endocrinology ( England ) Masters in Endocrinology RCP ( England ) Editorial Board Member Journal of Endocrinology and Metabolism Research Editorial Board Member MSD Research Publication ЯR akrilf-ch: Near Madan Mahal Police Station, Opposite HP Petrol Pump, Napier Town, Jabalpur Time: 11 am to 7 pm Regd. No. 31955 Sunday Holiday Mob.: 7869022999 , 6267089757 Ref.: 0004299 : Praveen Beoher ( 58y , Female ) - 9893043131 BP 90/60 mmHg Random Blood Sugar - RBS 258 mg/dL Complaints : NO MAJOR COMPLAINTS Diagnosis : DIABETES MELLITUS TYPE 2 , HYPERTENSION , CAD , POST PTCA R Medicine 1) AMARYL M FORTE 2MG TABLET Dosage 1-0-1 Daily - 30 days Composition : GLIMEPIRIDE 2 MG + METFORMIN 1000 MG Timing 1 - Before breakfast, 1 - Night - Before dinner 2) VIBITE M 50/500 1-0-1 Daily - 30 Days Composition : METFORMIN 500 MG + VILDAGLIPTIN 50 MG Timing : purn : be before breakfast, 1 - Night - before dinner 3 ) ECOSPRIN - AV 75/10 CAPSULE 0-0-1 Daily - 30 Days Composition : ASPIRIN 75 MG + ATORVASTATIN 10 MG Timing :: 1 / Night - after dinner 4 ) CALTIVITE PLUS M 0-0-1 Daily - 30 Days Timing 1- Night - after dinner MARYL M FORTE GLIVEPR MET CRM SPRIN - AV 75/15 ARIN 75 LIM TE PLUMB 4-33-8 Powered by HealthPlix EMR . www.healthplix.com Date : Date : 15 - Jul - 2021 Dr. Abhishek Shrivastava
    """
    text3 = """
    R. &amp; R. Diabetic &amp; Thyroid Clinic Dr. Abhishek Shrivastava MD, PGD, DMsc Endocrinology ECP Council American College of Physicians, India Chapter Editorial Board Member JEMR Thyroid &amp; Diabetes Hormones Specialist eeeees ЯК Sunday Holiday MeRe 0004299 : Praveen Beohar (59y, Female) - 9893043131 BP-110/70 mmHg Post Prandial Blood Sugar (PPBS) 148mg/dL Complaints: BURNING SENSATION IN LEGS Clinic: Near Madan Mahal Police Station, Opposite HP Petrol Pump, Napier Town, Jabalpur Timing: 12 Noon to 7:30 PM Regd. No. 31955 Diagnosis: DIABETES MELLITUS TYPE 2, HYPERTENSION, CAD, POST PTCA Date: 12-Dec-2022 Medicine Dosage 1) TRIVOLIB FORTE 2MG TABLET 0-1-1 Daily - 30 Days Composition : GLIMEPIRIDE 2 MG + METFORMIN 500MG + VOGLIBOSE 0.3 MG Timing : 1 - Afternoon - Before meal, 1- Night - Before meal Daily - 30 Days 2) XIGDUO XR 10MG/500MG TABLET 1-0-0 Composition : DAPAGLIFLOZIN 10 MG + METFORMIN 500 MG Timing : 1 - Before breakfast 3) GLURA SR 100 MG 1-0-0 Daily - 30 Days Composition Timing : SITAGLIPTIN 100MG : 1 - : 1- Night - After Dinner Daily - 30 Days Dr. Abhishek Shrivastava 8718035040 Appointment Time 10AM to 6.00PM. Mob: 9098215024, 9977369339, 7869022999 Powered by HealthPlix EMR, www.healthplix.com Please take an appointment. R. &amp; R. Diabetic &amp; Thyroid Clinic Dr. Abhishek Shrivastava MD, PGD, DMsc Endocrinology ECP Council American College of Physicians, India Chapter Editorial Board Member JEMR Thyroid &amp; Diabetes Hormones Specialist eeeees ЯК Sunday Off MeRe 0004299 : Praveen Beohar ( 59y , Female ) - 9893043131 BP - 110 / 70 mmHg Post Prandial Blood Sugar ( PPBS ) 148mg / dL Complaints : BURNING SENSATION IN LEGS Clinic: Near Madan Mahal Police Station, Opposite HP Petrol Pump, Napier Town, Jabalpur Timings: 12 Noon to 7:30 PM Regd. No. 31955 Diagnosis : DIABETES MELLITUS TYPE 2 , HYPERTENSION , CAD , POST PTCA Date : 12 - Dec - 2022 Medicine Dosage 1 ) TRIVOLIB FORTE 2MG TABLET 0-1-1 Daily - 30 Days Composition : GLIMEPIRIDE 2 MG + METFORMIN 500MG + VOGLIBOSE 0.3 MG Timing : 1 - Afternoon - Before meal, 1- Night - Before meal Daily - 30 Days 2 ) XIGDUO XR 10MG / 500MG TABLET 1-0-0 Composition : DAPAGLIFLOZIN 10 MG + METFORMIN 500 MG Timing : 1 - Before breakfast 3 ) GLURA SR 100 MG 1-0-0 Daily - 30 Days Composition Timing : SITAGLIPTIN 100MG : 1 - Before Breakfast 4 ) ROSULESS A 10MG CAPSULE Composition Timing 0-0-1 Daily - 30 Days : ASPIRIN 75MG + ROSUVASTATIN 10 MG : 1 - Night - After Dinner 5 ) LAREGAB NT TABLET Composition Timing 0-0-1 : GABAPENTIN 400 MG + NORTRIPTYLINE 10 MG : 1 - Night - After Dinner Daily - 30 Days Dr. Abhishek Shrivastava 8718035040 Appointment Time 10AM to 6.00PM. Mob: 9098215024, 9977369339, 7869022999 Powered by HealthPlix EMR, www.healthplix.com Please take an appointment.
    """
    text4 = """
    R. &amp; R. Diabetic &amp; Thyroid Clinic DR. ABHISHEK SHRIVASTAVA MD, FACE, MMsc, DMsc Endocrinology Advisory Council Member Central Zone American College of Physicians India Chapter Editorial Board Member JEMR ЯК Clinic : Near Madan Mahal Thana, Opposite HP Petrol Pump, Napier Town, Jabalpur Timings : 12 Noon to 7:30 PM Regd. No. 31955 Thyroid, Diabetes Obesity Specialist Sunday Closed 0008286 : Mr. Naveen Beohar (59y, Male ) - 9074210058 Date &amp; Time 18-May-202401:52PM .BP 113/72 mmHg | Random Blood Sugar - RBS 381mg/dL | Glycosylated Hemoglobin - HbA1c 11.2% [18-May-2024] Total Cholesterol - 191mg/dL. Serum HDL Cholesterol - 36.4md dL. Serum Triglycerides - 367mg/dL, Serum Creatinine - 0.6mg/dL eGFR - Creatinine Clearance - 111.20mL/min/1.73m2. TSH (Thyroid Stimulating Hormone) - 5.95ulU/mL. T4 - 6.18nmol/L Complaints: PAIN IN LEGS FLATULANCE BURNING SENSATION IN LEGS Diagnosis: DIABETES MELLITUS TYPE 2. DYSLIPIDEMIA, NEUROPATHY R Medicine 1) GLIZIHENZ M 80MG/500MG TABLET Dosage Freq. - Duration 1-0-1 Daily - 30 Days Composition : Gliclazide 80 MG + Metformin 500MG Timings : 1 Before Breakfast, 1 Night - Before Food -2) DAPAHENZ S 10/100 TABLET 0-1-0 Daily - 30 Days Composition : Dapagliflozin 10 MG Sitagliptin 100 MG Timings : 1 Afternoon - Before Food 3) FORTIUS F 20 0-0-1 Daily - 30 Days Timings : 1 Night - After Food 4) RABENDA PLUS 1-0-0 Daily - 20 Days Composition. Levosuipinde 75 MG - Rabeprazole 20 MG Timings 1 Before Breakfast 5) NEURONE G 0-0-1 Daily - 30 Days Composition. IMETHYLCOBALAMIN 1500 MCG - PREGABALIN 75MG Timings 1- Before sleeping at night Dr. phishek Shrivastava Appointment time 10 AM to 6.00 PM Mob. : 6267089757, 9977369339, 7869022999, 9098215024 Please take an appointment. R. &amp; R. Diabetic &amp; Thyroid Clinic DR. ABHISHEK SHRIVASTAVA MD, FACE, MMsc, DMsc Endocrinology Advisory Council Member Central Zone American College of Physicians India Chapter Editorial Board Member JEMR ЯК Clinic: Near Madan Mahal Police Station, Opposite HP Petrol Pump, Napier Town, Jabalpur Timings: 12 Noon to 7:30 PM Regd. No. 31955 Thyroid, Diabetes Obesity Specialist Sunday Holiday 0008286 : Mr. Naveen Beohar ( 59y, Male ) - 9074210058 Date &amp; Time 18 - May - 202401: 52PM .BP 113/72 mmHg | Random Blood Sugar - RBS 381mg / dL | Glycosylated Hemoglobin - HbA1c 11.2 % [ 18 - May - 2024 ] Total Cholesterol - 191mg / dL . Serum HDL Cholesterol - 36.4md dL. Serum Triglycerides - 367mg / dL , Serum Creatinine - 0.6mg / dL eGFR - Creatinine Clearance - 111.20mL / min / 1.73m2 . TSH (Thyroid Stimulating Hormone) – 5.95ulU/mL. T4 - 6.18nmol / L Complaints : PAIN IN LEGS FLATULANCE BURNING SENSATION IN LEGS Diagnosis : DIABETES MELLITUS TYPE 2. DYSLIPIDEMIA , NEUROPATHY R Medicine 1 ) GLIZIHENZ M 80MG / 500MG TABLET Dosage Freq . - Duration 1-0-1 Daily - 30 Days Composition : Gliclazide 80 MG + Metformin 500MG Timings : 1 Before Breakfast, 1 Night - Before Dinner - 2) DAPAHENZ S 10/100 TABLET 0-1-0 Daily - 30 Days Composition : Dapagliflozin 10 MG Sitagliptin 100 MG Timings : 1 Afternoon - Before Dinner 3) FORTIUS F 20 0-0-1 Daily - 30 Days Timings : 1 Night - After Dinner 4) RABENDA PLUS 1-0-0 Daily - 20 Days Composition . Levosuipinde 75 MG - Rabeprazole 20 MG Timings 1 Before Breakfast 5) NEURONE G 0-0-1 Daily - 30 Days Composition. IMETHYLCOBALAMIN 1500 MCG - PREGABALIN 75MG Timings 1- Before sleeping at night Dr. Phishek Shrivastava Appointment time 10 AM to 6.00 PM Mob. : 6267089757, 9977369339, 7869022999, 9098215024 Please take an appointment.
    """
    result = process_prescription_text(text4)


    # print(result)

    meds = get_unique_meds(text4)
    # print(meds)
    dosages = get_unique_dosages(text4)
    frequencies = get_frequencies(text4)
    n=len(set(meds))
    print(meds[0:n])
    print(dosages[0:n])
    print(frequencies[0:n])
    print("Len of meds:", len(set(meds)))
   

