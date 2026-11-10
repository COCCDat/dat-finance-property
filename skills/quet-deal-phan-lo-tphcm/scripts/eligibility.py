"""Three-valued sourcing gate; does not verify listing claims."""
import json
import math
import sys

def numeric(value, name):
    if value is None:
        return None
    if isinstance(value, bool) or not isinstance(value, (float, int)) or not math.isfinite(value) or value < 0:
        raise ValueError(name + ' must be nonnegative finite or null')
    return value

def evaluate(d):
    area = numeric(d.get('area_m2'), 'area_m2')
    width = numeric(d.get('width_m'), 'width_m')
    length = numeric(d.get('length_m'), 'length_m')
    ratio = numeric(d.get('width_to_length_ratio'), 'width_to_length_ratio')
    sides = numeric(d.get('access_sides'), 'access_sides')
    gv = d.get('go_vap')
    q12 = d.get('quan_12')
    adverse = d.get('adverse_planning')

    district = d.get('district')
    if district and isinstance(district, str):
        dist_lower = district.strip().lower()
        if 'gò vấp' in dist_lower or 'go vap' in dist_lower:
            gv = True
        elif 'quận 12' in dist_lower or 'quan 12' in dist_lower or 'q12' in dist_lower or 'q.12' in dist_lower:
            q12 = True

    if gv is not None and type(gv) is not bool:
        raise ValueError('go_vap must be bool or null')
    if q12 is not None and type(q12) is not bool:
        raise ValueError('quan_12 must be bool or null')
    if adverse is not None and type(adverse) is not bool:
        raise ValueError('adverse_planning must be bool or null')
    if sides is not None and sides != int(sides):
        raise ValueError('access_sides must be integer')

    is_exempt = (gv is True) or (q12 is True)

    if adverse is True:
        status, reason = 'REJECT', 'public adverse planning claim'
    elif area is not None and area < 150:
        status, reason = 'REJECT', 'land area below 150'
    elif area is None:
        status, reason = 'VERIFY', 'land area unknown'
    elif is_exempt:
        status, reason = 'ELIGIBLE', 'Go Vap / Quan 12 area exception'
    else:
        # Outside Go Vap & Quan 12: requires ratio width/length >= 2/3 OR sides >= 2
        has_two_sides = (sides is not None and sides >= 2)

        # Calculate width-to-length ratio
        calculated_ratio = ratio
        if calculated_ratio is None:
            if width is not None and length is not None and length > 0:
                calculated_ratio = width / length
            elif width is not None and area is not None and width > 0:
                eff_length = area / width
                if eff_length > 0:
                    calculated_ratio = width / eff_length

        has_good_ratio = (calculated_ratio is not None and calculated_ratio >= (2.0 / 3.0 - 1e-6))

        if has_two_sides or has_good_ratio:
            status, reason = 'ELIGIBLE', 'area and geometry pass without exception'
        elif gv is None and q12 is None:
            status, reason = 'VERIFY', 'location or geometry insufficient'
        elif sides is None and calculated_ratio is None:
            status, reason = 'VERIFY', 'geometry dimensions or access sides unknown'
        elif sides is None and not has_good_ratio:
            status, reason = 'VERIFY', 'ratio below 2/3 and access sides unknown'
        elif (sides is not None and sides < 2) and calculated_ratio is None:
            status, reason = 'VERIFY', 'access sides below 2 and dimensions unknown'
        else:
            status, reason = 'REJECT', 'outside Go Vap / Quan 12 geometry fails (ratio < 2/3 and access sides < 2)'

    return {'status': status, 'reason': reason, 'legal_verification': False}

if __name__ == '__main__':
    try:
        print(json.dumps(evaluate(json.load(sys.stdin))))
    except (ValueError, TypeError) as exc:
        print(json.dumps({'status': 'INVALID_INPUT', 'error': str(exc)}))
        sys.exit(2)
