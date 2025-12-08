import '../styles/styles.scss';
import { Provider } from 'react-redux';
import { configureStore } from '@reduxjs/toolkit';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import { AppPage } from '../pages/AppPage';

export const App = () => {
  const store = configureStore({
    reducer: {
      //"yourreducer": yourreducer,
    },
    middleware: (getDefaultMiddleware) => getDefaultMiddleware({
      serializableCheck: false,
    }),
  });

  return (
    <Provider store={store}>
      <Router>
        <Routes>
          {/* Standalone routes - no SearchPanel */}
          <Route path="/" element={<AppPage />} />
        </Routes>
      </Router>
    </Provider>
  );
};