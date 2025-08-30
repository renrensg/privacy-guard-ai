# Final Report: Privacy Guard for Generative AI

## Introduction
Generative AI poses risks of privacy leakage. This project ensures safe AI usage by detecting and removing sensitive data.

## Implementation
- Regex + hashing for redaction.
- JSON mapping for restoration.
- Pillow for stripping EXIF data.
- CLI-based interaction.

## Results
- Successfully redacted emails, phones, NRICs, credit cards, and IPs.
- Restored text accurately.
- Stripped GPS metadata from images.

## Conclusion
The project proves it is possible to use Generative AI without exposing private data.  
Future improvements include NER models, automatic risk scoring, and real-time API integration.
