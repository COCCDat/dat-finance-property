"""Compute disclosed comparable adjustments. All monetary inputs are VND."""
import json
import math
import sys

def number(value, name, minimum=None):
    if isinstance(value, bool) or not isinstance(value, (int, float)) or not math.isfinite(value):
        raise ValueError(name + ' must be finite numeric')
    if minimum is not None and value < minimum:
        raise ValueError(name + ' below minimum')
    return value

def calculate(data):
    area = number(data['target_area_m2'], 'target_area_m2', 0)
    qty = data['quantity']
    if area <= 0 or isinstance(qty, bool) or not isinstance(qty, int) or qty <= 0:
        raise ValueError('positive area and integer quantity required')
    comps = data['comparables']
    if not comps or len({c['id'] for c in comps}) != len(comps):
        raise ValueError('nonempty unique comparable ids required')
    rows = []
    for c in comps:
        ask = number(c['ask_vnd'], 'ask_vnd', 0)
        ca = number(c['area_m2'], 'area_m2', 0)
        weight = number(c['weight'], 'weight', 0)
        if ask <= 0 or ca <= 0:
            raise ValueError('positive ask and comparable area required')
        row = {'id': c['id'], 'weight': weight, 'value_per_lot_vnd': {}}
        for key in ['low', 'base', 'high']:
            s = c['scenarios'][key]
            discount = number(s['discount'], 'discount', 0)
            if discount >= 1:
                raise ValueError('discount must be <1')
            building = number(s['building_vnd'], 'building_vnd', 0)
            land = ask * (1-discount) - building
            if land <= 0:
                raise ValueError('nonpositive land residual')
            adjusted = land / ca
            for factor in s['adjustments']:
                factor = number(factor, 'adjustment')
                if factor <= -1:
                    raise ValueError('adjustment must be >-1')
                adjusted *= 1 + factor
            row['value_per_lot_vnd'][key] = adjusted * area
        vals = row['value_per_lot_vnd']
        if not vals['low'] <= vals['base'] <= vals['high']:
            raise ValueError('scenario order invalid for ' + str(c['id']))
        rows.append(row)
    total_weight = sum(r['weight'] for r in rows)
    if total_weight <= 0:
        raise ValueError('positive total weight required')
    values = {k: sum(r['value_per_lot_vnd'][k]*r['weight'] for r in rows)/total_weight for k in ['low','base','high']}
    return {'unit': 'VND', 'comparables': rows, 'value_per_lot': values,
        'quantity': qty, 'gross_revenue': {k: v*qty for k,v in values.items()},
        'warning': 'Arithmetic only; source quality and adjustments require evidence.'}

if __name__ == '__main__':
    try:
        print(json.dumps(calculate(json.load(sys.stdin)), ensure_ascii=False, allow_nan=False))
    except (KeyError, TypeError, ValueError, OverflowError) as exc:
        print(json.dumps({'status': 'INVALID_INPUT', 'error': str(exc)}))
        sys.exit(2)
