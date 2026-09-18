# Contributing Guidelines

Thank you for your interest in contributing to the **VicSteal** security research repository. This project is dedicated to defensive malware analysis, reverse engineering, detection engineering, and cybersecurity education.

To maintain the project's integrity, safety, and focus on defensive research, all contributors must adhere to the guidelines outlined below.

---

## 1. Ethical Standards & Legal Compliance

This repository is maintained strictly for **educational and defensive security research purposes**.

- **No Malicious Weaponization**: We do not accept contributions that add exploitation capabilities, weaponize payloads, add persistence mechanisms, or enhance evasion solely for offensive deployment.
- **No Real Credentials or Infrastructure**: Never submit PRs or issues containing live API keys, active Discord webhooks, Telegram bot tokens, real victim data, or operational C2 endpoints. All configuration samples must use sanitized dummy values.
- **Safe Testing**: Any testing or execution must take place in strictly isolated, non-production sandbox environments (e.g., isolated virtual machines, dedicated analysis networks).

---

## 2. Areas Where Contributions Are Welcomed

We encourage contributions that improve the educational and defensive value of this repository:

- **Detection Engineering**: YARA rules, Sigma rules, Suricata/Snort network rules, and Windows Defender / EDR detection telemetry.
- **Threat Intelligence & Analysis**: Expanded MITRE ATT&CK mapping, forensic artifact identification, and incident response playbooks.
- **Code Hardening & Isolation**: Refactoring to improve sandboxing, safety guards against accidental execution, and defensive test coverage.
- **Documentation**: Clarifications, technical breakdowns, flowcharts, and reverse-engineering walkthroughs.

---

## 3. Getting Started & Development Workflow

### Step 1: Fork & Clone

1. Fork the repository to your GitHub account.
2. Clone your fork locally:
   ```bash
   git clone https://github.com/miraimo/Vic-Stealer.git
   cd Vic-Stealer
   ```

### Step 2: Create a Feature Branch

Create a branch with a descriptive name:
```bash
# For defensive detection rules or documentation
git checkout -b docs/update-mitre-mapping

# For bug fixes or code refactoring
git checkout -b fix/sandbox-check-logic
```

### Step 3: Code & Documentation Standards

- **Python Style**: Follow [PEP 8](https://peps.python.org/pep-0008/) conventions. Keep code clean, readable, and well-documented with docstrings and type hints where appropriate.
- **Sanitization**: Double-check that all test configs (`vic_config.py`, etc.) contain only placeholder values (e.g., `YOUR_WEBHOOK_HERE`).
- **Markdown**: Use clear GitHub-Flavored Markdown (GFM) for documentation with appropriate section headers and code blocks.

---

## 4. Submitting a Pull Request (PR)

Before submitting your pull request, please verify the following checklist:

- [ ] The contribution strictly serves defensive, analytical, or educational goals.
- [ ] No real credentials, API tokens, or production infrastructure addresses are present.
- [ ] Code has been tested in a controlled development or sandbox environment.
- [ ] Commit messages are clear, concise, and explain the motivation behind the change.
- [ ] The PR description clearly explains what was changed and why.

When opening the PR:
1. Provide a clear title (e.g., `docs: add YARA rule for stage-1 staging directory`).
2. Fill out the description detailing the scope, relevant MITRE techniques, and test verification steps.
3. Be open to feedback and discussion during code review.

---

## 5. Reporting Sensitive Findings or Leaks

If you discover an accidental leak of active credentials, sensitive tokens, or personal identifiers anywhere in the repository history, please **do not open a public issue**. Instead, contact the repository maintainer directly:

- **Contact**: `mohamed.harbouli.hb@gmail.com`, `mohammedlelly2006@gmail.com`

---

Thank you for helping keep security research ethical, rigorous, and defensive!
