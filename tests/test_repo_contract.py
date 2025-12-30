import os

FORBIDDEN = [
    "Cipher-512", "QKS", "IKS", "HKDF", "AES-256", "ChaCha20", "Dilithium", "Kyber"
]

def test_public_repo_does_not_include_proprietary_keywords():
    # This is a blunt guardrail to prevent accidental IP/code drops.
    # Adjust the list as needed.
    root = os.path.dirname(os.path.dirname(__file__))
    for dirpath, _, filenames in os.walk(root):
        for fn in filenames:
            if fn.endswith((".py", ".md", ".txt")):
                p = os.path.join(dirpath, fn)
                data = open(p, "r", encoding="utf-8", errors="ignore").read()
                for w in FORBIDDEN:
                    assert w not in data, f"Forbidden keyword '{w}' found in {p}"
