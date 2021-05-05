import React from 'react';
import {
  BrowserRouter as Router, Switch, Route,
} from 'react-router-dom';
import { ResumeProvider } from './contexts/ResumeContext';
import LandingPage from './pages/LandingPage/LandingPage';
import ResultsPage from './pages/ResultsPage/ResultsPage';

function App() {
  return (
    <div>
      <ResumeProvider>
        <Router>
          <Switch>
            <Route exact path="/" component={LandingPage} />
            <Route exact path="/results" component={ResultsPage} />
          </Switch>
        </Router>
      </ResumeProvider>
    </div>
  );
}

export default App;
