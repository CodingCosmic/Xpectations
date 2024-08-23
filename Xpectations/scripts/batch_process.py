import os
from core.disasm import X86Analyzer
from core.log import setup_logging, log_message
from core.report import generate_report

def batch_process(input_dir, output_dir):
    setup_logging()
    log_message(f"Starting batch processing of directory: {input_dir}")

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for file_name in os.listdir(input_dir):
        file_path = os.path.join(input_dir, file_name)
        if os.path.isfile(file_path):
            log_message(f"Processing file: {file_path}")

            with open(file_path, 'rb') as f:
                binary_code = f.read()

            analyzer = X86Analyzer(binary_code)
            instructions = analyzer.identify_instructions()

            report = generate_report(instructions)
            report_file = os.path.join(output_dir, f"{file_name}.json")
            with open(report_file, 'w') as rf:
                rf.write(report)

            log_message(f"Report generated: {report_file}")

    log_message("Batch processing complete.")

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 3:
        print("Usage: python batch_process.py <input_dir> <output_dir>")
        sys.exit(1)
    batch_process(sys.argv[1], sys.argv[2])
