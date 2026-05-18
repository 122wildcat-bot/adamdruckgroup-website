// Express router for authentication.
// Mirrors the ADG / FlipIQ auth pattern: bcrypt password hashes + 30-day JWTs.
// Open signup; the ADMIN_EMAIL account is auto-granted the admin role.
const express = require('express');
const bcrypt = require('bcryptjs');
const jwt = require('jsonwebtoken');
const { createUser, getUserByEmail, getUserById, listUsers } = require('./db');

const router = express.Router();

const JWT_SECRET = process.env.JWT_SECRET || 'adg-suite-dev-secret-change-in-prod';
const ADMIN_EMAIL = (process.env.ADMIN_EMAIL || 'yourrealtoradamd@gmail.com').toLowerCase();

function safeUser(u) {
  if (!u) return null;
  return { id: u.id, email: u.email, name: u.name, role: u.role };
}

function requireAuth(req, res, next) {
  const token = (req.headers.authorization || '').replace(/^Bearer\s+/i, '');
  if (!token) return res.status(401).json({ error: 'Not authenticated' });
  try {
    const payload = jwt.verify(token, JWT_SECRET);
    req.userId = payload.userId;
    next();
  } catch (e) {
    res.status(401).json({ error: 'Invalid or expired session' });
  }
}

function requireAdmin(req, res, next) {
  const user = getUserById(req.userId);
  if (!user || user.role !== 'admin') {
    return res.status(403).json({ error: 'Admin access required' });
  }
  next();
}

// ── SIGN UP ──────────────────────────────────────────────────────────────────
router.post('/api/auth/signup', async (req, res) => {
  const { email, password, name } = req.body || {};
  if (!email || !password) return res.status(400).json({ error: 'Email and password are required' });
  if (password.length < 8) return res.status(400).json({ error: 'Password must be at least 8 characters' });
  if (getUserByEmail(email)) return res.status(409).json({ error: 'An account with this email already exists' });

  const passwordHash = await bcrypt.hash(password, 12);
  const isAdmin = String(email).toLowerCase() === ADMIN_EMAIL;
  const user = createUser({
    email, passwordHash, name: name || String(email).split('@')[0],
    role: isAdmin ? 'admin' : 'user',
  });
  const token = jwt.sign({ userId: user.id }, JWT_SECRET, { expiresIn: '30d' });
  res.json({ token, user: safeUser(user) });
});

// ── LOG IN ───────────────────────────────────────────────────────────────────
router.post('/api/auth/login', async (req, res) => {
  const { email, password } = req.body || {};
  const user = getUserByEmail(email || '');
  if (!user) return res.status(401).json({ error: 'Invalid email or password' });
  const ok = await bcrypt.compare(password || '', user.password_hash);
  if (!ok) return res.status(401).json({ error: 'Invalid email or password' });
  const token = jwt.sign({ userId: user.id }, JWT_SECRET, { expiresIn: '30d' });
  res.json({ token, user: safeUser(user) });
});

// ── ME ───────────────────────────────────────────────────────────────────────
router.get('/api/auth/me', requireAuth, (req, res) => {
  const user = getUserById(req.userId);
  if (!user) return res.status(404).json({ error: 'User not found' });
  res.json({ user: safeUser(user) });
});

// ── ADMIN: list team members ─────────────────────────────────────────────────
router.get('/api/admin/users', requireAuth, requireAdmin, (req, res) => {
  res.json({ users: listUsers() });
});

module.exports = { router, requireAuth, requireAdmin };
