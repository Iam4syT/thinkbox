import hashlib
import re

def verify_restore(expected_digest, restored_bytes):
    if not isinstance(expected_digest, str) or not re.fullmatch(r"[0-9a-fA-F]{64}", expected_digest):
        return "reference unavailable"
    if not isinstance(restored_bytes, bytes):
        return "restore unavailable"
    actual_digest = hashlib.sha256(restored_bytes).hexdigest()
    return "verified" if actual_digest == expected_digest.lower() else "mismatch"
