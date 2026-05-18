const express = require('express');
const path = require('path');
const { router: authRouter, requireAuth } = require('./auth');
const { TOOLS } = require('./tools');

const app = express();
const PORT = process.env.PORT || 3000;

app.use(express.json({ limit: '64kb' }));

// Auth routes
app.use(authRouter);

// Tools list — only visible to logged-in team members.
app.get('/api/tools', requireAuth, (req, res) => {
  res.json({ tools: TOOLS });
});

// Auth pages served without the .html extension, before the static handler.
app.get(['/login', '/login.html'], (req, res) => {
  res.sendFile(path.join(__dirname, 'public', 'login.html'));
});
app.get(['/signup', '/signup.html'], (req, res) => {
  res.sendFile(path.join(__dirname, 'public', 'signup.html'));
});

app.use(express.static(path.join(__dirname, 'public')));

app.get('*', (req, res) => {
  res.sendFile(path.join(__dirname, 'public', 'index.html'));
});

app.listen(PORT, () => {
  console.log(`ADG Team Suite running on port ${PORT}`);
});
