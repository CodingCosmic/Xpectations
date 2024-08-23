from core.file_upload import handle_upload
from core.disasm import X86Analyzer
from core.shellcode import ShellcodeDetector
from core.rop import ROPDetector
from core.obfuscation import ObfuscationDetector
from core.report import generate_report
from core.log import setup_logging, log_message

def analyze_uploaded_file(file_name, file_content):
    setup_logging()
    file_path = handle_upload(file_name, file_content)
    log_message(f"File uploaded and saved to {file_path}")

    with open(file_path, 'rb') as f:
        binary_code = f.read()

    analyzer = X86Analyzer(binary_code)
    instructions = analyzer.identify_instructions()

    shellcode_detector = ShellcodeDetector(binary_code)
    shellcode_detector.detect_shellcode()

    rop_detector = ROPDetector(binary_code)
    rop_detector.detect_rop_chains()

    obfuscation_detector = ObfuscationDetector(binary_code)
    obfuscation_detector.detect_obfuscation()

    report = generate_report(instructions)
    log_message("File analysis complete.")
    print(report)

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python file_upload.py <path_to_file>")
        sys.exit(1)

    with open(sys.argv[1], 'rb') as f:
        file_content = f.read()

    analyze_uploaded_file(sys.argv[1], file_content)
