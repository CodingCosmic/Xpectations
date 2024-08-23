from core.disasm import X86Analyzer
from core.log import setup_logging, log_message
from core.shellcode import ShellcodeDetector
from core.rop import ROPDetector
from core.obfuscation import ObfuscationDetector
from core.report import generate_report

def main(file_path):
    setup_logging()
    log_message(f"Starting analysis of {file_path}")

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
    log_message("Analysis complete.")
    print(report)

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python analyze_x86.py <path_to_binary>")
        sys.exit(1)
    main(sys.argv[1])
