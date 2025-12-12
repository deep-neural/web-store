import { useState } from 'react';
import './AddonPanel.module.scss';
import w1 from './images/w1.jpg';
import w2 from './images/w2.jpg';
import w3 from './images/w3.jpg';
import w4 from './images/w4.jpg';
import { 
  Volume2, 
  ExternalLink, 
  Share2, 
  Headphones, 
  User, 
  Star, 
  ChevronLeft, 
  ChevronRight,
  ChevronRight as ArrowRight,
  Lock,
  Trash2,
  Smartphone,
  Monitor,
  Tablet,
  MoreVertical,
  HelpCircle
} from 'lucide-react';

export const AddonPanel = () => {
  const [currentSlide, setCurrentSlide] = useState(0);
  const slides = [w1, w2, w3, w4];

  const renderStars = (rating: number) => {
    return Array.from({ length: 5 }, (_, i) => (
      <Star
        key={i}
        size={14}
        fill={i < Math.floor(rating) ? '#6b7280' : 'none'}
        stroke={i < Math.floor(rating) ? '#6b7280' : '#d1d5db'}
      />
    ));
  };

  const renderRatingStars = (rating: number, size: number = 20, color: string = '#5f6368') => {
    return Array.from({ length: 5 }, (_, i) => (
      <Star
        key={i}
        size={size}
        fill={i < Math.floor(rating) ? color : 'none'}
        stroke={color}
      />
    ));
  };

  const renderReviewStars = (rating: number) => {
    return Array.from({ length: 5 }, (_, i) => (
      <Star
        key={i}
        size={14}
        fill={i < rating ? '#4A9EFF' : 'none'}
        stroke={i < rating ? '#4A9EFF' : '#d1d5db'}
      />
    ));
  };

  return (
    <div className="addon-panel">
      {/* Hero Section */}
      <div className="hero-section">
        <div className="hero-content">
          <div className="app-icon">
            <Volume2 size={80} color="#4A9EFF" />
          </div>
          <div className="hero-info">
            <h1 className="title">Sound Booster Pro</h1>
            <div className="subtitle">Volume Enhancement & Audio Control</div>
            <div className="meta">
              <span>All Platforms</span>
              <span>Free - Premium Features Available</span>
            </div>
            <div className="hero-actions">
              <button className="view-store-btn">
                Add to Browser
              </button>
              <button className="share-btn">
                <Share2 size={18} />
              </button>
            </div>
          </div>
        </div>
      </div>

      {/* Info Grid */}
      <div className="info-grid">
        <div className="info-item">
          <div className="info-label">12,547 RATINGS</div>
          <div className="info-value">4.7</div>
          <div className="info-stars">{renderStars(4.7)}</div>
        </div>
        <div className="info-item">
          <div className="info-label">CATEGORY</div>
          <div className="info-icon">
            <Headphones size={24} color="#6b7280" />
          </div>
          <div className="info-sublabel">Audio & Music</div>
        </div>
        <div className="info-item">
          <div className="info-label">DEVELOPER</div>
          <div className="info-icon">
            <User size={24} color="#6b7280" />
          </div>
          <div className="info-sublabel">AudioTech Studios</div>
        </div>
        <div className="info-item">
          <div className="info-label">LANGUAGE</div>
          <div className="info-value">EN</div>
          <div className="info-sublabel">+ 28 More</div>
        </div>
        <div className="info-item">
          <div className="info-label">SIZE</div>
          <div className="info-value">2.4</div>
          <div className="info-sublabel">MB</div>
        </div>
      </div>

      {/* Main Content - Screenshots */}
      <div className="main-content">
        <div className="screenshots-container">
          <div className="screenshots-grid">
            {slides.map((slide, index) => (
              <div key={index} className="screenshot-card">
                <img src={slide} alt={`Screenshot ${index + 1}`} />
              </div>
            ))}
          </div>
          <button className="view-all-btn">
            View All
            <ArrowRight size={16} />
          </button>
        </div>
      </div>

      {/* About Section */}
      <div className="about-section">
        <div className="section-header">
          <h2 className="section-title">About this extension</h2>
          <ArrowRight className="arrow" size={20} />
        </div>
        <p className="description">
          Boost your audio experience with Sound Booster Pro! Increase volume beyond system limits and enjoy crystal-clear sound on any website or application.
        </p>
        <p className="description">
          Advanced audio enhancement technology, intuitive controls, and real-time volume boosting give you complete control over your listening experience.
        </p>
        <div className="features">
          <strong>Premium Features:</strong>
          <br />
          • Boost volume up to 500% beyond system maximum
          <br />
          • Real-time audio enhancement with zero latency
          <br />
          • Custom presets for music, movies, and gaming
          <br />
          • Per-tab volume control for ultimate flexibility
        </div>

        <div className="metadata">
          <div className="meta-item">
            <div className="meta-label">Updated on</div>
            <div className="meta-value">Dec 8, 2025</div>
          </div>
          <div className="meta-item">
            <div className="meta-label">Available on</div>
            <div className="meta-value">Chrome, <span className="link">Firefox, Edge</span></div>
          </div>
        </div>

        <div className="tags">
          <span className="tag">#3 top audio tool</span>
          <span className="tag">Audio Enhancement</span>
          <span className="tag">Volume Booster</span>
          <span className="tag">Music</span>
          <span className="tag">Sound Control</span>
          <span className="tag">Media Player</span>
          <span className="tag">Premium</span>
          <span className="tag">Browser Extension</span>
          <span className="tag">Cross-platform</span>
          <span className="tag">Real-time</span>
          <span className="tag">High Quality</span>
        </div>
      </div>

      {/* Data Safety Section */}
      <div className="data-section">
        <div className="section-header">
          <h2 className="section-title">Data safety</h2>
          <ArrowRight className="arrow" size={20} />
        </div>
        <p className="data-safety-text">
          Safety starts with understanding how developers collect and share your data. Data privacy and security practices may vary based on your use, region, and age. The developer provided this information and may update it over time.
        </p>
        
        <div className="safety-info">
          <div className="safety-item">
            <ExternalLink className="safety-icon" size={20} color="#5f6368" />
            <div>
              <div className="safety-title">No data shared with third parties</div>
              <div className="safety-detail">This extension does not share any user data</div>
            </div>
          </div>
          <div className="safety-item">
            <Share2 className="safety-icon" size={20} color="#5f6368" />
            <div>
              <div className="safety-title">This extension collects minimal data</div>
              <div className="safety-detail">Volume preferences and usage statistics only</div>
            </div>
          </div>
          <div className="safety-item">
            <Lock className="safety-icon" size={20} color="#5f6368" />
            <div className="safety-title">Data is encrypted in transit</div>
          </div>
          <div className="safety-item">
            <Trash2 className="safety-icon" size={20} color="#5f6368" />
            <div className="safety-title">You can request that data be deleted</div>
          </div>
        </div>
        <a href="#" className="see-details">See details</a>
      </div>

      {/* Ratings Section */}
      <div className="ratings-section">
        <div className="section-header">
          <h2 className="section-title">Ratings and reviews</h2>
          <ArrowRight className="arrow" size={20} />
          <span className="verified">
            Ratings and reviews are verified 
            <HelpCircle size={14} style={{ marginLeft: '4px', verticalAlign: 'middle' }} />
          </span>
        </div>

        <div className="device-tabs">
          <button className="device-tab active">
            <Smartphone size={16} style={{ marginRight: '6px' }} />
            Phone
          </button>
          <button className="device-tab">
            <Monitor size={16} style={{ marginRight: '6px' }} />
            Chromebook
          </button>
          <button className="device-tab">
            <Tablet size={16} style={{ marginRight: '6px' }} />
            Tablet
          </button>
        </div>

        <div className="rating-overview">
          <div className="rating-score">
            <div className="big-score">4.7</div>
            <div className="stars">{renderRatingStars(4.7)}</div>
            <div className="review-count">12.5K reviews</div>
          </div>

          <div className="rating-bars">
            <div className="rating-bar">
              <span className="bar-label">5</span>
              <div className="bar-track">
                <div className="bar-fill" style={{ width: '78%' }}></div>
              </div>
            </div>
            <div className="rating-bar">
              <span className="bar-label">4</span>
              <div className="bar-track">
                <div className="bar-fill" style={{ width: '15%' }}></div>
              </div>
            </div>
            <div className="rating-bar">
              <span className="bar-label">3</span>
              <div className="bar-track">
                <div className="bar-fill" style={{ width: '4%' }}></div>
              </div>
            </div>
            <div className="rating-bar">
              <span className="bar-label">2</span>
              <div className="bar-track">
                <div className="bar-fill" style={{ width: '2%' }}></div>
              </div>
            </div>
            <div className="rating-bar">
              <span className="bar-label">1</span>
              <div className="bar-track">
                <div className="bar-fill" style={{ width: '1%' }}></div>
              </div>
            </div>
          </div>
        </div>

        {/* Sample Review */}
        <div className="review">
          <div className="review-header">
            <div className="review-avatar">U</div>
            <div className="review-author">user978927</div>
            <button className="review-menu">
              <MoreVertical size={20} />
            </button>
          </div>
          <div className="review-stars">{renderReviewStars(5)}</div>
          <div className="review-date">November 15, 2025</div>
          <div className="review-text">
            This extension is absolutely amazing! I've been using Sound Booster Pro for 6 months now and it's transformed my audio experience. The volume boost is incredible - I can finally hear quiet videos and music clearly. The interface is super clean and easy to use. The per-tab controls are genius, letting me boost Netflix while keeping YouTube at normal levels. The sound quality remains crystal clear even at maximum boost. Premium features are totally worth it. Highly recommend to anyone who needs louder audio!
          </div>
          <div className="review-helpful">142 people found this review helpful</div>
          <div className="review-actions">
            <span className="review-question">Did you find this helpful?</span>
            <button className="review-btn">Yes</button>
            <button className="review-btn">No</button>
          </div>
        </div>
      </div>
    </div>
  );
};