import React, { Component } from 'react';
import MuiThemeProvider from 'material-ui/styles/MuiThemeProvider';
import AppBar from 'material-ui/AppBar';
import RaisedButton from 'material-ui/RaisedButton';
import TextField from 'material-ui/TextField'
import axios from 'axios';


class Login extends Component {
    constructor(props){
        super(props);
        this.state = {
            username:'',
            password:''
        }
    }
    render() {
        return(
            <div>
                <MuiThemeProvider>
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
                        <RaisedButton label="Submit" primary={true} style={style} onClick={(event) => this.handleClick(event)}/>
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
            console.log(response);
            if(response.data.code == 200){
                console.log("Login successfull");
                var uploadScreen = []
                uploadScreen.push( 
                    <UploadScreen appContext={self.props.appContext}/>)
                self.props.appContext.setState(
                    {loginPage: [], uploadScreen: uploadScreen}
                )
                
            }
            else if (response.data.code == 204){
                console.log("Username password do not match")
                
            }
        }).catch(function (error){
            console.log(error)
        });
    }
}

const style = {
    margin: 30,
};


export default Login;