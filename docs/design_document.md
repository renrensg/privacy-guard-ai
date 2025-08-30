# Design Document

## System Architecture
1. **PII Detector** → Regex identifies sensitive entities.
2. **Redactor** → Replace with pseudonym tokens.
3. **Mapping Store** → JSON file keeps token-to-original mapping.
4. **Restorer** → Replaces tokens with original data locally.
5. **Image Sanitizer** → Removes EXIF GPS metadata.

## Tools & Libraries
- Python 3.9+
- Regex (`re`)
- `hmac`, `hashlib`, `base64` for pseudonymization
- `PIL` (Pillow) for images
- `argparse` for CLI

## Security Model
- All processing local (no API calls).
- Secret salt ensures pseudonym uniqueness.
