"""Three-valued sourcing gate; does not verify listing claims."""
import json
import math
import sys

def numeric(value, name):
    if value is None:
        return None
    if isinstance(value, bool) or not isinstance(value, (float,int)) or not math.isfinite(value) or value < 0:
        raise ValueError(name + ' must be nonnegative finite or null')
    return value

def evaluate(d):
    area = numeric(d.get('area_m2'), 'area_m2')
    width = numeric(d.get('width_m'), 'width_m')
    sides = numeric(d.get('access_sides'), 'access_sides')
    gv = d.get('go_vap')
    adverse = d.get('adverse_planning')
    if gv is not None and type(gv) is not bool:
        raise ValueError('go_vap must be bool or null')
    if adverse is not None and type(adverse) is not bool:
        raise ValueError('adverse_planning must be bool or null')
    if sides is not None and sides != int(sides):
        raise ValueError('access_sides must be integer')
    if adverse is True:
        status, reason = 'REJECT', 'public adverse planning claim'
    elif area is not None and area < 150:
        status, reason = 'REJECT', 'land area below 150'
    elif area is None:
        status, reason = 'VERIFY', 'land area unknown'
    elif gv is True:
        status, reason = 'ELIGIBLE', 'Go Vap area exception'
    elif (width is not None and width >= 10) or (sides is not None and sides >= 2):
        status, reason = 'ELIGIBLE', 'area and geometry pass without exception'
    elif gv is None or width is None or sides is None:
        status, reason = 'VERIFY', 'location or geometry insufficient'
    else:
        status, reason = 'REJECT', 'outside Go Vap geometry fails'
    return {'status': status, 'reason': reason, 'legal_verification': False}

if __name__ == '__main__':
    try:
        print(json.dumps(evaluate(json.load(sys.stdin))))
    except (ValueError, TypeError) as exc:
        print(json.dumps({'status': 'INVALID_INPUT', 'error': str(exc)}))
        sys.exit(2)
