# Privacy Guard for Generative AI

## 🚀 Overview
This project prevents **privacy leakage** when using Generative AI by:
- Detecting Personally Identifiable Information (PII).
- Redacting PII with pseudonyms.
- Restoring originals locally after AI processing.
- Removing EXIF metadata from images.

## 🛠️ Features
- Redact sensitive data: Emails, Phone Numbers, NRIC, Credit Cards, IP.
- Restore originals safely.
- Remove GPS/metadata from images.
- Local only (no data leaves your machine).

## 📂 Project Structure
- `privacy_guard.py` → main code
- `examples/` → test files
- `docs/` → proposal, design, report

## ⚙️ Installation
```bash
git clone https://github.com/<your-username>/privacy-guard-ai.git
cd privacy-guard-ai
pip install -r requirements.txt
```

## ▶️ Usage
```bash
# Redact text
python privacy_guard.py redact-text --in examples/input.txt --out examples/redacted.txt

# Restore text
python privacy_guard.py restore-text --redacted examples/redacted.txt --map examples/redacted.txt.map.json --out examples/restored.txt

# Strip EXIF from image
python privacy_guard.py strip-exif --in examples/input.jpg --out examples/output_no_exif.jpg
```

## 📊 Example
Input:
```
Email: alex.tan@example.com, Phone: +65 9123 4567, NRIC: S1234567D
```

Redacted:
```
Email: <EMAIL:abc123>, Phone: <PHONE:def456>, NRIC: <NRIC:ghi789>
```

Restored:
```
Email: alex.tan@example.com, Phone: +65 9123 4567, NRIC: S1234567D
```

## 📌 Future Work
- Named Entity Recognition (NER).
- Face blurring for images.
- Risk scoring dashboard.

All content in repository © 2025 Jarren W. All rights reserved.
