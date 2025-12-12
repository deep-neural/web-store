import React from 'react';
import { Outlet } from 'react-router-dom';
import { SidePanel } from '../SidePanel';

interface AppLayoutProps {
  showRightPanel?: boolean;
}

export const AppLayout = ({ showRightPanel = false }: AppLayoutProps) => {
  return (
    <div className="app-layout">
      <div className={`main-container ${showRightPanel ? 'with-right-panel' : ''}`}>
        <SidePanel />
        <Outlet />
      </div>
    </div>
  );
};