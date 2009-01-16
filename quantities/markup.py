# -*- coding: utf-8 -*-
"""
"""

import operator

USE_UNICODE = True

def superscript(val):
    # TODO: use a regexp:
    for k, v in enumerate(['⁰', '¹', '²', '³', '⁴', '⁵', '⁶', '⁷', '⁸', '⁹']):
        val = val.replace('**'+str(k), v)
        val = val.replace('^'+str(k), v)
    return val

def format_units(udict):
    '''
    create a string representation of the units contained in a dimensionality
    '''
    num = []
    den = []
    keys = [k for k, o in
        sorted(
            [(k, k.format_order) for k in udict],
            key=operator.itemgetter(1)
        )
    ]
    for key in keys:
        d = udict[key]
        if USE_UNICODE:
            u = key.u_symbol
        else:
            u = key.symbol
        if d>0:
            if d > 1:
                u = u + ('**%s'%d)
            num.append(u)
        elif d<0:
            d = -d
            if d > 1:
                u = u + ('**%s'%d)
            den.append(u)
    res = '*'.join(num)
    if len(den):
        if not res: res = '1'
        fmt = '(%s)' if len(den) > 1 else '%s'
        res = res + '/' + fmt%('*'.join(den))
    if not res: res = 'dimensionless'
    return res

def format_units_unicode(udict):
    res = format_units(udict)
    res = superscript(res)
    res = res.replace('*','·')

    return res
