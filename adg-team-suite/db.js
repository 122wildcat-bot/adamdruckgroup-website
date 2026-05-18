// SQLite storage for ADG Team Suite users.
// On Railway the DB lives at the mounted volume so it survives redeploys
// (set RAILWAY_VOLUME_MOUNT_PATH to a volume, e.g. /data). Locally it falls
// back to ./data/suite.db.
const Database = require('better-sqlite3');
const path = require('path');
const fs = require('fs');

const DB_DIR = process.env.RAILWAY_VOLUME_MOUNT_PATH || path.join(__dirname, 'data');
fs.mkdirSync(DB_DIR, { recursive: true });
const DB_PATH = path.join(DB_DIR, 'suite.db');

const db = new Database(DB_PATH);
db.pragma('journal_mode = WAL');

db.exec(`
  CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    email TEXT UNIQUE NOT NULL,
    password_hash TEXT NOT NULL,
    name TEXT,
    role TEXT DEFAULT 'user',
    created_at TEXT DEFAULT CURRENT_TIMESTAMP
  );
`);

const _createUser = db.prepare(
  'INSERT INTO users (email, password_hash, name, role) VALUES (?, ?, ?, ?)'
);
const _getUserByEmail = db.prepare('SELECT * FROM users WHERE lower(email) = lower(?)');
const _getUserById = db.prepare('SELECT * FROM users WHERE id = ?');
const _listUsers = db.prepare(
  'SELECT id, email, name, role, created_at FROM users ORDER BY created_at ASC'
);

function createUser({ email, passwordHash, name, role = 'user' }) {
  const info = _createUser.run(email, passwordHash, name || null, role);
  return _getUserById.get(info.lastInsertRowid);
}
function getUserByEmail(email) { return _getUserByEmail.get(email); }
function getUserById(id) { return _getUserById.get(id); }
function listUsers() { return _listUsers.all(); }

module.exports = {
  db,
  createUser, getUserByEmail, getUserById, listUsers,
};
