import os
import re

 Public-safe guardrails:
 - Allow architecture names like QKS/IKS (branding is OK)
 - Forbid explicit cryptographic algorithm / primitive names and key material
 - Catch accidental private keys or PEM blobs

FORBIDDEN_KEYWORDS = [
     Symmetric / AEAD / modes
    "AES-128", "AES-192", "AES-256", "AES-GCM", "GCM", "CTR", "CBC",
    "ChaCha20", "Poly1305", "XChaCha20", "XSalsa20", "Salsa20",

     Hash / KDF / MAC
    "HKDF", "PBKDF2", "scrypt", "Argon2", "BLAKE3", "BLAKE2",
    "SHA-256", "SHA256", "SHA-512", "SHA512", "SHA3", "Keccak",
    "HMAC",

     PQC names
    "Kyber", "ML-KEM", "Dilithium", "ML-DSA", "SPHINCS", "SLH-DSA", "HQC",

     Classical public-key (avoid mentioning concrete algos in this public demo)
    "RSA", "ECDSA", "Ed25519", "Curve25519", "secp256k1",

     Implementation indicators that often imply real crypto code was dropped
    "reference implementation", "production cipher", "real encryption", "real key derivation",
]

FORBIDDEN_PATTERNS = [
     PEM / private key material patterns
    r"-----BEGIN (RSA )?PRIVATE KEY-----",
    r"-----BEGIN EC PRIVATE KEY-----",
    r"-----BEGIN OPENSSH PRIVATE KEY-----",
    r"-----BEGIN PRIVATE KEY-----",
    r"-----BEGIN CERTIFICATE-----",

     Hex-like key dumps (very rough heuristic): long uninterrupted hex strings
    r"\b[0-9a-fA-F]{128,}\b",
]

ALLOWED_KEYWORDS = [
     Explicitly allowed architecture/brand names:
    "QKS",
    "IKS",
]

def should_scan_file(filename: str) -> bool:
    return filename.endswith((".py", ".md", ".txt", ".toml", ".json"))

def test_public_repo_does_not_include_forbidden_crypto_terms_or_keys():
    root = os.path.dirname(os.path.dirname(__file__))

    for dirpath, _, filenames in os.walk(root):
         Avoid scanning virtualenvs/build artifacts if someone accidentally commits them
        if any(skip in dirpath for skip in (".venv", "__pycache__", "dist", "build", ".git")):
            continue

        for fn in filenames:
            if not should_scan_file(fn):
                continue

            p = os.path.join(dirpath, fn)
            data = open(p, "r", encoding="utf-8", errors="ignore").read()

             Allow-list check: we don't remove allowed keywords; we just ensure they don't cause false positives.
             (No action needed here because allow-list is separate.)

             Keyword blocks (case-sensitive on purpose; keeps intent explicit)
            for w in FORBIDDEN_KEYWORDS:
                assert w not in data, f"Forbidden crypto/implementation term '{w}' found in {p}"

             Regex blocks (keys, PEMs, suspicious key dumps)
            for pat in FORBIDDEN_PATTERNS:
                assert re.search(pat, data) is None, f"Forbidden key material pattern '{pat}' found in {p}"
}"
