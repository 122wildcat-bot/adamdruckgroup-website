(async function () {
  const token = localStorage.getItem('adg_token');
  if (!token) { location.href = '/login'; return; }

  const authHeader = { Authorization: 'Bearer ' + token };

  function signOut() {
    localStorage.removeItem('adg_token');
    location.href = '/login';
  }

  // Verify session.
  let me;
  try {
    const res = await fetch('/api/auth/me', { headers: authHeader });
    if (!res.ok) return signOut();
    me = (await res.json()).user;
  } catch (e) {
    return signOut();
  }

  const userbox = document.getElementById('userbox');
  userbox.hidden = false;
  document.getElementById('who').textContent = me.name || me.email;
  if (me.role === 'admin') document.getElementById('adminBadge').hidden = false;
  document.getElementById('logout').addEventListener('click', signOut);

  // Load tools.
  let tools = [];
  try {
    const res = await fetch('/api/tools', { headers: authHeader });
    if (!res.ok) return signOut();
    tools = (await res.json()).tools;
  } catch (e) {
    return signOut();
  }

  const catalog = document.getElementById('catalog');
  const order = [];
  const byCat = {};
  for (const t of tools) {
    const c = t.category || 'Tools';
    if (!byCat[c]) { byCat[c] = []; order.push(c); }
    byCat[c].push(t);
  }

  for (const cat of order) {
    const section = document.createElement('section');
    section.className = 'cat';
    const h2 = document.createElement('h2');
    h2.textContent = cat;
    section.appendChild(h2);

    const grid = document.createElement('div');
    grid.className = 'grid';
    for (const t of byCat[cat]) {
      const a = document.createElement('a');
      a.className = 'tile';
      a.href = t.url;
      a.target = '_blank';
      a.rel = 'noopener noreferrer';

      const dot = document.createElement('div');
      dot.className = 'dot';
      dot.style.background = t.accent || '#0f2a43';

      const h3 = document.createElement('h3');
      h3.textContent = t.name;

      const p = document.createElement('p');
      p.textContent = t.description || '';

      const open = document.createElement('span');
      open.className = 'open';
      open.textContent = 'Open →';

      a.append(dot, h3, p, open);
      grid.appendChild(a);
    }
    section.appendChild(grid);
    catalog.appendChild(section);
  }
})();
