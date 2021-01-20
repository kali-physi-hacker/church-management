import React from 'react';
import {Link} from "react-router-dom";


export const Nav = props => {
    return (
        <ul className={`navi ${props.className}`}>
            {props.children}
        </ul>
    )
}

export const NavItem = props => {
    return (
        <li className="navi-item">
            <Link to="#" className={`navi-${props.link ? "link": "item"}`}>
                <span className="navi-icon">
                    <i className="flaticon2-writing"></i>
                </span>
                <span className="navi-text">{props.text}</span>
            </Link>
        </li>
    )
}

const DropdownMenu = props => {
    return (
        <div className={`dropdown-menu dropdown-menu-${props.size} ${props.className} dropdown-menu-${props.side}`}>
            {props.children}
        </div>
    )
}


export const Dropdown = props => {
    return (
        <div className={`dropdown-menu dropdown-menu-${props.size} dropdown-menu-${props.side} ${props.className}`}>

        </div>
    )
}


export default DropdownMenu;