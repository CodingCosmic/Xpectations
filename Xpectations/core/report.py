import json

def generate_report(instructions, format='json'):
    report_data = {
        "instructions": instructions,
        "summary": {
            "total_instructions": len(instructions)
        }
    }

    if format == 'json':
        return json.dumps(report_data, indent=4)
    elif format == 'xml':
        import dicttoxml
        return dicttoxml.dicttoxml(report_data).decode()
    elif format == 'csv':
        import csv
        from io import StringIO
        output = StringIO()
        writer = csv.writer(output)
        writer.writerow(["Address", "Mnemonic", "Operands"])
        for instr in instructions:
            writer.writerow(instr.split())
        return output.getvalue()
