import React, { Component } from 'react';
import MuiThemeProvider from 'material-ui/styles/MuiThemeProvider';
import RaisedButton from 'material-ui/RaisedButton';
import Signup from './Signup';
import Login from './Login';


class LoginScreen extends Component {
    constructor(props){
        super(props)
        this.state = {
            username:'',
            password:'',
            loginscreen:[],
            loginmessage:'',
            buttonLabel:'Signup',
            loggedIN:true
        }

    }
    componentWillMount(){
        var loginscreen = []
        console.log(this.props.parentContext)
        loginscreen.push(<Login parentContext={this} appContext={this.props.parentContext}/>);
        var loginmessage = "Not registered, Signup NoW!!";
        this.setState({
            loginscreen:loginscreen,
            loginmessage:loginmessage
        })
    }
    handleClick(event){
        var loginmessage;
        if(this.state.loggedIN){
            let loginscreen=[];
            loginscreen.push(<Login parentContext={this} appContext={this.props.appContext} />);
            loginmessage = "Already registered.Go to Login";
            let loginButtons=[];
            loginButtons.push(
                <div key="login-button">
                <MuiThemeProvider>
                <div>
                    <RaisedButton label={"Login"} primary={true} style={style} onClick={(event) => this.handleClick(event)}/>
                </div>
                </MuiThemeProvider>
                </div>
            )
            this.setState({
                            loginscreen:loginscreen,
                            loginmessage:loginmessage,
                            loginButtons:loginButtons,
                            isLogin:false
                        })
        }
        else {
            var loginscreen = [];
            loginscreen.push(< Signup parentContext={this}/>);
            loginmessage = "Not registered.. Please register to continue";
            this.setState({
                loginscreen:loginscreen,
                loginmessage:loginmessage,
                buttonLabel:"Signup",
                loggedIN:true
              })

        }
    }
    render () {
        return (
            <div className="loginscreen" key="loginscreen">
            {this.state.loginscreen}
            <div>
              {this.state.loginmessage}
              {this.state.loginButtons}
            </div>
          </div>
          );
        }
}
const withErrorHandling = WrappedComponent => ({ showError, children }) => {
    return (
      <WrappedComponent>
        {showError && <div className="error-message">Oops! Something went wrong!</div>}
        {children}
      </WrappedComponent>
    );
  };
  const DivWithErrorHandling = withErrorHandling(({children}) => <div>{children}</div>)

const style = {
    margin: 15,
  };
export default LoginScreen;