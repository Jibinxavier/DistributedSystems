import React from 'react';
import { Router, Route } from 'react-router-dom';
import { connect } from 'react-redux';
 
import { history } from '../_helpers';
import { alertActions } from '../_actions';
import { PrivateRoute } from '../_components';
import { HomePage } from '../HomePage';
import { LoginPage } from '../LoginPage';
import { RegisterPage } from '../RegisterPage';  

import   Header   from './Header';  
class App extends React.Component {
    constructor(props) {
        super(props);

        const { dispatch } = this.props;
        history.listen((location, action) => {
            // clear alert on location change
            dispatch(alertActions.clear());
        });
    }

    render() {
        const { alert,authentication } = this.props;
        return (
     
            <div  >
                
                
                <div className="col-sm-8 col-sm-offset-2">
                    {alert.message &&
                        <div className={`alert ${alert.type}`}>{alert.message}</div>
                    }
                    <Router history={history}>
                        <div>
                        <Header appName={'Distributed store'} currentUser={this.props.user} />
                            <PrivateRoute exact path="/" component={HomePage} />
                            <Route path="/login" component={LoginPage} />
                            <Route path="/register" component={RegisterPage} />
                           
                        </div>
                    </Router>
                </div>
                 
               
            </div>
        
          
        );
    }
}

function mapStateToProps(state) {
    const { alert,authentication } = state;

    return {
        alert,
        authentication
    };
}

const connectedApp = connect(mapStateToProps)(App);
export { connectedApp as App }