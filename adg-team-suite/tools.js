// ─────────────────────────────────────────────────────────────────────────────
// ADG Team Suite — the one place to edit your tools.
//
// This list drives every tile on the dashboard. To add, remove, rename, or
// re-point a tool, just edit this array and redeploy. The Suite NEVER modifies
// the tools themselves — each tile simply opens the tool at its `url`.
//
// `url`: the LIVE production link for that tool. Placeholders below marked
// "REPLACE-ME" must be filled in with the real deployed URLs.
// ─────────────────────────────────────────────────────────────────────────────

const TOOLS = [
  {
    key: 'website',
    name: 'Adam Druck Group Website',
    description: 'The public ADG brand site — buy, sell, invest, communities & insights.',
    category: 'Brand & Marketing',
    url: 'https://adamdruckgroup.com',
    accent: '#0f4c81',
  },
  {
    key: 'listing-launchpad',
    name: 'Listing Launchpad',
    description: 'Spin up listing marketing fast — descriptions, social posts & launch checklists.',
    category: 'Brand & Marketing',
    url: 'https://REPLACE-ME-listing-launchpad.example.com',
    accent: '#c0392b',
  },
  {
    key: 'deal-finder',
    name: 'Central PA Deal Finder',
    description: 'Surface on- and off-market real estate deals across Central PA.',
    category: 'Deal Sourcing',
    url: 'https://REPLACE-ME-deal-finder.example.com',
    accent: '#1e8449',
  },
  {
    key: 'auction-finder',
    name: 'Central PA Auction Finder',
    description: 'Scans 9 counties for auctions, sheriff sales & auctioneer listings with ARV analysis.',
    category: 'Deal Sourcing',
    url: 'https://REPLACE-ME-auction-finder.example.com',
    accent: '#b9770e',
  },
  {
    key: 'flipiq',
    name: 'FlipIQ',
    description: 'Analyze fix-and-flip deals — ARV, rehab budget & profit projections.',
    category: 'Analysis & Valuation',
    url: 'https://REPLACE-ME-flipiq.example.com',
    accent: '#6c3483',
  },
  {
    key: 'real-estate-valuator',
    name: 'Real Estate Valuator',
    description: 'Fast property valuations backed by comparable sales.',
    category: 'Analysis & Valuation',
    url: 'https://REPLACE-ME-real-estate-valuator.example.com',
    accent: '#2471a3',
  },
  {
    key: 'mve-app',
    name: 'MVE App',
    description: 'Market value estimate workspace.',
    category: 'Analysis & Valuation',
    url: 'https://REPLACE-ME-mve-app.example.com',
    accent: '#117864',
  },
  {
    key: 'agent-success-builder',
    name: 'Agent Success Builder',
    description: 'Coaching, productivity & accountability builder for ADG agents.',
    category: 'Team & Coaching',
    url: 'https://REPLACE-ME-agent-success-builder.example.com',
    accent: '#884ea0',
  },
];

module.exports = { TOOLS };
