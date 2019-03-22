import React from 'react';
import { connect } from 'react-redux';

import { userActions, fileActions } from '../_actions';
import {
    Container, Row, Col, Form, Input, Button, Navbar, Nav,
    NavbarBrand, NavLink, NavItem, UncontrolledDropdown,
    DropdownToggle, DropdownMenu, DropdownItem
  } from 'reactstrap';
class HomePage extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            files: []
        };
        this.handleChange = this.handleChange.bind(this)
        this.handleFileUpload = this.handleFileUpload.bind(this);
    }
    componentDidMount() {
        this.props.dispatch(userActions.getAll());
    }

    handleDeleteUser(id) {
        return (e) => this.props.dispatch(userActions.delete(id));
    }
    handleFileUpload(e){
        e.preventDefault();
       
       
        const { files } = this.state;
        console.warn("data", files)
        if (files){
            this.props.dispatch(fileActions.upload(files))
        }
    }
  
    handleChange(e){
        let newFiles=e.target.files;
         
        this.setState({
            files: [...this.state.files, {"File": newFiles[0],"loaded": false}]
        })
    
    }
    render() {
        const { user, users } = this.props;
        return (
            <Container>
                <Row>
                <Col></Col>
                    <Col>
        
                <div className="col-md-6 col-md-offset-3">

                

                <div className="input-group">
                    <div className="input-group-prepend">
                        <span className="input-group-text" id="inputGroupFileAddon01" onClick={this.handleFileUpload}>
                        Upload
                        </span>
                    </div>
                    <div className="custom-file">
                        <input
                        type="file"
                        className="custom-file-input"
                        id="inputGroupFile01"
                        aria-describedby="inputGroupFileAddon01"
                        onChange={this.handleChange}
                        />
                        <label className="custom-file-label" htmlFor="inputGroupFile01">
                        Choose file
                        </label>
                    </div>
                </div>
                <h1>Hi {user.firstName}!</h1>

                <p>You're logged in with React!!</p>
                <h3>All files:</h3>
                {users.loading && <em>Loading users...</em>}
                {users.error && <span className="text-danger">ERROR: {users.error}</span>}
                {users.items &&
                    <ul>
                        {users.items.map((user, index) =>
                            <li key={user.id}>
                                {user.firstName + ' ' + user.lastName}
                                {
                                    user.deleting ? <em> - Deleting...</em>
                                    : user.deleteError ? <span className="text-danger"> - ERROR: {user.deleteError}</span>
                                    : <span> - <a onClick={this.handleDeleteUser(user.id)}>Delete</a></span>
                                }
                            </li>
                        )}
                    </ul>
                }

                </div>
                </Col>
            <Col></Col>
            </Row>
            </Container>
            
            
        );
    }
}

function mapStateToProps(state) {
    const { users, authentication } = state;
    const { user } = authentication;
    return {
        user,
        users
    };
}

const connectedHomePage = connect(mapStateToProps)(HomePage);
export { connectedHomePage as HomePage };