from core.log import setup_logging, log_message
from core.disasm import X86Analyzer
from core.report import generate_report

def analyze_memory_dump(dump_path):
    setup_logging()
    log_message(f"Starting analysis of memory dump: {dump_path}")

    with open(dump_path, 'rb') as f:
        memory_dump = f.read()

    analyzer = X86Analyzer(memory_dump)
    instructions = analyzer.identify_instructions()

    report = generate_report(instructions)
    report_file = f"{dump_path}_report.json"
    with open(report_file, 'w') as rf:
        rf.write(report)

    log_message(f"Memory dump analysis complete. Report saved to {report_file}")

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python live_memory.py <path_to_memory_dump>")
        sys.exit(1)
    analyze_memory_dump(sys.argv[1])
