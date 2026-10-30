"""Static SVG panels for the profile README (v2). Standard library only.

Every panel exists as {desktop, mobile} x {light, dark}. Real product screenshots are
embedded as JPEG data URIs (scripts/src/*.jpg, derived from assets/*.png) because an SVG
shown through <img> cannot load external files. No scripts, fonts or network references.
"""
import re
from base64 import b64encode
from html import escape
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUT = HERE.parents[0] / 'assets'
SRC = HERE / 'src'

# bg, panel-raised, ink, muted, brass, rule, warn
THEMES = {
    'dark': dict(bg='#15171c', raised='#1d2026', ink='#f3eee4', muted='#b8b3a9', brass='#d9bc88', rule='#34363b', warn='#e58a7b'),
    'light': dict(bg='#f4f0e7', raised='#fbf9f3', ink='#24262b', muted='#62615d', brass='#796038', rule='#d6cfc2', warn='#a8432f'),
}
# Per-project accents echo each product's own UI colour; (dark, light) tuned for >= 4.5:1 on the panel.
ACCENT = {
    'gridflex': ('#b7e07a', '#3d7a28'),
    'powercut': ('#ff8a3d', '#b04a10'),
    'cuda': ('#9bd13a', '#4a7800'),
    'policylens': ('#5fc4b8', '#17766c'),
    'orderbook': ('#e0a86b', '#94561a'),
    'sourced': ('#9db7f5', '#3a58ae'),
}
FONT = {
    'sans': '-apple-system, "Segoe UI", Helvetica, Arial, sans-serif',
    'serif': '"Iowan Old Style", "Palatino Linotype", Georgia, serif',
    'mono': 'ui-monospace, SFMono-Regular, Menlo, Consolas, monospace',
}


def T(x, y, s, size, fill, fam='sans', **a):
    attrs = ' '.join(f'{k.replace("_", "-")}="{escape(str(v))}"' for k, v in a.items())
    return f'<text x="{x}" y="{y}" font-family=\'{FONT[fam]}\' font-size="{size}" fill="{fill}" {attrs}>{escape(s)}</text>'


def R(x, y, w, h, fill='none', rx=0, stroke=None, sw=1, **a):
    st = f' stroke="{stroke}" stroke-width="{sw}"' if stroke else ''
    extra = ''.join(f' {k.replace("_", "-")}="{v}"' for k, v in a.items())
    return f'<rect x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" height="{h:.1f}" rx="{rx}" fill="{fill}"{st}{extra}/>'


def label(x, y, s, fill, **a):
    return T(x, y, s, 12, fill, 'mono', letter_spacing='1.6', **a)


def jpeg(name):
    return 'data:image/jpeg;base64,' + b64encode((SRC / name).read_bytes()).decode()


def shot(uid, name, x, y, w, h, c, chrome='browser', rx=8):
    """Real screenshot in a rounded frame. chrome: 'browser' adds a title bar, 'tv' a bezel."""
    out = []
    if chrome == 'browser':
        bar = 16
        out += [R(x, y, w, h + bar, '#1b1e24', 10, c['rule'])]
        out += [f'<circle cx="{x + 12 + i * 12}" cy="{y + 8}" r="3" fill="{col}"/>' for i, col in enumerate(('#ff5f57', '#febc2e', '#28c840'))]
        iy, ih, ix, iw = y + bar, h, x, w
        out.append(f'<clipPath id="{uid}"><path d="M{ix} {iy}H{ix + iw}V{iy + ih - 9}Q{ix + iw} {iy + ih} {ix + iw - 9} {iy + ih}H{ix + 9}Q{ix} {iy + ih} {ix} {iy + ih - 9}Z"/></clipPath>')
    else:
        pad = 6
        out += [R(x, y, w, h, '#0a0a0c', 12, c['rule'])]
        ix, iy, iw, ih = x + pad, y + pad, w - 2 * pad, h - 2 * pad
        out.append(f'<clipPath id="{uid}"><rect x="{ix}" y="{iy}" width="{iw}" height="{ih}" rx="7"/></clipPath>')
    out.append(f'<image href="{jpeg(name)}" x="{ix}" y="{iy}" width="{iw}" height="{ih}" preserveAspectRatio="xMidYMid slice" clip-path="url(#{uid})"/>')
    return out


def chips(x, y, maxw, items, ink, stroke, fill='none', size=12, gap=8):
    """Flow-wrapped pills; returns (svg, y after last row)."""
    out, cx, cy = [], x, y
    for s in items:
        w = len(s) * size * 0.58 + 22
        if cx + w > x + maxw and cx > x:
            cx, cy = x, cy + 34
        out += [R(cx, cy, w, 26, fill, 13, stroke), T(cx + w / 2, cy + 17.5, s, size, ink, text_anchor='middle')]
        cx += w + gap
    return out, cy + 26


def save(name, w, h, body, title, desc, c, a):
    if w <= 400:
        body = [e if 'data-keep' in e else re.sub(r'font-size="(\d+(?:\.\d+)?)"', lambda mo: f'font-size="{max(float(mo.group(1)), 13):g}"', e) for e in body]
    svg = (f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" '
           f'aria-labelledby="t d"><title id="t">{escape(title)}</title><desc id="d">{escape(desc)}</desc>'
           + f'<defs><radialGradient id="g" cx="90%" cy="0%" r="75%"><stop offset="0" stop-color="{a}" stop-opacity="0.2"/><stop offset="1" stop-color="{a}" stop-opacity="0"/></radialGradient></defs>'
           + R(0.5, 0.5, w - 1, h - 1, c['bg'], 14, c['rule']) + R(0.5, 0.5, w - 1, h - 1, 'url(#g)', 14) + R(28 if w > 500 else 16, 0.5, 56, 3, a, 1.5) + ''.join(body) + '</svg>\n')
    (OUT / name).write_text(svg)


# --------------------------------------------------------------------------- panels
def identity(c, x, width, m):
    """Name plate: monogram + name + credentials. Sits above the featured project."""
    ink, mut, br, rule = c['ink'], c['muted'], c['brass'], c['rule']
    r = 15 if m else 20
    cy = 36 if m else 38
    out = [f'<circle cx="{x + r}" cy="{cy}" r="{r}" fill="none" stroke="{br}" stroke-width="1.6"/>',
           T(x + r, cy + (5.5 if m else 7), 'HM', 14 if m else 18, br, 'serif', text_anchor='middle', font_weight='700'),
           T(x + 2 * r + 14, cy + (7 if m else 10), 'Hajar Mrifag', 25 if m else 36, ink, 'serif', font_weight='700')]
    if m:
        out += [T(x, 70, 'AI · SYSTEMS · PRODUCT ENGINEERING', 11.5, br, 'mono', letter_spacing='0.6'), R(x, 80, width, 1, rule)]
    else:
        out += [T(x + width, 30, 'AI · SYSTEMS · PRODUCT ENGINEERING', 12, br, 'mono', text_anchor='end', letter_spacing='1.4'),
                T(x + width, 50, 'Final-year Software Engineering · Sichuan University', 13, mut, text_anchor='end'), R(x, 68, width, 1, rule)]
    return out


def hero(c, a, m):
    ink, mut, br, rule = c['ink'], c['muted'], c['brass'], c['rule']
    ratio = 71.731 / 2.246
    if not m:
        w, h = 960, 514
        b = identity(c, 28, 904, False) + ['<g transform="translate(0,24)">']
        b += [label(28, 86, '01 — FEATURED', a), T(28, 138, 'GridFlex AI', 44, ink, 'serif', font_weight='700'),
              T(28, 170, 'Battery dispatch, flexible demand', 15, mut), T(28, 191, 'and chronological forecasts in', 15, mut), T(28, 212, 'one workspace you can run.', 15, mut)]
        b += [label(28, 262, '60-DAY SHIFT + BATTERY ENGINE', mut)]
        b += [T(28, 290, 'Before', 13, mut), T(298, 290, '71.731 ms', 13, ink, 'mono', text_anchor='end'), R(28, 298, 270, 8, mut + '66', 4),
              T(28, 332, 'After', 13, ink), T(298, 332, '2.246 ms', 13, a, 'mono', text_anchor='end', font_weight='700'), R(28, 340, 270 * 2.246 / 71.731, 8, a, 4)]
        b += [T(28, 380, f'≈{ratio:.0f}× on this recorded workload', 14, a, font_weight='700'),
              T(28, 400, 'Historical engine benchmark, not HTTP latency.', 12, mut),
              T(28, 432, 'github.com/hajarmrifag/gridflex-ai  ↗', 12, br, 'mono')]
        b += shot('gf', 'gf-wide.jpg', 312, 62, 620, 379, c)
        b += [T(932, 476, 'Actual GridFlex workspace · scenario shown is separate from the benchmark', 11, mut, text_anchor='end'), '</g>']
    else:
        w, h = 400, 470
        b = identity(c, 16, 368, True) + ['<g transform="translate(0,50)">']
        b += [T(16, 66, 'GridFlex AI', 32, ink, 'serif', font_weight='700'), T(384, 62, '↗', 24, a, text_anchor='end'),
              T(16, 87, 'Dispatch, flexible demand & forecasts', 13, mut)]
        b += shot('gf', 'gf-narrow.jpg', 16, 98, 368, 193, c)
        b += [T(16, 322, '60-day engine', 12, mut), T(384, 322, '71.731 ms', 12, ink, 'mono', text_anchor='end'), R(16, 329, 368, 6, mut + '66', 3),
              T(16, 358, 'after', 12, ink), T(384, 358, '2.246 ms', 12, a, 'mono', text_anchor='end', font_weight='700'), R(16, 365, 368 * 2.246 / 71.731, 6, a, 3),
              T(16, 396, f'≈{ratio:.0f}× · engine timing, not HTTP latency', 13, a, font_weight='700'), '</g>']
    return w, h, b, 'GridFlex AI — recorded engine workload 71.731 to 2.246 ms',\
        ('Hajar Mrifag, AI, systems and product engineering. Featured: GridFlex AI, with its real workspace screenshot. '
         'Recorded 60-day shift plus battery engine workload fell from 71.731 to 2.246 milliseconds, about 32 times. Historical engine timing, not HTTP latency; the screenshot scenario is separate from the benchmark.')


def powercut(c, a, m):
    ink, mut, br, rule = c['ink'], c['muted'], c['brass'], c['rule']
    gw = 312 if not m else 368
    over = gw * 108 / 1908
    cap = gw - over
    nodes = ['TypeScript solver', 'Schedule verifier', 'Python reference']
    def gauge(x, y):
        return [label(x, y, 'ONE SYNTHETIC 12-HOUR OUTAGE PLAN', mut), R(x, y + 12, cap, 12, mut + '88', 3), R(x + cap, y + 12, over, 12, a, 3),
                T(x, y + 44, '1,800 Wh budget', 12, mut), T(x + gw, y + 44, '+108 Wh over', 12, a, text_anchor='end', font_weight='700')]
    def pipe(x, y):
        nw = (gw - 2 * 18) / 3
        out = []
        for i, n in enumerate(nodes):
            nx = x + i * (nw + 18)
            out += [R(nx, y, nw, 38, c['raised'], 8, rule), T(nx + nw / 2, y + 15, ['on-device', 'independent', 'reference'][i], 9.5, mut, 'mono', text_anchor='middle'),
                    T(nx + nw / 2, y + 30, ['TS solver', 'verifier', 'Python'][i], 12, ink, text_anchor='middle', font_weight='700')]
            if i < 2:
                out.append(T(nx + nw + 9, y + 24, '→', 14, a, text_anchor='middle'))
        return out
    if not m:
        w, h = 960, 376
        b = shot('pc', 'pc-wide.jpg', 28, 28, 560, 315, c, 'tv') + [R(250, 343, 116, 5, rule, 2), R(220, 348, 176, 4, rule, 2)]
        x = 620
        b += [label(x, 50, '02 — POWERCUT', a), T(x, 96, 'PowerCut', 40, ink, 'serif', font_weight='700'),
              T(x, 122, 'A constraint solver you can operate', 14, mut), T(x, 141, 'with a TV remote.', 14, mut)] + gauge(x, 176) + pipe(x, 248)
        b += [T(x, 322, '231', 30, a, 'serif', font_weight='700'), T(x + 66, 321, 'differential scenarios check the port', 12.5, ink),
              T(x, 348, 'Synthetic estimates, not a safety guarantee.', 12, mut)]
    else:
        w, h = 400, 470
        b = [label(16, 28, '02 — POWERCUT', a), T(16, 66, 'PowerCut', 32, ink, 'serif', font_weight='700'), T(384, 62, '↗', 24, a, text_anchor='end'),
             T(16, 86, 'A constraint solver you operate with a TV remote.', 12.5, mut)]
        b += shot('pc', 'pc-narrow.jpg', 16, 98, 368, 207, c, 'tv') + gauge(16, 336) + pipe(16, 396)
        b += [T(16, 458, '231', 22, a, 'serif', font_weight='700'), T(60, 458, 'differential scenarios check the port', 12, ink)]
    return w, h, b, 'PowerCut — 1,908 Wh plan against a 1,800 Wh budget',\
        ('Real PowerCut Vega Virtual Device screenshot: six synthetic appliance estimates need 1,908 Wh against a 1,800 Wh battery, 108 Wh over. '
         'Pipeline: on-device TypeScript solver, independent schedule verifier, Python reference; 231 differential scenarios.')


def cuda(c, a, m):
    ink, mut, br, rule = c['ink'], c['muted'], c['brass'], c['rule']
    rows = [('Naive', 385.648, mut), ('Custom', 1278.508, a), ('cuBLAS', 5322.721, br)]
    top = 5322.721
    if not m:
        w, h = 960, 300
        b = [label(28, 44, '03 — CUDA TRANSFORMER KERNELS', a), T(28, 96, 'From memory access', 34, ink, 'serif', font_weight='700'), T(28, 136, 'to measurement.', 34, ink, 'serif', font_weight='700'),
             T(28, 176, 'Custom GEMM against naive and cuBLAS.', 14, mut), label(28, 202, 'T4 · FP32 · 1024 × 1024 · KERNEL TIME', mut),
             T(28, 250, 'cuBLAS stays in view as the stronger reference.', 13, ink)]
        gx, gw = 520, 320
        for i, (n, v, col) in enumerate(rows):
            y = 62 + i * 58
            b += [T(440, y + 16, n, 15, ink if col == a else mut, font_weight='700' if col == a else '400'), R(gx, y, gw, 22, rule + '99', 4), R(gx, y, gw * v / top, 22, col, 4),
                  T(932, y + 17, f'{v:,.0f}', 15, ink, 'mono', text_anchor='end')]
        b += [R(440, 236, 492, 1, rule), T(440, 266, '1.28 TFLOPS', 18, a, 'serif', font_weight='700'), T(572, 266, '· 3.32× naive · 24% of cuBLAS', 13, ink), T(932, 288, 'GFLOP/s · linear bars from zero', 11, mut, text_anchor='end')]
    else:
        w, h = 400, 330
        b = [label(16, 28, '03 — CUDA TRANSFORMER KERNELS', a), T(16, 66, 'From memory access', 26, ink, 'serif', font_weight='700'), T(16, 96, 'to measurement.', 26, ink, 'serif', font_weight='700'),
             label(16, 122, 'T4 · FP32 GEMM · 1024² · KERNEL TIME', mut)]
        for i, (n, v, col) in enumerate(rows):
            y = 148 + i * 46
            b += [T(16, y, n, 14, ink if col == a else mut, font_weight='700' if col == a else '400'), T(384, y, f'{v:,.0f}', 14, ink, 'mono', text_anchor='end'),
                  R(16, y + 8, 368, 14, rule + '99', 3), R(16, y + 8, 368 * v / top, 14, col, 3)]
        b += [T(16, 312, '1.28 TFLOPS · 3.32× naive · 24% of cuBLAS', 13, a, font_weight='700')]
    return w, h, b, 'CUDA GEMM on a T4 — naive, custom and cuBLAS',\
        ('Tesla T4, FP32 GEMM at 1024 by 1024, kernel time only. Naive 385.648, custom 1278.508 and cuBLAS 5322.721 GFLOP/s. '
         'Custom reaches 1.28 TFLOPS, 3.32 times naive and 24 percent of cuBLAS. Linear bars with zero origin; historical results.')


def policylens(c, a, m):
    ink, mut, rule, warn = c['ink'], c['muted'], c['rule'], c['warn']
    def meter(x, y, w, name, n, total, col, label_txt):
        gap = 3 if total > 20 else 5
        cw = (w - gap * (total - 1)) / total
        out = [T(x, y, name, 12.5, mut), T(x + w, y, label_txt, 15, col, 'mono', text_anchor='end', font_weight='700')]
        for i in range(total):
            out.append(R(x + i * (cw + gap), y + 9, cw, 16, col if i < n else 'none', 2.5, col if i >= n else None, 1.2))
        return out
    if not m:
        w, h = 960, 250
        b = [label(28, 44, '04 — POLICYLENS AI', a), T(28, 94, 'Finding the passage is not the', 26, ink, 'serif', font_style='italic'), T(28, 126, 'same as answering the question.', 26, ink, 'serif', font_style='italic'),
             T(28, 172, 'Document Q&A with source passages and refusal checks.', 14, mut), T(28, 194, 'Four synthetic documents; refusal calibration reused the', 13, mut), T(28, 213, 'same questions, so these are not held-out results.', 13, mut)]
        mx, mw = 540, 392
        b += meter(mx, 62, mw, 'Expected evidence in the top three', 15, 15, a, '15 / 15') + meter(mx, 124, mw, 'Evaluation cases passed', 24, 31, a, '24 / 31') + meter(mx, 186, mw, 'Partial-evidence cases handled', 0, 3, warn, '0 / 3')
    else:
        w, h = 400, 330
        b = [label(16, 28, '04 — POLICYLENS AI', a), T(16, 62, 'Finding the passage is', 21, ink, 'serif', font_style='italic'), T(16, 88, 'not the same as answering', 21, ink, 'serif', font_style='italic'), T(16, 114, 'the question.', 21, ink, 'serif', font_style='italic')]
        b += meter(16, 158, 368, 'Expected evidence in the top three', 15, 15, a, '15 / 15') + meter(16, 212, 368, 'Evaluation cases passed', 24, 31, a, '24 / 31') + meter(16, 266, 368, 'Partial-evidence cases handled', 0, 3, warn, '0 / 3')
        b += [T(16, 316, 'Synthetic documents · not held-out results', 12, mut)]
    return w, h, b, 'PolicyLens AI — retrieval 15/15, evaluation 24/31, partial evidence 0/3',\
        ('Expected evidence in the top three: 15 of 15. Evaluation cases passed: 24 of 31. Partial-evidence cases: 0 of 3. '
         'Four synthetic documents; refusal calibration used the same questions, so these are not held-out results.')


def orderbook(c, a, m):
    ink, mut, rule = c['ink'], c['muted'], c['rule']
    cols, rows_ = (20, 2) if not m else (10, 4)
    gx, gw = (452, 480) if not m else (16, 368)
    tw = (gw - (cols - 1) * 5) / cols
    th = 26 if not m else 18
    def grid(y):
        return [R(gx + (i % cols) * (tw + 5), y + (i // cols) * (th + 5), tw, th, a, 3) for i in range(40)]
    if not m:
        w, h = 960, 230
        b = [label(28, 44, '05 — JAVA ORDER BOOK', a), T(28, 92, 'Correctness', 32, ink, 'serif', font_weight='700'), T(28, 128, 'before throughput.', 32, ink, 'serif', font_weight='700')]
        ch, _ = chips(28, 152, 410, ['integer ticks', 'FIFO price levels', 'single writer'], ink, rule)
        b += ch + [T(28, 214, 'JMH measures batches and allocations.', 12, mut)]
        b += [label(gx, 44, '60,000 GENERATED COMMANDS', mut)] + grid(62) + [T(gx, 142, 'Each tile is one seed: 1,500 commands replayed against an', 13, ink), T(gx, 162, 'independent list-based model. 40 seeds × 1,500 = 60,000.', 13, ink),
              T(gx, 192, 'A finite regression set, not a proof of correctness.', 12, mut)]
    else:
        w, h = 400, 296
        b = [label(16, 28, '05 — JAVA ORDER BOOK', a), T(16, 64, 'Correctness', 26, ink, 'serif', font_weight='700'), T(16, 94, 'before throughput.', 26, ink, 'serif', font_weight='700'),
             label(16, 122, '40 SEEDS × 1,500 COMMANDS = 60,000', mut)] + grid(134)
        b += [T(16, 252, 'Replayed against an independent list-based model.', 12, ink), T(16, 272, 'Integer ticks · FIFO levels · single writer', 12, mut)]
    return w, h, b, 'Java Order Book — 40 seeds of 1,500 commands, 60,000 in total',\
        ('Forty seeds, each of 1,500 generated commands, are checked against an independent list-based reference model: 60,000 commands in a finite regression set. '
         'Integer ticks, FIFO price levels, single writer; JMH measures batches and allocations.')


def sourced(c, a, m):
    """Product flow and contribution split, taken from the Sourced README's own architecture diagram."""
    ink, mut, rule = c['ink'], c['muted'], c['rule']
    def node(x, y, w, name, sub, mine):
        return [R(x, y, w, 46, a if mine else c['raised'], 9, None if mine else rule),
                T(x + w / 2, y + 20, name, 13, c['bg'] if mine else ink, text_anchor='middle', font_weight='700'),
                T(x + w / 2, y + 36, sub, 12 if m else 10.5, c['bg'] if mine else mut, 'mono', text_anchor='middle', data_keep='1')]
    def arrow(x, y, s='→'):
        return [T(x, y, s, 15, a, text_anchor='middle')]
    def legend(x, y):
        return [R(x, y - 10, 12, 12, a, 3), T(x + 20, y, 'UI I built', 12.5, ink), R(x + 100, y - 10, 12, 12, 'none', 3, mut), T(x + 120, y, 'teammates’ or shared', 12.5, ink)]
    if not m:
        w, h = 960, 236
        b = [label(28, 44, '06 — TEAM PRODUCT', a), T(28, 92, 'Sourced', 34, ink, 'serif', font_weight='700'), T(28, 118, 'BUILD ACROSS Hackathon, Hong Kong.', 14, mut),
             T(28, 168, 'Unknown stays unknown.', 22, ink, 'serif', font_style='italic'), T(28, 192, 'Missing eligibility criteria are never', 13, mut), T(28, 210, 'treated as satisfied.', 13, mut)]
        x0, nw, g = 400, 118, 20
        col = [x0 + i * (nw + g) for i in range(4)]
        b += node(col[1], 40, nw, 'Passport', 'user-confirmed', False) + arrow(col[1] + nw / 2, 100, '↓')
        b += node(col[0], 108, nw, 'Search', 'source-linked', True) + arrow(col[0] + nw + g / 2, 136) + node(col[1], 108, nw, 'Review', 'unknown ≠ met', False) + arrow(col[1] + nw + g / 2, 136) + node(col[2], 108, nw, 'Compare', 'and plan', True)
        b += arrow(col[2] + nw + g / 2, 123) + node(col[3], 84, nw, 'My Journey', 'browser-local', True) + arrow(col[2] + nw + g / 2, 160) + node(col[3], 138, nw, 'Tracker', 'Supabase', False)
        b += legend(400, 218)
    else:
        w, h = 400, 372
        b = [label(16, 28, '06 — TEAM PRODUCT', a), T(16, 64, 'Sourced', 28, ink, 'serif', font_weight='700'), T(16, 88, 'BUILD ACROSS Hackathon, Hong Kong', 13, mut),
             T(16, 128, 'Unknown stays unknown.', 21, ink, 'serif', font_style='italic')]
        nw, g = 112, 16
        col = [16 + i * (nw + g) for i in range(3)]
        y1, y2 = 150, 218
        b += node(col[0], y1, nw, 'Search', 'source-linked', True) + arrow(col[0] + nw + g / 2, y1 + 28) + node(col[1], y1, nw, 'Review', 'unknown ≠ met', False) + arrow(col[1] + nw + g / 2, y1 + 28, '←') + node(col[2], y1, nw, 'Passport', 'user-confirmed', False)
        b += arrow(col[1] + nw / 2, y1 + 62, '↓') + node(col[1], y2, nw, 'Compare', 'and plan', True)
        b += node(col[0], y2, nw, 'Journey', 'browser-local', True) + arrow(col[0] + nw + g / 2, y2 + 28, '←') + arrow(col[1] + nw + g / 2, y2 + 28) + node(col[2], y2, nw, 'Tracker', 'Supabase', False)
        b += legend(16, 292) + [T(16, 322, 'Teammates owned CV extraction, retrieval', 13, mut), T(16, 342, 'and eligibility verification.', 13, mut)]
    return w, h, b, 'Sourced — product flow and who built which part',\
        ('Sourced flow from its README: source-linked search and a user-confirmed Passport feed a review of criteria and unknowns; compare and plan leads to My Journey (browser storage) and a Supabase-backed Tracker. '
         'I built search, comparison, My Journey, Opportunity Brief and affordability-scenario UI; teammates owned CV extraction, retrieval and eligibility verification. Unknown stays unknown.')


PANELS = dict(hero=(hero, 'gridflex'), powercut=(powercut, 'powercut'), cuda=(cuda, 'cuda'), policylens=(policylens, 'policylens'),
              orderbook=(orderbook, 'orderbook'), sourced=(sourced, 'sourced'))

if __name__ == '__main__':
    OUT.mkdir(exist_ok=True)
    for name, (fn, key) in PANELS.items():
        for theme, c in THEMES.items():
            a = ACCENT[key][0 if theme == 'dark' else 1]
            for m in (False, True):
                w, h, body, title, desc = fn(c, a, m)
                if m:  # mobile panels end where content ends; pad evenly
                    pass
                save(f'{name}{"-mobile" if m else ""}-{theme}.svg', w, h, body, title, desc, c, a)
