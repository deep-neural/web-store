import React from 'react';
import { SidePanel } from '../SidePanel';

interface AppLayoutProps {
  children: React.ReactNode;
  showRightPanel?: boolean;
}

export const AppLayout = ({ children, showRightPanel = false }: AppLayoutProps) => {
  return (
    <div className="app-layout">
      <div className={`main-container ${showRightPanel ? 'with-right-panel' : ''}`}>
        <SidePanel />
        {children}
      </div>
    </div>
  );
};