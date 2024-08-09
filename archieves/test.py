import re

text="""
R. &amp; R. Diabetic &amp; Thyroid Clinic DR. ABHISHEK SHRIVASTAVA MD, FACE, MMsc, DMsc Endocrinology Advisory Council Member Central Zone American College of Physicians India Chapter Editorial Board Member JEMR Thyroid, Diabetes Obesity Specialist R ЯК Sunday Off 0004299 Praveen Beohar ( 60y, Female) - 9893043131 Clinic: Near Madan Mahal Police Station, Opposite HP Petrol Pump, Napier Town, Jabalpur Timings: 12 Noon to 7:30 PM Regd. No. 31955 Date &amp; Time 28-Dec-2023 02:37 PM BP 77/53mmHg | Pulse 100bpm | Glycosylated Hemoglobin HbA1c 6.88% [28-Dec-2023] Serum Creatinine 1.36mg/dL, Serum Calcium - 7.13mg/dL, eGFR - Creatinine Clearance - 44.59mL/min/1.73m2 Complaints BREATHLESSNESS WEAKNESS Diagnosis : DIABETES MELLITUS TYPE 2, HYPERTENSION, CAD, PTCA RX Medicine Dosage Freq. - Duration 1) TRIOBIMET 2MG TABLET 1-0-1 Daily - 30 days Composition : Glimepiride 2MG + Metformin 500MG + Pioglitazone 15 MG Timings : 1 Before Breakfast, 1 Night - Before Dinner 2) LINARES E 0-1-0 Daily - 30 days Composition : LINAGLIPTIN 5MG + EMPAGLIFLOZIN 25MG Timings : 1 Afternoon - Before Dinner 3) BONJOY PLUS 0-0-1 Daily - 30 days Composition : CALCITRIOL 0, 25MCG + CALCIUM CARBONATE 500MG + ZINC 7.5MG... Timings : 1 Night - After Dinner 417. guober so with food To withden ॐ Dr. Abhishek Shrivastava Appointment time 10 AM to 6.00 PM. Mobile. 9 6267089757, 9977369339, 7869022999, 9098215024 Please take an appointment. R. &amp; R. Diabetic and Thyroid Clinic DR. ABHISHEK SHRIVASTAVA MD, FACE, MMsc, DMsc Endocrinology Advisory Council Member Central Zone American College of Physicians India Chapter Editorial Board Member JEMR Thyroid, Diabetes Obesity Specialist R ЯК Sunday Off 0004299 Praveen Beohar ( 60y, Female ) - 9893043131 Clinic: Near Madan Mahal Police Station, Opposite HP Petrol Pump, Napier Town, Jabalpur Timings: 12 Noon to 7:30 PM Regd. No. 31955 Date &amp; Time 28 - Dec - 2023 02:37 PM BP 77 / 53mmHg | Pulse 100bpm | Glycosylated Hemoglobin HbA1c 6.88 % [ 28 - Dec - 2023 ] Serum Creatinine 1.36mg / dL , Serum Calcium - 7.13mg / dL , eGFR - Creatinine Clearance - 44.59mL / min / 1.73m2 Complaints BREATHLESSNESS WEAKNESS Diagnosis : DIABETES MELLITUS TYPE 2 , HYPERTENSION , POST PTCA RX Medicine Dosage q. - Duration 1 ) TRIOBIMET 2MG TABLET 1-0-1 Daily - 30 days Composition : Glimepiride 2MG + Metformin 500MG + Pioglitazone 15 MG Timings : 1 Before Breakfast, 1 Night - Before Dinner 2 ) LINARES E 0-1-0 Daily - 30 days Composition : LINAGLIPTIN 5MG + EMPAGLIFLOZIN 25MG Timings : 1 Afternoon - Before Dinner 3 ) BONJOY PLUS 0-0-1 Daily - 30 days Composition : CALCITRIOL 0, 25MCG + CALCIUM CARBONATE 500MG + ZINC 7.5MG ... Timings : 1 Night - After Dinner 417. guober so with food To withden ॐ Dr. Abhishek Shrivastava Appointment time is 10 AM to 6 PM. Mobile: 9 6267089757, 9977369339, 7869022999, 9098215024 Please take an appointment."""


def getMeds(text):
    # Define the regex pattern
    pattern = r'\d+\)\s*(\w+)'

    # Find all matches
    matches = re.findall(pattern, text)

    return matches


def getDosage(text):
    # Define the regex pattern
    pattern = r'\d-\d-\d Daily'

    # Find all matches
    matches = re.findall(pattern, text)

    return matches


def getFreq(text):
    # Define the regex pattern
    pattern = r'\d+ days'

    # Find all matches
    matches = re.findall(pattern, text)

    return matches


def getTimings(text):

    pattern = r"Timings\s*:\s*(\d+ [A-Za-z]+ - [A-Za-z]+(?: [A-Za-z]+)*)"

    # Find all matches in the text
    matches = re.findall(pattern, text)

    # Return the list of timings
    return [match.strip() for match in matches]


def extend_list(lst, length, default_value=None):
    """Extend a list to a specific length with a default value."""
    return lst + [default_value] * (length - len(lst))

def mapMedicines(meds, dosages, frequencies, timings):
    # Extend dosages and frequencies to match the length of meds
    max_length = len(meds)
    dosages = extend_list(dosages, max_length)
    frequencies = extend_list(frequencies, max_length)
    timings=extend_list(timings, max_length)

    # Initialize an empty dictionary to hold the mappings
    medicine_map = {}

    # Iterate through the lists
    for i in range(max_length):
        med = meds[i]
        dosage = dosages[i]
        frequency = frequencies[i]
        timing = timings[i]

        # Store the medicine with its dosage and frequency
        if med not in medicine_map:
            medicine_map[med] = (dosage, frequency, timing)

    return medicine_map

# Example usage
meds =getMeds(text)
dosages = getDosage(text)
frequencies = getFreq(text)
timings=getTimings(text)

mapping = mapMedicines(meds, dosages, frequencies, timings)
print(mapping)