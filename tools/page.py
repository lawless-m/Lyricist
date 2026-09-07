"""The catalogue as one HTML page: a track list with mp4 download links.

Imported by db.py for its `page` subcommand. Kept separate because it is mostly
a lump of markup, and burying that in the middle of the database code would hide
both.

Published clips only, deliberately. cdn1.suno.ai serves an mp4 for anything
public and 403s everything else — ten of each checked, no exceptions — and the
published route is the one that neither spends the download allowance nor looks
like scraping. An unpublished row therefore gets no link at all rather than a
fallback down some other path. Those rows still earn their place in the list:
they are what to publish next, which is also what the band rail counts.

The links point at Suno's own CDN and nothing is proxied, so Save As names the
file by GUID. That is Suno's name for it, and renaming is the price of not
standing up a server to rewrite a header.

One template, two wrappers. A published Artifact supplies its own document
shell, so `render` emits no doctype or <head>; `wrap` adds the few lines a
browser wants before it will read the same markup out of a local file in
standards mode.
"""

import html
import json

LOCAL_PREFIX = """<!doctype html>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
"""

TEMPLATE = r'''<title>Lyricist Catalogue</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,500;9..144,600&family=IBM+Plex+Mono:wght@400;500&family=IBM+Plex+Sans:wght@400;500;600&display=swap">
<style>
:root {
  --paper:  #E9ECE7;
  --card:   #FBFCF9;
  --ink:    #191E1B;
  --dim:    #667069;
  --line:   #D2D8D0;
  --live:   #2B6A55;
  --rust:   #9A5330;
  --shade:  rgba(25,30,27,.05);
}
@media (prefers-color-scheme: dark) {
  :root:not([data-theme="light"]) {
    --paper:  #131714;
    --card:   #1A201C;
    --ink:    #E3E9E4;
    --dim:    #87948C;
    --line:   #2A322D;
    --live:   #6CBE99;
    --rust:   #D28C61;
    --shade:  rgba(255,255,255,.04);
  }
}
:root[data-theme="dark"] {
  --paper:  #131714;
  --card:   #1A201C;
  --ink:    #E3E9E4;
  --dim:    #87948C;
  --line:   #2A322D;
  --live:   #6CBE99;
  --rust:   #D28C61;
  --shade:  rgba(255,255,255,.04);
}

* { box-sizing: border-box; }
body {
  margin: 0; background: var(--paper); color: var(--ink);
  font-family: "IBM Plex Sans", ui-sans-serif, system-ui, sans-serif;
  font-size: 14px; line-height: 1.45;
  -webkit-font-smoothing: antialiased;
}
.shell { max-width: 1180px; margin: 0 auto; padding: 0 20px 64px; }

/* --- masthead --- */
.mast { padding: 34px 0 20px; border-bottom: 2px solid var(--ink); }
.mast h1 {
  font-family: Fraunces, Georgia, serif; font-weight: 600;
  font-size: clamp(28px, 4.5vw, 40px); margin: 0; letter-spacing: -.015em;
  text-wrap: balance;
}
.mast h1 em { font-style: normal; color: var(--rust); }
.mast p { margin: 8px 0 0; color: var(--dim); max-width: 62ch; }
.tallies {
  display: flex; flex-wrap: wrap; gap: 6px 26px; margin: 18px 0 0;
  font-family: "IBM Plex Mono", ui-monospace, monospace; font-size: 12.5px;
  color: var(--dim); font-variant-numeric: tabular-nums;
}
.tallies b { color: var(--ink); font-weight: 500; }

/* --- band rail --- */
.rail {
  display: flex; flex-wrap: wrap; gap: 7px;
  padding: 18px 0 16px; border-bottom: 1px solid var(--line);
}
.chip {
  font: inherit; font-size: 12.5px; cursor: pointer;
  background: transparent; color: var(--dim);
  border: 1px solid var(--line); border-radius: 2px;
  padding: 4px 9px; display: inline-flex; align-items: baseline; gap: 7px;
}
.chip:hover { color: var(--ink); border-color: var(--dim); }
.chip[aria-pressed="true"] { background: var(--ink); border-color: var(--ink); color: var(--paper); }
.chip[aria-pressed="true"] .frac b { color: var(--paper); }
.chip .frac {
  font-family: "IBM Plex Mono", ui-monospace, monospace;
  font-variant-numeric: tabular-nums; font-size: 11.5px; opacity: .8;
}
.chip .frac b { color: var(--live); font-weight: 500; }

/* --- controls --- */
.bar {
  position: sticky; top: 0; z-index: 5; background: var(--paper);
  display: flex; gap: 12px; align-items: center; flex-wrap: wrap;
  padding: 14px 0 13px; border-bottom: 1px solid var(--line);
}
input[type="search"] {
  flex: 1 1 250px; min-width: 190px; font: inherit;
  background: var(--card); color: var(--ink);
  border: 1px solid var(--line); border-radius: 2px; padding: 7px 10px;
}
input[type="search"]::placeholder { color: var(--dim); }
.toggle { display: flex; align-items: center; gap: 7px; cursor: pointer;
          color: var(--dim); user-select: none; white-space: nowrap; }
.toggle input { accent-color: var(--live); width: 15px; height: 15px; }
.toggle:hover { color: var(--ink); }
#count {
  margin-left: auto; color: var(--dim); white-space: nowrap;
  font-family: "IBM Plex Mono", ui-monospace, monospace; font-size: 12.5px;
  font-variant-numeric: tabular-nums;
}
:focus-visible { outline: 2px solid var(--rust); outline-offset: 2px; }

/* --- table --- */
.scroll { overflow-x: auto; }
table { border-collapse: collapse; width: 100%; min-width: 800px; }
thead th {
  position: sticky; top: 56px; z-index: 4; background: var(--paper);
  text-align: left; font-weight: 500; font-size: 11px;
  letter-spacing: .09em; text-transform: uppercase; color: var(--dim);
  padding: 12px 12px 9px; border-bottom: 1px solid var(--line);
  cursor: pointer; white-space: nowrap;
}
thead th:hover { color: var(--ink); }
thead th[aria-sort="ascending"]::after  { content: " \2191"; color: var(--rust); }
thead th[aria-sort="descending"]::after { content: " \2193"; color: var(--rust); }
thead th.plain { cursor: default; }
thead th.plain:hover { color: var(--dim); }
tbody td { padding: 9px 12px; border-bottom: 1px solid var(--line); white-space: nowrap; }
tbody tr:hover { background: var(--shade); }
td.song { white-space: normal; min-width: 190px; font-weight: 500; }
td.song small {
  display: block; font-weight: 400; color: var(--dim);
  font-family: "IBM Plex Mono", ui-monospace, monospace; font-size: 11px;
}
td.meta { color: var(--dim); }
td.num  { text-align: right; font-variant-numeric: tabular-nums;
          font-family: "IBM Plex Mono", ui-monospace, monospace; color: var(--dim); }
td.when { font-family: "IBM Plex Mono", ui-monospace, monospace;
          font-size: 12.5px; color: var(--dim); }

/* state is carried by form as well as colour, so it reads at a glance */
.get {
  display: inline-flex; align-items: center; gap: 6px; text-decoration: none;
  color: var(--live); font-weight: 500; border-bottom: 1px solid transparent;
}
.get::before {
  content: ""; width: 6px; height: 6px; border-radius: 50%;
  background: var(--live); flex: none;
}
.get:hover { border-bottom-color: var(--live); }
.held { color: var(--dim); display: inline-flex; align-items: center; gap: 6px; }
.held::before {
  content: ""; width: 6px; height: 6px; border-radius: 50%; flex: none;
  border: 1px solid var(--dim);
}
a.ext { color: var(--dim); text-decoration: none; }
a.ext:hover { color: var(--rust); }

#empty { padding: 48px 4px; color: var(--dim); }
footer {
  margin-top: 26px; padding-top: 18px; border-top: 1px solid var(--line);
  color: var(--dim); font-size: 12.5px; max-width: 68ch;
}
footer code { font-family: "IBM Plex Mono", ui-monospace, monospace;
              font-size: 12px; color: var(--ink); }
@media (prefers-reduced-motion: reduce) { * { transition: none !important; } }
</style>

<div class="shell">
  <div class="mast">
    <h1>Lyricist <em>Catalogue</em></h1>
    <p>Every clip Suno still holds, across __BANDCOUNT__ bands. The published ones
       carry an mp4 you can right-click and save; the rest are the list of what to
       publish next.</p>
    <div class="tallies">
      <span><b>__TOTAL__</b> clips</span>
      <span><b>__PUBLISHED__</b> published</span>
      <span><b>__PLAYS__</b> plays</span>
      <span>synced __WHEN__</span>
    </div>
  </div>

  <div class="rail" id="rail">__RAIL__</div>

  <div class="bar">
    <input type="search" id="q" placeholder="Search title, band, project or slug">
    <label class="toggle"><input type="checkbox" id="pub" checked> Published only</label>
    <span id="count"></span>
  </div>

  <div class="scroll">
    <table>
      <thead><tr>
        <th data-key="title" scope="col">Song</th>
        <th data-key="band" scope="col">Band</th>
        <th data-key="project" scope="col">Project</th>
        <th data-key="created_at" scope="col">Made</th>
        <th data-key="plays" scope="col">Plays</th>
        <th data-key="likes" scope="col">Likes</th>
        <th data-key="is_public" scope="col">Download</th>
        <th class="plain" scope="col">Suno</th>
      </tr></thead>
      <tbody id="body"></tbody>
    </table>
  </div>
  <p id="empty" hidden>Nothing matches that.</p>

  <footer>
    A snapshot taken __WHEN__ from <code>lyricist.db</code>, generated by
    <code>tools/db.py</code>. Download links go straight to Suno's CDN, so a saved
    file is named by its clip id rather than its title. Only published clips have
    one — <code>cdn1.suno.ai</code> returns 403 for everything else.
  </footer>
</div>

<script>
const CLIPS = __DATA__;
const body = document.getElementById('body');
const q = document.getElementById('q');
const pub = document.getElementById('pub');
const count = document.getElementById('count');
const empty = document.getElementById('empty');
const rail = document.getElementById('rail');
let sortKey = 'created_at', desc = true, band = '';

const esc = s => (s ?? '').toString()
  .replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;')
  .replace(/"/g, '&quot;');
const nf = new Intl.NumberFormat('en-GB');

function matching() {
  const needle = q.value.trim().toLowerCase();
  return CLIPS.filter(c => {
    if (pub.checked && !c.is_public) return false;
    if (band && (c.band || 'unfiled') !== band) return false;
    if (!needle) return true;
    return [c.title, c.band, c.project, c.slug].join(' ').toLowerCase().includes(needle);
  });
}

function draw() {
  const list = matching().slice().sort((a, b) => {
    let x = a[sortKey], y = b[sortKey];
    if (sortKey === 'plays' || sortKey === 'likes' || sortKey === 'is_public') {
      x = x ?? -1; y = y ?? -1;
    } else {
      x = (x ?? '').toString().toLowerCase(); y = (y ?? '').toString().toLowerCase();
    }
    return (x < y ? -1 : x > y ? 1 : 0) * (desc ? -1 : 1);
  });

  body.innerHTML = list.map(c => `<tr>
    <td class="song">${esc(c.title) || 'Untitled'}${c.slug ? `<small>${esc(c.slug)}</small>` : ''}</td>
    <td class="meta">${esc(c.band) || '—'}</td>
    <td class="meta">${esc(c.project) || '—'}</td>
    <td class="when">${(c.created_at || '').slice(0, 10)}</td>
    <td class="num">${c.plays == null ? '' : nf.format(c.plays)}</td>
    <td class="num">${c.likes == null ? '' : nf.format(c.likes)}</td>
    <td>${c.is_public
      ? `<a class="get" href="https://cdn1.suno.ai/${c.id}.mp4">mp4</a>`
      : `<span class="held">not published</span>`}</td>
    <td><a class="ext" href="https://suno.com/song/${c.id}" target="_blank" rel="noopener">open &#8599;</a></td>
  </tr>`).join('');

  const n = list.filter(c => c.is_public).length;
  count.textContent = `${nf.format(list.length)} shown · ${nf.format(n)} downloadable`;
  empty.hidden = list.length > 0;
}

document.querySelectorAll('th[data-key]').forEach(th => {
  th.addEventListener('click', () => {
    const k = th.dataset.key;
    if (k === sortKey) desc = !desc;
    else { sortKey = k; desc = ['created_at', 'plays', 'likes', 'is_public'].includes(k); }
    document.querySelectorAll('th').forEach(o => o.removeAttribute('aria-sort'));
    th.setAttribute('aria-sort', desc ? 'descending' : 'ascending');
    draw();
  });
});

rail.addEventListener('click', e => {
  const chip = e.target.closest('.chip');
  if (!chip) return;
  band = (band === chip.dataset.band) ? '' : chip.dataset.band;
  rail.querySelectorAll('.chip').forEach(c =>
    c.setAttribute('aria-pressed', String(c.dataset.band === band)));
  draw();
});

q.addEventListener('input', draw);
pub.addEventListener('change', draw);
document.querySelector('th[data-key="created_at"]').setAttribute('aria-sort', 'descending');
rail.querySelectorAll('.chip').forEach(c => c.setAttribute('aria-pressed', 'false'));
draw();
</script>
'''


def wrap(markup):
    """The same page, made a standalone document for file:// viewing."""
    return LOCAL_PREFIX + markup


def render(clips, bands, generated, published, plays):
    """`bands` is [(name, total, published)], widest catalogue first."""
    # A title holding "</script>" would otherwise close the block it sits in.
    # Escaping the slash keeps the JSON valid and the parser inside the tag.
    data = json.dumps(clips, separators=(",", ":")).replace("</", "<\\/")
    rail = "".join(
        f'<button class="chip" data-band="{html.escape(b, quote=True)}">'
        f'{html.escape(b)}<span class="frac"><b>{p}</b>/{t}</span></button>'
        for b, t, p in bands)
    return (TEMPLATE
            .replace("__DATA__", data)
            .replace("__RAIL__", rail)
            .replace("__BANDCOUNT__", str(len(bands)))
            .replace("__TOTAL__", f"{len(clips):,}")
            .replace("__PUBLISHED__", f"{published:,}")
            .replace("__PLAYS__", f"{plays:,}")
            .replace("__WHEN__", generated))
