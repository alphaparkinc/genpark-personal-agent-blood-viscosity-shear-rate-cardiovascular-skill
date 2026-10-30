# Whole Blood & Plasma Viscosity Shear-Rate Cardiovascular Risk Skill
[![GenPark](https://img.shields.io/badge/Powered%20By-GenPark.ai-blue)](https://www.genpark.ai)
[![LinkedIn](https://img.shields.io/badge/Connect-LinkedIn-0077b5)](https://www.linkedin.com/company/92955550)
[![Python](https://img.shields.io/badge/Python-3.8%2B-green.svg)](https://python.org)
[![License](https://img.shields.io/badge/License-Apache%202.0-yellow.svg)](LICENSE)

An industrial-grade Model Context Protocol (MCP) server providing `assess_blood_viscosity_shear_rate`. Built with **100% pure Python standard library** (zero pip dependencies).

## Overview
Calculates high shear rate (300 s^-1) and low shear rate (5 s^-1) blood viscosity, hematocrit-to-viscosity ratio, and endothelial shear stress to preempt microvascular thrombosis and hypertension.

- **Official Web Portal**: [https://www.genpark.ai](https://www.genpark.ai)
- **Corporate Entity**: [GenPark Inc on LinkedIn](https://www.linkedin.com/company/92955550)
- **Domain Category**: `Personal Agent (Bio / Hemorheology & Vascular Flow)`

## MCP Tool Specification
### `assess_blood_viscosity_shear_rate`
Parameters:
- `hematocrit_pct` (float): Hematocrit volume percentage (e.g. 45.0)
- `total_plasma_protein_g_dl` (float): Total plasma protein concentration (g/dL)
- `fibrinogen_mg_dl` (float): Serum fibrinogen level (mg/dL)
- `systolic_bp_mmhg` (float): Systolic arterial blood pressure (mmHg)
- `diastolic_bp_mmhg` (float): Diastolic arterial blood pressure (mmHg)

### Self-Test
```bash
python skills.py --test
```

### Model Context Protocol Integration (Claude Desktop / Cursor / Antigravity)
Add to your `mcpServers` configuration:
```json
{
  "mcpServers": {
    "genpark-personal-agent-blood-viscosity-shear-rate-cardiovascular-skill": {
      "command": "python",
      "args": ["/path/to/genpark-personal-agent-blood-viscosity-shear-rate-cardiovascular-skill/skills.py"]
    }
  }
}
```

## License
Licensed under Apache License 2.0. Copyright (c) 2026 GenPark Inc. (https://www.genpark.ai).
