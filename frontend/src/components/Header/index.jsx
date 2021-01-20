import React from "react";


const NavMenuItem = props => {
    return (
        <li className={`menu-item ${props.active ? 'menu-item-active menu-item-here menu-item-here': ''}`}>
            <a href="#" className="menu-link">
                <span className="menu-text">{props.text}</span>
            </a>
        </li>
    )
}


const Header = props => {
    return (
        <div id="kt_header" className="header header-fixed">
            <div className="container-fluid d-flex align-items-stretch justify-content-between">
                <div className="header-menu-wrapper header-menu-wrapper-left" id="kt_header_menu_wrapper">
                    <div id="kt_header_menu" className="header-menu header-menu-mobile header-menu-layout-default">
                        <ul className="menu-nav">
                            <NavMenuItem text={"Home"} active={true}/>
                            <NavMenuItem text={"Pages"} />
                        </ul>
                    </div>
                </div>
            </div>
        </div>
    )
}


export default Header;