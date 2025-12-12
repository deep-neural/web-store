import '../styles/styles.scss';
import { Provider } from 'react-redux';
import { configureStore } from '@reduxjs/toolkit';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import { 
  AppPage,
  AddonPage,
} from '../pages';
import { AppLayout } from '../components/AppLayout';

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
          {/* AppLayout wraps all routes */}
          <Route element={<AppLayout />}>
            <Route path="/" element={<AppPage />} />
            <Route path="/addons/:id" element={<AddonPage />} />
          </Route>
        </Routes>
      </Router>
    </Provider>
  );
};