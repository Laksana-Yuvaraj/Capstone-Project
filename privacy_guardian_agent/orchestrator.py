from .document_scanner import scan_document
from .sensitive_classifier import classify_sensitive_data
from .summary_writer import write_summary
from .redaction_executor import redact_data
from .audit_log import log_action
from .compliance_checker import check_compliance
from .output_manager import save_output

def run_pipeline(input_file):
    text = scan_document(input_file)
    pii_segments = classify_sensitive_data(text)
    summary = write_summary(pii_segments)
    redacted_file = redact_data(text, pii_segments)
    log_action(input_file, pii_segments, redacted_file)
    compliance_report = check_compliance(pii_segments)
    save_output(redacted_file)
    return summary, compliance_report
