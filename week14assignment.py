def create_patient_index(daily_schedule):
    patient_index = {}           

    for patient in daily_schedule:
        ssn = patient['ssn']     
        name = patient['patient_name'] 
        patient_index[ssn] = name

    return patient_index


def audit_check_ins(patient_index, arrived_ssns):
    missed_appointments = set()
    walk_in_patients = set()

    for ssn in patient_index:
        if ssn not in arrived_ssns:
            missed_appointments.add(ssn)

    for ssn in arrived_ssns:
        if ssn not in patient_index:
            walk_in_patients.add(ssn)

    return missed_appointments, walk_in_patients


def list_no_shows(patient_index, missed_set):
    report = []

    for ssn in missed_set:
        name = patient_index[ssn]
        message = "NO-SHOW: " + name.upper()
        report.append(message)

    report.sort()
    return report
schedule = [
    {'ssn': 11122, 'patient_name': "John Doe"},
    {'ssn': 33344, 'patient_name': "Jane Smith"},
    {'ssn': 55566, 'patient_name': "Emily Blunt"}
]

arrived = [11122, 55566, 77788]

patient_index = create_patient_index(schedule)
missed, walk_ins = audit_check_ins(patient_index, arrived)
report = list_no_shows(patient_index, missed)

print("Missed Appointments:", missed)
print("Walk-ins:", walk_ins)
print("Report:", report)
