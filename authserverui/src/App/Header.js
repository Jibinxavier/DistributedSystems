import React from 'react';
import { Link } from 'react-router-dom';

import {
  Container, Row, Col, Form, Input, Button, Navbar, Nav,
  NavbarBrand, NavLink, NavItem, UncontrolledDropdown,
  DropdownToggle, DropdownMenu, DropdownItem
} from 'reactstrap';
 
const LoggedOutView = props => {
    if (!props.currentUser) {
      return (
    <Row>
        <Col className="d-none d-lg-flex justify-content-end">
        <span>
        <Link to="/register" className="nav-link-font-weight-bold">Register</Link>

        </span>
        </Col>
        <Col>
        <span><Link to="/login" className="nav-link-font-weight-bold">Login</Link></span>
        </Col>
        </Row> 

        
      );
    }
    return null;
}  

const AVATAR = 'https://www.gravatar.com/avatar/429e504af19fc3e1cfa5c4326ef3394c?s=240&d=mm&r=pg';

class Header extends React.Component {
    render() {
        return(<header>
            <Navbar  color="light" light expand="xs" className="border-bottom border-gray bg-white" style={{ height: 80 }}>
            
            <Container>
                <Row noGutters className="position-relative w-100 align-items-center">
                
                <Col className="d-none d-lg-flex justify-content-start">
                    <Nav className="mrx-auto" navbar>
                    
                    <NavItem className="d-flex align-items-center">
                        <NavLink className="font-weight-bold" href="/">
                        <img src={AVATAR} alt="avatar" className="img-fluid rounded-circle" style={{ width: 36 }} />
                        </NavLink>
                    </NavItem>
                    
                    <NavItem className="d-flex align-items-center">
                        <NavLink className="font-weight-bold" href="/">Home</NavLink>
                    </NavItem>
                        
                    <NavItem className="d-flex align-items-center">
                        <NavLink className="font-weight-bold" href="/">Files</NavLink>
                    </NavItem>
                    
                
                    
                    </Nav>
                </Col>
                
                <Col className="d-flex justify-content-xs-start justify-content-lg-center">
                    <NavbarBrand className="d-inline-block p-0" href="/" style={{ width: 80 }}>
                    <p>Distributed File Store</p>
                    </NavbarBrand>
                </Col>
                
                {/* <Col className="d-none d-lg-flex justify-content-end">
                    <NavLink className="font-weight-bold" href="/">Logout</NavLink>
                </Col> */}
                <LoggedOutView currentUser={this.props.currentUser} />
                
                
                </Row>
            </Container>
            
            </Navbar>
        </header>);
    }

}

export default Header;