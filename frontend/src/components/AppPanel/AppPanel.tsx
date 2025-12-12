import { AppLayout } from "../AppLayout";
import { DiscoverPanel } from "../DiscoverPanel";

export const AppPanel = () => {
  return (
    <div className="app-panel">
      <AppLayout showRightPanel={false}>
        <DiscoverPanel />
      </AppLayout>
    </div>
  );
};