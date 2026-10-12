import json

def format_llama_prompt(payload_str: str) -> str:
    data = json.loads(payload_str)
    chars = data["defect_characteristics"]

    return f"""<|begin_of_text|><|start_header_id|>system<|end_header_id|>
You are an edge AI quality-control assistant on an automated assembly line. 
Give concise, strictly actionable advice in at most 2 sentences.<|eot_id|>
<|start_header_id|>user<|end_header_id|>
Component: {data['component_type']}
Anomaly Score: {data['anomaly_score']} (Threshold: {data['threshold']})
Defect: {chars['category']}
Affected Area: {chars['affected_area_pct']}%

What immediate corrective step must the operator take?<|eot_id|>
<|start_header_id|>assistant<|end_header_id|>"""
