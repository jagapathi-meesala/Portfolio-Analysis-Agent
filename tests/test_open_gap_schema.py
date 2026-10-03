from pathlib import Path
import yaml

def test_manifest_and_skills():
    root = Path(__file__).parents[1]
    manifest = yaml.safe_load((root / "agent.yaml").read_text())
    assert manifest["spec_version"] == "0.1.0"
    for skill in manifest["skills"]:
        p = root / "skills" / skill / "SKILL.md"
        assert p.exists()
        assert p.read_text().startswith("---")
    for tool in manifest["tools"]:
        p = root / "tools" / f"{tool}.yaml"
        assert p.exists()
        data = yaml.safe_load(p.read_text())
        assert data["name"] == tool
        assert "input_schema" in data
