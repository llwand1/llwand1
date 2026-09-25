# -*- coding: utf-8 -*-
"""
生成个人主页 README 用的自绘 SVG 资产。

设计约束（有意为之，不是偷懒）：
  1. 零第三方依赖 —— 不用 capsule-render / vercel 系服务，避免国内 DNS 污染导致断图。
  2. 明暗双主题 —— GitHub 支持 <picture> + prefers-color-scheme，输出两份调色板。
  3. 动画只走 SVG 内部 CSS/SMIL —— 在 <img> 上下文里可播，且不引外部字体、不跑脚本。
  4. 字体栈全部回落系统字体 —— SVG 作为图片加载时取不到 webfont。

用法：python tools/gen_assets.py
产出：assets/hero-{dark,light}.svg、assets/milestone-{dark,light}.svg
"""
import os
import xml.etree.ElementTree as ET

HERE = os.path.dirname(os.path.abspath(__file__))
ASSETS = os.path.normpath(os.path.join(HERE, '..', 'assets'))

FONT = ("-apple-system, BlinkMacSystemFont, 'Segoe UI', 'PingFang SC', "
        "'Hiragino Sans GB', 'Microsoft YaHei', 'Noto Sans SC', Roboto, "
        "Helvetica, Arial, sans-serif")
MONO = ("ui-monospace, SFMono-Regular, Menlo, Consolas, 'DejaVu Sans Mono', "
        "monospace")

# ---------------------------------------------------------------- 调色板

PALETTES = {
    'dark': dict(
        bg0='#0b1020', bg1='#141d33', grid='#5b7bd6', grid_op='0.10',
        card='#111a2e', card_stroke='#2b3c60',
        text='#eef3fb', text2='#b9c7e0', muted='#7f93b3',
        a1='#3b82f6', a2='#8a63f6', a3='#22d3ee',
        accent='#6ea8ff', live='#34d399',
        chip_bg='#18233c', chip_stroke='#2c3d61', chip_text='#c3d1ea',
        glow_op='0.30', sweep_op='0.10', ring_op='0.55',
    ),
    'light': dict(
        bg0='#ffffff', bg1='#f1f6fd', grid='#3b6fd4', grid_op='0.11',
        card='#f8fbff', card_stroke='#d7e2f3',
        text='#0d1526', text2='#33415c', muted='#5f7391',
        a1='#007aff', a2='#6d4ae0', a3='#0ea5e9',
        accent='#0057d9', live='#0f9d58',
        chip_bg='#eaf1fb', chip_stroke='#cfdcf0', chip_text='#2a3b57',
        glow_op='0.16', sweep_op='0.07', ring_op='0.40',
    ),
}


def text_w(s, fs):
    """粗略测宽：CJK/箭头按 1.0em，其余按 0.58em。用于排版对齐，不求像素级精确。"""
    w = 0.0
    for ch in s:
        o = ord(ch)
        if 0x2E80 <= o <= 0x9FFF or 0xF900 <= o <= 0xFAFF or 0xFF00 <= o <= 0xFF60 \
                or 0x2190 <= o <= 0x21FF or 0x3000 <= o <= 0x303F or 0x2022 <= o <= 0x2027:
            w += fs * 1.0
        elif ch == ' ':
            w += fs * 0.28
        else:
            w += fs * 0.58
    return w


def esc(s):
    return (s.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
             .replace('"', '&quot;'))


# ---------------------------------------------------------------- 头图

def hero(p, mode):
    W, H = 1000, 272
    gid = f'g-{mode}'

    # ---- 左侧：身份块
    mono_x, mono_y, mono_s = 48, 44, 60
    name_x, name_base, name_fs = 126, 80, 36
    sub_x, sub_base, sub_fs = 128, 102, 14.5
    chips = [('TypeScript', 88), ('Node.js 22+', 95), ('React 18', 75),
             ('SSE', 42), ('SQLite WAL', 88)]
    chip_y, chip_h, chip_gap = 130, 28, 8

    chip_svg, cx = [], 48
    for label, cw in chips:
        chip_svg.append(
            f'<rect x="{cx}" y="{chip_y}" width="{cw}" height="{chip_h}" rx="14" '
            f'fill="{p["chip_bg"]}" stroke="{p["chip_stroke"]}" stroke-width="1"/>'
            f'<text x="{cx + cw / 2}" y="{chip_y + 19}" font-size="12.5" '
            f'fill="{p["chip_text"]}" font-family="{MONO}" text-anchor="middle">{esc(label)}</text>')
        cx += cw + chip_gap

    tagline = '学 → 练 → 析 → 忆 → 反馈'
    tag_fs, tag_base = 19, 200
    tag_x = 48
    caret_x = tag_x + text_w(tagline, tag_fs) + 10

    subline = '本地优先 · 数据自持 · 可自托管'
    sub2_fs, sub2_base = 12.5, 228

    # ---- 右侧：11wand.com 实况卡
    card_x, card_y, card_w, card_h = 640, 44, 312, 188
    inner_x = card_x + 24
    dot_cx, dot_cy = inner_x + 5, card_y + 36

    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" aria-label="llwan · AI 应用与 Node 服务端 · 线上实例 11wand.com">
<title>llwan · AI 应用与 Node 服务端 · 线上实例 11wand.com</title>
<defs>
  <linearGradient id="bg{gid}" x1="0" y1="0" x2="1" y2="1">
    <stop offset="0" stop-color="{p['bg0']}"/>
    <stop offset="1" stop-color="{p['bg1']}"/>
  </linearGradient>
  <linearGradient id="brand{gid}" x1="0" y1="0" x2="1" y2="1">
    <stop offset="0" stop-color="{p['a1']}"/>
    <stop offset="0.5" stop-color="{p['a2']}">
      <animate attributeName="offset" values="0.5;0.86;0.5" dur="7s" repeatCount="indefinite"/>
    </stop>
    <stop offset="1" stop-color="{p['a3']}"/>
  </linearGradient>
  <linearGradient id="sweep{gid}" x1="0" y1="0" x2="1" y2="0">
    <stop offset="0" stop-color="{p['accent']}" stop-opacity="0"/>
    <stop offset="0.5" stop-color="{p['accent']}" stop-opacity="1"/>
    <stop offset="1" stop-color="{p['accent']}" stop-opacity="0"/>
  </linearGradient>
  <radialGradient id="glowA{gid}" cx="0.5" cy="0.5" r="0.5">
    <stop offset="0" stop-color="{p['a1']}" stop-opacity="{p['glow_op']}"/>
    <stop offset="1" stop-color="{p['a1']}" stop-opacity="0"/>
  </radialGradient>
  <radialGradient id="glowB{gid}" cx="0.5" cy="0.5" r="0.5">
    <stop offset="0" stop-color="{p['a2']}" stop-opacity="{p['glow_op']}"/>
    <stop offset="1" stop-color="{p['a2']}" stop-opacity="0"/>
  </radialGradient>
  <pattern id="grid{gid}" width="40" height="40" patternUnits="userSpaceOnUse">
    <path d="M40 0H0V40" fill="none" stroke="{p['grid']}" stroke-width="1"/>
  </pattern>
  <clipPath id="frame{gid}">
    <rect x="1" y="1" width="{W - 2}" height="{H - 2}" rx="17"/>
  </clipPath>
  <clipPath id="cardclip{gid}">
    <rect x="{card_x}" y="{card_y}" width="{card_w}" height="{card_h}" rx="16"/>
  </clipPath>
</defs>

<style>
  .caret-{mode}   {{ animation: blink-{mode} 1.05s steps(1,end) infinite; }}
  .ping-{mode}    {{ transform-box: fill-box; transform-origin: center;
                     animation: ping-{mode} 2.4s cubic-bezier(0,0,.2,1) infinite; }}
  .pulse-{mode}   {{ animation: pulse-{mode} 2.4s ease-in-out infinite; }}
  .sweep-{mode}   {{ animation: sweep-{mode} 5.5s linear infinite; }}
  .ring-{mode}    {{ animation: ring-{mode} 3.2s ease-in-out infinite; }}
  @keyframes blink-{mode}   {{ 0%,55% {{ opacity: 1; }} 56%,100% {{ opacity: 0; }} }}
  @keyframes ping-{mode}    {{ 0% {{ transform: scale(1); opacity: .75; }}
                               70%,100% {{ transform: scale(2.9); opacity: 0; }} }}
  @keyframes pulse-{mode}   {{ 0%,100% {{ opacity: 1; }} 50% {{ opacity: .45; }} }}
  @keyframes sweep-{mode}   {{ 0% {{ transform: translateX(-180px); }}
                               100% {{ transform: translateX(1030px); }} }}
  @keyframes ring-{mode}    {{ 0%,100% {{ stroke-opacity: .28; }}
                               50% {{ stroke-opacity: .85; }} }}
  @media (prefers-reduced-motion: reduce) {{
    .caret-{mode}, .ping-{mode}, .pulse-{mode}, .sweep-{mode}, .ring-{mode} {{ animation: none; }}
  }}
</style>

<g clip-path="url(#frame{gid})">
  <rect width="{W}" height="{H}" fill="url(#bg{gid})"/>
  <rect width="{W}" height="{H}" fill="url(#grid{gid})" opacity="{p['grid_op']}"/>
  <ellipse cx="140" cy="24" rx="330" ry="210" fill="url(#glowA{gid})"/>
  <ellipse cx="890" cy="296" rx="300" ry="180" fill="url(#glowB{gid})"/>
  <!-- 底部扫光 -->
  <rect class="sweep-{mode}" x="0" y="{H - 3}" width="180" height="3"
        fill="url(#sweep{gid})" opacity="{p['sweep_op']}"/>
</g>
<rect x="1" y="1" width="{W - 2}" height="{H - 2}" rx="17" fill="none"
      stroke="{p['card_stroke']}" stroke-width="2"/>

<!-- 归一化：11 标 -->
<rect x="{mono_x}" y="{mono_y}" width="{mono_s}" height="{mono_s}" rx="15" fill="url(#brand{gid})"/>
<text x="{mono_x + mono_s / 2}" y="{mono_y + mono_s / 2 + 11}" font-size="29"
      font-weight="700" font-family="{MONO}" fill="#ffffff" text-anchor="middle"
      letter-spacing="-1">11</text>

<!-- 名称与身份：名字必须用 SANS —— 等宽栈下 llwan 与 11wan 字形完全相同，会读错 -->
<text x="{name_x}" y="{name_base}" font-size="{name_fs}" font-weight="800"
      font-family="{FONT}" fill="{p['text']}" letter-spacing="-0.5">llwan</text>
<text x="{sub_x}" y="{sub_base}" font-size="{sub_fs}" font-family="{FONT}"
      fill="{p['muted']}">AI 应用 &amp; Node 服务端 · 全栈独立开发</text>

{''.join(chip_svg)}

<!-- 闭环口号 -->
<text x="{tag_x}" y="{tag_base}" font-size="{tag_fs}" font-weight="600"
      font-family="{FONT}" fill="{p['text2']}">{esc(tagline)}</text>
<rect class="caret-{mode}" x="{caret_x}" y="{tag_base - 16}" width="3" height="19"
      rx="1.5" fill="{p['accent']}"/>
<text x="{tag_x}" y="{sub2_base}" font-size="{sub2_fs}" font-family="{FONT}"
      fill="{p['muted']}">{esc(subline)}</text>

<!-- 11wand.com 实况卡 -->
<rect class="ring-{mode}" x="{card_x}" y="{card_y}" width="{card_w}" height="{card_h}" rx="16"
      fill="{p['card']}" stroke="{p['a1']}" stroke-width="1.5" stroke-opacity="0.3"/>
<circle class="ping-{mode}" cx="{dot_cx}" cy="{dot_cy}" r="5" fill="none"
        stroke="{p['live']}" stroke-width="2"/>
<circle cx="{dot_cx}" cy="{dot_cy}" r="5" fill="{p['live']}"/>
<text x="{dot_cx + 16}" y="{dot_cy + 5}" font-size="12" font-weight="700"
      font-family="{MONO}" fill="{p['live']}" letter-spacing="1.4">LIVE</text>
<text x="{card_x + card_w - 24}" y="{dot_cy + 5}" font-size="12"
      font-family="{FONT}" fill="{p['muted']}" text-anchor="end">线上实例</text>

<text x="{inner_x}" y="{card_y + 96}" font-size="28" font-weight="800"
      font-family="{MONO}" fill="{p['accent']}" letter-spacing="-0.8">11wand.com</text>
<text x="{inner_x}" y="{card_y + 122}" font-size="12.5" font-family="{FONT}"
      fill="{p['text2']}">StudentBuddy · 以词条为中心的学习助手</text>

<line x1="{inner_x}" y1="{card_y + 140}" x2="{card_x + card_w - 24}" y2="{card_y + 140}"
      stroke="{p['card_stroke']}" stroke-width="1"/>
<text x="{inner_x}" y="{card_y + 164}" font-size="13" font-weight="600"
      font-family="{FONT}" fill="{p['text2']}">免注册，点开就能试 →</text>
<text x="{inner_x}" y="{card_y + 184}" font-size="11" font-family="{MONO}"
      fill="{p['muted']}">Caddy · systemd · SQLite WAL</text>
</svg>
'''


# ---------------------------------------------------------------- 里程碑

MILESTONES = [
    ('2026.03', 'GitHub 起步', '第一个公开仓'),
    ('2026.07', '个人博客上线', 'Hexo · 持续更新'),
    ('2026.07', 'StudentBuddy v1', '学习闭环成型'),
    ('2026.09.05', 'v2 全新重写', '3 包 monorepo'),
    ('2026.09.13', 'AI 编排中心', '多家 AI 协作池'),
    ('2026.09.19', '11wand.com 上线', '多用户 Web 形态'),
    ('2026.09.24', 'v0.2.118 发布', '更新日志页上线'),
]


def milestone(p, mode):
    W, H = 1000, 196
    gid = f'm{mode}'
    x0, x1, y = 92, 908, 100
    step = (x1 - x0) / (len(MILESTONES) - 1)

    nodes = []
    for i, (date, title, sub) in enumerate(MILESTONES):
        cx = x0 + i * step
        hot = (i == 5)          # 11wand.com 上线 —— 唯一的强调节点
        col = p['a1'] if hot else p['muted']
        if hot:
            nodes.append(f'<circle cx="{cx}" cy="{y}" r="14" fill="{p["a1"]}" opacity="0.14"/>')
        nodes.append(
            f'<circle cx="{cx}" cy="{y}" r="{9 if hot else 5.5}" fill="{p["bg0"]}" '
            f'stroke="{col}" stroke-width="2.5"/>')
        if hot:
            nodes.append(f'<circle cx="{cx}" cy="{y}" r="3.5" fill="{p["a1"]}"/>')
        nodes.append(
            f'<text x="{cx}" y="{y - 26}" font-size="12" font-family="{MONO}" '
            f'fill="{p["muted"]}" text-anchor="middle">{date}</text>'
            f'<text x="{cx}" y="{y + 38}" font-size="13" font-weight="{800 if hot else 600}" '
            f'font-family="{FONT}" fill="{p["accent"] if hot else p["text"]}" '
            f'text-anchor="middle">{esc(title)}</text>'
            f'<text x="{cx}" y="{y + 57}" font-size="11" font-family="{FONT}" '
            f'fill="{p["muted"]}" text-anchor="middle">{esc(sub)}</text>')

    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" aria-label="成长时间线：2026.03 GitHub 起步 → 2026.09.19 11wand.com 上线">
<title>成长时间线</title>
<defs>
  <linearGradient id="rail{gid}" x1="0" y1="0" x2="1" y2="0">
    <stop offset="0" stop-color="{p['muted']}" stop-opacity="0.15"/>
    <stop offset="0.18" stop-color="{p['muted']}" stop-opacity="0.55"/>
    <stop offset="0.78" stop-color="{p['a2']}" stop-opacity="0.65"/>
    <stop offset="1" stop-color="{p['a1']}" stop-opacity="0.9"/>
  </linearGradient>
  <linearGradient id="mbg{gid}" x1="0" y1="0" x2="1" y2="1">
    <stop offset="0" stop-color="{p['bg0']}"/>
    <stop offset="1" stop-color="{p['bg1']}"/>
  </linearGradient>
  <clipPath id="mframe{gid}"><rect x="1" y="1" width="{W - 2}" height="{H - 2}" rx="16"/></clipPath>
</defs>
<g clip-path="url(#mframe{gid})">
  <rect width="{W}" height="{H}" fill="url(#mbg{gid})"/>
</g>
<rect x="1" y="1" width="{W - 2}" height="{H - 2}" rx="16" fill="none"
      stroke="{p['card_stroke']}" stroke-width="1.5"/>
<line x1="{x0 - 22}" y1="{y}" x2="{x1 + 22}" y2="{y}"
      stroke="url(#rail{gid})" stroke-width="2.5" stroke-linecap="round"/>
{''.join(nodes)}
</svg>
'''


def main():
    os.makedirs(ASSETS, exist_ok=True)
    written = []
    for mode, pal in PALETTES.items():
        for name, fn in (('hero', hero), ('milestone', milestone)):
            svg = fn(pal, mode)
            ET.fromstring(svg)                      # XML 合法性自检，畸形就当场炸
            path = os.path.join(ASSETS, f'{name}-{mode}.svg')
            with open(path, 'w', encoding='utf-8', newline='\n') as f:
                f.write(svg)
            written.append((path, len(svg.encode("utf-8"))))
    for path, size in written:
        print(f'OK  {os.path.relpath(path, os.path.dirname(ASSETS))}  {size} bytes')


if __name__ == '__main__':
    main()
