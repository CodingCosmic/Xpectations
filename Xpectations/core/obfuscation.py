import re

class ObfuscationDetector:
    def __init__(self, binary_code):
        self.binary_code = binary_code

    def detect_obfuscation(self):
        obfuscation_patterns = [b'\x90\x90\x90\x90', b'\xcc\xcc\xcc\xcc']  # Example patterns
        found_obfuscations = []
        for pattern in obfuscation_patterns:
            if pattern in self.binary_code:
                found_obfuscations.append(pattern)
                print(f"Obfuscation detected: {pattern}")
        return found_obfuscations

    def deobfuscate(self):
        deobfuscated_code = self.binary_code.replace(b'\x90', b'')
        deobfuscated_code = deobfuscated_code.replace(b'\xcc', b'')
        return deobfuscated_code
