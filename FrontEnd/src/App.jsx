import React from 'react';
import {
  BrowserRouter as Router, Switch, Route, BrowserRouter,
} from 'react-router-dom';
import { ResumeProvider } from './contexts/ResumeContext';
import Nav from './components/Nav/Nav';
import Footer from './components/Footer/Footer';
import LandingPage from './pages/LandingPage/LandingPage';
import Test from './Test';

function App() {
  return (
    <div>
      <ResumeProvider>
        <BrowserRouter>
          <Nav />
        </BrowserRouter>
        <Router>
          <Switch>
            <Route path="/" component={LandingPage} exact />
            <Route path="/results" component={Test} exact />
          </Switch>
        </Router>
        <Footer />
      </ResumeProvider>
    </div>
  );
}

export default App;
