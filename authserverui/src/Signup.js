import React, { Component } from 'react';
import MuiThemeProvider from 'material-ui/styles/MuiThemeProvider';
import AppBar from 'material-ui/AppBar';
import RaisedButton from 'material-ui/RaisedButton';
import TextField from 'material-ui/TextField';
import axios from 'axios';
import Login from './Login';
class Signup extends Component {
    constructor(props){
        super(props);
        this.state = {
            username: '',
            email: '',
            password: ''
        }
    }
    

    render () {
        return (
                <div>
                    <MuiThemeProvider>
                        <div>
                            <AppBar title="Register"/>
                            <TextField
                                hintText="Enter your username"
                                floatingLabelText="Username"
                                onChange = {(event,newValue) => this.setState({username:newValue})}
                            />
                            <br/>
                            <TextField
                                hintText="Enter your email"
                                floatingLabelText="Email"
                                onChange = {(event,newValue) => this.setState({email:newValue})}
                            />
                            <br/>
                            <TextField
                                type = "password"
                                hintText="Enter password"
                                floatingLabelText="Password"
                                onChange = {(event,newValue) => this.setState({password:newValue})}
                            />
                            <br/>
                            <RaisedButton label="Submit" primary={true} style={style} onClick={(event) => this.handleClick(event)}/>
                        </div>
                    </MuiThemeProvider>
                </div>
        );
    }
    handleClick(event){
        var apiBaseUrl = "http://localhost:9000";
        console.log("vaules ",this.state.first_name,this.state.last_name,this.state.email,this.state.password);
        var self = this;
        var payload = {
            "username": this.state.username,
            "email": this.state.email,
            "password": this.state.password
        }
        axios.post(apiBaseUrl + '/signup', payload).then(function(response){
            console.log(response);
            if(response.data.code == 200){
                console.log("registration successfull");
                var loginscreen = [];
                loginscreen.push(<Login parentContext={this}/>);
                var loginMessage = "Unknown user. To register";
                self.props.parentContext.setState({loginscreen: loginscreen,
                loginmessage: loginMessage,
                buttonLabel: "Signup",
                isLogin:true
                
                });
           }
            
        }).catch(function (error){
            console.log(error);
        });
    }
}

const style = {
    margin: 15,
  };
export default Signup;