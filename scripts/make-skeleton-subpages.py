#!/usr/bin/env python3
"""Create skeleton subpage HTML, images folder, and .gitkeep for each subpage."""
import os

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# (parent_folder, subfolder, page_title, parent_display_name)
# parent_display_name is used in "Back to X" and "Part of X"
PAGES = [
    # Drivetrain
    ("Drivetrain", "motor-and-reducer", "Motor and reducer", "Drivetrain"),
    ("Drivetrain", "gears-and-cam-bearings", "Gears and cam bearings", "Drivetrain"),
    ("Drivetrain", "drivetrain-mount-plate", "Drivetrain mount plate", "Drivetrain"),
    # Transmission
    ("Transmission", "transmission-mount-plate", "Transmission mount plate", "Transmission system"),
    ("Transmission", "drive-shafts", "Drive shafts", "Transmission system"),
    ("Transmission", "yoke", "Yoke", "Transmission system"),
    # Extraction-syncronisation
    ("Extraction-syncronisation", "peelers", "Peelers", "Extraction & synchronisation"),
    ("Extraction-syncronisation", "driven-bracket", "Driven bracket", "Extraction & synchronisation"),
    # Collection
    ("Collection", "juice-collection", "Juice collection", "Collection"),
    ("Collection", "plungers-and-filter", "Plungers and filter", "Collection"),
    # Feeder
    ("Feeder", "feeder-body", "Feeder body", "Fruit intake system"),
    ("Feeder", "entry-tubes", "Entry tubes", "Fruit intake system"),
    # Plug-ejection
    ("Plug-ejection", "plunger-drive-bracket", "Plunger drive bracket", "Core ejection"),
    ("Plug-ejection", "plunger-drive-system-in-side-panels", "Plunger drive system in side panels", "Core ejection"),
    # Outflow-disposal
    ("Outflow-disposal", "chutes-and-augers", "Chutes and augers", "Disposal system"),
    ("Outflow-disposal", "deflectors", "Deflectors", "Disposal system"),
    # Enclosure-shell
    ("Enclosure-shell", "protective-covers", "Protective covers (plunger, drivetrain)", "Enclosure / shell"),
    ("Enclosure-shell", "overcentered-hinges", "Overcentered hinges", "Enclosure / shell"),
    # Clean-in-place
    ("Clean-in-place", "cip-nozzles-and-feed-pipes", "CIP nozzles and feed pipes", "Clean-in-place (CIP)"),
    ("Clean-in-place", "third-party-cip-control-equipment", "Third-party CIP control equipment", "Clean-in-place (CIP)"),
    # Controls-Electronics
    ("Controls-Electronics", "machine-control-definition-and-ui", "Machine control definition and UI", "Controls and electronics"),
    ("Controls-Electronics", "motor-power-management", "Motor power management", "Controls and electronics"),
    ("Controls-Electronics", "yoke-position-sensor", "Yoke position sensor", "Controls and electronics"),
]

SKELETON = '''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{page_title} — {parent_short} — P6 RFP</title>
  <style>
    :root {{ --bg: #1a1d21; --text: #e6edf3; --muted: #8b949e; --accent: #58a6ff; --border: #30363d; }}
    body {{ font-family: system-ui, sans-serif; background: var(--bg); color: var(--text); line-height: 1.6; margin: 0; padding: 1.5rem; max-width: 52rem; margin-left: auto; margin-right: auto; }}
    a {{ color: var(--accent); }}
    h1 {{ font-size: 1.35rem; }}
    h2 {{ font-size: 1.1rem; margin-top: 1.25rem; }}
    h3 {{ font-size: 1rem; margin-top: 1rem; color: var(--muted); }}
    ul, ol {{ padding-left: 1.25rem; }}
    .back {{ margin-bottom: 1rem; font-size: 0.9rem; }}
    .muted {{ color: var(--muted); font-size: 0.9rem; }}
    .swatch {{ display: inline-block; width: 1.25rem; height: 1.25rem; border: 1px solid var(--border); border-radius: 3px; vertical-align: middle; }}
    table {{ border-collapse: collapse; width: 100%; font-size: 0.9rem; }}
    th, td {{ text-align: left; padding: 0.4rem 0.5rem; border-bottom: 1px solid var(--border); }}
    .iface-table th {{ color: var(--muted); font-weight: 600; }}
    .slideshow {{ margin: 1.5rem 0; }}
    .slideshow .slide {{ display: none; }}
    .slideshow .slide.active {{ display: block; }}
    .slideshow .slide img {{ max-width: 100%; height: auto; border: 1px solid var(--border); display: block; }}
    .slideshow-caption {{ margin-top: 0.5rem; font-size: 0.9rem; color: var(--muted); min-height: 2.5em; }}
    .slideshow-controls {{ display: flex; align-items: center; gap: 1rem; margin-top: 0.75rem; flex-wrap: wrap; }}
    .slideshow-controls button {{ background: var(--border); color: var(--text); border: none; padding: 0.35rem 0.75rem; border-radius: 4px; cursor: pointer; font-size: 0.9rem; }}
    .slideshow-controls button:hover {{ background: var(--accent); color: #fff; }}
    .slideshow-counter {{ font-size: 0.85rem; color: var(--muted); }}
  </style>
</head>
<body>
  <p class="back"><a href="../index.html">← Back to {parent_display}</a> · <a href="../../index.html">P6 RFP overview</a></p>
  <h1>{h1_title}</h1>
  <p class="muted">Part of the <a href="../index.html">{parent_display}</a> section. <em>Fill in one-line description.</em></p>

  <h2>Introduction</h2>
  <p><em>Fill in: purpose of this subassembly, how it fits in the subsystem, key specs or design intent.</em></p>

  <h2>Colour key &amp; components</h2>
  <p class="muted">CAD colours for this subpage. Add rows for each coloured component with purpose/spec.</p>
  <table>
    <tr><th>Colour(s)</th><th>Component</th></tr>
    <tr><td><em>—</em></td><td><em>Add colour swatches and component names/descriptions.</em></td></tr>
  </table>

  <h2 id="gallery">Figures</h2>
  <p class="muted">Add CAD views to the <code>images/</code> folder and reference them below. Refer to <a href="#fig1">Figure 1</a>, etc.</p>
  <div class="slideshow" id="skel-slideshow">
    <div class="slideshow-track">
      <div class="slide active" id="fig1" data-caption="Figure 1. (Add caption.)"><img src="images/fig1.png" alt="Figure 1"></div>
    </div>
    <p class="slideshow-caption" id="skel-caption" aria-live="polite">Figure 1. (Add caption.)</p>
    <div class="slideshow-controls">
      <button type="button" id="skel-prev" aria-label="Previous">← Previous</button>
      <span class="slideshow-counter" id="skel-counter">1 / 1</span>
      <button type="button" id="skel-next" aria-label="Next">Next →</button>
    </div>
  </div>

  <h2>Discussion</h2>
  <h3>Components</h3>
  <ul>
    <li><em>List main components and their role; expand as needed.</em></li>
  </ul>
  <h3>Interfaces</h3>
  <ul>
    <li><strong>Input:</strong> <em>…</em></li>
    <li><strong>Output:</strong> <em>…</em></li>
    <li><strong>Mount:</strong> <em>…</em></li>
  </ul>
  <h3>Interfaces and tolerances</h3>
  <p class="muted">Known interfaces and tolerances. Links go to related subsystems.</p>
  <table class="iface-table">
    <thead><tr><th>Part</th><th>Interface / tolerance</th><th>Related</th></tr></thead>
    <tbody>
      <tr><td><em>—</em></td><td><em>Add rows.</em></td><td>—</td></tr>
    </tbody>
  </table>

  <p class="back"><a href="../index.html">← Back to {parent_display}</a></p>
  <script>
(function(){{
  var el = document.getElementById('skel-slideshow');
  if (!el) return;
  var slides = el.querySelectorAll('.slide');
  var cap = document.getElementById('skel-caption');
  var counter = document.getElementById('skel-counter');
  var n = slides.length, i = 0;
  function go(k) {{ i = (k + n) % n; slides.forEach(function(s,j){{ s.classList.toggle('active', j===i); }}); if (cap) cap.textContent = slides[i].getAttribute('data-caption') || ''; if (counter) counter.textContent = (i+1) + ' / ' + n; }}
  el.querySelector('#skel-prev').addEventListener('click', function(){{ go(i-1); }});
  el.querySelector('#skel-next').addEventListener('click', function(){{ go(i+1); }});
  var hash = window.location.hash;
  if (hash && hash.match(/^#fig(\\d+)$/)) {{ var idx = parseInt(RegExp.$1, 10) - 1; if (idx >= 0 && idx < n) {{ i = idx; go(i); }} }}
}})();
  </script>
</body>
</html>
'''

def parent_short(parent_display):
    m = {
        "Drivetrain": "Drivetrain",
        "Transmission system": "Transmission",
        "Extraction & synchronisation": "Extraction & synchronisation",
        "Collection": "Collection",
        "Fruit intake system": "Feeder",
        "Core ejection": "Core ejection",
        "Disposal system": "Disposal",
        "Enclosure / shell": "Enclosure",
        "Clean-in-place (CIP)": "CIP",
        "Controls and electronics": "Controls",
    }
    return m.get(parent_display, parent_display)

def main():
    for parent_folder, subfolder, page_title, parent_display in PAGES:
        parent_short_name = parent_short(parent_display)
        dir_path = os.path.join(BASE, parent_folder, subfolder)
        images_path = os.path.join(dir_path, "images")
        os.makedirs(images_path, exist_ok=True)
        with open(os.path.join(images_path, ".gitkeep"), "w") as f:
            f.write("")
        html = SKELETON.format(
            page_title=page_title,
            parent_short=parent_short_name,
            parent_display=parent_display,
            h1_title=page_title,
        )
        # Use unique slideshow ids per page to avoid duplicate IDs when multiple skeletons on same parent
        sid = subfolder.replace("-", "")[:20]
        html = html.replace("skel-slideshow", f"skel-{sid}-slideshow")
        html = html.replace("skel-caption", f"skel-{sid}-caption")
        html = html.replace("skel-counter", f"skel-{sid}-counter")
        html = html.replace("skel-prev", f"skel-{sid}-prev")
        html = html.replace("skel-next", f"skel-{sid}-next")
        html = html.replace("#skel-prev", f"#skel-{sid}-prev")
        html = html.replace("#skel-next", f"#skel-{sid}-next")
        html = html.replace("getElementById('skel-slideshow')", f"getElementById('skel-{sid}-slideshow')")
        index_path = os.path.join(dir_path, "index.html")
        with open(index_path, "w") as f:
            f.write(html)
        print(index_path)

if __name__ == "__main__":
    main()
