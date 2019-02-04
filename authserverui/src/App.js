import React, { Component } from 'react';
import NavBar from './components/NavBar'
// Needed for onTouchTap
// http://stackoverflow.com/a/34015469/988941


import './App.css';
import LoginScreen from './Loginscreen';
//injectTapEventPlugin();
class App extends Component {
  constructor(props){
    super(props);
    this.state={
      loginPage:[],
      homePage:[]
    }
  }
  componentWillMount(){
    var loginPage =[];
    loginPage.push(<LoginScreen parentContext={this}/>);
    this.setState({ loginPage:loginPage  })
  }
  
  render() {
    return (
      
      <div className="App">
       <NavBar />
        {this.state.loginPage}
        {this.state.homePage}
      </div>
    );
  }
}
const style = {
  margin: 15,
};

export default App;
