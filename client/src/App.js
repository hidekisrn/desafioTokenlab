import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import './App.css';

import Login from './pages/Login'
import Register from './pages/Register'
import Schedules from './pages/Schedules'
import NewSchedule from './pages/NewSchedule'
import EditSchedule from './pages/EditSchedule'

function App() {
  return (
    <Router>
      <Switch>
        <Route exact path ="/" component={Login}/>
        <Route exact path ="/register" component={Register}/>
        <Route exact path ="/schedules" component={Schedules}/>
        <Route exact path ="/newschedule" component={NewSchedule}/>
        <Route exact path ="/editschedule" component={EditSchedule}/>
      </Switch>
    </Router>
  );
}

export default App;
