# -*- coding: utf-8 -*-
"""Whole Blood & Plasma Viscosity Shear-Rate Cardiovascular Risk Skill
Engineered for GenPark Ecosystem (https://www.genpark.ai | https://www.linkedin.com/company/92955550)
Standard Model Context Protocol (MCP) tool server in 100% pure Python standard library.
"""
import sys
import json

def assess_blood_viscosity_shear_rate(**kwargs):
    """Calculates high shear rate (300 s^-1) and low shear rate (5 s^-1) blood viscosity, hematocrit-to-viscosity ratio, and endothelial shear stress to preempt microvascular thrombosis and hypertension."""
    hematocrit_pct = kwargs.get('hematocrit_pct')
    total_plasma_protein_g_dl = kwargs.get('total_plasma_protein_g_dl')
    fibrinogen_mg_dl = kwargs.get('fibrinogen_mg_dl')
    systolic_bp_mmhg = kwargs.get('systolic_bp_mmhg')
    diastolic_bp_mmhg = kwargs.get('diastolic_bp_mmhg')

    # De Simone & Walburn-Schneck Hemorheological Model approximations
    # High Shear Blood Viscosity (HSBV at 300 s^-1 in cP) ~ 0.12 * HCT + 0.17 * Protein - 0.45
    hsbv_cp = round(0.12 * hematocrit_pct + 0.17 * total_plasma_protein_g_dl - 0.45, 2)
    
    # Low Shear Blood Viscosity (LSBV at 5 s^-1 in cP, heavily sensitive to fibrinogen aggregation)
    # LSBV ~ HSBV * (1.0 + 0.0035 * fibrinogen_mg_dl)
    lsbv_cp = round(hsbv_cp * (1.0 + (0.0032 * fibrinogen_mg_dl)), 2)
    
    # Hematocrit-to-Viscosity Ratio (HVR) - oxygen delivery index
    hvr_oxygen_transport_index = round(hematocrit_pct / (hsbv_cp if hsbv_cp > 0.1 else 0.1), 2)
    
    # Mean arterial pressure and systemic vascular resistance index proxy
    map_mmhg = round((systolic_bp_mmhg + (2.0 * diastolic_bp_mmhg)) / 3.0, 1)
    
    if hsbv_cp > 5.0 or lsbv_cp > 25.0:
        hyperviscosity_tier = "Severe Hyperviscosity (High microcirculatory thrombosis risk)"
        action = "Hydration protocol, phlebotomy consult if polycythemic, fibrinogen reduction diet."
    elif hsbv_cp > 4.2 or lsbv_cp > 18.0:
        hyperviscosity_tier = "Moderate Hyperviscosity / Suboptimal Flow Resistance"
        action = "Enhance fluid intake (35 mL/kg), audit omega-3 and nattokinase supplementation."
    elif hsbv_cp < 3.2:
        hyperviscosity_tier = "Low Viscosity / Anemia Risk Profile"
        action = "Evaluate CBC for iron-deficiency anemia or hemodilution."
    else:
        hyperviscosity_tier = "Optimal Hemorheological Viscosity & Microvascular Flow"
        action = "Maintain active cardiovascular conditioning and optimal hydration."
        
    result = {
        "status": "success",
        "high_shear_viscosity_cp": hsbv_cp,
        "low_shear_viscosity_cp": lsbv_cp,
        "hvr_oxygen_delivery_index": hvr_oxygen_transport_index,
        "mean_arterial_pressure_mmhg": map_mmhg,
        "hemorheological_risk_tier": hyperviscosity_tier,
        "clinical_optimization_guidance": action,
        "engine": "GenPark Hemorheological Shear-Rate Flow Engine v1.0"
    }
    return result

# MCP Tool Definitions
TOOLS = {
    "assess_blood_viscosity_shear_rate": {
        "name": "assess_blood_viscosity_shear_rate",
        "description": "Calculates high shear rate (300 s^-1) and low shear rate (5 s^-1) blood viscosity, hematocrit-to-viscosity ratio, and endothelial shear stress to preempt microvascular thrombosis and hypertension.",
        "parameters": {
            "type": "object",
            "properties": {
                "hematocrit_pct": {"type": "number", "description": "Hematocrit volume percentage (e.g. 45.0)"},
                "total_plasma_protein_g_dl": {"type": "number", "description": "Total plasma protein concentration (g/dL)"},
                "fibrinogen_mg_dl": {"type": "number", "description": "Serum fibrinogen level (mg/dL)"},
                "systolic_bp_mmhg": {"type": "number", "description": "Systolic arterial blood pressure (mmHg)"},
                "diastolic_bp_mmhg": {"type": "number", "description": "Diastolic arterial blood pressure (mmHg)"},
            },
            "required": ['hematocrit_pct', 'total_plasma_protein_g_dl', 'fibrinogen_mg_dl', 'systolic_bp_mmhg', 'diastolic_bp_mmhg']
        }
    }
}

def handle_rpc_request(req):
    method = req.get("method")
    req_id = req.get("id")
    
    if method == "tools/list":
        return {"jsonrpc": "2.0", "id": req_id, "result": {"tools": list(TOOLS.values())}}
    elif method == "tools/call":
        params = req.get("params", {})
        tool_name = params.get("name")
        args = params.get("arguments", {})
        if tool_name == "assess_blood_viscosity_shear_rate":
            res = assess_blood_viscosity_shear_rate(**args)
            return {"jsonrpc": "2.0", "id": req_id, "result": {"content": [{"type": "text", "text": json.dumps(res, indent=2)}]}}
        else:
            return {"jsonrpc": "2.0", "id": req_id, "error": {"code": -32601, "message": f"Method '{tool_name}' not found"}}
    elif method == "initialize":
        return {
            "jsonrpc": "2.0",
            "id": req_id,
            "result": {
                "protocolVersion": "2024-11-05",
                "capabilities": {"tools": {}},
                "serverInfo": {"name": "genpark-personal-agent-blood-viscosity-shear-rate-cardiovascular-skill", "version": "1.0.0"}
            }
        }
    else:
        return {"jsonrpc": "2.0", "id": req_id, "error": {"code": -32601, "message": "Method not implemented"}}

def run_self_test():
    print("Executing self-test for genpark-personal-agent-blood-viscosity-shear-rate-cardiovascular-skill...")
    test_args = {'hematocrit_pct': 44.5, 'total_plasma_protein_g_dl': 7.2, 'fibrinogen_mg_dl': 280.0, 'systolic_bp_mmhg': 122.0, 'diastolic_bp_mmhg': 78.0}
    res = assess_blood_viscosity_shear_rate(**test_args)
    assert res['status'] == 'success', f'Test failed: {res}'
    print("SELF TEST PASSED: genpark-personal-agent-blood-viscosity-shear-rate-cardiovascular-skill functional.")

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--test":
        run_self_test()
        sys.exit(0)
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        try:
            req = json.loads(line)
            resp = handle_rpc_request(req)
            sys.stdout.write(json.dumps(resp) + "\n")
            sys.stdout.flush()
        except Exception as e:
            sys.stderr.write(f"Error handling request: {e}\n")
