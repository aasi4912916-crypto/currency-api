import os
from pdf2image import convert_from_path

POPPLER_PATH = r"C:\poppler\poppler-25.12.0\Library\bin"
GENUINE_PDF = r"C:\Users\AASRITHA\OneDrive\Documents\REAL.pdf"
FAKE_PDF = r"C:\Users\AASRITHA\OneDrive\Documents\fAKE.pdf"
GENUINE_OUT = r"C:\Users\AASRITHA\currency_project\dataset\train\genuine"
FAKE_OUT = r"C:\Users\AASRITHA\currency_project\dataset\train\counterfeit"

print("Extracting genuine note images...")
os.makedirs(GENUINE_OUT, exist_ok=True)
pages = convert_from_path(GENUINE_PDF, dpi=200, poppler_path=POPPLER_PATH)
for i, page in enumerate(pages):
    page.save(os.path.join(GENUINE_OUT, f"my_genuine_{i+1}.jpg"), "JPEG")
    print(f"Saved: my_genuine_{i+1}.jpg")
print(f"Done! {len(pages)} genuine images extracted")

print("\nExtracting fake note images...")
os.makedirs(FAKE_OUT, exist_ok=True)
pages = convert_from_path(FAKE_PDF, dpi=200, poppler_path=POPPLER_PATH)
for i, page in enumerate(pages):
    page.save(os.path.join(FAKE_OUT, f"my_fake_{i+1}.jpg"), "JPEG")
    print(f"Saved: my_fake_{i+1}.jpg")
print(f"Done! {len(pages)} fake images extracted")

print("\nTotal Genuine:", len(os.listdir(GENUINE_OUT)))
print("Total Counterfeit:", len(os.listdir(FAKE_OUT)))