"""Extend the existing visual system with WebAtlas and ViewShift evidence panels."""
from build_artwork import THEMES, T, R, label, save


def webatlas(c, a, mobile):
    ink, muted, rule = c['ink'], c['muted'], c['rule']
    if mobile:
        w, h = 400, 430
        b = [label(16, 30, 'DATA & DISTRIBUTED SYSTEMS', a), T(16, 76, 'WebAtlas', 34, ink, 'serif', font_weight='700'),
             T(16, 105, 'The worker stops. The work survives.', 16, muted)]
        x, y, nw, gap = 16, 140, 368, 62
        for i, (name, sub) in enumerate([('Claim a lease', 'PostgreSQL · SKIP LOCKED'), ('Process an observation', 'Bounded workers · provenance'), ('Commit and acknowledge', 'Observation + history + job')]):
            yy = y+i*gap
            b += [R(x, yy, nw, 48, c['raised'], 5, rule), T(x+14, yy+20, name, 15, ink), T(x+14, yy+39, sub, 12, muted, 'mono')]
        b += [T(16, 362, '64 leases reclaimed · 300/300 jobs', 17, a, 'serif', font_weight='700'),
              T(16, 389, 'Recorded synthetic crash test; at-least-once', 13, muted), T(16, 410, 'execution with idempotent committed effects.', 13, muted)]
    else:
        w, h = 960, 290
        b = [label(28, 38, 'DATA & DISTRIBUTED SYSTEMS', a), T(28, 91, 'WebAtlas', 39, ink, 'serif', font_weight='700'),
             T(28, 126, 'The worker stops.', 22, ink, 'serif'), T(28, 155, 'The work survives.', 22, ink, 'serif', font_style='italic'),
             T(28, 204, '64 leases reclaimed · 300/300 jobs', 16, a, font_weight='700'), T(28, 230, 'Recorded synthetic crash-recovery test.', 13, muted)]
        for i, (name, sub) in enumerate([('Claim', 'expiring lease'), ('Process', 'bounded workers'), ('Commit', 'history + ack')]):
            x = 420+i*174
            b += [R(x, 75, 156, 86, c['raised'], 7, rule), T(x+78, 111, name, 21, ink, 'serif', text_anchor='middle'), T(x+78, 139, sub, 11, muted, 'mono', text_anchor='middle')]
            if i < 2: b += [T(x+165, 124, '→', 16, a, text_anchor='middle')]
        b += [T(420, 206, 'At-least-once execution.', 17, ink, 'serif'), T(420, 232, 'Idempotent committed effects; not exactly once.', 13, muted)]
    return w, h, b, 'WebAtlas — durable observations and crash recovery', 'Architecture schematic: PostgreSQL lease, bounded processing, transactional persistence and acknowledgement. Recorded synthetic SIGKILL test recovered 64 leases and completed 300 of 300 jobs. At-least-once execution, not exactly once.'


def viewshift(c, a, mobile):
    ink, muted, rule = c['ink'], c['muted'], c['rule']
    if mobile:
        w, h = 400, 370
        b = [label(16, 30, 'INDEPENDENT AI RESEARCH', a), T(16, 74, 'ViewShift Lab', 32, ink, 'serif', font_weight='700'), T(16, 105, 'When does a second view help?', 16, muted)]
        gx, gy, gw = 16, 145, 368
    else:
        w, h = 960, 280
        b = [label(28, 38, 'INDEPENDENT AI RESEARCH', a), T(28, 90, 'ViewShift Lab', 38, ink, 'serif', font_weight='700'),
             T(28, 127, 'When does a second', 23, ink, 'serif'), T(28, 158, 'view help?', 23, ink, 'serif', font_style='italic'),
             T(28, 209, 'Matched parameters. Paired predictions.', 13, muted), T(28, 232, 'Same synthetic scenes; four training seeds.', 13, muted)]
        gx, gy, gw = 444, 68, 488
    for i, (name, value, color) in enumerate([('Single-view CNN', 48.1, muted), ('Two-view CNN', 57.8, a)]):
        yy = gy+i*66
        b += [T(gx, yy, name, 14, ink), T(gx+gw, yy, f'{value}%', 18, color, 'mono', text_anchor='end'), R(gx, yy+12, gw, 12, rule, 3), R(gx, yy+12, gw*value/100, 12, color, 3)]
    if mobile:
        b += [T(16, 295, 'Held-out camera-angle accuracy · 0–100% bars', 13, muted), T(16, 320, 'Synthetic projected disks; extra two-view compute.', 13, muted), T(16, 345, 'Real-photo validation pending.', 13, a)]
    else:
        b += [T(gx, 209, 'Held-out camera-angle accuracy · 0–100% bars', 12, muted), T(gx, 233, 'Synthetic disks; extra compute. Real-photo validation pending.', 12, muted)]
    return w, h, b, 'ViewShift Lab — synthetic viewpoint-reasoning study', 'Recorded mean OOD accuracy across four training seeds on fixed synthetic scenes: 48.1 percent single-view CNN and 57.8 percent two-view CNN. Matched parameter counts, extra two-view input and compute. Zero to 100 percent bars. Real-photo validation pending.'


if __name__ == '__main__':
    for name, fn, accents in [('webatlas', webatlas, ('#b2ce9a', '#476334')), ('viewshift', viewshift, ('#b6b8ee', '#56528c'))]:
        for theme, c in THEMES.items():
            a = accents[0 if theme == 'dark' else 1]
            for mobile in (False, True):
                w, h, body, title, desc = fn(c, a, mobile)
                save(f'{name}{"-mobile" if mobile else ""}-{theme}.svg', w, h, body, title, desc, c, a)
