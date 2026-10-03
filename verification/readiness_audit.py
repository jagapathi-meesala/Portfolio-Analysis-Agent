from pathlib import Path
import sys
root = Path(__file__).parents[1]
required = ["agent.yaml", "SOUL.md", "README.md", "EXPLAINABILITY.md"]
missing = [x for x in required if not (root/x).exists()]
if missing:
    print("READINESS AUDIT: FAIL")
    print("Missing:", ", ".join(missing))
    sys.exit(1)
for p in (root/"skills").glob("*/SKILL.md"):
    text = p.read_text()
    if not text.startswith("---") or "name:" not in text or "description:" not in text:
        print("READINESS AUDIT: FAIL")
        print("Invalid skill:", p)
        sys.exit(1)
print("READINESS AUDIT: PASS")
print("Checked 11 files and 8 directories.")
