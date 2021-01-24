import React from 'react';
import {Link, NavLink} from "react-router-dom";
import DashboardIcon from "../../Resources/Icons/Dashboard";
import AddUserIcon from "../../Resources/Icons/AddUser";
import UserGroupIcon from "../../Resources/Icons/UserGroup";
import BuildingIcon from "../../Resources/Icons/Building";
import AddFileIcon from "../../Resources/Icons/AddFile";
import MenuIcon from "../../Resources/Icons/Menu";


const Logo = () => {
    return (
        <Link to="#" className="brand-logo">
            <img alt="Logo"
                 src="https://preview.keenthemes.com/keen/theme/demo1/dist/assets/media/logos/logo-1.svg"
                 className="h-30px"/>
        </Link>
    )
}

const Toggle = props => {
    return (
        <button onClick={props.onClick} className="brand-toggle btn btn-sm px-0" id="kt_aside_toggle">
            <MenuIcon size={"xl"} />
        </button>
    )
}

const Brand = props => {
    return (
        <div className="brand flex-column-auto" id="kt_brand">
            <Logo/>
            <Toggle onClick={props.toggle}/>
        </div>
    )
}

const SidebarLink = props => {
    return (
        <li className="menu-item">
            <NavLink to={props.to} className="menu-link">
                <props.icon className={"menu-icon"}/>
                <span className="menu-text">{props.text}</span>
            </NavLink>
        </li>
    )
}

const SidebarLinkSection = props => {
    return (
        <li className="menu-section">
            <h4 className="menu-text">{props.text}</h4>
            <i className="menu-icon ki ki-bold-more-hor icon-md"></i>
        </li>
    )
}

const SidebarMenu = () => {
    return (
        <div className="aside-menu-wrapper flex-column-fluid" id="kt_aside_menu_wrapper">
            <div id="kt_aside_menu" className="aside-menu my-4">
                <div className={"menu-nav"}>
                    <SidebarLink to={"#"} text={"Dashboard"} icon={DashboardIcon}/>
                    <SidebarLinkSection text={"Member"} />
                    <SidebarLink to={"#"} text={"List Members"} icon={UserGroupIcon}/>
                    <SidebarLink to={"#"} text={"Add Member"} icon={AddUserIcon}/>

                    <SidebarLinkSection text={"Ministries"} />
                    <SidebarLink to={"#"} text={"List Ministries"} icon={BuildingIcon}/>
                    <SidebarLink to={"#"} text={"Add Ministries"} icon={AddFileIcon}/>
                </div>
            </div>
        </div>
    )
}


const Sidebar = () => {

    const toggleSidebar = e => {
        console.log("Toggled")
    }
    return (
        <div className="aside aside-left aside-fixed d-flex flex-column flex-row-auto " id="kt_aside">
            <Brand toggle={toggleSidebar}/>
            <SidebarMenu/>
        </div>
    )
}


export default Sidebar;