import React, { Component } from 'react';

class HomePage extends Component {
    

    render() {
        const { user, users } = this.props;
        return (
            <div className="col-md-6 col-md-offset-3">
                <h1>Hi {user.firstName}!</h1>
                <p>You're logged in with React!!</p>
                <h3>All registered users:</h3>
                
                <p>
                   
                </p>
            </div>
        );
    }

    
}

export default HomePage;