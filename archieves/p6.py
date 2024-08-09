import re

text="""
R. &amp; R. Diabetic &amp; Thyroid Clinic Dr. Abhishek Shrivastava MD DMsc Endocrinology (England) Masters in Endocrinology RCP (England) Editorial Board Member Journal of Endocrinology and Metabolism Research Editorial Board Member MSD Research Publication ЯR akrilf-ch: Near Madan Mahal Police Station, Opposite HP Petrol Pump, Napier Town, Jabalpur Time :- 11 am to 7 pm Regd. No. 31955 Sunday Holiday Mob.: 7869022999, 6267089757 Ref.: 0004299: Praveen Beoher (58y, Female) - 9893043131 BP 90/60 mmHg Random Blood Sugar - RBS 258 mg/dL Complaints: NO MAJOR COMPLAINTS Diagnosis: DIABETES MELLITUS TYPE 2, HYPERTENSION, CAD, POST PTCA R Medicine 1) AMARYL M FORTE 2MG TABLET Dosage 1-0-1 Daily - 30 Days Composition : GLIMEPIRIDE 2 MG + METFORMIN 1000 MG Timing 1 - Before Breakfast, 1 - Night - Before Dinner 2) VIBITE M 50/500 1-0-1 Daily - 30 Days Composition : 1) ECOSPRIN-AV 75/10 CAPSULE 0-0-1 Daily - 30 Days Composition : ASPIRIN 75 MG + ATORVASTATIN 10 MG Timing ::1 / Night - After Food 4) CALTIVITE PLUS M 0-0-1 Daily - 30 Days Timing 1- Night - After Food MARYL M FORTE GLIVEPR MET CRM SPRIN-AV 75/15 ARIN 75 LIM TE PLUMB 4-33-8 Powered by HealthPlix EMR. www.healthplix.com Date: Date: 15-Jul-2021 Dr. Abhishek Shrivastava R. &amp; R. Diabetic &amp; Thyroid Clinic Dr. Abhishek Shrivastava MD DMsc Endocrinology ( England ) Masters in Endocrinology RCP ( England ) Editorial Board Member Journal of Endocrinology and Metabolism Research Editorial Board Member MSD Research Publication ЯR akrilf-ch: Near Madan Mahal Police Station, Opposite HP Petrol Pump, Napier Town, Jabalpur Time: 11 am to 7 pm Regd. No. 31955 Sunday Holiday Mob.: 7869022999 , 6267089757 Ref.: 0004299 : Praveen Beoher ( 58y , Female ) - 9893043131 BP 90/60 mmHg Random Blood Sugar - RBS 258 mg/dL Complaints : NO MAJOR COMPLAINTS Diagnosis : DIABETES MELLITUS TYPE 2 , HYPERTENSION , CAD , POST PTCA R Medicine 1) AMARYL M FORTE 2MG TABLET Dosage 1-0-1 Daily - 30 days Composition : GLIMEPIRIDE 2 MG + METFORMIN 1000 MG Timing 1 - Before breakfast, 1 - Night - Before dinner 2) VIBITE M 50/500 1-0-1 Daily - 30 Days Composition : METFORMIN 500 MG + VILDAGLIPTIN 50 MG Timing : purn : be before breakfast, 1 - Night - before dinner 3 ) ECOSPRIN - AV 75/10 CAPSULE 0-0-1 Daily - 30 Days Composition : ASPIRIN 75 MG + ATORVASTATIN 10 MG Timing :: 1 / Night - after dinner 4 ) CALTIVITE PLUS M 0-0-1 Daily - 30 Days Timing 1- Night - after dinner MARYL M FORTE GLIVEPR MET CRM SPRIN - AV 75/15 ARIN 75 LIM TE PLUMB 4-33-8 Powered by HealthPlix EMR . www.healthplix.com Date : Date : 15 - Jul - 2021 Dr. Abhishek Shrivastava
"""

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
meds =get_unique_meds(text)
dosages = get_unique_dosages(text)
frequencies = getFreq(text)
timings=getTimings(text)

mapping = mapMedicines(meds, dosages, frequencies, timings)
print(mapping)