# hospital_simple_no_id.py

doctors = []        # list of dicts: {"name":..., "spec":..., "times":[...]}
patients = []       # list of dicts: {"name":..., "age":..., "disease":...}
appointments = []   # list of dicts: {"patient":..., "doctor":..., "time":...}

def add_doctor():
    name = input("Doctor name: ").strip()
    spec = input("Specialization: ").strip()
    times = input("Available timings (comma separated, e.g. 10:00,11:00): ").strip()
    times_list = [t.strip() for t in times.split(",") if t.strip()]
    doctors.append({"name": name, "spec": spec, "times": times_list})
    print(f"✅ Doctor {name} added successfully!")

def register_patient():
    name = input("Patient name: ").strip()
    try:
        age = int(input("Age: ").strip())
    except ValueError:
        print("❌ Invalid age. Try again.")
        return
    disease = input("Disease/Description: ").strip()
    patients.append({"name": name, "age": age, "disease": disease})
    print(f"✅ Patient {name} registered successfully!")

def show_doctors():
    if not doctors:
        print("❌ No doctors available.")
        return
    print("\n🏥 List of Doctors:")
    for i, d in enumerate(doctors, start=1):
        times = ", ".join(d["times"]) if d["times"] else "No timings"
        print(f"{i}. Dr.{d['name']} — {d['spec']} | Timings: {times}")

def show_appointments():
    if not appointments:
        print("❌ No appointments yet.")
        return
    print("\n📅 Appointments:")
    for i, a in enumerate(appointments, start=1):
        print(f"{i}. {a['patient']} with Dr.{a['doctor']} at {a['time']}")

def book_appointment():
    if not doctors:
        print("❌ No doctors available. Add a doctor first.")
        return
    if not patients:
        print("❌ No patients registered. Register a patient first.")
        return

    patient_name = input("Enter patient name: ").strip()
    doctor_name = input("Enter doctor name: ").strip()

    # find doctor
    doctor = None
    for d in doctors:
        if d["name"].lower() == doctor_name.lower():
            doctor = d
            break
    if not doctor:
        print("❌ Doctor not found.")
        return

    time = input("Enter preferred time (exactly as listed): ").strip()
    if time not in doctor["times"]:
        print(f"❌ Doctor not available at {time}. Available: {', '.join(doctor['times'])}")
        return

    # check if booked already
    for a in appointments:
        if a["doctor"].lower() == doctor_name.lower() and a["time"] == time:
            print("❌ That time slot is already booked.")
            return

    appointments.append({"patient": patient_name, "doctor": doctor_name, "time": time})
    print(f"✅ Appointment booked for {patient_name} with Dr.{doctor_name} at {time}!")

def menu():
    while True:
        print("\n=== 🏥 HOSPITAL MANAGEMENT SYSTEM ===")
        print("1️⃣ Add Doctor")
        print("2️⃣ Register Patient")
        print("3️⃣ Book Appointment")
        print("4️⃣ Show Doctors")
        print("5️⃣ Show Appointments")
        print("6️⃣ Exit")

        choice = input("Enter choice: ").strip()
        if choice == "1":
            add_doctor()
        elif choice == "2":
            register_patient()
        elif choice == "3":
            book_appointment()
        elif choice == "4":
            show_doctors()
        elif choice == "5":
            show_appointments()
        elif choice == "6":
            print("👋 Exiting... Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please try again.")

if __name__ == "__main__":
    menu()
