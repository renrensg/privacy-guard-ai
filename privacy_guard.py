import re, hmac, hashlib, base64, json, argparse
from PIL import Image

SECRET_SALT = b"my_secret_salt"

patterns = {
    "EMAIL": r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}",
    "PHONE": r"(?:\+65\s?)?[689]\d{7}",
    "NRIC_SG": r"[STFG]\d{7}[A-Z]",
    "CREDIT_CARD": r"\b(?:\d[ -]*?){13,16}\b",
    "IP": r"\b(?:\d{1,3}\.){3}\d{1,3}\b"
}

def pseudonymize(value: str, tag: str) -> str:
    digest = hmac.new(SECRET_SALT, value.encode(), hashlib.sha256).digest()
    token = base64.urlsafe_b64encode(digest)[:8].decode()
    return f"<{tag}:{token}>"

def redact_text(input_file, output_file):
    with open(input_file) as f: text = f.read()
    mapping = {}
    for tag, pattern in patterns.items():
        matches = re.findall(pattern, text)
        for m in matches:
            if m not in mapping:
                mapping[m] = pseudonymize(m, tag)
            text = text.replace(m, mapping[m])
    with open(output_file, "w") as f: f.write(text)
    with open(output_file + ".map.json", "w") as f: json.dump(mapping, f, indent=2)
    print(f"Redacted -> {output_file}, Mapping -> {output_file}.map.json")

def restore_text(redacted_file, map_file, output_file):
    with open(redacted_file) as f: text = f.read()
    with open(map_file) as f: mapping = json.load(f)
    reverse_map = {v:k for k,v in mapping.items()}
    for token, original in reverse_map.items():
        text = text.replace(token, original)
    with open(output_file, "w") as f: f.write(text)
    print(f"Restored -> {output_file}")

def strip_exif(input_img, output_img):
    img = Image.open(input_img)
    data = list(img.getdata())
    new_img = Image.new(img.mode, img.size)
    new_img.putdata(data)
    new_img.save(output_img)
    print(f"Stripped EXIF -> {output_img}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    sub = parser.add_subparsers(dest="command")
    r1 = sub.add_parser("redact-text")
    r1.add_argument("--in", dest="input_file")
    r1.add_argument("--out", dest="output_file")
    r2 = sub.add_parser("restore-text")
    r2.add_argument("--redacted")
    r2.add_argument("--map")
    r2.add_argument("--out", dest="output_file")
    r3 = sub.add_parser("strip-exif")
    r3.add_argument("--in", dest="input_img")
    r3.add_argument("--out", dest="output_img")
    args = parser.parse_args()

    if args.command == "redact-text":
        redact_text(args.input_file, args.output_file)
    elif args.command == "restore-text":
        restore_text(args.redacted, args.map, args.output_file)
    elif args.command == "strip-exif":
        strip_exif(args.input_img, args.output_img)
    else:
        parser.print_help()
