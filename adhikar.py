print("🇮🇳 Welcome to Adhikar")
print("Select Language / भाषा चुनें:")

languages = {
    "1": "English",
    "2": "Hindi",
    "3": "Marathi",
    "4": "Tamil",
    "5": "Telugu",
    "6": "Kannada",
    "7": "Malayalam",
    "8": "Bengali",
    "9": "Gujarati",
    "10": "Punjabi"
}

for key, value in languages.items():
    print(f"{key}. {value}")

choice = input("Enter your choice: ") 
text = {
    "English": {
        "age": "1. What is your age? ",
        "income": "2. Annual family income (₹)? ",
        "occupation": "3. Occupation (farmer/student/worker/other): ",
        "gender": "4. Gender (male/female/other): ",
        "bpl": "5. BPL category? (yes/no): ",
        "checking": "\nChecking eligible schemes...\n",
        "eligible": "You are eligible for:",
        "none": "No matching schemes found.",
        "thanks": "Thank you for using Sarkar Mitra!"
    },

    "Hindi": {
        "age": "1. आपकी उम्र क्या है? ",
        "income": "2. वार्षिक आय (₹)? ",
        "occupation": "3. व्यवसाय (farmer/student/worker/other): ",
        "gender": "4. लिंग (male/female/other): ",
        "bpl": "5. क्या आप BPL में हैं? (yes/no): ",
        "checking": "\nपात्र योजनाएं खोजी जा रही हैं...\n",
        "eligible": "आप इन योजनाओं के पात्र हैं:",
        "none": "कोई योजना नहीं मिली।",
        "thanks": "Sarkar Mitra का उपयोग करने के लिए धन्यवाद!"
    },
    "Marathi": {
        "age": "1. तुमचे वय किती आहे? ",
        "income": "2. वार्षिक उत्पन्न (₹)? ",
        "occupation": "3. व्यवसाय (farmer/student/worker/other): ",
        "gender": "4. लिंग (male/female/other): ",
        "bpl": "5. तुम्ही BPL मध्ये आहात का? (yes/no): ",
        "checking": "\nपात्र योजना तपासत आहोत...\n",
        "eligible": "तुम्ही या योजनांसाठी पात्र आहात:",
        "none": "कोणतीही योजना सापडली नाही.",
        "thanks": "Sarkar Mitra वापरल्याबद्दल धन्यवाद!"
    },

    "Tamil": {
        "age": "1. உங்கள் வயது என்ன? ",
        "income": "2. ஆண்டு வருமானம் (₹)? ",
        "occupation": "3. தொழில் (farmer/student/worker/other): ",
        "gender": "4. பாலினம் (male/female/other): ",
        "bpl": "5. BPL பிரிவில் உள்ளீர்களா? (yes/no): ",
        "checking": "\nதகுதியான திட்டங்கள் சரிபார்க்கப்படுகிறது...\n",
        "eligible": "நீங்கள் தகுதியான திட்டங்கள்:",
        "none": "திட்டங்கள் எதுவும் இல்லை.",
        "thanks": "Sarkar Mitra பயன்படுத்தியதற்கு நன்றி!"
    }
}

selected_lang = languages.get(choice, "English")

if selected_lang not in text:
    selected_lang = "English"

t = text[selected_lang]
age = int(input(t["age"]))
income = int(input(t["income"]))
occupation = input(t["occupation"]).lower()
gender = input(t["gender"]).lower()
bpl = input(t["bpl"]).lower()

print(t["checking"])

eligible_schemes = []

if occupation == "farmer" and income < 600000:
    eligible_schemes.append(("PM-KISAN", "https://pmkisan.gov.in/"))

if income < 300000 or bpl == "yes":
    eligible_schemes.append(("Ayushman Bharat", "https://pmjay.gov.in/"))

if gender == "female" and income < 200000:
    eligible_schemes.append(("Ujjwala Yojana", "https://www.pmuy.gov.in/"))

if occupation == "student" and income < 800000:
    eligible_schemes.append(("National Scholarship Portal", "https://scholarships.gov.in/"))

if 18 <= age <= 40:
    eligible_schemes.append(("Atal Pension Yojana", "https://www.npscra.nsdl.co.in/scheme-details.php"))

# Show Results
if eligible_schemes:
    print("\n", t["eligible"])
    for scheme in eligible_schemes:
        print("📌", scheme[0])
        print("🔗", scheme[1])
        print()
else:
    print(t["none"])

print("\n", t["thanks"])