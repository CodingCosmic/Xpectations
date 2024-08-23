from core.disasm import X86Analyzer
from core.shellcode import ShellcodeDetector
from core.rop import ROPDetector
from core.obfuscation import ObfuscationDetector
from core.report import generate_report
from core.log import setup_logging, log_message

def interactive_analysis(binary_code):
    setup_logging()
    log_message("Starting interactive analysis.")

    analyzer = X86Analyzer(binary_code)
    shellcode_detector = ShellcodeDetector(binary_code)
    rop_detector = ROPDetector(binary_code)
    obfuscation_detector = ObfuscationDetector(binary_code)

    while True:
        print("\nInteractive Analysis Menu:")
        print("1. Disassemble")
        print("2. Detect Shellcode")
        print("3. Detect ROP Chains")
        print("4. Detect Obfuscation")
        print("5. Generate Report")
        print("6. Exit")

        choice = input("Select an option: ")

        if choice == '1':
            instructions = analyzer.identify_instructions()
            for instr in instructions:
                print(instr)

        elif choice == '2':
            shellcode_detector.detect_shellcode()

        elif choice == '3':
            rop_detector.detect_rop_chains()

        elif choice == '4':
            obfuscation_detector.detect_obfuscation()

        elif choice == '5':
            instructions = analyzer.identify_instructions()
            report = generate_report(instructions)
            report_file = "interactive_report.json"
            with open(report_file, 'w') as rf:
                rf.write(report)
            print(f"Report generated: {report_file}")

        elif choice == '6':
            log_message("Interactive analysis ended.")
            break

        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python interactive_mode.py <path_to_binary>")
        sys.exit(1)

    with open(sys.argv[1], 'rb') as f:
        binary_code = f.read()

    interactive_analysis(binary_code)
