# ADG Team Suite

One dashboard that connects every Adam Druck Group tool. Team members log in
once and get a launcher of tiles that open each tool in its existing live
location. **The Suite never modifies the underlying tools** — it only links to
them.

## Stack

Node + Express · SQLite (`better-sqlite3`) · bcrypt password hashes ·
30-day JWT sessions · deployed on Railway. Same pattern as Auction Finder /
FlipIQ.

## Editing the tool list

Everything on the dashboard is driven by [`tools.js`](./tools.js). To add,
rename, re-point, or remove a tool, edit that file and redeploy. Each entry's
`url` is the live link the tile opens — fill in any `REPLACE-ME` placeholders
with the real production URLs.

## Environment variables

| Var | Purpose |
| --- | --- |
| `JWT_SECRET` | Signs login sessions. **Set a long random value in production** (`openssl rand -hex 32`). |
| `ADMIN_EMAIL` | The email auto-granted the admin role on signup (Adam). |
| `RAILWAY_VOLUME_MOUNT_PATH` | Set by a Railway volume so the user database survives redeploys. |
| `PORT` | Set automatically by Railway; defaults to 3000 locally. |

## Run locally

```bash
npm install
cp .env.example .env   # then edit values
npm start              # http://localhost:3000
```

## Deploy (Railway)

1. New Railway project → deploy this repo (root = adg-team-suite/ if copied standalone).
2. Add a **Volume**, mount it (e.g. /data); Railway exposes
   `RAILWAY_VOLUME_MOUNT_PATH` so the SQLite DB persists across deploys.
3. Set `JWT_SECRET` and `ADMIN_EMAIL` service variables.
4. The first person to sign up with `ADMIN_EMAIL` becomes the admin.
