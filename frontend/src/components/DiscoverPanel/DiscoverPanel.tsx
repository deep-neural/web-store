import React from 'react';
import w1 from './images/w1.jpg';
import w2 from './images/w2.jpg';
import w3 from './images/w3.jpg';
import {
  Shield,
  Zap,
  Palette,
  Download,
  Lock,
  Video,
  Music,
  Camera,
  FileText,
  BookOpen,
  Calendar,
  Mail,
  MessageSquare,
  Cloud,
  Database,
  Code,
} from 'lucide-react';

interface AppItem {
  id: string;
  name: string;
  description: string;
  icon: React.ComponentType<any>;
  color: string;
  category?: string;
  wallpaper?: string;
}

export const DiscoverPanel = () => {
  const featuredApps: AppItem[] = [
    {
      id: '1',
      name: 'uBlock Origin',
      description: 'Efficient ad blocker',
      icon: Shield,
      color: '#e74c3c',
      category: 'FEATURED',
      wallpaper: w1,
    },
    {
      id: '2',
      name: 'Dark Reader',
      description: 'Dark mode for every website',
      icon: Palette,
      color: '#2c3e50',
      category: 'FEATURED',
      wallpaper: w2,
    },
    {
      id: '3',
      name: 'Video Downloader',
      description: 'Download videos easily',
      icon: Download,
      color: '#3498db',
      category: 'FEATURED',
      wallpaper: w3,
    },
  ];

  const appsWeLove: AppItem[] = [
    {
      id: '5',
      name: 'Grammar Check',
      description: 'Writing assistant',
      icon: FileText,
      color: '#16a085',
    },
    {
      id: '6',
      name: 'Video Enhancer',
      description: 'Improve video quality',
      icon: Video,
      color: '#8e44ad',
    },
    {
      id: '7',
      name: 'Music Player Pro',
      description: 'Enhanced audio experience',
      icon: Music,
      color: '#e67e22',
    },
    {
      id: '8',
      name: 'Screenshot Tool',
      description: 'Capture and edit',
      icon: Camera,
      color: '#f39c12',
    },
    {
      id: '9',
      name: 'Note Taker',
      description: 'Quick notes anywhere',
      icon: BookOpen,
      color: '#2980b9',
    },
    {
      id: '10',
      name: 'Calendar Sync',
      description: 'Manage your schedule',
      icon: Calendar,
      color: '#c0392b',
    },
    {
      id: '11',
      name: 'Email Tracker',
      description: 'Track email opens',
      icon: Mail,
      color: '#d35400',
    },
    {
      id: '12',
      name: 'Chat Translator',
      description: 'Translate messages',
      icon: MessageSquare,
      color: '#7f8c8d',
    },
    {
      id: '13',
      name: 'Cloud Storage',
      description: 'Store files securely',
      icon: Cloud,
      color: '#3498db',
    },
    {
      id: '14',
      name: 'Data Sync',
      description: 'Sync across devices',
      icon: Database,
      color: '#9b59b6',
    },
    {
      id: '15',
      name: 'Code Highlighter',
      description: 'Syntax highlighting',
      icon: Code,
      color: '#34495e',
    },
    {
      id: '16',
      name: 'Speed Booster',
      description: 'Faster browsing',
      icon: Zap,
      color: '#f1c40f',
    },
  ];

  return (
    <div className="discover-panel">
      {/* Hero Section */}
      <div className="hero-section">
        <div className="hero-slide">
          <img src={w1} alt="Featured" className="hero-image" />
          <div className="hero-overlay">
            <div className="hero-content">
              <div className="hero-app-icon" style={{ backgroundColor: '#667eea' }}>
                <Shield size={32} color="#ffffff" />
              </div>
              <div className="hero-app-info">
                <h1 className="hero-title">uBlock Origin</h1>
                <p className="hero-description">Efficient ad blocker</p>
              </div>
            </div>
          </div>
        </div>
      </div>

      {/* Featured Apps Row */}
      <div className="featured-apps-section">
        <h2 className="featured-section-title">Popular Utilities</h2>
        <div className="featured-apps-grid">
          {featuredApps.map((app) => {
            const IconComponent = app.icon;
            return (
              <div key={app.id} className="featured-app-card">
                <div className="featured-app-image-container">
                  <img src={app.wallpaper} alt={app.name} className="featured-app-image" />
                </div>
                <div className="featured-app-bottom">
                  <div className="featured-app-icon" style={{ backgroundColor: app.color }}>
                    <IconComponent size={24} color="#ffffff" />
                  </div>
                  <div className="featured-app-info">
                    <h3 className="featured-app-name">{app.name}</h3>
                    <p className="featured-app-description">{app.description}</p>
                  </div>
                </div>
              </div>
            );
          })}
        </div>
      </div>

      {/* Apps We Love Section */}
      <div className="apps-section">
        <div className="section-header">
          <h2 className="section-title">Apps and Extensions We Love Right Now</h2>
          <button className="see-all-button">See All →</button>
        </div>
        
        <div className="apps-grid">
          {appsWeLove.map((app) => {
            const IconComponent = app.icon;
            return (
              <div key={app.id} className="app-item">
                <div className="app-icon" style={{ backgroundColor: app.color }}>
                  <IconComponent size={24} color="#ffffff" />
                </div>
                <div className="app-info">
                  <h3 className="app-name">{app.name}</h3>
                  <p className="app-description">{app.description}</p>
                </div>
                <button className="view-button">Get</button>
              </div>
            );
          })}
        </div>
      </div>
    </div>
  );
};