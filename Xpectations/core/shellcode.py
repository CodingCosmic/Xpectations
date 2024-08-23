import re

class ShellcodeDetector:
    def __init__(self, binary_code):
        self.binary_code = binary_code

    def detect_shellcode(self):
        shellcode_patterns = [b"\xeb\xfe", b"\xcc", b"\x90"]  # Example shellcode patterns
        found_patterns = []
        for pattern in shellcode_patterns:
            if pattern in self.binary_code:
                found_patterns.append(pattern)
                print(f"Possible shellcode detected: {pattern}")
        return found_patterns
