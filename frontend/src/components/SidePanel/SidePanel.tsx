import React from 'react';
import {
  Compass,
  Palette,
  Layers,
  Sparkles,
  Bell,
  Flame,
  Award,
  CheckSquare,
  Code2,
  Shield,
  ShoppingBag,
  MessageSquare,
  Share2,
  Tv,
  Newspaper,
  Eye,
  Workflow,
  Wrench,
  Search,
  ChevronDown
} from 'lucide-react';
import logoIcon from './images/logo.png';

interface NavItem {
  id: string;
  label: string;
  icon: React.ComponentType<any>;
  active?: boolean;
}

const mainNavItems: NavItem[] = [
  { id: 'discover', label: 'Discover', icon: Compass, active: true },
  { id: 'themes', label: 'Themes', icon: Palette },
  { id: 'collections', label: 'Collections', icon: Layers },
  { id: 'for-you', label: 'For You', icon: Sparkles },
  { id: 'whats-new', label: "What's New", icon: Bell },
  { id: 'popular', label: 'Popular', icon: Flame },
  { id: 'editor-picks', label: "Editor's Picks", icon: Award },
];

const categoryItems: NavItem[] = [
  { id: 'productivity', label: 'Productivity', icon: CheckSquare },
  { id: 'developer-tools', label: 'Developer Tools', icon: Code2 },
  { id: 'privacy-security', label: 'Privacy & Security', icon: Shield },
  { id: 'shopping', label: 'Shopping', icon: ShoppingBag },
  { id: 'communication', label: 'Communication', icon: MessageSquare },
  { id: 'social-media', label: 'Social & Media', icon: Share2 },
  { id: 'entertainment', label: 'Entertainment', icon: Tv },
  { id: 'news-weather', label: 'News & Weather', icon: Newspaper },
  { id: 'accessibility', label: 'Accessibility', icon: Eye },
  { id: 'workflow', label: 'Workflow & Tools', icon: Workflow },
  { id: 'utilities', label: 'Utilities', icon: Wrench },
];

export const SidePanel = () => {
  return (
    <div className="side-panel">
      <div className="side-panel-header">
        <button className="store-selector">
          <img src={logoIcon} alt="Store logo" className="store-icon" width={20} height={20} />
          <span className="store-name">Browser Web Store</span>
          <ChevronDown className="chevron" size={18} />
        </button>
      </div>

      <div className="search-container">
        <div className="search-box">
          <Search className="search-icon" size={16} />
          <input 
            type="text" 
            placeholder="Search extensions" 
            className="search-input"
          />
        </div>
      </div>

      <nav className="side-nav">
        <ul className="nav-list">
          {mainNavItems.map((item) => {
            const IconComponent = item.icon;
            return (
              <li key={item.id} className={`nav-item ${item.active ? 'active' : ''}`}>
                <a href={`#${item.id}`} className="nav-link">
                  <IconComponent className="nav-icon" size={20} />
                  <span className="nav-label">{item.label}</span>
                </a>
              </li>
            );
          })}
        </ul>

        <div className="nav-divider"></div>

        <div className="categories-section">
          <h3 className="section-title">Categories</h3>
          <ul className="nav-list">
            {categoryItems.map((item) => {
              const IconComponent = item.icon;
              return (
                <li key={item.id} className="nav-item">
                  <a href={`#${item.id}`} className="nav-link">
                    <IconComponent className="nav-icon" size={20} />
                    <span className="nav-label">{item.label}</span>
                  </a>
                </li>
              );
            })}
          </ul>
        </div>
      </nav>
    </div>
  );
};