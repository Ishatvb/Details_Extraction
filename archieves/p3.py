import re

text="""
R. &amp; R. Diabetic &amp; Thyroid Clinic Dr. Abhishek Shrivastava MD DMsc Endocrinology (England) Masters in Endocrinology RCP (England) Editorial Board Member Journal of Endocrinology and Metabolism Research Editorial Board Member MSD Research Publication ЯR akrilf-ch: Near Madan Mahal Police Station, Opposite HP Petrol Pump, Napier Town, Jabalpur Time :- 11 am to 7 pm Regd. No. 31955 Sunday Holiday Mob.: 7869022999, 6267089757 Ref.: 0004299: Praveen Beoher (58y, Female) - 9893043131 BP 90/60 mmHg Random Blood Sugar - RBS 258 mg/dL Complaints: NO MAJOR COMPLAINTS Diagnosis: DIABETES MELLITUS TYPE 2, HYPERTENSION, CAD, POST PTCA R Medicine 1) AMARYL M FORTE 2MG TABLET Dosage 1-0-1 Daily - 30 Days Composition : GLIMEPIRIDE 2 MG + METFORMIN 1000 MG Timing 1 - Before Breakfast, 1 - Night - Before Dinner 2) VIBITE M 50/500 1-0-1 Daily - 30 Days Composition : 1) ECOSPRIN-AV 75/10 CAPSULE 0-0-1 Daily - 30 Days Composition : ASPIRIN 75 MG + ATORVASTATIN 10 MG Timing ::1 / Night - After Food 4) CALTIVITE PLUS M 0-0-1 Daily - 30 Days Timing 1- Night - After Food MARYL M FORTE GLIVEPR MET CRM SPRIN-AV 75/15 ARIN 75 LIM TE PLUMB 4-33-8 Powered by HealthPlix EMR. www.healthplix.com Date: Date: 15-Jul-2021 Dr. Abhishek Shrivastava R. &amp; R. Diabetic &amp; Thyroid Clinic Dr. Abhishek Shrivastava MD DMsc Endocrinology ( England ) Masters in Endocrinology RCP ( England ) Editorial Board Member Journal of Endocrinology and Metabolism Research Editorial Board Member MSD Research Publication ЯR akrilf-ch: Near Madan Mahal Police Station, Opposite HP Petrol Pump, Napier Town, Jabalpur Time: 11 am to 7 pm Regd. No. 31955 Sunday Holiday Mob.: 7869022999 , 6267089757 Ref.: 0004299 : Praveen Beoher ( 58y , Female ) - 9893043131 BP 90/60 mmHg Random Blood Sugar - RBS 258 mg/dL Complaints : NO MAJOR COMPLAINTS Diagnosis : DIABETES MELLITUS TYPE 2 , HYPERTENSION , CAD , POST PTCA R Medicine 1) AMARYL M FORTE 2MG TABLET Dosage 1-0-1 Daily - 30 days Composition : GLIMEPIRIDE 2 MG + METFORMIN 1000 MG Timing 1 - Before breakfast, 1 - Night - Before dinner 2) VIBITE M 50/500 1-0-1 Daily - 30 Days Composition : METFORMIN 500 MG + VILDAGLIPTIN 50 MG Timing : purn : be before breakfast, 1 - Night - before dinner 3 ) ECOSPRIN - AV 75/10 CAPSULE 0-0-1 Daily - 30 Days Composition : ASPIRIN 75 MG + ATORVASTATIN 10 MG Timing :: 1 / Night - after dinner 4 ) CALTIVITE PLUS M 0-0-1 Daily - 30 Days Timing 1- Night - after dinner MARYL M FORTE GLIVEPR MET CRM SPRIN - AV 75/15 ARIN 75 LIM TE PLUMB 4-33-8 Powered by HealthPlix EMR . www.healthplix.com Date : Date : 15 - Jul - 2021 Dr. Abhishek Shrivastava
"""
def get_unique_meds(text):
    # Define the regex pattern
    pattern = r'\d+\)\s*(\w+)'
    # pattern = r"\d+\)\s*([A-Z\s\dMG\+\(\)\/]+(?:TABLET|CAPSULE|SYRUP)?)"


    # Find all matches
    matches = re.findall(pattern, text)

    # Get unique matches by converting the list to a set
    unique_matches = set(matches)

    return list(unique_matches)


meds = get_unique_meds(text)
print(meds)