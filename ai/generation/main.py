import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

GOOGLE_API_KEY=os.getenv('GOOGLE_API_KEY')

genai.configure(api_key=GOOGLE_API_KEY)

# Create the model
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-1.5-flash",
  generation_config=generation_config,
  # safety_settings = Adjust safety settings
  # See https://ai.google.dev/gemini-api/docs/safety-settings
)


def generate_content(prompt):
  response = model.generate_content([
    "You are a assistant that creates treatment plans for patients based on their medical history and recent data. Create a comprehensive treatment plan for them based on the information",
    "Patient Info and Research: Patient: 45-year-old female\nConditions: Type 2 diabetes (diagnosed 5 years ago), hypertension, obesity (BMI 32)\nCurrent medications: Metformin, Lisinopril\nRecent lab results: HbA1c 7.8%, LDL cholesterol 140 mg/dL\nLifestyle: Sedentary job, minimal exercise, high-stress levels\nGenetic analysis: Increased risk for cardiovascular disease\nWearable data: Average daily steps 3,000, sleep 6 hours/night",
    "Treatment plan: Adjust medications:\n\nIncrease Metformin to 1000mg twice daily\nAdd Empagliflozin 10mg daily\nContinue Lisinopril, add Atorvastatin 20mg daily\n\n\nLifestyle changes:\n\nGradual increase to 10,000 steps/day\nMediterranean diet, limit to 1800 calories/day\nStress reduction: 15-min daily meditation\n\n\nMonitoring:\n\nWeekly weight check\nDaily blood glucose and blood pressure readings\nFollow-up HbA1c and lipid panel in 3 months\n\n\nReferrals:\n\nNutritionist consult\nCardiovascular risk assessment\n\n\nPatient education:\n\nDiabetes management class\nHeart disease prevention resources",
    "Patient Info and Research: Patient: 60-year-old male\nConditions: Rheumatoid arthritis, osteoporosis\nCurrent medications: Methotrexate, Prednisone, Calcium/Vitamin D supplement\nRecent labs: High inflammatory markers, low bone density\nLifestyle: Former smoker, moderate alcohol consumption, limited mobility\nGenetic analysis: Higher risk for certain cancer types\nWearable data: Irregular sleep patterns, low activity levels",
    "Treatment plan: Medications:\n\nAdd biologic therapy: Adalimumab 40mg every other week\nTaper Prednisone dose\nStart Alendronate 70mg weekly for osteoporosis\n\n\nLifestyle:\n\nSmoking cessation support\nLimit alcohol to 1 drink/day\nLow-impact exercises: swimming, tai chi\n\n\nMonitoring:\n\nQuarterly rheumatology check-ups\nAnnual bone density scan\nRegular cancer screenings\n\n\nReferrals:\n\nPhysical therapy for mobility\nSleep study\n\n\nPatient education:\n\nJoint protection techniques\nFall prevention strategies",
    "Patient Info and Research: Patient: 35-year-old female\nConditions: Polycystic ovary syndrome (PCOS), anxiety\nCurrent medications: Oral contraceptives, Metformin\nRecent labs: Elevated testosterone, normal thyroid function\nLifestyle: Vegetarian diet, regular yoga practice, trying to conceive\nGenetic analysis: Carrier for cystic fibrosis\nWearable data: Irregular menstrual cycles, elevated stress levels",
    "Patient Info and Research:" + prompt,
    "Treatment plan: ", 
  ])
  return response.text
