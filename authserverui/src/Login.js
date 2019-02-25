import React, { Component } from 'react';
import MuiThemeProvider from 'material-ui/styles/MuiThemeProvider';
import AppBar from 'material-ui/AppBar';
import RaisedButton from 'material-ui/RaisedButton';
import TextField from 'material-ui/TextField'
import axios from 'axios';
import HomePage from './HomePage';
import Signup from './Signup';
 
class Login extends Component {
    constructor(props){
        super(props);
        this.state = {
            username:'',
            password:'',
            toSignUp: false
        }
    }
    render() {
        return(
            <div>
                <MuiThemeProvider >
                    <div>
                        <AppBar title="Login"/>
                        <br/>
                        <TextField hintText="Enter your username"   
                                floatingLabelText="Username"
                                onChange = {(envent, newValue) => this.setState({username:newValue})
                                }/>
                        
                        <br/>
                        <TextField type="password"
                                hintText="Enter your password"
                                floatingLabelText = "Password"
                                onChange = {(event,newValue) => this.setState({password:newValue})}
                        />
                        <br/>
                        <br>
                        </br>
                        <RaisedButton label="Login" primary={true} style={style} onClick={(event) => this.handleClick(event)}/>
                        <RaisedButton label="Signup" primary={false} style={style} onClick={(event) => this.handleSignupClick(event)}/>
                    </div>
                </MuiThemeProvider>

            </div>
        );

    }
    handleClick(event){
      
        var apiBaseUrl = "http://localhost:9000/";
        var self = this;
        var payload = {
            "email": this.state.username,
            "password": this.state.password
        }
        axios.post(apiBaseUrl+'login', payload).then( function(response){
            console.log("heres the response")
            console.log(response)
            if(response.status === 200){ 
                var homepage = []
                 homepage.push( 
                    <HomePage appContext={self.props.appContext}/>)
                self.props.appContext.setState(
                    {loginPage: [], homePage: homepage}
                )
                
            }
            else if (response.data.code === 204){
                console.log("Username password do not match")
                
            }
        }).catch(function (error){
            console.log("Error occurred")

            console.log(error)
        });
    }
    handleSignupClick(event){
        var signup = []
        signup.push( 
            <Signup appContext={this.props.appContext}/>)
        this.props.appContext.setState(
            {loginPage: signup, homepage: []}
        )
    }
}

const style = {
    margin: 40,
};


export default Login;