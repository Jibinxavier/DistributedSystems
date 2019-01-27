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
            isLogin:true
        }

    }
    componentWillMount(){
        var loginscreen = []
        loginscreen.push(<Login parentContext={this} appContext={this.props.parentContext}/>);
        var loginmessage = "Not registered, Signup NoW!!";
        this.setState({
            loginscreen:loginscreen,
            loginmessage:loginmessage
        })
    }
    handleClick(event){
        var loginmessage;
        if(this.state.isLogin){
            var loginscreen = [];
            loginmessage = "Already registered, Login";
            this.setState({
                loginscreen:loginscreen,
                loginmessage:loginmessage,
                buttonLabel:"Login",
                isLogin:false
              })
        }
        else {
            var loginscreen = [];
            loginscreen.push(<Login parentContext={this}/>);
            loginmessage = "Not registered.. Please register to continue";
            this.setState({
                loginscreen:loginscreen,
                loginmessage:loginmessage,
                buttonLabel:"Signup",
                isLogin:true
              })

        }
    }
    render () {
        return (
            <div className="loginscreen">
              {this.state.loginscreen}
              <div>
                {this.state.loginmessage}
                <MuiThemeProvider>
                  <div>
                     <RaisedButton label={this.state.buttonLabel} primary={true} style={style} onClick={(event) => this.handleClick(event)}/>
                 </div>
                </MuiThemeProvider>
              </div>
            </div>
          );
        }
}
const style = {
    margin: 15,
  };
export default LoginScreen;